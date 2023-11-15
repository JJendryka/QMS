"""Contains RFScanner and helpers."""

import logging
import time

import numpy as np
from euromeasure import EMConnectionError, EMError, EMIncorrectResponseError, EuroMeasure
from PySide6.QtCore import QObject, QRunnable, Signal, Slot

from qms.consts import MONITOR_VOLTMETER_CHANNEL, QUADRUPOLE_GENERATOR_CHANNEL

logger = logging.getLogger("main")

SLEEP_TIME = 0.03


class RFScannerSignals(QObject):
    """Class containing signals needed for RFScanner.

    RFScanner cannot hold them as it isn't a QObject.
    """

    data_point_acquired = Signal(float, float)
    error_occured = Signal(Exception)
    finished = Signal()


class RFScanner(QRunnable):
    """RFScanner QRunnable used to preform source current vs voltage scan."""

    def __init__(self, euromeasure: EuroMeasure, stop: float, step_count: int, frequency: float):
        """Initialize with scan config parameters."""
        super().__init__()
        self.em = euromeasure
        self.stop = stop
        self.step_count = step_count
        self.frequency = frequency
        self.signals = RFScannerSignals()

    @Slot()
    def run(self) -> None:
        """Run the scan."""
        try:
            self.em.set_pid_state(False)
            self.em.set_generator_frequency(QUADRUPOLE_GENERATOR_CHANNEL, self.frequency)

            for amplitude in np.linspace(0, self.stop, num=self.step_count):
                self.em.set_generator_amplitude(QUADRUPOLE_GENERATOR_CHANNEL, amplitude)
                time.sleep(SLEEP_TIME)
                result = self.em.get_voltmeter_voltage(MONITOR_VOLTMETER_CHANNEL)
                self.signals.data_point_acquired.emit(amplitude, result)
            self.signals.finished.emit()
        except (EMError, EMConnectionError, EMIncorrectResponseError) as exc:
            self.signals.error_occured.emit(exc)
