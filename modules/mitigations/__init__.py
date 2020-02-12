from . import mitigations
from . import mitigations_config

def get_priority():
    return mitigations_config.priority

def get_menu():
    return {
        "name": "Mitigations", 
        "url": "/mitigations/", 
        "external_link": False,
        "priority": mitigations_config.priority,
        "children": [
            {
                "name": "Enterprise", 
                "url": "/mitigations/enterprise/", 
                "external_link": False,
                "children": []
            },
            {
                "name": "Mobile", 
                "url": "/mitigations/mobile/", 
                "external_link": False,
                "children": []
            }
        ]
    }

def run_module():
    return (mitigations.generate_mitigations(), mitigations_config.module_name)