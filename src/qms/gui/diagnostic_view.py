"""Contains DiagnosticView widget."""

import logging
from typing import TYPE_CHECKING, Any, cast

from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.backends.backend_qt import NavigationToolbar2QT
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.lines import Line2D
from PySide6 import QtGui, QtWidgets

from qms.backend.resonance_scan import ResonanceScanner
from qms.backend.rf_scan import RFScanner
from qms.backend.rf_test import RFTester
from qms.backend.source_scan import SourceScanner
from qms.backend.source_test import SourceTester
from qms.backend.upload_config import upload_configuration, upload_setpoint
from qms.config import Config
from qms.layouts.diagnostic_view_ui import Ui_diagnostic_view

if TYPE_CHECKING:
    from qms.gui.main_window import MainWindow

logger = logging.getLogger("main")


class Plot(QtWidgets.QWidget):
    """Custom Plot widget used in DiagnosticView."""

    def __init__(self, parent: QtWidgets.QWidget | None = None, line_count: int = 1):
        """Initialize with GUI."""
        super().__init__(parent)
        self.setLayout(QtWidgets.QVBoxLayout())
        self.canvas = MplCanvas(self, line_count)
        self.layout().addWidget(self.canvas)
        self.layout().addWidget(NavigationToolbar2QT(self.canvas, self))

    def add_point(self, x: float, y: float, line_index: int = 0) -> None:
        """Add new data point to plot."""
        self.canvas.x_data[line_index].append(x)
        self.canvas.y_data[line_index].append(y)

        self.canvas.lines[line_index].set_xdata(self.canvas.x_data[line_index])
        self.canvas.lines[line_index].set_ydata(self.canvas.y_data[line_index])

        self.canvas.axes[0].set_xlim(min(self.canvas.x_data[0]), max(self.canvas.x_data[0]))
        self.canvas.axes[line_index].set_ylim(min(self.canvas.y_data[line_index]), max(self.canvas.y_data[line_index]))

    def update_drawing(self) -> None:
        """Update drawn plot."""
        self.canvas.draw()

    def clear_points(self) -> None:
        """Clear all points from plot."""
        for i in range(len(self.canvas.y_data)):
            self.canvas.x_data[i] = []
            self.canvas.lines[i].set_xdata(self.canvas.x_data[i])

            self.canvas.y_data[i] = []
            self.canvas.lines[i].set_ydata(self.canvas.y_data[i])

        self.canvas.draw()


def get_color_from_cycle(index: int) -> str:
    """Return color from default color cycle by index."""
    colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    return colors[index]


class MplCanvas(FigureCanvasQTAgg):
    """Custom matplotlib canvas used in DiagnosticView."""

    def __init__(self, parent: QtWidgets.QWidget | None = None, count: int = 1):
        """Initialize with defaults."""
        # Initialize data
        self.x_data: list[list[float]] = []
        self.y_data: list[list[float]] = []
        for _ in range(count):
            self.x_data.append([])
            self.y_data.append([])

        # Initialize figure and axes
        fig = Figure()
        self.axes: list[Axes] = []
        self.axes.append(fig.add_subplot(111))
        self.axes[0].tick_params(axis="y", colors=get_color_from_cycle(0))
        for i in range(count - 1):
            axes = self.axes[0].twinx()
            if axes is not None:
                self.axes.append(cast(Axes, axes))
                axes.tick_params(axis="y", colors=get_color_from_cycle(i + 1))

        # Initialize lines
        self.lines: list[Line2D] = []
        for i in range(count):
            (line,) = self.axes[i].plot(self.x_data[i], self.y_data[i])
            line.set_color(get_color_from_cycle(i))
            self.lines.append(line)
        super().__init__(fig)

        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:  # noqa: N802
        """Handle resize event - update layout."""
        super().resizeEvent(event)
        (x, y) = self.figure.get_size_inches()
        x_scale = 1 / x
        y_scale = 1 / y
        left = 0.5 * x_scale
        bottom = 0.3 * y_scale
        width = 1 - left - ((0.5 * (len(self.axes) - 1) + 0.05) * x_scale)
        height = 1 - bottom - (0.05 * y_scale)
        # TODO: Do something about those magic consts
        self.axes[0].set_position((left, bottom, width, height))

        for index, axes in enumerate(self.axes[1:]):
            axes.spines.right.set_position(("outward", index * 40))


class DiagnosticView(QtWidgets.QWidget, Ui_diagnostic_view):
    """Widget for running different diagnostics on spectrometer."""

    def __init__(self, *args: Any, **kwargs: Any):
        """Initialize GUI and all children."""
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.main_window: MainWindow | None = None
        self.resonance_plot = Plot(self)
        self.rf_plot = Plot(self)
        self.source_plot = Plot(self, 2)
        self.rf_test_plot = Plot(self)
        self.source_test_plot = Plot(self, 3)

        self.rf_tester: RFTester | None = None
        self.source_tester: SourceTester | None = None

        self.replace_charts()
        self.setup_signals()

        self.frequency_at_maximum_resonance: float = 0
        self.voltage_at_maximum_resonance: float = -1e10

        self.spectrometer_config_update_paused: bool = False

    def setup_signals(self) -> None:
        """Connect all signals in the widget."""
        self.resonance_scan_button.clicked.connect(self.start_resonance_scan)
        self.min_frequency_spinbox.valueChanged.connect(self.resonance_updated)
        self.max_frequency_spinbox.valueChanged.connect(self.resonance_updated)
        self.frequency_steps_spinbox.valueChanged.connect(self.resonance_updated)

        self.rf_scan_button.clicked.connect(self.start_rf_scan)
        self.rf_max_spinbox.valueChanged.connect(self.rf_updated)
        self.rf_step_count_spinbox.valueChanged.connect(self.rf_updated)

        self.source_scan_button.clicked.connect(self.start_source_scan)
        self.source_min_spinbox.valueChanged.connect(self.source_updated)
        self.source_max_spinbox.valueChanged.connect(self.source_updated)
        self.source_steps_spinbox.valueChanged.connect(self.source_updated)

        self.rf_test_button.clicked.connect(self.start_rf_test)
        self.source_test_button.clicked.connect(self.start_source_test)

        self.working_frequency_spinbox.valueChanged.connect(self.spectrometer_config_updated)
        self.use_pid_checkbox.clicked.connect(self.spectrometer_config_updated)
        self.pid_p_spinbox.valueChanged.connect(self.spectrometer_config_updated)
        self.pid_i_spinbox.valueChanged.connect(self.spectrometer_config_updated)
        self.pid_d_spinbox.valueChanged.connect(self.spectrometer_config_updated)
        self.source_voltage_spinbox.valueChanged.connect(self.spectrometer_config_updated)
        self.source_current_spinbox.valueChanged.connect(self.spectrometer_config_updated)
        self.source_buttongroup.buttonToggled.connect(self.spectrometer_config_updated)

        self.rf_setpoint_spinbox.valueChanged.connect(self.setpoint_updated)

    def start_resonance_scan(self) -> None:
        """Start RF amplitude vs frequency scan."""
        logger.info("Resonance scan starting")
        if self.main_window is not None:
            if self.main_window.euromeasure is not None:
                self.main_window.set_allow_new_scans(False, "Resonance scan is running")

                self.voltage_at_maximum_resonance = -1e10
                self.frequency_at_maximum_resonance = 0
                self.resonance_plot.clear_points()

                scanner = ResonanceScanner(
                    self.main_window.euromeasure,
                    self.min_frequency_spinbox.value() * 1e6,
                    self.max_frequency_spinbox.value() * 1e6,
                    self.frequency_steps_spinbox.value(),
                )
                scanner.signals.data_point_acquired.connect(self.received_resonance_scan_point)
                scanner.signals.error_occured.connect(self.handle_em_exception)
                scanner.signals.finished.connect(self.finished_scan)
                self.main_window.thread_pool.start(scanner)
            else:
                logger.error("Tried to start resonance scan when EuroMeasure system is not connected")
                QtWidgets.QMessageBox.critical(self.main_window, "Error!", "EuroMeasure system is not connected")
        else:
            logger.error("Main window reference is not set")

    def start_rf_scan(self) -> None:
        """Start RF output vs input amplitude scan."""
        logger.info("RF scan starting")
        if self.main_window is not None:
            if self.main_window.euromeasure is not None:
                self.main_window.set_allow_new_scans(False, "RF scan is running")

                self.rf_plot.clear_points()
                scanner = RFScanner(
                    self.main_window.euromeasure,
                    self.rf_max_spinbox.value(),
                    self.rf_step_count_spinbox.value(),
                    self.working_frequency_spinbox.value(),
                )
                scanner.signals.data_point_acquired.connect(self.received_rf_scan_point)
                scanner.signals.error_occured.connect(self.handle_em_exception)
                scanner.signals.finished.connect(self.finished_scan)
                self.main_window.thread_pool.start(scanner)
            else:
                logger.error("Tried to start rf scan when EuroMeasure system is not connected")
                QtWidgets.QMessageBox.critical(self.main_window, "Error!", "EuroMeasure system is not connected")
        else:
            logger.error("Main window reference is not set")

    def start_source_scan(self) -> None:
        """Start source current vs voltage scan."""
        logger.info("Source scan starting")
        if self.main_window is not None:
            if self.main_window.euromeasure is not None:
                self.main_window.set_allow_new_scans(False, "Source scan is running")
                self.source_plot.clear_points()

                scanner = SourceScanner(
                    self.main_window.euromeasure,
                    self.source_min_spinbox.value() * 1e3,
                    self.source_max_spinbox.value() * 1e3,
                    self.source_steps_spinbox.value(),
                )
                scanner.signals.data_point_acquired.connect(self.received_source_scan_point)
                scanner.signals.error_occured.connect(self.handle_em_exception)
                scanner.signals.finished.connect(self.finished_scan)
                self.main_window.thread_pool.start(scanner)
            else:
                logger.error("Tried to start source scan when EuroMeasure system is not connected")
                QtWidgets.QMessageBox.critical(self.main_window, "Error!", "EuroMeasure system is not connected")
        else:
            logger.error("Main window reference is not set")

    def start_rf_test(self) -> None:
        """Start RF stability test."""
        logger.info("RF test starting")
        if self.main_window is not None:
            if self.main_window.euromeasure is not None:
                self.main_window.set_allow_new_scans(False, "RF test is running")
                self.rf_test_button.setText("Stop")
                self.rf_test_button.setToolTip("")
                self.rf_test_button.setEnabled(True)
                self.rf_test_button.clicked.disconnect(self.start_rf_test)
                self.rf_test_button.clicked.connect(self.stop_rf_test)

                self.rf_test_plot.clear_points()

                self.rf_tester = RFTester(self.main_window.euromeasure)
                self.rf_tester.signals.data_point_acquired.connect(self.received_rf_test_point)
                self.rf_tester.signals.error_occured.connect(self.handle_em_exception)
                self.rf_tester.signals.finished.connect(self.finished_scan)
                self.main_window.thread_pool.start(self.rf_tester)
            else:
                logger.error("Tried to start source scan when EuroMeasure system is not connected")
                QtWidgets.QMessageBox.critical(self.main_window, "Error!", "EuroMeasure system is not connected")
        else:
            logger.error("Main window reference is not set")

    def stop_rf_test(self) -> None:
        """Stop already running RF stability test."""
        if self.rf_tester is not None:
            self.rf_tester.signals.stop()
            self.rf_test_button.setText("Test")
            self.rf_test_button.setToolTip("")
            self.rf_test_button.clicked.disconnect(self.stop_rf_test)
            self.rf_test_button.clicked.connect(self.start_rf_test)
        else:
            logger.error("RF test stop even though rf_tester not initalized")

    def start_source_test(self) -> None:
        """Start source stability test."""
        logger.info("Source test starting")
        if self.main_window is not None:
            if self.main_window.euromeasure is not None:
                self.main_window.set_allow_new_scans(False, "Source test is running")
                self.source_test_button.setText("Stop")
                self.source_test_button.setToolTip("")
                self.source_test_button.setEnabled(True)
                self.source_test_button.clicked.disconnect(self.start_source_test)
                self.source_test_button.clicked.connect(self.stop_source_test)

                self.source_test_plot.clear_points()

                self.source_tester = SourceTester(self.main_window.euromeasure)
                self.source_tester.signals.data_point_acquired.connect(self.received_source_test_point)
                self.source_tester.signals.error_occured.connect(self.handle_em_exception)
                self.source_tester.signals.finished.connect(self.finished_scan)
                self.main_window.thread_pool.start(self.source_tester)
            else:
                logger.error("Tried to start source scan when EuroMeasure system is not connected")
                QtWidgets.QMessageBox.critical(self.main_window, "Error!", "EuroMeasure system is not connected")
        else:
            logger.error("Main window reference is not set")

    def stop_source_test(self) -> None:
        """Stop already running source stability test."""
        if self.source_tester is not None:
            self.source_tester.signals.stop()
            self.source_test_button.setText("Test")
            self.source_test_button.setToolTip("")
            self.source_test_button.clicked.disconnect(self.stop_source_test)
            self.source_test_button.clicked.connect(self.start_source_test)
        else:
            logger.error("Source test stop even though source_tester not initalized")

    def received_resonance_scan_point(self, frequency: float, voltage: float) -> None:
        """Handle new point received from resonance scan."""
        self.resonance_plot.add_point(frequency, voltage)
        self.resonance_plot.update_drawing()

        if voltage > self.voltage_at_maximum_resonance:
            self.voltage_at_maximum_resonance = voltage
            self.frequency_at_maximum_resonance = frequency
            self.working_frequency_spinbox.setValue(frequency / 1e6)

    def received_rf_scan_point(self, amplitude: float, monitor_voltage: float) -> None:
        """Handle new point received from rf scan."""
        self.rf_plot.add_point(amplitude, monitor_voltage)
        self.rf_plot.update_drawing()

    def received_source_scan_point(self, voltage: float, source_current: float, detector_current: float) -> None:
        """Handle new point received from source scan."""
        self.source_plot.add_point(voltage, source_current, 0)
        self.source_plot.add_point(voltage, detector_current, 1)
        self.source_plot.update_drawing()

    def received_rf_test_point(self, time_elapsed: float, monitor_voltage: float) -> None:
        """Handle new point received from rf stability test scan."""
        self.rf_test_plot.add_point(time_elapsed, monitor_voltage)
        self.rf_test_plot.update_drawing()

    def received_source_test_point(
        self, time_elapsed: float, voltage: float, current: float, detector_current: float
    ) -> None:
        """Handle new point received from rf stability test scan."""
        self.source_test_plot.add_point(time_elapsed, voltage, 0)
        self.source_test_plot.add_point(time_elapsed, current, 1)
        self.source_test_plot.add_point(time_elapsed, detector_current, 2)
        self.source_test_plot.update_drawing()

    def replace_charts(self) -> None:
        """Insert plot widgets into correct places."""
        self.layout().replaceWidget(self.resonance_chart, self.resonance_plot)
        self.layout().replaceWidget(self.rf_chart, self.rf_plot)
        self.layout().replaceWidget(self.source_chart, self.source_plot)
        self.layout().replaceWidget(self.rf_stability_chart, self.rf_test_plot)
        self.layout().replaceWidget(self.source_stability_chart, self.source_test_plot)

    def resonance_updated(self) -> None:
        """Handle resonance scan parameters update."""
        step_size = (self.max_frequency_spinbox.value() - self.min_frequency_spinbox.value()) / (
            self.frequency_steps_spinbox.value() - 1
        )
        self.frequency_step_size_label.setText(f"{step_size:.3f} MHz")

    def rf_updated(self) -> None:
        """Handle rf scan parameters update."""
        step_size = self.rf_max_spinbox.value() / (self.rf_step_count_spinbox.value() - 1)
        self.rf_step_size_label.setText(f"{step_size:.3f} Vpp")

    def source_updated(self) -> None:
        """Handle source scan parameters update."""
        step_size = (self.source_max_spinbox.value() - self.source_min_spinbox.value()) / (
            self.source_steps_spinbox.value() - 1
        )
        self.source_step_size_label.setText(f"{int(step_size * 1e3)} V")

    def handle_em_exception(self, exception: Exception) -> None:
        """Handle exception from EuroMeasure. Display it to user."""
        if self.main_window is not None:
            self.main_window.set_allow_new_scans(True)
            QtWidgets.QMessageBox.critical(self.main_window, "Error!", exception.args[0])

    def finished_scan(self) -> None:
        """Handle scan finishing."""
        if self.main_window is not None:
            self.main_window.set_allow_new_scans(True)

    def set_allow_new_scans(self, allow: bool = True, reason: str = "") -> None:
        """Enable/disable UI elements that start new scan."""
        self.resonance_scan_button.setEnabled(allow)
        self.resonance_scan_button.setToolTip(reason)
        self.rf_scan_button.setEnabled(allow)
        self.rf_scan_button.setToolTip(reason)
        self.rf_test_button.setEnabled(allow)
        self.rf_test_button.setToolTip(reason)
        self.source_scan_button.setEnabled(allow)
        self.source_scan_button.setToolTip(reason)
        self.source_test_button.setEnabled(allow)
        self.source_test_button.setToolTip(reason)

    def load_profile(self) -> None:
        """Load data from currently loaded profile."""
        # Need to pause spectrometer config update as it would cause the loaded config to be overwritten.
        self.spectrometer_config_update_paused = True
        config = Config.get().spectrometer_config
        self.working_frequency_spinbox.setValue(config.frequency)
        self.use_pid_checkbox.setChecked(config.pid_enabled)
        self.pid_p_spinbox.setValue(config.pid_p)
        self.pid_i_spinbox.setValue(config.pid_i)
        self.pid_d_spinbox.setValue(config.pid_d)
        self.cc_radiobutton.setChecked(config.source_cc)
        self.cv_radiobutton.setChecked(not config.source_cc)
        if config.source_voltage is not None:
            self.source_voltage_spinbox.setValue(config.source_voltage)
        if config.source_current is not None:
            self.source_current_spinbox.setValue(config.source_current)

        self.spectrometer_config_update_paused = False

    def spectrometer_config_updated(self) -> None:
        """Handle spectrometer configuration parameter update.

        Save all params to config object.
        """
        if not self.spectrometer_config_update_paused:
            logger.info("Spectrometer config changed, uploading new values")
            config = Config.get().spectrometer_config
            config.frequency = self.working_frequency_spinbox.value() * 1e6
            config.pid_enabled = self.use_pid_checkbox.isChecked()
            config.pid_p = self.pid_p_spinbox.value()
            config.pid_i = self.pid_i_spinbox.value()
            config.pid_d = self.pid_d_spinbox.value()
            config.source_cc = self.cc_radiobutton.isChecked()
            config.source_voltage = self.source_voltage_spinbox.value() * 1e3
            config.source_current = self.source_current_spinbox.value() * 1e-3
            if self.main_window is not None and self.main_window.euromeasure is not None:
                upload_configuration(self.main_window.euromeasure)

    def setpoint_updated(self) -> None:
        """When setpoint is updated, send it to euromeasure."""
        logger.info("Setpoint changed, sending to EM")
        if self.main_window is not None and self.main_window.euromeasure is not None:
            upload_setpoint(self.main_window.euromeasure, self.rf_setpoint_spinbox.value())
