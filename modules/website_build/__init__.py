from . import website_build
from . import website_build_config


def get_priority():
    return website_build_config.priority


def run_module():
    return (website_build.generate_website(), website_build_config.module_name)
