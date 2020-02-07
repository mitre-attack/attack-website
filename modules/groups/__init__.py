import time
from . import groups 
from . import groups_config
from modules import util

def get_menu():
    return {
        "name": "Groups", 
        "url": "/groups", 
        "external_link": False,
        "priority": 4,
        "children": []
    }

def run_module():

    return (groups.generate_groups(), groups_config.module_name)