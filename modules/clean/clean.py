import shutil
import os
from modules import site_config
from . import clean_config

def clean_website_build():
    """Clean content directory and remove output directory"""

    # Clean content directory
    for filename in os.listdir(clean_config.content_path):
        if filename != "docs" and filename != "pages":
            # Generate full file path
            full_file_path = os.path.join(clean_config.content_path, filename)
            if os.path.isdir(full_file_path):
                shutil.rmtree(full_file_path)
            else:
                os.remove(full_file_path)
        
    # Clean content/pages directory
    for filename in os.listdir(clean_config.content_pages_path):
        # Get full file path
        full_file_path = os.path.join(clean_config.content_pages_path, filename)
        if os.path.isdir(full_file_path):
            shutil.rmtree(full_file_path)
        else:
            os.remove(full_file_path)
    
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