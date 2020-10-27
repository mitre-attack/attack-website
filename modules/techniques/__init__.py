from . import techniques
from . import techniques_config
import json

def get_priority():
    return techniques_config.priority

def get_menu():
    return {
        "name": "Techniques", 
        "url": "/techniques/", 
        "external_link": False,
        "priority": techniques_config.priority,
        "children": [
            {
                "name": "Enterprise", 
                "url": "/techniques/enterprise/", 
                "external_link": False,
                "children": []
            },
            {
                "name": "Mobile", 
                "url": "/techniques/mobile/", 
                "external_link": False,
                "children": []
            }
        ]
    }

def get_redirections():
    with open(techniques_config.techniques_redirection_location , "r", encoding="utf8") as json_redirections:
        return json.load(json_redirections)
    return []

def run_module():
    return (techniques.generate_techniques(), techniques_config.module_name)