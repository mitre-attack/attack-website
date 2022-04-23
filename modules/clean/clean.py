import os
import shutil

from modules import site_config

from . import clean_config


def clean_website_build():
    """Clean content directory and remove output directory"""

    # Clean content directory
    if os.path.isdir(site_config.content_dir):
        shutil.rmtree(site_config.content_dir)

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

    # Remove reports directory
    if os.path.isdir(site_config.test_report_directory):
        shutil.rmtree(site_config.test_report_directory)

    # Remove dynamic javascript file
    settings_js = os.path.join(site_config.javascript_path, "settings.js")
    if os.path.isfile(settings_js):
        os.remove(settings_js)
