from PySide6 import QtWidgets, QtGui, QtCore

import serial.tools.list_ports
from backend.euromeasure import EMCannotConnectError, EuroMeasure
from backend.fake_euromeasure import FakeEuroMeasure
from config import Config

from layouts.main_window_ui import Ui_MainWindow

import logging

logger = logging.getLogger("main")


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.euromeasure: EuroMeasure | None = None
        self.thread_pool = QtCore.QThreadPool(self)

        self.setup_backreferences()
        self.showMaximized()
        self.setup_callbacks()

        logger.debug("Finished main_window initialization")

    def setup_backreferences(self) -> None:
        self.diagnostic_tab.main_window = self

    def setup_callbacks(self) -> None:
        self.connection_menu.aboutToShow.connect(self.fill_connection_menu)

    def fill_connection_menu(self) -> None:
        for action in self.connection_menu.actions():
            self.connection_menu.removeAction(action)

        if self.euromeasure is None:
            logger.debug("Searching for ports")
            ports = serial.tools.list_ports.comports()
            for port, desc, hwid in sorted(ports):
                logger.debug("Found port: %s with description: %s, hwid: %s", port, desc, hwid)
                action = QtGui.QAction(f"{port} - {desc}", self)
                action.triggered.connect((lambda a: lambda: self.connect_port(a))(port))
                self.connection_menu.addAction(action)

            if not ports:
                logger.info("There are no ports found")
                action = QtGui.QAction("No ports found", self)
                action.setEnabled(False)
                self.connection_menu.addAction(action)

            if Config.get().args.debug:
                action = QtGui.QAction("Debug port", self)
                action.triggered.connect((lambda a: lambda: self.connect_port(a))("debug/port"))
                self.connection_menu.addAction(action)

        else:
            action = QtGui.QAction("Disconnect", self)
            action.triggered.connect(self.disconnect_port)
            self.connection_menu.addAction(action)

    def connect_port(self, port: str) -> None:
        logger.info("Connecting to port: %s", port)
        self.connection_menu.setTitle(f"Connected to: {port}")
        if self.euromeasure is not None:
            self.euromeasure.disconnect()
            self.euromeasure = None
            logger.warn("Connect when other port is already connected")
        if Config.get().args.debug:
            self.euromeasure = FakeEuroMeasure()
        else:
            self.euromeasure = EuroMeasure()

        try:
            self.euromeasure.connect(port)
        except EMCannotConnectError:
            self.euromeasure = None
            logger.error("Couldn't connect to port")

    def disconnect_port(self) -> None:
        logger.info("Disconnecting from serial port")
        self.connection_menu.setTitle("Connect")
        if self.euromeasure is not None:
            self.euromeasure.disconnect()
            self.euromeasure = None
        else:
            logger.warn("Trying to disconnect already disconnected port")
