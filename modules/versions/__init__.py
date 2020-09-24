from . import versions 
from . import versions_config

def get_priority():
    return versions_config.priority

def run_module():
    return (versions.deploy(), versions_config.module_name)