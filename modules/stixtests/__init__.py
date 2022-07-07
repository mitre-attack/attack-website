from . import stixtests
from . import stixtests_config


def get_priority():
    return stixtests_config.priority


def run_module():
    return (stixtests.run_tests(), stixtests_config.module_name)
