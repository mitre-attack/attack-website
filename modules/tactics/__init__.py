import json

from . import tactics, tactics_config


def get_priority():
    return tactics_config.priority


def get_menu():
    return {
        "display_name": tactics_config.module_name,
        "module_name": tactics_config.module_name,
        "url": "/tactics/",
        "external_link": False,
        "priority": tactics_config.priority,
        "children": [
            {"display_name": "Enterprise", "url": "/tactics/enterprise/", "external_link": False, "children": []},
            {"display_name": "Mobile", "url": "/tactics/mobile/", "external_link": False, "children": []},
            {"display_name": "ICS", "url": "/tactics/ics/", "external_link": False, "children": []},
        ],
    }


def run_module():
    return tactics.generate_tactics(), tactics_config.module_name
