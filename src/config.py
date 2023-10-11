from __future__ import annotations
from argparse import Namespace

import logging


logger = logging.getLogger("__main__")


class Config:
    """Class representing program configuration."""

    __instance: Config | None = None

    @classmethod
    def get(cls) -> Config:
        """Return already instantiated config."""
        if cls.__instance is not None:
            return cls.__instance

        logger.error("Config hasn't been instantiated")
        raise Exception("Config hasn't been instatiated")

    def __init__(self, args: Namespace) -> None:
        """Initialize Config"""
        if self.__class__.__instance is not None:
            logger.warning("Config has already beed instatiated. Use Config.get() to get the instance. Skipping")
            return

        self.args = args
        self.__class__.__instance = self
