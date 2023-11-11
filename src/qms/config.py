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
        self.state = State()


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

    def load_from_json(self, json_object: Dict):
        self.source_cc = safely_get(json_object, ["source", "cc"], bool, False)
        self.source_voltage = safely_get(json_object, ["source", "voltage"], (int, float, NoneType), 0)
        self.source_current = safely_get(json_object, ["source", "current"], (int, float, NoneType), 0)
        self.pid_enabled = safely_get(json_object, ["pid", "enabled"], bool, True)
        self.pid_p = float(safely_get(json_object, ["pid", "p"], (int, float), 1))
        self.pid_i = float(safely_get(json_object, ["pid", "i"], (int, float), 1))
        self.pid_d = float(safely_get(json_object, ["pid", "d"], (int, float), 1))
        self.frequency = float(safely_get(json_object, ["frequency"], (int, float), 6e6))

    def dump_to_json(self) -> Dict:
        return {
            "source": {"cc": self.source_cc, "voltage": self.source_voltage, "current": self.source_current},
            "pid": {"p": self.pid_p, "i": self.pid_i, "d": self.pid_d, "enabled": self.pid_enabled},
            "frequency": self.frequency,
        }


class State:
    def __init__(self) -> None:
        self.loaded_profile: str | None = None
        self.previous_profile: str | None = None

    def load_from_json(self, json_object: Dict):
        self.previous_profile = safely_get(json_object, ["loaded_config"], (str, NoneType), "")

    def dump_to_json(self) -> Dict:
        return {"loaded_config": self.loaded_profile if self.loaded_profile is not None else self.previous_profile}


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
