from . import random_page
from . import random_page_config


def get_priority():
    return random_page_config.priority


def run_module():
    return (random_page.generate_json(), random_page_config.module_name)
