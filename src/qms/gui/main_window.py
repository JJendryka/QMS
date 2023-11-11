import json
from pathlib import Path
from PySide6 import QtWidgets, QtGui, QtCore

import serial.tools.list_ports
from qms.backend.euromeasure import EMCannotConnectError, EuroMeasure
from qms.backend.fake_euromeasure import FakeEuroMeasure
from qms.config import Config
from qms.consts import LAST_STATE_FILENAME

from qms.layouts.main_window_ui import Ui_MainWindow

import logging

from qms.misc import get_home_dir

logger = logging.getLogger("main")


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Setting so that closing works correctly when any dialog is shown
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_DeleteOnClose, True)

        self.euromeasure: EuroMeasure | None = None
        self.thread_pool = QtCore.QThreadPool(self)

        self.setup_backreferences()
        self.showMaximized()
        self.setup_callbacks()
        logger.debug("Finished main_window initialization")

        load_last_state()
        self.open_profile()

        self.set_allow_new_scans(False, "EuroMeasure is not connected")

    def setup_backreferences(self) -> None:
        self.diagnostic_tab.main_window = self

    def setup_callbacks(self) -> None:
        self.connection_menu.aboutToShow.connect(self.fill_connection_menu)
        self.load_profile_action.triggered.connect(self.open_profile)
        self.save_profile_action.triggered.connect(self.save_profile)

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
            self.set_allow_new_scans(True)
        except EMCannotConnectError:
            self.euromeasure = None
            logger.error("Couldn't connect to port")
            QtWidgets.QMessageBox.critical(self, "Error!", "Couldn't connect to EuroMeasure system on this port")

    def disconnect_port(self) -> None:
        logger.info("Disconnecting from serial port")
        self.connection_menu.setTitle("Connect")
        if self.euromeasure is not None:
            self.euromeasure.disconnect()
            self.euromeasure = None
        else:
            logger.warn("Trying to disconnect already disconnected port")
        self.set_allow_new_scans(False, "EuroMeasure is not connected")

    def set_allow_new_scans(self, allow=True, reason: str = "") -> None:
        self.diagnostic_tab.set_allow_new_scans(allow, reason)
        self.spectrum_tab.set_allow_new_scans(allow, reason)
        self.stability_map_tab.set_allow_new_scans(allow, reason)

    def closeEvent(self, event: QtGui.QCloseEvent):  # noqa: N802
        logger.debug("Saving state to file")
        json_object = Config.get().state.dump_to_json()

        with open(get_home_dir() / LAST_STATE_FILENAME, "w") as json_file:
            json_file.write(json.dumps(json_object))
        self.save_profile()

        super().closeEvent(event)

    def open_profile(self):
        dialog = ProfileOpenDialog(self)
        dialog.finished.connect(self.open_profile_finished)
        dialog.exec()

    def open_profile_finished(self):
        opened_profile = Config.get().state.loaded_profile
        if (opened_profile is None or not opened_profile) and self.isVisible():
            self.open_profile()

        if opened_profile is not None and Path(opened_profile).exists():
            with open(opened_profile, "r") as json_file:
                json_object = json.load(json_file)
                Config.get().spectrometer_config.load_from_json(json_object["spectrometer"])

    def save_profile(self):
        profile_filename = Config.get().state.loaded_profile
        if profile_filename is not None:
            logger.debug(f"Saving config to {profile_filename}")
            json_object = {"spectrometer": Config.get().spectrometer_config.dump_to_json()}
            with open(profile_filename, "w") as json_file:
                json.dump(json_object, json_file)


class ProfileOpenDialog(QtWidgets.QDialog):
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Open profile...")
        v_layout = QtWidgets.QVBoxLayout()
        h_layout = QtWidgets.QHBoxLayout()
        message = QtWidgets.QLabel(parent=parent, text="Select which profile to open...")
        v_layout.addWidget(message)
        v_layout.addLayout(h_layout)
        self.create_new_button = QtWidgets.QPushButton(parent=parent, text="Create new")
        self.load_other_button = QtWidgets.QPushButton(parent=parent, text="Load other")
        self.create_new_button.clicked.connect(self.on_create_new)
        self.load_other_button.clicked.connect(self.on_load_existing)
        h_layout.addWidget(self.load_other_button)
        h_layout.addWidget(self.create_new_button)
        self.setLayout(v_layout)
        self.setWindowModality(QtCore.Qt.WindowModality.WindowModal)

        if Config.get().state.loaded_profile is None:
            self.setWindowFlags(QtCore.Qt.WindowType.Dialog | QtCore.Qt.WindowType.FramelessWindowHint)

        previous_profile = Config.get().state.previous_profile
        if previous_profile is not None and previous_profile and Path(previous_profile).exists():
            name = Path(Config.get().state.previous_profile).stem
            self.load_last_button = QtWidgets.QPushButton(parent=parent, text=f"Load last: {name}")
            self.load_last_button.clicked.connect(self.on_load_last)
            h_layout.addWidget(self.load_last_button)

    def on_create_new(self):
        path = get_home_dir() / "profiles"
        path.mkdir(exist_ok=True, parents=True)
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            self.parent(), "Save profile to...", str(path), "JSON files (*.json)"
        )
        if filename is not None and filename:
            path = Path(filename)
            path = path.with_suffix(".json")
            Config.get().state.loaded_profile = str(path)
            self.close()

    def on_load_existing(self):
        path = get_home_dir() / "profiles"
        path.mkdir(exist_ok=True, parents=True)
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            self.parent(), "Load profile from...", str(path), "JSON files (*.json)"
        )
        if filename is not None and filename:
            Config.get().state.loaded_profile = filename
            self.close()

    def on_load_last(self):
        Config.get().state.loaded_profile = Config.get().state.previous_profile
        self.close()


def load_last_state():
    file = get_home_dir() / LAST_STATE_FILENAME
    if file.exists():
        logger.debug("Loading last state")
        with open(file, "r") as json_file:
            json_object = json.load(json_file)
            Config.get().state.load_from_json(json_object)
    else:
        logger.info("There is no previous state found. Initializing with defaults")
