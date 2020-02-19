from . import software 
from . import software_config

def get_priority():
    return software_config.priority

def get_menu():
    return {
        "name": "Software", 
        "url": "/software/", 
        "external_link": False,
        "priority": software_config.priority,
        "children": []
    }

def run_module():
    return (software.generate_software(), software_config.module_name)