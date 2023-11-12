from __future__ import annotations
from argparse import Namespace
import json

import logging
from pathlib import Path
import sys
import time
from types import NoneType
from typing import Any, Dict, List, Tuple
from qms.consts import LAST_STATE_FILENAME

from qms.misc import get_home_dir


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
        self.loaded_profile: Path | None = None
        self.recent_profiles: List[Tuple[Path, float]] = []

    def load_last_state(self):
        path = get_home_dir() / LAST_STATE_FILENAME
        if path.exists():
            logger.debug("Loading last state")
            try:
                with open(path, "r") as json_file:
                    json_object = json.load(json_file)
                    self.load_from_json(json_object)
            except OSError as e:
                logger.error(f"Couldn't load last state. OS Error {e.strerror}")
        else:
            logger.info("There is no previous state found. Initializing with defaults")

    def load_from_json(self, json_object: Dict) -> None:
        recent_profiles = safely_get(json_object, ["recent_profiles"], List, [])
        if recent_profiles is not None:
            for recent in recent_profiles:
                if (
                    isinstance(recent, list)
                    and len(recent) == 2
                    and isinstance(recent[0], str)
                    and (isinstance(recent[1], float) or isinstance(recent[1], int))
                ):
                    self.recent_profiles.append((Path(recent[0]), float(recent[1])))
                else:
                    logger.warning("Incorrect type in recent profiles in state file. Ignoring")

    def dump_to_json(self) -> Dict:
        return {"recent_profiles": [(str(recent[0]), recent[1]) for recent in self.recent_profiles]}

    def add_recent_profile(self, path):
        for index, (exitsting_path, _) in enumerate(self.recent_profiles):
            if path == exitsting_path:
                self.recent_profiles[index][1] = time.time()
                break
        else:
            self.recent_profiles.append((path, time.time()))
            if len(self.recent_profiles) > 8:
                self.recent_profiles.remove(min(self.recent_profiles, key=lambda x: x[1]))


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
