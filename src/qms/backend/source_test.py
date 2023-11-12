"""Contains SourceTester and helpers."""

import logging
import time

from PySide6 import QtCore, QtWidgets

from qms.backend.euromeasure import EMConnectionError, EMError, EMIncorrectResponseError, EuroMeasure
from qms.consts import (
    DETECTOR_VOLTMETER_CHANNEL,
)

logger = logging.getLogger("main")

SLEEP_TIME = 0.03


class SourceTesterSignals(QtCore.QObject):
    """Class containing signals needed for SourceTester.

    SourceTester cannot hold them as it isn't a QObject.
    """

    data_point_acquired = QtCore.Signal(float, float, float, float)
    error_occured = QtCore.Signal(Exception)
    finished = QtCore.Signal()

    def __init__(self, parent: QtWidgets.QWidget | None = None):
        """Initialize in running state."""
        super().__init__(parent)
        self.stopped = False

    @QtCore.Slot()
    def stop(self) -> None:
        """Stop the test."""
        self.stopped = True


class SourceTester(QtCore.QRunnable):
    """SourceTester QRunnable used to preform source current vs voltage scan."""

    def __init__(self, euromeasure: EuroMeasure):
        """Initialize with test config parameters."""
        super().__init__()
        self.em = euromeasure
        self.signals = SourceTesterSignals()

    @QtCore.Slot()
    def run(self) -> None:
        """Run the test."""
        try:
            while not self.signals.stopped:
                time.sleep(SLEEP_TIME)
                detector_current = self.em.get_voltmeter_voltage(DETECTOR_VOLTMETER_CHANNEL)
                source_voltage = self.em.get_source_psu_voltage()
                source_current = self.em.get_source_psu_current()
                self.signals.data_point_acquired.emit(time.time(), source_voltage, source_current, detector_current)
            self.signals.finished.emit()
        except (EMError, EMConnectionError, EMIncorrectResponseError) as exc:
            self.signals.error_occured.emit(exc)
