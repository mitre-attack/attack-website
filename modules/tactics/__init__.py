from . import tactics
from . import tactics_config

def get_priority():
    return tactics_config.priority

def get_menu():
    return {
        "name": "Tactics", 
        "url": "/tactics", 
        "external_link": False,
        "priority": tactics_config.priority,
        "children": [
            {
                "name": "PRE-ATT&CK", 
                "url": "/tactics/pre", 
                "external_link": False,
                "children": []
            },
            {
                "name": "Enterprise", 
                "url": "/tactics/enterprise", 
                "external_link": False,
                "children": []
            },
            {
                "name": "Mobile", 
                "url": "/tactics/mobile", 
                "external_link": False,
                "children": []
            }
        ]
    }

def run_module():
    return (tactics.generate_tactics(), tactics_config.module_name)