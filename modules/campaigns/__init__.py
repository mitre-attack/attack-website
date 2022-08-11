from . import campaigns
from . import campaigns_config


def get_priority():
    return campaigns_config.priority


def get_menu():
    return {
        "display_name": campaigns_config.module_name,
        "module_name": campaigns_config.module_name,
        "url": "/campaigns",
        "external_link": False,
        "priority": campaigns_config.priority,
        "children": [],
    }


def run_module():
    return (campaigns.generate_campaigns(), campaigns_config.module_name)
