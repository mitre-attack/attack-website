from . import software
from . import software_config
import json

def get_priority():
    return software_config.priority

def get_menu():
    return {
        "display_name": software_config.module_name,
        "module_name": software_config.module_name,
        "url": "/software/",
        "external_link": False,
        "priority": software_config.priority,
        "children": []
    }

# TODO commented out to resolve infinite redirect loop when run locally. Needs further testing before code removal.
# def get_redirections():
#     with open(software_config.software_redirection_location , "r", encoding="utf8") as json_redirections:
#         return json.load(json_redirections)
#     return []

def run_module():
    return software.generate_software(), software_config.module_name
