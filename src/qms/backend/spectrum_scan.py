"""Contains RFScanner and helpers."""

import logging
import time

from euromeasure import EMConnectionError, EMError, EMIncorrectResponseError, EuroMeasure
from PySide6 import QtCore, QtWidgets

from qms.backend import upload_config
from qms.config import Config
from qms.consts import (
    DC_MINUS_HVPSU_CHANNEL,
    DC_PLUS_HVPSU_CHANNEL,
    DETECTOR_VOLTMETER_CHANNEL,
    MONITOR_VOLTMETER_CHANNEL,
    QUADRUPOLE_GENERATOR_CHANNEL,
)

logger = logging.getLogger("main")

SLEEP_TIME = 0.1


class SpectrumScannerSignals(QtCore.QObject):
    """Class containing signals needed for SpectrumScanner.

    SpectrumScanner cannot hold them as it isn't a QObject.
    """

    data_point_acquired = QtCore.Signal(int, float, float, float)
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


class SpectrumScanner(QtCore.QRunnable):
    """SpectrumScanner QRunnable used to preform source current vs voltage scan."""

    def __init__(self, euromeasure: EuroMeasure, ac_voltages: list[float], dc_voltages: list[float]):
        """Initialize with scan config parameters."""
        super().__init__()
        self.em = euromeasure
        self.ac_voltages = ac_voltages
        self.dc_voltages = dc_voltages
        self.index = 0
        self.signals = SpectrumScannerSignals()

    @QtCore.Slot()
    def run(self) -> None:
        """Run the scan."""
        try:
            upload_config.upload_configuration(self.em)
            for i in range(len(self.ac_voltages)):
                self.em.set_hvpsu_voltage(DC_PLUS_HVPSU_CHANNEL, self.dc_voltages[i])
                self.em.set_hvpsu_voltage(DC_MINUS_HVPSU_CHANNEL, -self.dc_voltages[i])
                if Config.get().spectrometer_config.pid_enabled:
                    self.em.set_pid_setpoint(self.ac_voltages[i])
                else:
                    self.em.set_generator_amplitude(QUADRUPOLE_GENERATOR_CHANNEL, self.ac_voltages[i])

                time.sleep(SLEEP_TIME)

                detector_voltage = self.em.get_voltmeter_voltage(DETECTOR_VOLTMETER_CHANNEL)
                monitor_voltage = self.em.get_voltmeter_voltage(MONITOR_VOLTMETER_CHANNEL)

                source = None
                if Config.get().spectrometer_config.source_cc:
                    source = self.em.get_source_psu_voltage()
                else:
                    source = self.em.get_source_psu_current()

                self.signals.data_point_acquired.emit(i, detector_voltage, monitor_voltage, source)
            self.signals.finished.emit()
        except (EMError, EMConnectionError, EMIncorrectResponseError) as exc:
            self.signals.error_occured.emit(exc)
