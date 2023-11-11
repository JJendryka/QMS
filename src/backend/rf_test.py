import time
import logging
from backend.euromeasure import EMConnectionError, EMError, EMIncorrectResponseError, EuroMeasure

from PySide6.QtCore import QRunnable, Slot, Signal, QObject

from consts import MONITOR_VOLTMETER_CHANNEL

logger = logging.getLogger("main")

SLEEP_TIME = 0.03


class RFTesterSignals(QObject):
    data_point_acquired = Signal(float, float)
    error_occured = Signal(Exception)
    finished = Signal()

    def __init__(self, parent=None):
        super(RFTesterSignals, self).__init__(parent)
        self.stopped = False

    @Slot()
    def stop(self):
        self.stopped = True


class RFTester(QRunnable):
    def __init__(self, euromeasure: EuroMeasure):
        super(RFTester, self).__init__()
        self.em = euromeasure
        self.signals = RFTesterSignals()

    @Slot()
    def run(self):
        try:
            while not self.signals.stopped:
                time.sleep(SLEEP_TIME)
                result = self.em.get_voltmeter_voltage(MONITOR_VOLTMETER_CHANNEL)
                self.signals.data_point_acquired.emit(time.time(), result)
            self.signals.finished.emit()
        except (EMError, EMConnectionError, EMIncorrectResponseError) as exc:
            self.signals.error_occured.emit(exc)
