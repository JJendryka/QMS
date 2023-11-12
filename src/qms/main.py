"""Main file of the application."""
import argparse
import logging
import signal

from PySide6.QtWidgets import QApplication

import qms.custom_logging as custom_logging
from qms.config import Config
from qms.gui.main_window import MainWindow

signal.signal(signal.SIGINT, signal.SIG_DFL)

logger = logging.getLogger("main")


def parse_args() -> argparse.Namespace:
    """Parse arguments from the command line."""
    parser = argparse.ArgumentParser(
        prog="QMS", description="Quadrupole Management Software - used to controll a quadrupole mass spectrometer"
    )
    parser.add_argument(
        "-l",
        "--log",
        dest="log_level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="INFO",
    )
    parser.add_argument("-d", "--debug", dest="debug", action="store_true")
    return parser.parse_args()


def main() -> None:
    """Entry point to the program."""
    args = parse_args()
    custom_logging.setup_logging(args.log_level, logger)
    _ = Config(args)
    Config.get().state.load_last_state()
    logger.debug("Starting QApplication")
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
