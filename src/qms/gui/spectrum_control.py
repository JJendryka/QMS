"""Contains SpectrumControl widget."""
import logging
from typing import TYPE_CHECKING, Any

import numpy as np
from PySide6 import QtWidgets

from qms.backend.spectrum_scan import SpectrumScanner
from qms.config import Config
from qms.gui.spectrum_plot import SpectrumPlot
from qms.layouts.spectrum_control_ui import Ui_spectrum_control
from qms.misc import Array1Df, UILock

if TYPE_CHECKING:
    from qms.gui.main_window import MainWindow

logger = logging.getLogger("main")


class SpectrumControl(QtWidgets.QWidget, Ui_spectrum_control):
    """SpectrumControl is a widget that allows spectrum measurement configuration."""

    def __init__(self, *args: Any, **kwargs: Any):
        """Initialize with default configuration."""
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.ui_lock = UILock()
        self.spectrum_plot: SpectrumPlot | None = None
        self.scanner: SpectrumScanner | None = None
        self.main_window: MainWindow | None = None
        self.setup_signals()
        self.load_profile()

    def load_profile(self) -> None:
        """Load data from currently loaded profile."""
        params = Config.get().parameters
        with self.ui_lock:
            self.min_spinbox.setValue(params.u_min)
            self.max_spinbox.setValue(params.u_max)
        self.step_size_spinbox.setValue(params.step_size)

    def setup_signals(self) -> None:
        """Connect all needed signals to their handlers."""
        self.min_spinbox.valueChanged.connect(self.ui_lock(self.min_max_size_updated))
        self.max_spinbox.valueChanged.connect(self.ui_lock(self.min_max_size_updated))
        self.step_size_spinbox.valueChanged.connect(self.ui_lock(self.min_max_size_updated))
        self.step_count_spinbox.valueChanged.connect(self.ui_lock(self.count_updated))

        self.start_button.clicked.connect(self.start_measurement)
        self.stop_button.clicked.connect(self.stop_measurement)

    def min_max_size_updated(self, *_: Any) -> None:
        """On spinbox value change, update other values and save."""
        minimum = self.min_spinbox.value()
        maximum = self.max_spinbox.value()
        step_size = self.step_size_spinbox.value()

        params = Config.get().parameters

        params.u_min = minimum
        params.u_max = maximum
        params.step_size = step_size
        with self.ui_lock:
            self.step_count_spinbox.setValue(params.get_step_count())

    def count_updated(self, *_: Any) -> None:
        """On spinbox value change, update other values and save."""
        minimum = self.min_spinbox.value()
        maximum = self.max_spinbox.value()
        step_count = self.step_count_spinbox.value()
        step_size = (maximum - minimum) / step_count
        Config.get().parameters.step_size = step_size
        with self.ui_lock:
            self.step_size_spinbox.setValue(step_size)

    def start_measurement(self) -> None:
        """Start measurement of stability map."""
        if self.main_window is not None:
            self.main_window.set_allow_new_scans(False, "Spectrum scan is running")
        self.stop_button.setEnabled(True)
        if self.spectrum_plot is not None:
            self.spectrum_plot.clear()
        self.measure_spectrum()

    def calculate_measurement_points(self) -> tuple[Array1Df, Array1Df]:
        """Calculate rf and dc values for next sweep."""
        params = Config.get().parameters
        rf = (
            np.arange(self.min_spinbox.value(), self.max_spinbox.value(), step=self.step_size_spinbox.value())
            / params.rf_to_unit_factor
        )
        dc = rf * params.a + params.b
        return rf, dc

    def measure_spectrum(self) -> None:
        """Measure a single spectrum."""
        rf, dc = self.calculate_measurement_points()

        if self.spectrum_plot is not None:
            self.spectrum_plot.new_scan(rf)
        if self.main_window is not None:
            if self.main_window.euromeasure is not None:
                self.scanner = SpectrumScanner(self.main_window.euromeasure, list(rf), list(dc))
                self.scanner.signals.data_point_acquired.connect(self.received_spectrum_point)
                self.scanner.signals.error_occured.connect(self.handle_em_exception)
                self.scanner.signals.finished.connect(self.measurement_finished)
                self.main_window.thread_pool.start(self.scanner)
            else:
                logger.error("Tried to start spectrum scan when EuroMeasure system is not connected")
                QtWidgets.QMessageBox.critical(self.main_window, "Error!", "EuroMeasure system is not connected")

    def received_spectrum_point(self, rf_step: int, detector_voltage: float) -> None:
        """Handle received data from spectrum scanner."""
        if self.spectrum_plot is not None:
            self.spectrum_plot.new_point(rf_step, detector_voltage)
        else:
            logger.error("Tried to access spectrum_plot when it wasn't set.")

    def stop_measurement(self) -> None:
        """Stop current measurement."""
        if self.scanner is not None:
            self.scanner.signals.stop()
        self.clean_after_measurement_stoped()

    def measurement_finished(self) -> None:
        """Handle finished spectrum measurement."""
        if self.repeating_checkbox.isChecked():
            self.measure_spectrum()
        else:
            self.clean_after_measurement_stoped()

    def clean_after_measurement_stoped(self) -> None:
        """Clean up UI so that it is in a state where no measurement is happening."""
        if self.main_window is not None:
            self.main_window.set_allow_new_scans(True)
        self.stop_button.setEnabled(False)

    def set_allow_new_scans(self, allow: bool = True, reason: str = "") -> None:
        """Enable/disable UI elements that start new scan."""
        self.start_button.setEnabled(allow)
        self.start_button.setToolTip(reason)

    # TODO: merge with one in diagnostic tab
    def handle_em_exception(self, exception: Exception) -> None:
        """Handle exception from EuroMeasure. Display it to user."""
        if self.main_window is not None:
            self.main_window.set_allow_new_scans(True)
            QtWidgets.QMessageBox.critical(self.main_window, "Error!", exception.args[0])
