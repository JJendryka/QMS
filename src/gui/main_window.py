from PySide6 import QtWidgets
from PySide6 import QtGui

import serial.tools.list_ports

from layouts.main_window_ui import Ui_MainWindow

import logging

logger = logging.getLogger("main")


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.showMaximized()
        self.setup_callbacks()

        self.selected_port: str | None = None

        logger.debug("Finished main_window initialization")

    def setup_callbacks(self) -> None:
        self.connection_menu.aboutToShow.connect(self.fill_connection_menu)

    def fill_connection_menu(self) -> None:
        for action in self.connection_menu.actions():
            self.connection_menu.removeAction(action)

        if self.selected_port is None:
            logger.debug("Searching for ports")
            ports = serial.tools.list_ports.comports()
            for port, desc, hwid in sorted(ports):
                logger.debug("Found port: %s with description: %s, hwid: %s", port, desc, hwid)
                action = QtGui.QAction(f"{port} - {desc}", self)
                action.triggered.connect((lambda a: lambda: self.connect_port(a))(port))
                self.connection_menu.addAction(action)
        else:
            action = QtGui.QAction("Disconnect", self)
            action.triggered.connect(self.disconnect_port)
            self.connection_menu.addAction(action)

    def connect_port(self, port: str) -> None:
        logger.info("Connecting to port: %s", port)
        self.connection_menu.setTitle(f"Connected to: {port}")
        self.selected_port = port

    def disconnect_port(self) -> None:
        logger.info("Disconnecting from serial port")
        self.connection_menu.setTitle("Connect")
        self.selected_port = None
