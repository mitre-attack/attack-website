from . import release
from . import release_config



def get_priority():
    return release_config.priority


def run_module():
    return (release.generate_release_changelog(), release_config.module_name)
