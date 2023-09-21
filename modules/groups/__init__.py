from . import groups
from . import groups_config
from modules import util


def get_priority():
    return groups_config.priority

def run_module():
    return (groups.generate_groups(), groups_config.module_name)
