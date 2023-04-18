from . import redirections
from . import redirections_config
import json


def get_priority():
    return redirections_config.priority


def get_redirections():
    with open(redirections_config.redirections_location, "r", encoding="utf8") as json_redirections:
        return json.load(json_redirections)
    return []


def run_module():
    return redirections.generate_redirections(), redirections_config.module_name
