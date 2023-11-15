"""Contains SpectrumControl widget."""

from typing import Any

from PySide6 import QtWidgets

from qms.layouts.spectrum_control_ui import Ui_spectrum_control


class SpectrumControl(QtWidgets.QWidget, Ui_spectrum_control):
    """SpectrumControl is a widget that allows spectrum measurement configuration."""

    def __init__(self, *args: Any, **kwargs: Any):
        """Initialize with default configuration."""
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    def load_profile(self) -> None:
        """Load data from currently loaded profile."""
        # TODO: Implement
