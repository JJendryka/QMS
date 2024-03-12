"""Contains SpectrumControl widget."""

from typing import Any

from PySide6 import QtWidgets

from qms.config import Config
from qms.layouts.spectrum_control_ui import Ui_spectrum_control
from qms.misc import UILock


class SpectrumControl(QtWidgets.QWidget, Ui_spectrum_control):
    """SpectrumControl is a widget that allows spectrum measurement configuration."""

    def __init__(self, *args: Any, **kwargs: Any):
        """Initialize with default configuration."""
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.ui_lock = UILock()
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
