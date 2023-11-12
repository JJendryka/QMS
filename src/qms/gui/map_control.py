from typing import Any
from PySide6 import QtWidgets
from qms.layouts.map_control_ui import Ui_map_control


class MapControl(QtWidgets.QWidget, Ui_map_control):
    def __init__(self, *args: Any, **kwargs: Any):
        super(MapControl, self).__init__(*args, **kwargs)
        self.setupUi(self)
