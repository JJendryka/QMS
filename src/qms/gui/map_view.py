"""Contains MapView widget."""
from typing import Any

from PySide6 import QtWidgets

from qms.layouts.map_view_ui import Ui_map_view


class MapView(QtWidgets.QWidget, Ui_map_view):
    """MapView is a widget that allows for controling map scans and viewing the results."""

    def __init__(self, *args: Any, **kwargs: Any):
        """Initialize with default configuration."""
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    def set_allow_new_scans(self, allow: bool = True, reason: str = "") -> None:
        """Change is starting new scans is allowed."""

    def load_profile(self) -> None:
        """Load data from currently loaded profile."""
        self.map_control.load_profile()
