import time
import logging
from backend.euromeasure import EMConnectionError, EMError, EMIncorrectResponseError, EuroMeasure

from PySide6.QtCore import QRunnable, Slot, Signal, QObject

import numpy as np

logger = logging.getLogger("main")

SLEEP_TIME = 0.03
VOLTMETER_CHANNEL = 3
GENERATOR_CHANNEL = 2


class RFScannerSignals(QObject):
    data_point_acquired = Signal(float, float)
    error_occured = Signal(Exception)
    finished = Signal()


class RFScanner(QRunnable):
    def __init__(self, euromeasure: EuroMeasure, stop: float, step_count: int, frequency: float):
        super(RFScanner, self).__init__()
        self.em = euromeasure
        self.stop = stop
        self.step_count = step_count
        self.frequency = frequency
        self.signals = RFScannerSignals()

    @Slot()
    def run(self):
        try:
            self.em.set_pid_state(False)
            self.em.set_generator_frequency(GENERATOR_CHANNEL, self.frequency)

            for amplitude in np.linspace(0, self.stop, num=self.step_count):
                self.em.set_generator_amplitude(GENERATOR_CHANNEL, amplitude)
                time.sleep(SLEEP_TIME)
                result = self.em.get_voltmeter_voltage(VOLTMETER_CHANNEL)
                self.signals.data_point_acquired.emit(amplitude, result)
            self.signals.finished.emit()
        except (EMError, EMConnectionError, EMIncorrectResponseError) as exc:
            self.signals.error_occured.emit(exc)
