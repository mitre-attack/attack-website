from . import mitigations
from . import mitigations_config


def get_priority():
    return mitigations_config.priority


def run_module():
    return (mitigations.generate_mitigations(), mitigations_config.module_name)
