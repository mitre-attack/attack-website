from . import benefactors
from . import benefactors_config
import json


def get_priority():
    return benefactors_config.priority


def get_menu():
    return {
        "display_name": "Benefactors",
        "module_name": "Benefactors",
        "url": "/resources/engage-with-attack/benefactors/",
        "external_link": False,
        "priority": benefactors_config.priority,
        "children": [],
    }


def run_module():
    return (benefactors.generate_benefactors(), benefactors_config.module_name)
