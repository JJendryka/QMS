"""Contains MapControl widget."""

import logging
from typing import TYPE_CHECKING, Any

from PySide6 import QtWidgets

from qms.backend.spectrum_scan import SpectrumScanner
from qms.config import Config
from qms.layouts.map_control_ui import Ui_map_control

if TYPE_CHECKING:
    from qms.gui.main_window import MainWindow

logger = logging.getLogger("main")


class MapControl(QtWidgets.QWidget, Ui_map_control):
    """Widget for controlling map scans."""

    def __init__(self, *args: Any, **kwargs: Any):
        """Initialize with default configuration."""
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.parameters_update_paused: bool = False
        self.pause_xy_updates: bool = False
        self.dc_step = 0
        self.main_window: MainWindow | None = None
        self.scanner: SpectrumScanner | None = None
        self.setup_signals()

    def setup_signals(self) -> None:
        """Connect all needed signals to their handlers."""
        self.rf_u_scale_spinbox.valueChanged.connect(self.rf_to_unit_factor_updated)
        self.dc_offset_spinbox.valueChanged.connect(self.map_dc_offset_updated)
        self.a_spinbox.valueChanged.connect(self.a_updated)
        self.b_spinbox.valueChanged.connect(self.b_updated)
        self.x1_spinbox.valueChanged.connect(self.xy_updated)
        self.x2_spinbox.valueChanged.connect(self.xy_updated)
        self.y1_spinbox.valueChanged.connect(self.xy_updated)
        self.y2_spinbox.valueChanged.connect(self.xy_updated)
        self.rf_min_spinbox.valueChanged.connect(self.rf_min_max_size_updated)
        self.rf_max_spinbox.valueChanged.connect(self.rf_min_max_size_updated)
        self.rf_step_size_spinbox.valueChanged.connect(self.rf_min_max_size_updated)
        self.rf_step_count_spinbox.valueChanged.connect(self.rf_step_count_updated)
        self.dc_min_spinbox.valueChanged.connect(self.dc_min_max_size_updated)
        self.dc_max_spinbox.valueChanged.connect(self.dc_min_max_size_updated)
        self.dc_step_size_spinbox.valueChanged.connect(self.dc_min_max_size_updated)
        self.dc_step_count_spinbox.valueChanged.connect(self.dc_step_count_updated)
        self.start_push_button.clicked.connect(self.start_measurement)
        self.stop_push_button.clicked.connect(self.stop_measurement)

    def load_profile(self) -> None:
        """Load data from currently loaded profile."""
        params = Config.get().parameters
        self.rf_u_scale_spinbox.setValue(params.rf_to_unit_factor)
        self.dc_offset_spinbox.setValue(params.map_dc_offset)
        self.pause_scanline_updates = True
        self.a_spinbox.setValue(params.a)
        self.b_spinbox.setValue(params.b)
        self.pause_xy_updates = False

    def rf_to_unit_factor_updated(self) -> None:
        """On spinbox value change, update other values and save."""
        rf_to_unit_factor = self.rf_u_scale_spinbox.value()
        Config.get().parameters.rf_to_unit_factor = rf_to_unit_factor
        mass = self.mass_spinbox.value()
        self.rf_spinbox.setValue(mass / rf_to_unit_factor)
        self.ab_updated()

    def mass_updated(self) -> None:
        """On spinbox value change, update other values and save."""
        mass = self.mass_spinbox.value()
        rf = self.rf_spinbox.value()
        rf_to_unit_factor = mass / rf
        Config.get().parameters.rf_to_unit_factor = rf_to_unit_factor

    def rf_updated(self) -> None:
        """On spinbox value change, update other values and save."""
        mass = self.mass_spinbox.value()
        rf = self.rf_spinbox.value()
        rf_to_unit_factor = mass / rf
        Config.get().parameters.rf_to_unit_factor = rf_to_unit_factor

    def map_dc_offset_updated(self) -> None:
        """On spinbox value change, update other values and save."""
        Config.get().parameters.map_dc_offset = self.dc_offset_spinbox.value()

    def a_updated(self) -> None:
        """On spinbox value change, update other values and save."""
        Config.get().parameters.a = self.a_spinbox.value()
        self.ab_updated()

    def b_updated(self) -> None:
        """On spinbox value change, update other values and save."""
        Config.get().parameters.b = self.b_spinbox.value()
        self.ab_updated()

    def ab_updated(self) -> None:
        """Recalculate calibration points based on changed a and b."""
        if not self.pause_xy_updates:
            a = self.a_spinbox.value()
            b = self.b_spinbox.value()

            rf_u_factor = Config.get().parameters.rf_to_unit_factor

            self.pause_xy_updates = True
            self.y1_spinbox.setValue(self.x1_spinbox.value() / rf_u_factor * a + b)
            self.y2_spinbox.setValue(self.x2_spinbox.value() / rf_u_factor * a + b)
            self.pause_xy_updates = False

    def xy_updated(self) -> None:
        """If any of the calibration coordinates change, update a and b."""
        if not self.pause_xy_updates:
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
            self.pause_xy_updates = True
            self.a_spinbox.setValue(a)
            self.b_spinbox.setValue(b)
            self.pause_xy_updates = False

    def rf_min_max_size_updated(self) -> None:
        """Update RF step count based when other values changed."""
        rf_min = self.rf_min_spinbox.value()
        rf_max = self.rf_max_spinbox.value()
        rf_step_size = self.rf_step_size_spinbox.value()
        self.rf_step_count_spinbox.setValue((rf_max - rf_min) / rf_step_size)

    def dc_min_max_size_updated(self) -> None:
        """Update DC step count based when other values changed."""
        dc_min = self.dc_min_spinbox.value()
        dc_max = self.dc_max_spinbox.value()
        dc_step_size = self.dc_step_size_spinbox.value()
        self.dc_step_count_spinbox.setValue((dc_max - dc_min) / dc_step_size)

    def rf_step_count_updated(self) -> None:
        """Update RF step size when step count changes."""
        rf_min = self.rf_min_spinbox.value()
        rf_max = self.rf_max_spinbox.value()
        rf_step_count = self.rf_step_count_spinbox.value()
        self.rf_step_size_spinbox.setValue((rf_max - rf_min) / rf_step_count)

    def dc_step_count_updated(self) -> None:
        """Update RF step size when step count changes."""
        dc_min = self.dc_min_spinbox.value()
        dc_max = self.dc_max_spinbox.value()
        dc_step_count = self.dc_step_count_spinbox.value()
        self.dc_step_size_spinbox.setValue((dc_max - dc_min) / dc_step_count)

    def start_measurement(self) -> None:
        """Start measurement of stability map."""
        if self.main_window is not None:
            self.main_window.set_allow_new_scans(False, "Stability map scan is running")
        self.dc_step = 0
        self.stop_push_button.setEnabled(True)
        self.next_measurement_step()

    def measurement_finished(self) -> None:
        """Handle finished stability map measurement."""
        if self.main_window is not None:
            self.main_window.set_allow_new_scans(True)
        self.dc_step = 0
        self.stop_push_button.setEnabled(False)

    def measurement_step_finished(self) -> None:
        """Handle last measurement finishing."""
        if self.dc_step == self.dc_step_count_spinbox.value():
            self.measurement_finished()
        else:
            self.next_measurement_step()

    def next_measurement_step(self) -> None:
        """Start next measurement step."""
        if self.main_window is not None:
            if self.main_window.euromeasure is not None:
                ac, dc = self.calculate_ac_dc()
                self.dc_step += 1
                self.scanner = SpectrumScanner(self.main_window.euromeasure, ac, dc)
                self.scanner.signals.data_point_acquired.connect(self.received_spectrum_point)
                self.scanner.signals.error_occured.connect(self.handle_em_exception)
                self.scanner.signals.finished.connect(self.measurement_step_finished)
                self.main_window.thread_pool.start(self.scanner)
            else:
                logger.error("Tried to start stability map scan when EuroMeasure system is not connected")
                QtWidgets.QMessageBox.critical(self.main_window, "Error!", "EuroMeasure system is not connected")
        else:
            logger.error("Main window reference is not set")

    def received_spectrum_point(
        self, ac_step: int, detector_voltage: float, monitor_voltage: float, source: float
    ) -> None:
        """Handle received data from spectrum scanner."""

    def calculate_ac_dc(self) -> tuple[list[float], list[float]]:
        """Calculate DC and AC values for next spectrum measurement."""
        rf_min = self.rf_min_spinbox.value()
        rf_step_count = self.rf_step_count_spinbox.value()
        rf_step_size = self.rf_step_size_spinbox.value()
        ac = [rf_min + i * rf_step_size for i in range(rf_step_count)]

        dc_min = self.dc_min_spinbox.value()
        dc_step_size = self.dc_step_size_spinbox.value()
        dc_rf_offset = self.dc_offset_spinbox.value()
        dc = [dc_min + self.dc_step * dc_step_size + dc_rf_offset * ac[i] for i in range(rf_step_count)]

        return (ac, dc)

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
