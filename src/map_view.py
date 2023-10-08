from PySide6 import QtWidgets

from layouts.map_view_ui import Ui_map_view


class MapView(QtWidgets.QWidget, Ui_map_view):
    def __init__(self, *args, **kwargs) -> None:
        super(MapView, self).__init__(*args, **kwargs)
        self.setupUi(self)