"""Contains RFTester and helpers."""
import logging
import time

from PySide6 import QtWidgets
from PySide6.QtCore import QObject, QRunnable, Signal, Slot

from qms.backend.euromeasure import EMConnectionError, EMError, EMIncorrectResponseError, EuroMeasure
from qms.consts import MONITOR_VOLTMETER_CHANNEL

logger = logging.getLogger("main")

SLEEP_TIME = 0.03


class RFTesterSignals(QObject):
    """Class containing signals needed for RFTester.

    RFTester cannot hold them as it isn't a QObject.
    """

    data_point_acquired = Signal(float, float)
    error_occured = Signal(Exception)
    finished = Signal()

    def __init__(self, parent: QtWidgets.QWidget | None = None):
        """Initialize in running state."""
        super().__init__(parent)
        self.stopped = False

    @Slot()
    def stop(self) -> None:
        """Stop the test."""
        self.stopped = True


class RFTester(QRunnable):
    """RFTester QRunnable used to preform source current vs voltage scan."""

    def __init__(self, euromeasure: EuroMeasure):
        """Initialize."""
        super().__init__()
        self.em = euromeasure
        self.signals = RFTesterSignals()

    @Slot()
    def run(self) -> None:
        """Start the test."""
        try:
            while not self.signals.stopped:
                time.sleep(SLEEP_TIME)
                result = self.em.get_voltmeter_voltage(MONITOR_VOLTMETER_CHANNEL)
                self.signals.data_point_acquired.emit(time.time(), result)
            self.signals.finished.emit()
        except (EMError, EMConnectionError, EMIncorrectResponseError) as exc:
            self.signals.error_occured.emit(exc)
