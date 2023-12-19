"""Contains global config class that stores all configurations."""

from __future__ import annotations

import json
import logging
import sys
import time
from argparse import Namespace
from pathlib import Path
from typing import Any

from qms.consts import LAST_STATE_FILENAME
from qms.misc import get_home_dir

logger = logging.getLogger("main")


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
        """Initialize Config."""
        if self.__class__.__instance is not None:
            logger.warning("Config has already beed instatiated. Use Config.get() to get the instance. Skipping")
            return

        self.args = args
        self.__class__.__instance = self
        self.spectrometer_config = SpectrometerConfig()
        self.parameters = MeasurementParameters()
        self.state = State()


class SpectrometerConfig:
    """Stores physical configuraition of the spectrometer."""

    def __init__(self) -> None:
        """Create new SpectrometerConfig objec with default values."""
        self.source_cc: bool = False
        self.source_voltage: float | None = 0
        self.source_current: float | None = None
        self.pid_enabled: bool = True
        self.pid_p: float = 0
        self.pid_i: float = 0
        self.pid_d: float = 0
        self.frequency: float = 0

    def load_from_json(self, json_object: dict) -> None:
        """Update object with data from json_object."""
        self.source_cc = safely_get(json_object, ["source", "cc"], bool, False)
        self.source_voltage = safely_get(json_object, ["source", "voltage"], (int, float), 0)
        self.source_current = safely_get(json_object, ["source", "current"], (int, float), 0)
        self.pid_enabled = safely_get(json_object, ["pid", "enabled"], bool, True)
        self.pid_p = float(safely_get(json_object, ["pid", "p"], (int, float), 1))
        self.pid_i = float(safely_get(json_object, ["pid", "i"], (int, float), 1))
        self.pid_d = float(safely_get(json_object, ["pid", "d"], (int, float), 1))
        self.frequency = float(safely_get(json_object, ["frequency"], (int, float), 6e6))

    def dump_to_json(self) -> dict:
        """Dump the object to json object."""
        return {
            "source": {"cc": self.source_cc, "voltage": self.source_voltage, "current": self.source_current},
            "pid": {"p": self.pid_p, "i": self.pid_i, "d": self.pid_d, "enabled": self.pid_enabled},
            "frequency": self.frequency,
        }


class MeasurementParameters:
    """Stores parameters for measurement that are not physical."""

    def __init__(self) -> None:
        """Create new MeasurementParameters objec with default values."""
        self.rf_to_unit_factor: float = 1
        self.map_dc_offset: float = 0
        self.a: float = 0
        self.b: float = 0
        self.map_rf_min: float = 0
        self.map_rf_max: float = 1
        self.map_rf_step_size = 0.1
        self.map_dc_min: float = 0
        self.map_dc_max: float = 1
        self.map_dc_step_size = 0.1

    def load_from_json(self, json_object: dict) -> None:
        """Update object with data from json_object."""
        self.rf_to_unit_factor = float(safely_get(json_object, ["rf_to_unit_factor"], (float, int), 1))
        self.map_dc_offset = float(safely_get(json_object, ["map_dc_offset"], (float, int), 0))
        self.a = float(safely_get(json_object, ["a"], (float, int), 0))
        self.b = float(safely_get(json_object, ["b"], (float, int), 0))
        self.map_rf_min = safely_get(json_object, ["map_rf_min"], float, 0)
        self.map_rf_max = safely_get(json_object, ["map_rf_max"], float, 1)
        self.map_rf_step_size = safely_get(json_object, ["map_rf_step_size"], float, 0.1)
        self.map_dc_min = safely_get(json_object, ["map_dc_min"], float, 0)
        self.map_dc_max = safely_get(json_object, ["map_dc_max"], float, 1)
        self.map_dc_step_size = safely_get(json_object, ["map_dc_step_size"], float, 0.1)

    def dump_to_json(self) -> dict:
        """Dump the object to json object."""
        return {
            "a": self.a,
            "b": self.b,
            "rf_to_unit_factor": self.rf_to_unit_factor,
            "map_dc_offset": self.map_dc_offset,
            "map_rf_min": self.map_rf_min,
            "map_rf_max": self.map_rf_max,
            "map_rf_step_size": self.map_rf_step_size,
            "map_dc_min": self.map_dc_min,
            "map_dc_max": self.map_dc_max,
            "map_dc_step_size": self.map_dc_step_size,
        }

    def get_map_rf_step_count(self) -> int:
        """Return calculated map rf step count."""
        return int((self.map_rf_max - self.map_rf_min) // self.map_rf_step_size)

    def get_map_dc_step_count(self) -> int:
        """Return calculated map dc step count."""
        return int((self.map_dc_max - self.map_dc_min) // self.map_dc_step_size)


class State:
    """Stores temporary state of the app, such as currently loaded profile."""

    def __init__(self) -> None:
        """Initialize State with defaults."""
        self.loaded_profile: Path | None = None
        self.recent_profiles: list[tuple[Path, float]] = []

    def load_last_state(self) -> None:
        """Load last state from default path."""
        path = get_home_dir() / LAST_STATE_FILENAME
        if path.exists():
            logger.debug("Loading last state")
            try:
                with path.open("r") as json_file:
                    json_object = json.load(json_file)
                    self.load_from_json(json_object)
            except OSError as e:
                logger.error("Couldn't load last state. OS Error %s", e.strerror)
        else:
            logger.info("There is no previous state found. Initializing with defaults")

    def load_from_json(self, json_object: dict) -> None:
        """Update object with data from json object."""
        recent_profiles = safely_get(json_object, ["recent_profiles"], list, [])
        if recent_profiles is not None:
            for recent in recent_profiles:
                if (
                    isinstance(recent, list)
                    and len(recent) == 2
                    and isinstance(recent[0], str)
                    and isinstance(recent[1], float | int)
                ):
                    self.recent_profiles.append((Path(recent[0]), float(recent[1])))
                else:
                    logger.warning("Incorrect type in recent profiles in state file. Ignoring")

    def dump_to_json(self) -> dict:
        """Dump object to json object."""
        return {
            "recent_profiles": [(str(recent[0]), recent[1]) for recent in self.recent_profiles],
        }

    def add_recent_profile(self, path: Path) -> None:
        """Add profile to recently loaded profiles.

        If alreay exists, update last used timestamp.
        If doesn't exist, add and if over 8 recents exist, delete oldest one.
        """
        for index, (exitsting_path, _) in enumerate(self.recent_profiles):
            if path == exitsting_path:
                self.recent_profiles[index] = (path, time.time())
                break
        else:
            self.recent_profiles.append((path, time.time()))
            if len(self.recent_profiles) > 8:
                self.recent_profiles.remove(min(self.recent_profiles, key=lambda x: x[1]))


def safely_get(
    json_object: Any,
    path: list[str | int],
    kind: type | tuple[type, ...],
    default: Any = None,
) -> Any:
    """Gracefully look for value in object."""
    for name in path:
        if isinstance(json_object, dict) and name in json_object:  # noqa: SIM114
            json_object = json_object[name]
        elif isinstance(name, int) and isinstance(json_object, list) and name < len(json_object):
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
