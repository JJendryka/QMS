from PySide6 import QtWidgets
from PySide6.QtGui import QResizeEvent

from layouts.spectrum_plot_ui import Ui_spectrum_plot

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure


class Canvas(FigureCanvasQTAgg):
    def __init__(self, parent=None):
        figure = Figure()
        self.axes = figure.add_subplot(111)
        super(Canvas, self).__init__(figure)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

    def resizeEvent(self, event: QResizeEvent):
        super(Canvas, self).resizeEvent(event)
        self.figure.tight_layout(pad=0.5)


class SpectrumPlot(QtWidgets.QWidget, Ui_spectrum_plot):
    def __init__(self, *args, **kwargs) -> None:
        super(SpectrumPlot, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.canvas = Canvas(self)
        self.nav_bar = NavigationToolbar2QT(self.canvas, self)
        self.layout().replaceWidget(self.plot, self.canvas)
        self.layout().replaceWidget(self.navigation_bar, self.nav_bar)
