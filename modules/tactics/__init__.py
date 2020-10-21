from . import tactics
from . import tactics_config
import json

def get_priority():
    return tactics_config.priority

def get_menu():
    return {
        "name": "Tactics", 
        "url": "/tactics/", 
        "external_link": False,
        "priority": tactics_config.priority,
        "children": [
            {
                "name": "Enterprise", 
                "url": "/tactics/enterprise/", 
                "external_link": False,
                "children": []
            },
            {
                "name": "Mobile", 
                "url": "/tactics/mobile/", 
                "external_link": False,
                "children": []
            }
        ]
    }

def get_redirections():
    with open(tactics_config.tactics_redirection_location , "r", encoding="utf8") as json_redirections:
        return json.load(json_redirections)
    return []

def run_module():
    return (tactics.generate_tactics(), tactics_config.module_name)