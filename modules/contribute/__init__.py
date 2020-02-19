from . import contribute 
from . import contribute_config

def get_priority():
    return contribute_config.priority

def get_menu():
    return {
        "name": "Contribute", 
        "url": "/resources/contribute/", 
        "external_link": False,
        "priority": contribute_config.priority,
        "children": []
    }

def run_module():
    return (contribute.generate_contribute(), contribute_config.module_name)