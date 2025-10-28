from . import mitigations
from . import mitigations_config


def get_priority():
    return mitigations_config.priority


def get_menu():
    return {
        "display_name": mitigations_config.module_tab_name,
        "module_name": mitigations_config.module_name,
        "url": "/mitigations",
        "external_link": False,
        "priority": mitigations_config.priority,
        "children": [
            {
                "display_name": "Mitigations",
                "url": "/mitigations/",
                "external_link": False,
                "children": [
                    {
                        "display_name": "Enterprise",
                        "url": "/mitigations/enterprise/",
                        "external_link": False,
                        "children": [],
                    },
                    {"display_name": "Mobile", "url": "/mitigations/mobile/", "external_link": False, "children": []},
                    {"display_name": "ICS", "url": "/mitigations/ics/", "external_link": False, "children": []},
                ],
            },
            {"display_name": "Assets", "url": "/assets", "external_link": False, "children": []},
            {
                "display_name": "Detections",
                "url": "/detectionstrategies/",
                "external_link": False,
                "children": [
                    {
                        "display_name": "Detection Strategies",
                        "url": "/detectionstrategies/",
                        "external_link": False,
                        "children": []
                    },
                    {
                        "display_name": "Analytics",
                        "url": "/analytics/",
                        "external_link": False,
                        "children": []
                    },
                    {
                        "display_name": "Data Components",
                        "url": "/datacomponents",
                        "external_link": False,
                        "children": []
                    }
                ]
            },
        ],
    }


def run_module():
    return (mitigations.generate_mitigations(), mitigations_config.module_name)
