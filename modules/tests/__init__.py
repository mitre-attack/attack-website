from . import tests, tests_config


def get_priority():
    return tests_config.priority


def run_module():
    return (tests.run_tests(), tests_config.module_name)
