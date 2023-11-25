"""Contains MapPlot widget."""

import logging
from typing import Any, Literal

import numpy as np
from matplotlib.backends.backend_qt import NavigationToolbar2QT
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.collections import QuadMesh
from matplotlib.figure import Figure
from PySide6 import QtWidgets
from PySide6.QtGui import QResizeEvent

from qms.layouts.map_plot_ui import Ui_map_plot

logger = logging.getLogger("main")


class MplCanvas(FigureCanvasQTAgg):
    """Custom matplotlib canvas for use with MapPlot widget."""

    def __init__(self) -> None:
        """Initialize with default configuration."""
        figure = Figure()
        super().__init__(figure)

        self.axes = figure.add_subplot(111)
        self.mesh: QuadMesh | None = None
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

    def update_drawing(self) -> None:
        """Re-render the plot."""
        self.draw()

    def new_plot(
        self,
        x_coords: np.ndarray[Literal["N"], np.dtype[np.float_]],
        y_coords: np.ndarray[Literal["N"], np.dtype[np.float_]],
        data: np.ndarray[Literal["N"], np.dtype[np.float_]],
    ) -> None:
        """Create new colormesh with new coordinates."""
        self.mesh = self.axes.pcolormesh(x_coords, y_coords, data, shading="nearest")
        self.update_drawing()

    def update_data(self, data: np.ndarray[Literal["N"], np.dtype[np.float_]]) -> None:
        """Update data for color mesh."""
        if self.mesh is not None:
            self.mesh.set_array(data)
            self.update_drawing()
        else:
            logger.error("Trying to update plot when no plot was created")

    def set_range(self, minimum: float, maximum: float) -> None:
        """Set range for plot."""
        if self.mesh is not None:
            self.mesh.set_clim(minimum, maximum)
        else:
            logger.error("Trying to update plot when no plot was created")

    def resizeEvent(self, event: QResizeEvent) -> None:  # noqa: N802
        """Handle resize event - update layout."""
        super().resizeEvent(event)
        self.figure.tight_layout(pad=0.5)


class MapPlot(QtWidgets.QWidget, Ui_map_plot):
    """Widget for plotting results from map scans."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize with default configuration."""
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.canvas = MplCanvas()
        self.layout().replaceWidget(self.canvas_temp, self.canvas)
        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        self.layout().replaceWidget(self.toolbar_temp, self.toolbar)

        self.data: np.ndarray[Literal["N"], np.dtype[Any]] = np.zeros(4)
        self.x_coords: np.ndarray[Literal["N"], np.dtype[Any]] = np.zeros(4)
        self.y_coords: np.ndarray[Literal["N"], np.dtype[Any]] = np.zeros(4)

    def new_plot(
        self,
        x_coords: np.ndarray[Literal["N", "N"], np.dtype[np.float_]],
        y_coords: np.ndarray[Literal["N", "N"], np.dtype[np.float_]],
    ) -> None:
        """Start new plot."""
        self.data = np.zeros(x_coords.shape)
        self.x_coords = x_coords
        self.y_coords = y_coords

        self.canvas.axes.set_xlim(float(np.min(x_coords)), float(np.max(x_coords)))
        self.canvas.axes.set_ylim(float(np.min(y_coords)), float(np.max(y_coords)))

        self.canvas.new_plot(x_coords, y_coords, self.data)
        self.canvas.update_drawing()

    def new_point(self, x: int, y: int, value: float) -> None:
        """Add new data point."""
        self.data[y, x] = value
        self.canvas.update_data(self.data)
        self.canvas.set_range(np.min(self.data), np.max(self.data))
