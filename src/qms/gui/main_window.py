"""Contains MainWindow widget."""

import json
import logging
from pathlib import Path

import serial.tools.list_ports
from PySide6 import QtCore, QtGui, QtWidgets

from qms.backend.euromeasure import EMCannotConnectError, EuroMeasure
from qms.backend.fake_euromeasure import FakeEuroMeasure
from qms.config import Config
from qms.consts import LAST_STATE_FILENAME
from qms.layouts.main_window_ui import Ui_MainWindow
from qms.misc import get_home_dir

logger = logging.getLogger("main")


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """MainWindow for QMS app."""

    def __init__(self) -> None:
        """Initialize GUI, callbacks, backreferences."""
        super().__init__()
        self.setupUi(self)
        self.showMaximized()
        # Setting so that closing works correctly when any dialog is shown
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_DeleteOnClose, True)

        self.euromeasure: EuroMeasure | None = None
        self.thread_pool = QtCore.QThreadPool(self)

        self.setup_backreferences()
        self.setup_callbacks()

        logger.debug("Finished main_window initialization")

        self.set_allow_new_scans(False, "EuroMeasure is not connected")

    def setup_backreferences(self) -> None:
        """Setup needed backreferences to self in children."""  # noqa: D401
        self.diagnostic_tab.main_window = self

    def setup_callbacks(self) -> None:
        """Setup needed callbacks."""  # noqa: D401
        self.connection_menu.aboutToShow.connect(self.fill_connection_menu)
        self.load_profile_action.triggered.connect(self.load_profile)
        self.save_profile_action.triggered.connect(self.save_profile)
        self.save_profile_as_action.triggered.connect(self.save_profile_as)

    def fill_connection_menu(self) -> None:
        """Fill connection menu with available devices.

        If there are none display that none are found.
        If debug flag is passed, add debug port.
        """
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
        """Connect to port.

        First disconnect if already connected.
        If in debug mode, connect to fake euromeasure.
        Allow starting scans after connecting.
        """
        logger.info("Connecting to port: %s", port)
        self.connection_menu.setTitle(f"Connected to: {port}")
        if self.euromeasure is not None:
            self.euromeasure.disconnect()
            self.euromeasure = None
            logger.warning("Connect when other port is already connected")
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
        """Disconnect from currently connected port."""
        logger.info("Disconnecting from serial port")
        self.connection_menu.setTitle("Connect")
        if self.euromeasure is not None:
            self.euromeasure.disconnect()
            self.euromeasure = None
        else:
            logger.warning("Trying to disconnect already disconnected port")
        self.set_allow_new_scans(False, "EuroMeasure is not connected")

    def set_allow_new_scans(self, allow: bool = True, reason: str = "") -> None:
        """Change UI to allow or disallow starting new scans."""
        self.diagnostic_tab.set_allow_new_scans(allow, reason)
        self.spectrum_tab.set_allow_new_scans(allow, reason)
        self.stability_map_tab.set_allow_new_scans(allow, reason)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:  # noqa: N802
        """Handle clode event. Save state and ask user to save profile."""
        logger.debug("Saving state to file")
        json_object = Config.get().state.dump_to_json()

        with (get_home_dir() / LAST_STATE_FILENAME).open("w") as json_file:
            json_file.write(json.dumps(json_object))

        # TODO: Ask user whether to save profile

        super().closeEvent(event)

    def set_loaded_profile(self, path: Path) -> None:
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
            logger.info("Opening profile: %s", path)
            try:
                with path.open("r") as json_file:
                    json_object = json.load(json_file)
                    Config.get().spectrometer_config.load_from_json(json_object["spectrometer"])
                self.set_loaded_profile(path)
            except OSError as e:
                logger.error("Cannot load profile: %s, os error: %s", path, e.strerror)
        else:
            logger.error("Cannot load profile: %s, file doesn't exist", path)

    def save_profile(self) -> None:
        """Save profile to currently loaded profile file."""
        path = Config.get().state.loaded_profile
        self.save_profile_to(path)

    def save_profile_to(self, path: Path) -> None:
        """Save profile to path."""
        if path is not None:
            logger.info("Saving profile to: %s", path)
            json_object = {"spectrometer": Config.get().spectrometer_config.dump_to_json()}
            try:
                with path.open("w") as json_file:
                    json.dump(json_object, json_file)
            except OSError as e:
                logger.error("Cannot save profile to: %s. OS Error: %s", path, e.strerror)

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
