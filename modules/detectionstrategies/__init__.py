from . import detectionstrategies, detectionstrategies_config


def get_priority():
    return detectionstrategies_config.priority


def run_module():
    return detectionstrategies.generate_detectionstrategy(), detectionstrategies_config.module_name_no_spaces
