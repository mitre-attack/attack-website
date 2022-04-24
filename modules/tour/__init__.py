from . import tour
from . import tour_config


def get_priority():
    return tour_config.priority


def run_module():
    return (tour.generate_tour(), tour_config.module_name)
