"""Contains SpectrumPlot widget."""

from typing import Any

import numpy as np
from matplotlib.backends.backend_qt import NavigationToolbar2QT
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PySide6 import QtWidgets
from PySide6.QtGui import QResizeEvent

from qms.layouts.spectrum_plot_ui import Ui_spectrum_plot
from qms.misc import Array1Df


class Canvas(FigureCanvasQTAgg):
    """Customized canvas for use with SpectrumPlot."""

    def __init__(self) -> None:
        """Initialize with default configuration."""
        figure = Figure()
        self.axes = figure.add_subplot(111)
        super().__init__(figure)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

    def resizeEvent(self, event: QResizeEvent) -> None:  # noqa: N802
        """Handle resizeEvent - update layout."""
        super().resizeEvent(event)
        self.figure.tight_layout(pad=0.5)


class SpectrumPlot(QtWidgets.QWidget, Ui_spectrum_plot):
    """Widget for plotting results of spectrum measurement."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize with default configuration."""
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.canvas = Canvas()
        self.nav_bar = NavigationToolbar2QT(self.canvas, self)
        self.layout().replaceWidget(self.plot, self.canvas)
        self.layout().replaceWidget(self.navigation_bar, self.nav_bar)

        self.y_current: list[Array1Df] = []
        self.x_volts: list[Array1Df] = []

    def clear(self) -> None:
        """Clear plot history."""
        self.y_current = []
        self.x_volts = []

    def new_scan(self, rf_values: Array1Df) -> None:
        """Start saving to new scan."""
        self.y_current.append(np.ma.masked_all(rf_values.shape))
        self.x_volts.append(rf_values)

    def new_point(self, rf_step: int, current: float) -> None:
        """Add new point to plot."""
        self.y_current[-1][rf_step] = current
