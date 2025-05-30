from . import datasources
from . import datasources_config
from modules import util


def get_priority():
    return datasources_config.priority


def get_menu():
    return {
        "display_name": datasources_config.module_tab_name,
        "module_name": datasources_config.module_name_no_spaces,
        "url": "/datasources",
        "external_link": False,
        "priority": datasources_config.priority,
        "children": [
            {"display_name": "Data Sources", "url": "/datasources", "external_link": False, "children": []},
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
        ],
    }


def run_module():
    return (datasources.generate_datasources(), datasources_config.module_name_no_spaces)
