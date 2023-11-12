"""Module contains SpectrumView class."""
from pyparsing import Any
from PySide6 import QtWidgets

from qms.layouts.spectrum_view_ui import Ui_SpectrumView


class SpectrumView(QtWidgets.QWidget, Ui_SpectrumView):
    """SpectrumView is a QWidget that allows run spectra measurements and view the resuls."""

    def __init__(self, *args: Any, **kwargs: Any):
        """Init SpectrumView together with GUI."""
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    def set_allow_new_scans(self, allow: bool = True, reason: str = "") -> None:
        """Change if starting new scans is allowed."""
