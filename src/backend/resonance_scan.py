import time
import logging
from backend.euromeasure import EuroMeasure

from PySide6.QtCore import QRunnable, Slot, Signal, QObject

import numpy as np

logger = logging.getLogger("main")

SLEEP_TIME = 0.2
VOLTMETER_CHANNEL = 1
GENERATOR_CHANNEL = 2
GENERATOR_AMPLITUDE = 0.2


class ResonanceScannerSignals(QObject):
    data_point_acquired = Signal(float, float)


class ResonanceScanner(QRunnable):
    def __init__(self, euromeasure: EuroMeasure, start: float, stop: float, step_count: int):
        super(ResonanceScanner, self).__init__()
        self.em = euromeasure
        self.start = start
        self.stop = stop
        self.step_count = step_count
        self.signals = ResonanceScannerSignals()

    @Slot()
    def run(self):
        self.em.set_pid_state(False)
        self.em.set_generator_amplitude(GENERATOR_CHANNEL, GENERATOR_AMPLITUDE)
        for frequency in np.linspace(self.start, self.stop, num=self.step_count):
            self.em.set_generator_frequency(GENERATOR_CHANNEL, frequency)
            time.sleep(SLEEP_TIME)
            result = self.em.get_voltmeter_voltage(VOLTMETER_CHANNEL)
            logger.debug("Sending signal")
            self.signals.data_point_acquired.emit(frequency, result)
