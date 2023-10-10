import logging
import numpy as np

logger = logging.getLogger("main")


class EuroMeasure:
    def set_pid_p(self, p: float) -> None:
        logger.debug("Virtual EM: Setting PID P to: %f", p)

    def set_pid_i(self, i: float) -> None:
        logger.debug("Virtual EM: Setting PID I to: %f", i)

    def set_pid_d(self, d: float) -> None:
        logger.debug("Virtual EM: Setting PID D to: %f", d)

    def set_pid_state(self, enabled: bool) -> None:
        logger.debug("Virtual EM: Setting PID state to: %i", enabled)

    def set_generator_amplitude(self, channel: int, amplitude: float) -> None:
        logger.debug("Virtual EM: Setting generator channel %i amplitude to: %f", channel, amplitude)

    def set_generator_frequency(self, channel: int, frequency: float) -> None:
        logger.debug("Virtual EM: Setting generator channel %i frequency to: %f", channel, frequency)

    def set_hvpsu_voltage(self, channel: int, voltage: float) -> None:
        logger.debug("Virtual EM: Setting HVPSU channel %i voltage to: %f", channel, voltage)

    def set_source_psu_voltage(self, voltage: float) -> None:
        logger.debug("Virtual EM: Setting SourcePSU voltage to: %f", voltage)

    def set_source_psu_current(self, current: float) -> None:
        logger.debug("Virtual EM: Setting SourcePSU current to: %f", current)

    def get_source_psu_voltage(self) -> float:
        return np.random.normal()

    def get_source_psu_current(self) -> float:
        return np.random.normal()

    def get_voltmeter_voltage(self, channel: int) -> float:
        return np.random.normal()

    def connect(self, port_name: str) -> None:
        pass

    def disconnect(self) -> None:
        pass
