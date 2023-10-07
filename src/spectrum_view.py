from PySide6 import QtWidgets

from layouts.spectrum_view_ui import Ui_SpectrumView


class SpectrumView(QtWidgets.QWidget, Ui_SpectrumView):
    def __init__(self, *args, **kwargs) -> None:
        super(SpectrumView, self).__init__(*args, **kwargs)
        self.setupUi(self)
