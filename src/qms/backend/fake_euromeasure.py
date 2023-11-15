"""Contains virtual euromeasure."""

import logging

import numpy as np
from euromeasure import EuroMeasure

logger = logging.getLogger("main")


class FakeEuroMeasure(EuroMeasure):
    """Virtual EuroMeasure object that overrides the standard EuroMeasure behaviour with simulated one."""

    def connect(self, _: str) -> None:
        """Disable any connect logic."""

    def disconnect(self) -> None:
        """Disable any disconnect logic."""

    # Dirty trick for overriding private method behaviour
    def _EuroMeasure__execute_command(self, command: str) -> list[str]:  # noqa: N802
        logger.debug("Virtual command received: %s", command)
        return [str(np.random.random())]
