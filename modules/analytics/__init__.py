from . import analytics, analytics_config


def get_priority():
    return analytics_config.priority


def run_module():
    return analytics.generate_analytic(), analytics_config.module_name
