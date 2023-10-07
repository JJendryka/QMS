from PySide6 import QtWidgets

from layouts.diagnostic_view_ui import Ui_DiagnosticView


class DiagnosticView(QtWidgets.QWidget, Ui_DiagnosticView):
    def __init__(self, *args, **kwargs) -> None:
        super(DiagnosticView, self).__init__(*args, **kwargs)
        self.setupUi(self)
