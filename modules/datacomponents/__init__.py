from . import datacomponents, datacomponents_config


def get_priority():
    return datacomponents_config.priority


def run_module():
    return datacomponents.generate_datacomponents(), datacomponents_config.module_name
