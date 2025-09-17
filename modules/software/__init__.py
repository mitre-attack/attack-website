import json

from . import software, software_config


def get_priority():
    return software_config.priority


def run_module():
    return software.generate_software(), software_config.module_name
