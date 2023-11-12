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

        self.set_allow_new_scans(False, "EuroMeasure is not connected")

    def setup_backreferences(self) -> None:
        self.diagnostic_tab.main_window = self

    def setup_callbacks(self) -> None:
        self.connection_menu.aboutToShow.connect(self.fill_connection_menu)
        self.load_profile_action.triggered.connect(self.load_profile)
        self.save_profile_action.triggered.connect(self.save_profile)
        self.save_profile_as_action.triggered.connect(self.save_profile_as)

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

        # TODO: Ask user whether to save profile

        super().closeEvent(event)

    def set_loaded_profile(self, path):
        """Set currently loaded profile to path. Don't actually load the profile."""
        if path is not None and path.exists():
            Config.get().state.loaded_profile = path
            Config.get().state.add_recent_profile(path)
            profile_name = path.stem
            self.profile_menu.setTitle(f"Profile: {profile_name}")

    def load_profile(self) -> None:
        """Load profile from path selected by user."""
        path = self.load_profile_dialog()
        if path is not None:
            self.load_profile_from(path)

    def load_profile_dialog(self) -> None | Path:
        """Ask user for path of the profile to load."""
        path = get_home_dir() / "profiles"
        path.mkdir(exist_ok=True, parents=True)
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Load profile from...", str(path), "JSON files (*.json)"
        )
        if filename is not None and filename:
            return Path(filename).with_suffix(".json")
        return None

    def load_profile_from(self, path: Path) -> None:
        """Load profile from path."""
        if path is not None and path.exists():
            logger.info(f"Opening profile: {path}")
            try:
                with open(path, "r") as json_file:
                    json_object = json.load(json_file)
                    Config.get().spectrometer_config.load_from_json(json_object["spectrometer"])
                self.set_loaded_profile(path)
            except OSError as e:
                logger.error(f"Cannot load profile: {path}, os error: {e.strerror}")
        else:
            logger.error(f"Cannot load profile {path}, file doesn't exist")

    def save_profile(self) -> None:
        """Save profile to currently loaded profile file."""
        path = Config.get().state.loaded_profile
        self.save_profile_to(path)

    def save_profile_to(self, path: Path) -> None:
        """Save profile to path."""
        if path is not None:
            logger.info(f"Saving profile to: {path}")
            json_object = {"spectrometer": Config.get().spectrometer_config.dump_to_json()}
            try:
                with open(path, "w") as json_file:
                    json.dump(json_object, json_file)
            except OSError as e:
                logger.error(f"Cannot save profile to: {path}. OS Error: {e.strerror}")

    def save_profile_as(self) -> None:
        """Save profile to path selected by user."""
        path = self.save_profile_as_dialog()
        if path is not None:
            self.save_profile_to(path)
            self.set_loaded_profile(path)

    def save_profile_as_dialog(self) -> None | Path:
        """Ask user about the path to save the profile to."""
        path = get_home_dir() / "profiles"
        path.mkdir(exist_ok=True, parents=True)
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save profile to...", str(path), "JSON files (*.json)"
        )
        if filename is not None and filename:
            return Path(filename).with_suffix(".json")
        return None
