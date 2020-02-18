from . import search 
from . import search_config

def get_priority():
    return search_config.priority

def get_menu():
    return {
        "name": "Search", 
        "url": None, 
        "external_link": False,
        "search_bar": True,
        "priority": search_config.priority,
        "children": []
    }

def run_module():
    return (search.generate_index(), search_config.module_name)