import logging
import sys
import time
from pathlib import Path


class ColoredFormatter(logging.Formatter):
    GRAY = "\033[90m"
    BLUE = "\033[94m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    form = "[%(levelname)s] %(module)s: %(message)s"

    FORMATS = {
        logging.DEBUG: GRAY + form + ENDC,
        logging.INFO: BLUE + form + ENDC,
        logging.WARNING: WARNING + BOLD + form + ENDC,
        logging.ERROR: FAIL + BOLD + form + ENDC,
        logging.CRITICAL: UNDERLINE + FAIL + BOLD + form + ENDC,
    }

    def format(self, record: logging.LogRecord) -> str:  # noqa: A003
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def setup_logging(level: str, logger: logging.Logger) -> None:
    logger.setLevel(logging.DEBUG)

    terminal_formatter = ColoredFormatter()

    terminal_handler = logging.StreamHandler(stream=sys.stdout)
    terminal_handler.setLevel(level)
    terminal_handler.setFormatter(terminal_formatter)
    logger.addHandler(terminal_handler)

    file_formatter = logging.Formatter("%(asctime)s %(levelname)s [%(filename)s:%(lineno)s] %(message)s")

    path = Path("logs")
    path.mkdir(exist_ok=True)
    file_handler = logging.FileHandler(filename=path / time.strftime("%Y_%m_%d-%H_%M_%S.log"))
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
