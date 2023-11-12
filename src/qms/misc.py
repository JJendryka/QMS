"""Contains misc methods: get_home_dir."""

import logging
import os
import sys
from pathlib import Path

import xdg_base_dirs

logger = logging.getLogger("main")


def get_home_dir() -> Path:
    """Return directory where all application files are stored."""
    if os.name == "nt":
        path = Path("%APPDATA%") / "QMS"
    elif os.name == "posix":
        path = xdg_base_dirs.xdg_data_home() / "QMS"
    else:
        logger.error("This system is not supported")
        sys.exit(1)

    path.mkdir(parents=True, exist_ok=True)
    return path
