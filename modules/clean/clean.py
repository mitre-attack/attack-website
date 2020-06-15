import shutil
import os
from modules import site_config
from . import clean_config

def clean_website_build():
    """Clean content directory and remove output directory"""

    # Clean content directory
    for filename in os.listdir(clean_config.content_path):
        if filename != "docs":
            # Generate full file path
            full_file_path = os.path.join(clean_config.content_path, filename)
            if os.path.isdir(full_file_path):
                shutil.rmtree(full_file_path)
            else:
                os.remove(full_file_path)
    
    # Make empty content/pages dir
    if not os.path.isdir(clean_config.content_pages_path):
        os.mkdir(clean_config.content_pages_path)
    
    # Delete module templates from template directory
    for filename in os.listdir(site_config.templates_directory):
        if filename != "general" and filename != "macros":
            # Generate full file path
            full_file_path = os.path.join(site_config.templates_directory, filename)
            if os.path.isdir(full_file_path):
                shutil.rmtree(full_file_path)
            else:
                os.remove(full_file_path)
                
    # Remove output directory
    if os.path.isdir(site_config.web_directory):
        shutil.rmtree(site_config.web_directory)
    
    # Remove dynamic javascript file
    settings_js = os.path.join(site_config.javascript_path, "settings.js")
    if os.path.isfile(settings_js):
        os.remove(settings_js)

    # Remove stix replacement settings file
    stix_replacement_settings = os.path.join(site_config.data_directory, "stix_replacement.js")
    if os.path.isfile(stix_replacement_settings):
        os.remove(stix_replacement_settings)