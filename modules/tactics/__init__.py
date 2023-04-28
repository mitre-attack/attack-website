from . import tactics
from . import tactics_config
import json


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

# TODO resolve infinite redirect loop when run locally. Needs further testing before code removal.
def get_redirections():
    with open(tactics_config.tactics_redirection_location, "r", encoding="utf8") as json_redirections:
        return json.load(json_redirections)
    return []


def run_module():
    return tactics.generate_tactics(), tactics_config.module_name
