from . import stix_data 
from . import stix_data_config

def get_priority():
    return stix_data_config.priority
    
def run_module():
    return (stix_data.get_stix_data(), stix_data_config.module_name)