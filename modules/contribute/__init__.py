from . import contribute
from . import contribute_config
import json


def get_priority():
    return contribute_config.priority


def get_menu():
    return {
        "display_name": "Contribute",
        "module_name": "Contribute",
        "url": "/resources/contribute/",
        "external_link": False,
        "priority": contribute_config.priority,
        "children": [],
    }


def get_redirections():
    with open(contribute_config.contribute_redirection_location, "r", encoding="utf8") as json_redirections:
        return json.load(json_redirections)
    return []


def run_module():
    return (contribute.generate_contribute(), contribute_config.module_name)
