"""Contains function for uploading constant parameters to EuroMeasure."""

from qms.backend.euromeasure import EuroMeasure
from qms.config import Config
from qms.consts import MAX_SOURCE_CURRENT, MAX_SOURCE_VOLTAGE


def upload_configuration(em: EuroMeasure) -> None:
    """Upload current spectrometer configuration to EuroMeasure."""
    conf = Config.get().spectrometer_config

    if conf.source_cc:
        em.set_source_psu_current(conf.source_current)
        em.set_source_psu_voltage(MAX_SOURCE_VOLTAGE)
    else:
        em.set_source_psu_current(MAX_SOURCE_CURRENT)
        em.set_source_psu_voltage(conf.source_voltage)

    em.set_pid_state(conf.pid_enabled)
    em.set_pid_p(conf.pid_p)
    em.set_pid_i(conf.pid_i)
    em.set_pid_d(conf.pid_d)

    em.set_generator_frequency(conf.frequency)
