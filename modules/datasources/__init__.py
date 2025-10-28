from . import datasources
from . import datasources_config
from modules import util


def get_priority():
    return datasources_config.priority

def run_module():
    return (datasources.generate_datasources(), datasources_config.module_name_no_spaces)
