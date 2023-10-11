import time
import logging
from backend.euromeasure import EMConnectionError, EMError, EMIncorrectResponseError, EuroMeasure

from PySide6.QtCore import QRunnable, Slot, Signal, QObject

import numpy as np

logger = logging.getLogger("main")

SLEEP_TIME = 0.5


class SourceScannerSignals(QObject):
    data_point_acquired = Signal(float, float)
    error_occured = Signal(Exception)
    finished = Signal()


class SourceScanner(QRunnable):
    def __init__(self, euromeasure: EuroMeasure, start: float, stop: float, step_count: int):
        super(SourceScanner, self).__init__()
        self.em = euromeasure
        self.start = start
        self.stop = stop
        self.step_count = step_count
        self.signals = SourceScannerSignals()

    @Slot()
    def run(self):
        try:
            for voltage in np.linspace(self.start, self.stop, num=self.step_count):
                self.em.set_source_psu_voltage(voltage)
                time.sleep(SLEEP_TIME)
                source_current = self.em.get_source_psu_current()
                self.signals.data_point_acquired.emit(voltage, source_current)
            self.signals.finished.emit()
        except (EMError, EMConnectionError, EMIncorrectResponseError) as exc:
            self.signals.error_occured.emit(exc)
