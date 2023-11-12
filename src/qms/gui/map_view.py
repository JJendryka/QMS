from typing import Any
from PySide6 import QtWidgets

from qms.layouts.map_view_ui import Ui_map_view


class MapView(QtWidgets.QWidget, Ui_map_view):
    def __init__(self, *args: Any, **kwargs: Any):
        super(MapView, self).__init__(*args, **kwargs)
        self.setupUi(self)

    def set_allow_new_scans(self, allow: bool = True, reason: str = "") -> None:
        pass
