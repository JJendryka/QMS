import logging
from PySide6 import QtWidgets
from PySide6.QtGui import QResizeEvent
from backend.resonance_scan import ResonanceScanner

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gui.main_window import MainWindow

from layouts.diagnostic_view_ui import Ui_diagnostic_view

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure

logger = logging.getLogger("main")


class Plot(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Plot, self).__init__(parent)
        self.setLayout(QtWidgets.QVBoxLayout())
        self.canvas = MplCanvas(self)
        self.layout().addWidget(self.canvas)
        self.layout().addWidget(NavigationToolbar2QT(self.canvas, self))

        self.x_data = []
        self.y_data = []

    def add_point(self, x, y):
        logger.debug("Adding point to graph")
        self.canvas.x_data.append(x)
        self.canvas.y_data.append(y)

        self.canvas.line.set_xdata(self.x_data)
        self.canvas.line.set_ydata(self.y_data)

        self.canvas.draw()

    def clear_points(self):
        self.canvas.x_data = []
        self.canvas.y_data = []

        self.canvas.line.set_xdata(self.x_data)
        self.canvas.line.set_ydata(self.y_data)

        self.canvas.draw()


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None):
        self.x_data = []
        self.y_data = []
        fig = Figure()
        self.axes = fig.add_subplot(111)
        (self.line,) = self.axes.plot(self.x_data, self.y_data)
        super(MplCanvas, self).__init__(fig)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

    def resizeEvent(self, event: QResizeEvent):  # noqa: N802
        super(MplCanvas, self).resizeEvent(event)
        self.figure.tight_layout(pad=0.5)


class DiagnosticView(QtWidgets.QWidget, Ui_diagnostic_view):
    def __init__(self, *args, **kwargs) -> None:
        super(DiagnosticView, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.main_window: MainWindow | None = None
        self.resonance_plot = Plot(self)

        self.replace_charts()
        self.setup_signals()

    def setup_signals(self) -> None:
        self.resonance_scan_button.clicked.connect(self.start_resonance_scan)

    def start_resonance_scan(self) -> None:
        if self.main_window is not None:
            if self.main_window.euromeasure is not None:
                self.resonance_plot.clear_points()
                scanner = ResonanceScanner(
                    self.main_window.euromeasure,
                    float(self.min_frequency_lineedit.text()) * 1e6,
                    float(self.max_frequency_lineedit.text()) * 1e6,
                    self.frequency_steps_spinbox.value(),
                )
                scanner.signals.data_point_acquired.connect(self.received_resonance_scan_point)
                self.main_window.thread_pool.start(scanner)
            else:
                logger.error("EuroMeasure system is not connected")
        else:
            logger.error("Main window reference is not set")

    def received_resonance_scan_point(self, frequency: float, voltage: float) -> None:
        logger.debug("Received resonance scan point")
        self.resonance_plot.add_point(frequency, voltage)

        # Find maximum here

    def replace_charts(self) -> None:
        self.layout().replaceWidget(self.resonance_chart, self.resonance_plot)

        rf_chart = Plot(self)
        self.layout().replaceWidget(self.rf_chart, rf_chart)

        rf_stability_chart = Plot(self)
        self.layout().replaceWidget(self.rf_stability_chart, rf_stability_chart)

        source_chart = Plot(self)
        self.layout().replaceWidget(self.source_chart, source_chart)

        source_stability_chart = Plot(self)
        self.layout().replaceWidget(self.source_stability_chart, source_stability_chart)
