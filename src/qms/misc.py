"""Contains misc methods: get_home_dir."""

import logging
import os
import sys
from pathlib import Path
from types import TracebackType
from typing import Literal, Protocol, TypeAlias, TypeVarTuple, Unpack

import numpy as np
import xdg_base_dirs

logger = logging.getLogger("main")

Array1Df: TypeAlias = np.ndarray[Literal["N"], np.dtype[np.float32]]
Array2Df: TypeAlias = np.ndarray[Literal["N", "N"], np.dtype[np.float32]]

T = TypeVarTuple("T")


class UILock:
    """Lock that is manually set with 'with' and evaluates to True if locked and can wrap a function."""

    def __init__(self) -> None:
        """Initialize in unlocked state."""
        self.locked: bool = False

    def __bool__(self) -> bool:
        """Evaluate to True if locked."""
        return self.locked

    def __enter__(self) -> None:
        """Lock when entering."""
        self.locked = True

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        exc_traceback: TracebackType | None,
    ) -> None:
        """Unlock when exiting."""
        self.locked = False

    class _Callback(Protocol[Unpack[T]]):
        def __call__(self, *args: Unpack[T]) -> None:
            pass

    def __call__(self, callback: _Callback) -> _Callback:
        """Wrap callback with lock. Won't be called when locked."""
        return lambda *arg: callback(*arg) if not self.locked else None


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
