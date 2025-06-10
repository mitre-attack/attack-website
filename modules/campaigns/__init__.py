from . import campaigns
from . import campaigns_config


def get_priority():
    return campaigns_config.priority


def run_module():
    return (campaigns.generate_campaigns(), campaigns_config.module_name)
