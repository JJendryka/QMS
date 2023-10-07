from os import replace
from PySide6 import QtWidgets
from PySide6.QtGui import QResizeEvent

from layouts.diagnostic_view_ui import Ui_DiagnosticView

from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure()
        fig.tight_layout(pad=3)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

    def resizeEvent(self, event: QResizeEvent):
        super(MplCanvas, self).resizeEvent(event)
        self.figure.tight_layout(pad=0.5)


class DiagnosticView(QtWidgets.QWidget, Ui_DiagnosticView):
    def __init__(self, *args, **kwargs) -> None:
        super(DiagnosticView, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.replace_charts()

    def replace_charts(self) -> None:
        resonance_chart = MplCanvas(self)
        self.layout().replaceWidget(self.resonance_chart, resonance_chart)

        rf_chart = MplCanvas(self)
        self.layout().replaceWidget(self.rf_chart, rf_chart)

        rf_stability_chart = MplCanvas(self)
        self.layout().replaceWidget(self.rf_stability_chart, rf_stability_chart)

        source_chart = MplCanvas(self)
        self.layout().replaceWidget(self.source_chart, source_chart)

        source_stability_chart = MplCanvas(self)
        self.layout().replaceWidget(self.source_stability_chart, source_stability_chart)
