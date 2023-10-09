from PySide6 import QtWidgets
from PySide6.QtGui import QResizeEvent

from layouts.diagnostic_view_ui import Ui_diagnostic_view

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure


class Plot(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Plot, self).__init__(parent)
        self.setLayout(QtWidgets.QVBoxLayout())
        canvas = MplCanvas(self)
        self.layout().addWidget(canvas)
        self.layout().addWidget(NavigationToolbar2QT(canvas, self))


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None):
        fig = Figure()
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

    def resizeEvent(self, event: QResizeEvent):  # noqa: N802
        super(MplCanvas, self).resizeEvent(event)
        self.figure.tight_layout(pad=0.5)


class DiagnosticView(QtWidgets.QWidget, Ui_diagnostic_view):
    def __init__(self, *args, **kwargs) -> None:
        super(DiagnosticView, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.replace_charts()

    def replace_charts(self) -> None:
        resonance_chart = Plot(self)
        self.layout().replaceWidget(self.resonance_chart, resonance_chart)

        rf_chart = Plot(self)
        self.layout().replaceWidget(self.rf_chart, rf_chart)

        rf_stability_chart = Plot(self)
        self.layout().replaceWidget(self.rf_stability_chart, rf_stability_chart)

        source_chart = Plot(self)
        self.layout().replaceWidget(self.source_chart, source_chart)

        source_stability_chart = Plot(self)
        self.layout().replaceWidget(self.source_stability_chart, source_stability_chart)
