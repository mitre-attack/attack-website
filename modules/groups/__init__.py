from . import groups
from . import groups_config
from modules import util


def get_priority():
    return groups_config.priority


def get_menu():
    return {
        "display_name": groups_config.module_name,
        "module_name": groups_config.module_name,
        "url": "/groups",
        "external_link": False,
        "priority": groups_config.priority,
        "children": [],
    }


def run_module():
    return (groups.generate_groups(), groups_config.module_name)
