"""Contains MapControl widget."""

from typing import Any

from PySide6 import QtWidgets

from qms.config import Config
from qms.layouts.map_control_ui import Ui_map_control


class MapControl(QtWidgets.QWidget, Ui_map_control):
    """Widget for controlling map scans."""

    def __init__(self, *args: Any, **kwargs: Any):
        """Initialize with default configuration."""
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.parameters_update_paused: bool = False
        self.pause_ab_updates: bool = False

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

    def load_profile(self) -> None:
        """Load data from currently loaded profile."""
        params = Config.get().parameters
        self.rf_u_scale_spinbox.setValue(params.rf_to_unit_factor)
        self.dc_offset_spinbox.setValue(params.map_dc_offset)
        self.pause_scanline_updates = True
        self.a_spinbox.setValue(params.a)
        self.b_spinbox.setValue(params.b)
        self.pause_ab_updates = False

    def rf_to_unit_factor_updated(self) -> None:
        """On spinbox value change, update other values and save."""
        rf_to_unit_factor = self.rf_u_scale_spinbox.value()
        Config.get().parameters.rf_to_unit_factor = rf_to_unit_factor
        mass = self.mass_spinbox.value()
        self.rf_spinbox.setValue(mass / rf_to_unit_factor)

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
        a = self.a_spinbox.value()
        b = self.b_spinbox.value()

        self.y1_spinbox.setValue(self.x1_spinbox.value() * a + b)
        self.y2_spinbox.setValue(self.x2_spinbox.value() * a + b)

    def xy_updated(self) -> None:
        """If any of the calibration coordinates change, update a and b."""
        if not self.pause_ab_updates:
            x1 = self.x1_spinbox.value()
            x2 = self.x2_spinbox.value()
            y1 = self.y1_spinbox.value()
            y2 = self.y2_spinbox.value()
            a = (y2 - y1) / (x2 - x1)
            b = y1 - a * x1
            params = Config.get().parameters
            params.a = a
            params.b = b
            self.a_spinbox.setValue(a)
            self.b_spinbox.setValue(b)
