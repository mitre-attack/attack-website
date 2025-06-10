from . import resources
from . import resources_config
import json


def get_priority():
    return resources_config.priority


def get_menu():
    return {
        "display_name": resources_config.module_name,
        "module_name": resources_config.module_name,
        "url": "/resources/",
        "external_link": False,
        "priority": resources_config.priority,
        "children": [
            {
                "display_name": "Get Started",
                "url": "/resources/",
                "external_link": False,
                "children": [],
            },
            {
                "display_name": "Learn More about ATT&CK",
                "url": "/resources/learn-more-about-attack/",
                "external_link": False,
                "children": [],
            },
            {"display_name": "ATT&CKcon", "url": "/resources/attackcon/", "external_link": False, "children": []},
            {
                "display_name": "ATT&CK Data & Tools",
                "url": "/resources/attack-data-and-tools/",
                "external_link": False,
                "children": [],
            },
            {"display_name": "FAQ", "url": "/resources/faq/", "external_link": False, "children": []},
            {
                "display_name": "Engage with ATT&CK",
                "url": "/resources/engage-with-attack/contact/",
                "external_link": False,
                "children": [],
            },
            {
                "display_name": "Version History",
                "url": "/resources/versions/",
                "external_link": False,
                "children": [],
            },
            {
                "display_name": "Updates",
                "url": "/resources/updates/",
                "external_link": False,
                "children": [],
            },
            {
                "display_name": "Legal & Branding",
                "url": "/resources/legal-and-branding/",
                "external_link": False,
                "children": [],
            },
        ],
    }


def run_module():
    return (resources.generate_resources(), resources_config.module_name)
