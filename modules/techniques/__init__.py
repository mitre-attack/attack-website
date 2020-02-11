from . import techniques
from . import techniques_config

def get_priority():
    return techniques_config.priority

def get_menu():
    return {
        "name": "Techniques", 
        "url": "/techniques", 
        "external_link": False,
        "priority": techniques_config.priority,
        "children": [
            {
                "name": "PRE-ATT&CK", 
                "url": "/techniques/pre", 
                "external_link": False,
                "children": []
            },
            {
                "name": "Enterprise", 
                "url": "/techniques/enterprise", 
                "external_link": False,
                "children": []
            },
            {
                "name": "Mobile", 
                "url": "/techniques/mobile", 
                "external_link": False,
                "children": []
            }
        ]
    }

def run_module():
    return (techniques.generate_techniques(), techniques_config.module_name)