from . import search
from . import search_config


def get_priority():
    return search_config.priority


def get_menu():
    return {
        "display_name": search_config.module_name,
        "module_name": search_config.module_name,
        "url": None,
        "external_link": False,
        "search_bar": True,
        "priority": search_config.priority,
        "children": [],
    }


def run_module():
    return search.generate_index(), search_config.module_name
