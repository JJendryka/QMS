"""Contains virtual euromeasure."""

import logging

import numpy as np

from qms.backend.euromeasure import EuroMeasure

logger = logging.getLogger("main")


class FakeEuroMeasure(EuroMeasure):
    """Virtual EuroMeasure object that overrides the standard EuroMeasure behaviour with simulated one."""

    def connect(self, _: str) -> None:
        """Disable any connect logic."""

    def disconnect(self) -> None:
        """Disable any disconnect logic."""

    def __execute_command(self, command: str) -> list[str]:
        return [str(np.random.random())]
