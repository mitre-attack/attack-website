from . import website_build 
from . import website_build_config
from modules import site_config

def get_priority():
    return website_build_config.priority
    
def run_module():
    return (website_build.generate_website(), website_build_config.module_name)

def send_to_pelican():
    print(site_config.args)
    return {'no-stix-link-replacement': site_config.args.no_stix_link_replacement}