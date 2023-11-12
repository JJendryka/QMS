from typing import Any
from PySide6 import QtWidgets
from qms.layouts.spectrum_control_ui import Ui_spectrum_control


class SpectrumControl(QtWidgets.QWidget, Ui_spectrum_control):
    def __init__(self, *args: Any, **kwargs: Any):
        super(SpectrumControl, self).__init__(*args, **kwargs)
        self.setupUi(self)
