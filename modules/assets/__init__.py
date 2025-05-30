from . import assets
from . import assets_config


def get_priority():
    return assets_config.priority


def run_module():
    return (assets.generate_assets(), assets_config.module_name)
