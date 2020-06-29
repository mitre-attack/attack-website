from . import resources 
from . import resources_config
import json

def get_priority():
    return resources_config.priority

def get_menu():
    return {
        "name": "Resources", 
        "url": "/resources/", 
        "external_link": False,
        "priority": resources_config.priority,
        "children": [
            {
                "name": "General Information",
                "url": "/resources/",
                "external_link": False,
                "children": []
            },
            {
                "name": "Getting Started",
                "url": "/resources/getting-started/",
                "external_link": False,
                "children": []            
            },
            {
                "name": "Training",
                "url": "/resources/training/",
                "external_link": False,
                "children": []
            },
            {
                "name": "ATT&CKcon",
                "url": "/resources/attackcon/",
                "external_link": False,
                "children": []
            },
            {
                "name": "Working with ATT&CK",
                "url": "/resources/working-with-attack/",
                "external_link": False,
                "children": []
            },
            {
                "name": "FAQ",
                "url": "/resources/faq/",
                "external_link": False,
                "children": []
            },
            {
                "name": "Updates",
                "url": "/resources/updates/",
                "external_link": False,
                "children": []
            },
            {
                "name": "Versions of ATT&CK",
                "url": "/resources/versions/",
                "external_link": False,
                "children": []
            },
            {
                "name": "Related Projects",
                "url": "/resources/related-projects/",
                "external_link": False,
                "children": []
            }
        ]
    }

def run_module():
    return (resources.generate_resources(), resources_config.module_name)