from PySide6 import QtWidgets
from pyparsing import Any

from qms.layouts.spectrum_view_ui import Ui_SpectrumView


class SpectrumView(QtWidgets.QWidget, Ui_SpectrumView):
    def __init__(self, *args: Any, **kwargs: Any):
        super(SpectrumView, self).__init__(*args, **kwargs)
        self.setupUi(self)

    def set_allow_new_scans(self, allow: bool = True, reason: str = "") -> None:
        pass
