"""Contains MapControl widget."""

import logging
from typing import TYPE_CHECKING, Any

import numpy as np
from PySide6 import QtWidgets

from qms.backend.spectrum_scan import SpectrumScanner
from qms.config import Config
from qms.gui.map_plot import MapPlot
from qms.layouts.map_control_ui import Ui_map_control
from qms.misc import Array2Df, UILock

if TYPE_CHECKING:
    from qms.gui.main_window import MainWindow

logger = logging.getLogger("main")


class MapControl(QtWidgets.QWidget, Ui_map_control):
    """Widget for controlling map scans."""

    def __init__(self, *args: Any, **kwargs: Any):
        """Initialize with default configuration."""
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.ui_lock = UILock()
        self.dc_step = 0
        self.rf_points: Array2Df | None = None
        self.dc_points: Array2Df | None = None
        self.main_window: MainWindow | None = None
        self.map_plot: MapPlot | None = None
        self.scanner: SpectrumScanner | None = None
        self.setup_signals()
        self.load_profile()

    def setup_signals(self) -> None:
        """Connect all needed signals to their handlers."""
        self.rf_u_scale_spinbox.valueChanged.connect(self.ui_lock(self.rf_to_unit_factor_updated))
        self.dc_offset_spinbox.valueChanged.connect(self.ui_lock(self.map_dc_offset_updated))
        self.a_spinbox.valueChanged.connect(self.ui_lock(self.a_updated))
        self.b_spinbox.valueChanged.connect(self.ui_lock(self.b_updated))
        self.x1_spinbox.valueChanged.connect(self.ui_lock(self.xy_updated))
        self.x2_spinbox.valueChanged.connect(self.ui_lock(self.xy_updated))
        self.y1_spinbox.valueChanged.connect(self.ui_lock(self.xy_updated))
        self.y2_spinbox.valueChanged.connect(self.ui_lock(self.xy_updated))
        self.rf_min_spinbox.valueChanged.connect(self.ui_lock(self.rf_min_max_size_updated))
        self.rf_max_spinbox.valueChanged.connect(self.ui_lock(self.rf_min_max_size_updated))
        self.rf_step_size_spinbox.valueChanged.connect(self.ui_lock(self.rf_min_max_size_updated))
        self.rf_step_count_spinbox.valueChanged.connect(self.ui_lock(self.rf_step_count_updated))
        self.dc_min_spinbox.valueChanged.connect(self.ui_lock(self.dc_min_max_size_updated))
        self.dc_max_spinbox.valueChanged.connect(self.ui_lock(self.dc_min_max_size_updated))
        self.dc_step_size_spinbox.valueChanged.connect(self.ui_lock(self.dc_min_max_size_updated))
        self.dc_step_count_spinbox.valueChanged.connect(self.ui_lock(self.dc_step_count_updated))
        self.start_push_button.clicked.connect(self.start_measurement)
        self.stop_push_button.clicked.connect(self.stop_measurement)

    def load_profile(self) -> None:
        """Load data from currently loaded profile."""
        params = Config.get().parameters
        self.rf_u_scale_spinbox.setValue(params.rf_to_unit_factor)
        self.dc_offset_spinbox.setValue(params.map_dc_offset)
        self.a_spinbox.setValue(params.a)
        self.b_spinbox.setValue(params.b)
        with self.ui_lock:
            self.rf_max_spinbox.setValue(params.map_rf_max)
            self.rf_min_spinbox.setValue(params.map_rf_min)
        self.rf_step_size_spinbox.setValue(params.map_rf_step_size)
        with self.ui_lock:
            self.dc_max_spinbox.setValue(params.map_dc_max)
            self.dc_min_spinbox.setValue(params.map_dc_min)
        self.dc_step_size_spinbox.setValue(params.map_dc_step_size)

    def rf_to_unit_factor_updated(self, *_: Any) -> None:
        """On spinbox value change, update other values and save."""
        rf_to_unit_factor = self.rf_u_scale_spinbox.value()
        Config.get().parameters.rf_to_unit_factor = rf_to_unit_factor
        mass = self.mass_spinbox.value()
        with self.ui_lock:
            self.rf_spinbox.setValue(mass / rf_to_unit_factor)
        self.ab_updated()

    def mass_updated(self, *_: Any) -> None:
        """On spinbox value change, update other values and save."""
        mass = self.mass_spinbox.value()
        rf = self.rf_spinbox.value()
        rf_to_unit_factor = mass / rf
        Config.get().parameters.rf_to_unit_factor = rf_to_unit_factor
        with self.ui_lock:
            self.rf_u_scale_spinbox.setValue(rf_to_unit_factor)
        self.ab_updated()

    def rf_updated(self, *_: Any) -> None:
        """On spinbox value change, update other values and save."""
        mass = self.mass_spinbox.value()
        rf = self.rf_spinbox.value()
        rf_to_unit_factor = mass / rf
        Config.get().parameters.rf_to_unit_factor = rf_to_unit_factor
        with self.ui_lock:
            self.rf_u_scale_spinbox.setValue(rf_to_unit_factor)
        self.ab_updated()

    def map_dc_offset_updated(self, *_: Any) -> None:
        """On spinbox value change, update other values and save."""
        Config.get().parameters.map_dc_offset = self.dc_offset_spinbox.value()

    def a_updated(self, *_: Any) -> None:
        """On spinbox value change, update other values and save."""
        Config.get().parameters.a = self.a_spinbox.value()
        self.ab_updated()

    def b_updated(self, *_: Any) -> None:
        """On spinbox value change, update other values and save."""
        Config.get().parameters.b = self.b_spinbox.value()
        self.ab_updated()

    def ab_updated(self, *_: Any) -> None:
        """Recalculate calibration points based on changed a and b."""
        a = self.a_spinbox.value()
        b = self.b_spinbox.value()

        rf_u_factor = self.rf_u_scale_spinbox.value()

        with self.ui_lock:
            self.y1_spinbox.setValue(self.x1_spinbox.value() / rf_u_factor * a + b)
            self.y2_spinbox.setValue(self.x2_spinbox.value() / rf_u_factor * a + b)
        if self.map_plot is not None:
            self.map_plot.update_scanline(a, b)

    def xy_updated(self, *_: Any) -> None:
        """If any of the calibration coordinates change, update a and b."""
        params = Config.get().parameters
        rf_u_factor = params.rf_to_unit_factor
        x1 = self.x1_spinbox.value() / rf_u_factor
        x2 = self.x2_spinbox.value() / rf_u_factor
        y1 = self.y1_spinbox.value()
        y2 = self.y2_spinbox.value()
        a = (y2 - y1) / (x2 - x1)
        b = y1 - a * x1
        params.a = a
        params.b = b
        with self.ui_lock:
            self.a_spinbox.setValue(a)
            self.b_spinbox.setValue(b)
        if self.map_plot is not None:
            self.map_plot.update_scanline(a, b)

    def rf_min_max_size_updated(self, *_: Any) -> None:
        """Update RF step count based when other values changed."""
        rf_min = self.rf_min_spinbox.value()
        rf_max = self.rf_max_spinbox.value()
        rf_step_size = self.rf_step_size_spinbox.value()
        params = Config.get().parameters
        params.map_rf_min = rf_min
        params.map_rf_max = rf_max
        params.map_rf_step_size = rf_step_size
        with self.ui_lock:
            self.rf_step_count_spinbox.setValue(params.get_map_rf_step_count())

    def dc_min_max_size_updated(self, *_: Any) -> None:
        """Update DC step count based when other values changed."""
        dc_min = self.dc_min_spinbox.value()
        dc_max = self.dc_max_spinbox.value()
        dc_step_size = self.dc_step_size_spinbox.value()
        params = Config.get().parameters
        params.map_dc_min = dc_min
        params.map_dc_max = dc_max
        params.map_dc_step_size = dc_step_size
        with self.ui_lock:
            self.dc_step_count_spinbox.setValue(params.get_map_dc_step_count())

    def rf_step_count_updated(self, *_: Any) -> None:
        """Update RF step size when step count changes."""
        rf_min = self.rf_min_spinbox.value()
        rf_max = self.rf_max_spinbox.value()
        rf_step_count = self.rf_step_count_spinbox.value()
        rf_step_size = (rf_max - rf_min) / rf_step_count
        Config.get().parameters.map_rf_step_size = rf_step_size
        with self.ui_lock:
            self.rf_step_size_spinbox.setValue(rf_step_size)

    def dc_step_count_updated(self, *_: Any) -> None:
        """Update RF step size when step count changes."""
        dc_min = self.dc_min_spinbox.value()
        dc_max = self.dc_max_spinbox.value()
        dc_step_count = self.dc_step_count_spinbox.value()
        dc_step_size = (dc_max - dc_min) / dc_step_count
        Config.get().parameters.map_dc_step_size = dc_step_size
        with self.ui_lock:
            self.dc_step_size_spinbox.setValue(dc_step_size)

    def calculate_measurement_points(
        self,
    ) -> tuple[Array2Df, Array2Df]:
        """Calculate all measurement points given current UI settings."""
        params = Config.get().parameters
        logger.debug(
            "Calculating scan points from: RF: (min: %d, max: %d, size: %d, step: %d)",
            params.map_rf_min,
            params.map_rf_max,
            params.map_rf_step_size,
            params.get_map_rf_step_count(),
        )
        rf = np.arange(0, params.get_map_rf_step_count()) * params.map_rf_step_size + params.map_rf_min
        dc = np.arange(0, params.get_map_dc_step_count()) * params.map_dc_step_size + params.map_dc_min
        rfs, dcs = np.meshgrid(rf, dc)
        dcs = dcs + Config.get().parameters.map_dc_offset * rfs
        return (rfs, dcs)

    def start_measurement(self) -> None:
        """Start measurement of stability map."""
        if self.main_window is not None:
            self.main_window.set_allow_new_scans(False, "Stability map scan is running")
        self.dc_step = 0
        self.stop_push_button.setEnabled(True)
        self.rf_points, self.dc_points = self.calculate_measurement_points()
        params = Config.get().parameters
        if self.map_plot is not None:
            self.map_plot.new_plot(self.rf_points, self.dc_points, params.a, params.b)
        self.next_measurement_step()

    def measurement_finished(self) -> None:
        """Handle finished stability map measurement."""
        if self.main_window is not None:
            self.main_window.set_allow_new_scans(True)
        self.dc_step = 0
        self.stop_push_button.setEnabled(False)

    def measurement_step_finished(self) -> None:
        """Handle last measurement finishing."""
        self.dc_step += 1
        if self.dc_step == self.dc_step_count_spinbox.value():
            self.measurement_finished()
        else:
            self.next_measurement_step()

    def next_measurement_step(self) -> None:
        """Start next measurement step."""
        if self.main_window is not None:
            if self.main_window.euromeasure is not None:
                if self.rf_points is not None and self.dc_points is not None:
                    self.scanner = SpectrumScanner(
                        self.main_window.euromeasure, self.rf_points[self.dc_step], self.dc_points[self.dc_step]
                    )
                    self.scanner.signals.data_point_acquired.connect(self.received_spectrum_point)
                    self.scanner.signals.error_occured.connect(self.handle_em_exception)
                    self.scanner.signals.finished.connect(self.measurement_step_finished)
                    self.main_window.thread_pool.start(self.scanner)
                else:
                    logger.error("next_measurement_step run without setting measurement points")
            else:
                logger.error("Tried to start stability map scan when EuroMeasure system is not connected")
                QtWidgets.QMessageBox.critical(self.main_window, "Error!", "EuroMeasure system is not connected")
        else:
            logger.error("Main window reference is not set")

    def received_spectrum_point(self, rf_step: int, detector_voltage: float) -> None:
        """Handle received data from spectrum scanner."""
        if self.map_plot is not None:
            self.map_plot.new_point(rf_step, self.dc_step, detector_voltage)
        else:
            logger.error("Tried to access map_plot when it wasn't set.")

    def stop_measurement(self) -> None:
        """Stop current measurement."""
        if self.scanner is not None:
            self.scanner.signals.stop()
            self.measurement_finished()

    # TODO: merge with one in diagnostic tab
    def handle_em_exception(self, exception: Exception) -> None:
        """Handle exception from EuroMeasure. Display it to user."""
        if self.main_window is not None:
            self.main_window.set_allow_new_scans(True)
            QtWidgets.QMessageBox.critical(self.main_window, "Error!", exception.args[0])

    def set_allow_new_scans(self, allow: bool = True, reason: str = "") -> None:
        """Enable/disable UI elements that start new scan."""
        self.start_push_button.setEnabled(allow)
        self.start_push_button.setToolTip(reason)
