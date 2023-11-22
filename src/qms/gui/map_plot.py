"""Contains MapPlot widget."""

from typing import Any, Literal

import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
from PySide6 import QtWidgets
from PySide6.QtGui import QResizeEvent

from qms.layouts.map_plot_ui import Ui_map_plot


class MplCanvas(FigureCanvasQTAgg):
    """Custom matplotlib canvas for use with MapPlot widget."""

    def __init__(self, parent: QtWidgets.QWidget | None = None):
        """Initialize with default configuration."""
        self.data: np.ndarray[Literal["N"], np.dtype[Any]] = np.zeros(4)
        self.x_coords: np.ndarray[Literal["N"], np.dtype[Any]] = np.zeros(4)
        self.y_coords: np.ndarray[Literal["N"], np.dtype[Any]] = np.zeros(4)

        figure = Figure()
        self.axes = figure.add_subplot(111)
        self.axes.pcolormesh([self.x_coords, self.y_coords, self.data], shading="nearest")

        super().__init__(figure)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

    def resizeEvent(self, event: QResizeEvent) -> None:  # noqa: N802
        """Handle resize event - update layout."""
        super().resizeEvent(event)
        self.figure.tight_layout(pad=0.5)


class Plot(QtWidgets.QWidget):
    """Custom Plot widget used in MapPlot."""

    def __init__(self, parent: QtWidgets.QWidget | None = None):
        """Initialize with GUI."""
        super().__init__(parent)
        self.setLayout(QtWidgets.QVBoxLayout())
        self.canvas = MplCanvas(self)
        self.layout().addWidget(self.canvas)
        self.layout().addWidget(NavigationToolbar2QT(self.canvas, self))

    def new_plot(self, size_x: int, min_x: float, max_x: float, size_y: int, min_y: float, max_y: float) -> None:
        """Start new plot."""
        self.canvas.data = np.zeros(size_x * size_y)
        self.canvas.x_coords = np.zeros(size_x * size_y)
        self.canvas.y_coords = np.zeros(size_x * size_y)

        self.canvas.axes.set_xlim(min_x, max_x)
        self.canvas.axes.set_ylim(min_y, max_y)

        self.update_drawing()

    def insert_point(self, index: int, x: float, y: float, value: float) -> None:
        """Add new data point to plot."""
        self.canvas.data[index] = value
        self.canvas.x_coords[index] = x
        self.canvas.y_coords[index] = y

    def update_drawing(self) -> None:
        """Update drawn plot."""
        self.canvas.draw()

    def clear_points(self) -> None:
        """Clear all points from plot."""
        self.data: np.ndarray[Literal["N"], np.dtype[Any]] = np.zeros(4)
        self.y_coords: np.ndarray[Literal["N"], np.dtype[Any]] = np.zeros(4)
        self.x_coords: np.ndarray[Literal["N"], np.dtype[Any]] = np.zeros(4)

        self.update_drawing()


class MapPlot(QtWidgets.QWidget, Ui_map_plot):
    """Widget for plotting results from map scans."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize with default configuration."""
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.plot = Plot(self)
        self.layout().replaceWidget(self.chart, self.plot)
