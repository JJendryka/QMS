import logging
from PySide6 import QtWidgets, QtGui
from qms.backend.resonance_scan import ResonanceScanner

from qms.backend.rf_scan import RFScanner
from qms.backend.rf_test import RFTester
from qms.backend.source_scan import SourceScanner

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from qms.gui.main_window import MainWindow

from qms.layouts.diagnostic_view_ui import Ui_diagnostic_view

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure


logger = logging.getLogger("main")


class Plot(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Plot, self).__init__(parent)
        self.setLayout(QtWidgets.QVBoxLayout())
        self.canvas = MplCanvas(self)
        self.layout().addWidget(self.canvas)
        self.layout().addWidget(NavigationToolbar2QT(self.canvas, self))

    def add_point(self, x, y):
        self.canvas.x_data.append(x)
        self.canvas.y_data.append(y)

        self.canvas.line.set_xdata(self.canvas.x_data)
        self.canvas.line.set_ydata(self.canvas.y_data)

        self.canvas.axes.set_xlim(min(self.canvas.x_data), max(self.canvas.x_data))
        self.canvas.axes.set_ylim(min(self.canvas.y_data), max(self.canvas.y_data))

        self.canvas.draw()

    def clear_points(self):
        self.canvas.x_data = []
        self.canvas.y_data = []

        self.canvas.line.set_xdata(self.canvas.x_data)
        self.canvas.line.set_ydata(self.canvas.y_data)

        self.canvas.draw()


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None):
        self.x_data = []
        self.y_data = []
        fig = Figure()
        self.axes = fig.add_subplot(111)
        (self.line,) = self.axes.plot(self.x_data, self.y_data)
        super(MplCanvas, self).__init__(fig)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

    def resizeEvent(self, event: QtGui.QResizeEvent):  # noqa: N802
        super(MplCanvas, self).resizeEvent(event)
        self.figure.tight_layout(pad=0.5)


class DiagnosticView(QtWidgets.QWidget, Ui_diagnostic_view):
    def __init__(self, *args, **kwargs) -> None:
        super(DiagnosticView, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.main_window: MainWindow | None = None
        self.resonance_plot = Plot(self)
        self.rf_plot = Plot(self)
        self.source_plot = Plot(self)
        self.rf_test_plot = Plot(self)

        self.rf_tester: RFTester | None = None

        self.replace_charts()
        self.setup_signals()

        self.frequency_at_maximum_resonance: float = 0
        self.voltage_at_maximum_resonance: float = -1e10

    def setup_signals(self) -> None:
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

    def start_resonance_scan(self) -> None:
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
        if self.rf_tester is not None:
            self.rf_tester.signals.stop()
            self.rf_test_button.setText("Test")
            self.rf_test_button.setToolTip("")
            self.rf_test_button.clicked.disconnect(self.stop_rf_test)
            self.rf_test_button.clicked.connect(self.start_rf_test)
        else:
            logger.error("RF test stop even though rf_tester not initalized")

    def received_resonance_scan_point(self, frequency: float, voltage: float) -> None:
        self.resonance_plot.add_point(frequency, voltage)

        if voltage > self.voltage_at_maximum_resonance:
            self.voltage_at_maximum_resonance = voltage
            self.frequency_at_maximum_resonance = frequency
            self.working_frequency_spinbox.setValue(frequency / 1e6)

    def received_rf_scan_point(self, amplitude: float, monitor_voltage: float):
        self.rf_plot.add_point(amplitude, monitor_voltage)

    def received_source_scan_point(self, voltage: float, current: float):
        self.source_plot.add_point(voltage, current)

    def received_rf_test_point(self, time_elapsed: float, monitor_voltage: float):
        self.rf_test_plot.add_point(time_elapsed, monitor_voltage)

    def replace_charts(self) -> None:
        self.layout().replaceWidget(self.resonance_chart, self.resonance_plot)
        self.layout().replaceWidget(self.rf_chart, self.rf_plot)
        self.layout().replaceWidget(self.source_chart, self.source_plot)
        self.layout().replaceWidget(self.rf_stability_chart, self.rf_test_plot)

        source_stability_chart = Plot(self)
        self.layout().replaceWidget(self.source_stability_chart, source_stability_chart)

    def resonance_updated(self) -> None:
        step_size = (self.max_frequency_spinbox.value() - self.min_frequency_spinbox.value()) / (
            self.frequency_steps_spinbox.value() - 1
        )
        self.frequency_step_size_label.setText(f"{step_size:.3f} MHz")

    def rf_updated(self) -> None:
        step_size = self.rf_max_spinbox.value() / (self.rf_step_count_spinbox.value() - 1)
        self.rf_step_size_label.setText(f"{step_size:.3f} Vpp")

    def source_updated(self) -> None:
        step_size = (self.source_max_spinbox.value() - self.source_min_spinbox.value()) / (
            self.source_steps_spinbox.value() - 1
        )
        self.source_step_size_label.setText(f"{int(step_size * 1e3)} V")

    def handle_em_exception(self, exception: Exception) -> None:
        if self.main_window is not None:
            self.main_window.set_allow_new_scans(True)
            QtWidgets.QMessageBox.critical(self.main_window, "Error!", exception.args[0])

    def finished_scan(self) -> None:
        if self.main_window is not None:
            self.main_window.set_allow_new_scans(True)

    def set_allow_new_scans(self, allow=True, reason: str = ""):
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
