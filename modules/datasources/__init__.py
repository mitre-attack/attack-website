from . import datasources 
from . import datasources_config
from modules import util

def get_priority():
    return datasources_config.priority

def get_menu():
    return {
        "name": datasources_config.module_name, 
        "url": "/datasources", 
        "external_link": False,
        "priority": datasources_config.priority,
        "children": []
    }

def run_module():
    return (datasources.generate_datasources(), datasources_config.module_name)