from . import assets
from . import assets_config


def get_priority():
    return assets_config.priority


def get_menu():
    return {
        "display_name": assets_config.module_name,
        "module_name": assets_config.module_name,
        "url": "/assets",
        "external_link": False,
        "priority": assets_config.priority,
        "children": [],
    }


def run_module():
    return (assets.generate_assets(), assets_config.module_name)
