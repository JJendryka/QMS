import time
import logging

from PySide6.QtCore import QRunnable, Slot, Signal, QObject
import numpy as np

from qms.backend.euromeasure import EMConnectionError, EMError, EMIncorrectResponseError, EuroMeasure
from qms.consts import GENERATOR_AMPLITUDE_RF_TEST, MONITOR_VOLTMETER_CHANNEL, QUADRUPOLE_GENERATOR_CHANNEL


logger = logging.getLogger("main")

SLEEP_TIME = 0.03


class ResonanceScannerSignals(QObject):
    data_point_acquired = Signal(float, float)
    error_occured = Signal(Exception)
    finished = Signal()


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
        try:
            self.em.set_pid_state(False)
            self.em.set_generator_amplitude(QUADRUPOLE_GENERATOR_CHANNEL, GENERATOR_AMPLITUDE_RF_TEST)
            for frequency in np.linspace(self.start, self.stop, num=self.step_count):
                self.em.set_generator_frequency(QUADRUPOLE_GENERATOR_CHANNEL, frequency)
                time.sleep(SLEEP_TIME)
                result = self.em.get_voltmeter_voltage(MONITOR_VOLTMETER_CHANNEL)
                self.signals.data_point_acquired.emit(frequency, result)
            self.signals.finished.emit()
        except (EMError, EMConnectionError, EMIncorrectResponseError) as exc:
            self.signals.error_occured.emit(exc)
