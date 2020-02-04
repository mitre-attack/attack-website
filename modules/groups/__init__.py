from . import groups 

def get_menu():
    return {
        "name": "Groups", 
        "url": "/groups", 
        "external_link": False,
        "priority": 4,
        "children": []
    }

def run_module():
    return (groups.generate_groups(), "Groups")