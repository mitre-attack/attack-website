from . import clean
from . import clean_config


def get_priority():
    return clean_config.priority


def run_module():
    return (clean.clean_website_build(), clean_config.module_name)
