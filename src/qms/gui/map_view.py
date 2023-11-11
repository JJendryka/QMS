from PySide6 import QtWidgets

from qms.layouts.map_view_ui import Ui_map_view


class MapView(QtWidgets.QWidget, Ui_map_view):
    def __init__(self, *args, **kwargs) -> None:
        super(MapView, self).__init__(*args, **kwargs)
        self.setupUi(self)

    def set_allow_new_scans(self, allow=True, reason: str = ""):
        pass
