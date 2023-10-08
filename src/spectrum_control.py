from PySide6 import QtWidgets
from layouts.spectrum_control_ui import Ui_spectrum_control


class SpectrumControl(QtWidgets.QWidget, Ui_spectrum_control):
    def __init__(self, *args, **kwargs) -> None:
        super(SpectrumControl, self).__init__(*args, **kwargs)
        self.setupUi(self)
