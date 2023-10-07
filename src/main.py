import logging
import argparse

from PySide6.QtWidgets import QApplication

import custom_logging
from main_window import MainWindow

import signal

signal.signal(signal.SIGINT, signal.SIG_DFL)

logger = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
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
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    custom_logging.setup_logging(args.log_level, logger)

    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
