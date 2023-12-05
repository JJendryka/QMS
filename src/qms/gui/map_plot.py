"""Contains MapPlot widget."""

import logging
from typing import Any, Literal

import numpy as np
from matplotlib import colors
from matplotlib.backends.backend_qt import NavigationToolbar2QT
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.collections import QuadMesh
from matplotlib.figure import Figure
from matplotlib.lines import Line2D
from PySide6 import QtWidgets
from PySide6.QtGui import QResizeEvent

from qms.layouts.map_plot_ui import Ui_map_plot
from qms.misc import Array2Df, UILock

logger = logging.getLogger("main")


class MplCanvas(FigureCanvasQTAgg):
    """Custom matplotlib canvas for use with MapPlot widget."""

    def __init__(self) -> None:
        """Initialize with default configuration."""
        figure = Figure()
        super().__init__(figure)

        self.axes = figure.add_subplot(111)
        self.mesh: QuadMesh | None = None
        self.line: Line2D | None = None
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

    def new_plot(
        self,
        x_coords: np.ndarray[Literal["N"], np.dtype[np.float_]],
        y_coords: np.ndarray[Literal["N"], np.dtype[np.float_]],
        data: np.ndarray[Literal["N"], np.dtype[np.float_]],
    ) -> None:
        """Create new colormesh with new coordinates."""
        self.axes.clear()
        self.mesh = self.axes.pcolormesh(x_coords, y_coords, data, shading="nearest")
        (self.line,) = self.axes.plot([np.min(x_coords).item(), np.max(x_coords).item()], [0, 0], color="red")
        self.draw()

    def update_data(self, data: np.ndarray[Literal["N"], np.dtype[np.float_]]) -> None:
        """Update data for color mesh."""
        if self.mesh is not None:
            self.mesh.set_array(data)
            self.draw()
        else:
            logger.error("Trying to update plot when no plot was created")

    def update_line(self, a: float, b: float) -> None:
        """Update scanline with linear function parameters."""
        if self.line is not None:
            self.line.set_ydata(np.asanyarray(self.line.get_xdata()) * a + b)
            self.draw()

    def set_range(self, minimum: float, maximum: float, logarithmic: bool) -> None:
        """Set range for plot."""
        if self.mesh is not None:
            if not logarithmic:
                self.mesh.set_norm(colors.Normalize(minimum, maximum))
            else:
                self.mesh.set_norm(colors.LogNorm(max(0, minimum), max(0, maximum)))
            self.draw()
        else:
            logger.error("Trying to update plot when no plot was created")

    def set_scanline_visibility(self, visible: bool) -> None:
        """Change scanline visibility."""
        if self.line is not None:
            self.line.set_visible(visible)
            self.draw()

    def set_x_range(self, minimum: float, maximum: float) -> None:
        """Set x range."""
        self.axes.set_xlim(minimum, maximum)
        self.draw()

    def set_y_range(self, minimum: float, maximum: float) -> None:
        """Set x range."""
        self.axes.set_ylim(minimum, maximum)
        self.draw()

    def resizeEvent(self, event: QResizeEvent) -> None:  # noqa: N802
        """Handle resize event - update layout."""
        super().resizeEvent(event)
        self.figure.tight_layout(pad=0.5)


class MapPlot(QtWidgets.QWidget, Ui_map_plot):
    """Widget for plotting results from map scans."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize with default configuration."""
        super().__init__(*args, **kwargs)

        self.data: Array2Df | None = None
        self.x_coords: Array2Df | None = None
        self.y_coords: Array2Df | None = None

        self.ui_lock: UILock = UILock()

        self.setupUi(self)
        self.canvas = MplCanvas()
        self.layout().replaceWidget(self.canvas_temp, self.canvas)
        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        self.layout().replaceWidget(self.toolbar_temp, self.toolbar)

        self.connect_signals()

    def connect_signals(self) -> None:
        """Connect all needed signals."""
        self.log_checkbox.clicked.connect(self.set_scale)
        self.scale_current_checkbox.clicked.connect(self.current_autoscale_changed)
        self.current_min_lineedit.editingFinished.connect(self.ui_lock(self.current_scale_changed))
        self.current_max_lineedit.editingFinished.connect(self.ui_lock(self.current_scale_changed))
        self.scale_rf_button.clicked.connect(self.scale_rf)
        self.scale_dc_button.clicked.connect(self.scale_dc)
        self.scanline_checkbox.clicked.connect(self.scanline_visibility_changed)

    def new_plot(
        self,
        x_coords: np.ndarray[Literal["N", "N"], np.dtype[np.float_]],
        y_coords: np.ndarray[Literal["N", "N"], np.dtype[np.float_]],
        scanline_a: float,
        scanline_b: float,
    ) -> None:
        """Start new plot."""
        self.data = np.ma.masked_all(x_coords.shape)
        self.x_coords = x_coords
        self.y_coords = y_coords

        self.canvas.set_x_range(float(np.min(x_coords)), float(np.max(x_coords)))
        self.canvas.set_y_range(float(np.min(y_coords)), float(np.max(y_coords)))

        self.canvas.new_plot(x_coords, y_coords, self.data)
        self.canvas.update_line(scanline_a, scanline_b)

    def new_point(self, x: int, y: int, value: float) -> None:
        """Add new data point."""
        if self.data is not None:
            self.data[y, x] = value
            self.canvas.update_data(self.data)
            self.set_scale()

    def current_autoscale_changed(self, *_: Any) -> None:
        """Handle autoscaling status change - set scale."""
        self.set_scale()

    def current_scale_changed(self, *_: Any) -> None:
        """Handle user changing current scale manually."""
        with self.ui_lock:
            self.scale_current_checkbox.setChecked(False)
        self.set_scale()

    def scale_rf(self, *_: Any) -> None:
        """Autoscale rf on user request."""
        if self.x_coords is not None:
            minimum = np.min(self.x_coords).item()
            maximum = np.max(self.x_coords).item()
            self.canvas.set_x_range(minimum, maximum)

    def scale_dc(self, *_: Any) -> None:
        """Autoscale dc on user request."""
        if self.y_coords is not None:
            minimum = np.min(self.y_coords).item()
            maximum = np.max(self.y_coords).item()
            self.canvas.set_y_range(minimum, maximum)

    def set_scale(self) -> None:
        """Set scale according to UI."""
        if self.data is not None:
            if self.scale_current_checkbox.isChecked():
                minimum = np.min(self.data).item()
                maximum = np.max(self.data).item()
                self.canvas.set_range(minimum, maximum, self.log_checkbox.isChecked())
                self.canvas.draw()
                with self.ui_lock:
                    self.current_min_lineedit.setText(f"{minimum:.2E}")
                    self.current_max_lineedit.setText(f"{maximum:.2E}")
            else:
                minimum = float(self.current_min_lineedit.text())
                maximum = float(self.current_max_lineedit.text())
                print(minimum, maximum)
                self.canvas.set_range(minimum, maximum, self.log_checkbox.isChecked())
                self.canvas.draw()

    def scanline_visibility_changed(self, *_: Any) -> None:
        """Update scanline visibiliy on UI change."""
        self.canvas.set_scanline_visibility(self.scanline_checkbox.isChecked())

    def update_scanline(self, a: float, b: float) -> None:
        """Update scanline based on linear function parameters."""
        self.canvas.update_line(a, b)
