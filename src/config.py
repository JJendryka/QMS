from __future__ import annotations
from argparse import Namespace

import logging
import sys
from types import NoneType
from typing import Any, Dict, List, Tuple


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
        self.spectrometer_config = SpectrometerConfig()


class SpectrometerConfig:
    def __init__(self) -> None:
        self.source_cc: bool = False
        self.source_voltage: float | None = 0
        self.source_current: float | None = None
        self.pid_enabled: bool = True
        self.pid_p: float = 0
        self.pid_i: float = 0
        self.pid_d: float = 0
        self.frequency: float = 0

    def load_from_json(self, json_object: Any):
        self.source_cc = safely_get(json_object, ["source", "cc"], bool, False)
        self.source_voltage = safely_get(json_object, ["source", "voltage"], (float, NoneType), None)
        self.source_current = safely_get(json_object, ["source", "current"], (float, NoneType), None)
        self.pid_enabled = safely_get(json_object, ["pid", "enabled"], bool, True)
        self.pid_p = safely_get(json_object, ["pid", "p"], float, 1)
        self.pid_i = safely_get(json_object, ["pid", "i"], float, 1)
        self.pid_d = safely_get(json_object, ["pid", "d"], float, 1)
        self.frequency = safely_get(json_object, ["frequency"], float, 6e6)

    def dump_to_json(self) -> Any:
        return {
            "source": {"cc": self.source_cc, "voltage": self.source_voltage, "current": self.source_current},
            "pid": {"p": self.pid_p, "i": self.pid_i, "d": self.pid_d, "enabled": self.pid_enabled},
            "frequency": self.frequency,
        }


def safely_get(
    json_object: Any,
    path: List[str | int],
    kind: type | Tuple[type, ...],
    default=None,
) -> Any:
    """Gracefully look for value in object."""
    for name in path:
        if isinstance(json_object, Dict) and name in json_object:
            json_object = json_object[name]
        elif isinstance(name, int) and isinstance(json_object, List) and name < len(json_object):
            json_object = json_object[name]
        elif default is None:
            logger.error("No field %s found in json object", path)
            sys.exit(1)
        else:
            logger.warning("No field %s found in json object. Using default: %s", path, str(default))
            return default

    if isinstance(json_object, kind):
        return json_object

    if default is None:
        logger.error(
            "Field %s found in json object has incorrect type %s (correct is %s)",
            path,
            type(json_object),
            kind,
        )
        sys.exit(1)
    else:
        logger.warning(
            "Field %s found in json object has incorrect type %s (correct is %s). Using default: %s",
            path,
            type(json_object),
            kind,
            str(default),
        )
        return default
