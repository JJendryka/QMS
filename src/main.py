import logging
import argparse
import signal

from PySide6.QtWidgets import QApplication

import custom_logging
from gui.main_window import MainWindow

signal.signal(signal.SIGINT, signal.SIG_DFL)

logger = logging.getLogger("main")


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

    logger.debug("Starting QApplication")
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
