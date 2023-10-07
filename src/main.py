import logging
import argparse

import custom_logging

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


if __name__ == "__main__":
    main()
