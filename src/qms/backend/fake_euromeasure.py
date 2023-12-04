"""Contains virtual euromeasure."""

import logging

import numpy as np
from euromeasure import EMArgument, EuroMeasure

logger = logging.getLogger("main")


class FakeEuroMeasure(EuroMeasure):
    """Virtual EuroMeasure object that overrides the standard EuroMeasure behaviour with simulated one."""

    def connect(self, _: str) -> None:
        """Disable any connect logic."""

    def disconnect(self) -> None:
        """Disable any disconnect logic."""

    # Dirty trick for overriding private method behaviour
    def _EuroMeasure__execute_command(  # noqa: N802
        self, command: str, args: list[EMArgument] | None = None
    ) -> list[str]:  # noqa: N802
        logger.debug("Virtual command received: %s, its args are: %s", command, args)
        return [str(np.random.random())]
