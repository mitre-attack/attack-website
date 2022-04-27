from . import subdirectory
from . import subdirectory_config


def get_priority():
    return subdirectory_config.priority


def run_module():
    return (subdirectory.generate_subdirectory(), subdirectory_config.module_name)
