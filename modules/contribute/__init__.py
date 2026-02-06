from . import contribute, contribute_config


def get_priority():
    return contribute_config.priority


def get_menu():
    return {
        "display_name": "Contribute",
        "module_name": "Contribute",
        "url": "/resources/engage-with-attack/contribute/",
        "external_link": False,
        "priority": contribute_config.priority,
        "children": [],
    }


def run_module():
    return (contribute.generate_contribute(), contribute_config.module_name)
