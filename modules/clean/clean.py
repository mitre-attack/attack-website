import os
import shutil

from loguru import logger

from modules import site_config


def clean_website_build():
    """Clean content directory and remove output directory."""
    # Clean content directory
    logger.info(f"Deleting content directory: {site_config.content_dir}")
    if os.path.isdir(site_config.content_dir):
        shutil.rmtree(site_config.content_dir)

    # Delete module templates from template directory
    for filename in os.listdir(site_config.templates_directory):
        if filename != "general" and filename != "macros":
            # Generate full file path
            full_file_path = os.path.join(site_config.templates_directory, filename)
            logger.info(f"Deleting module template: {full_file_path}")
            if os.path.isdir(full_file_path):
                shutil.rmtree(full_file_path)
            else:
                os.remove(full_file_path)

    # Remove output directory
    logger.info(f"Deleting output directory: {site_config.web_directory}")
    if os.path.isdir(site_config.web_directory):
        shutil.rmtree(site_config.web_directory)

    # Remove reports directory
    logger.info(f"Deleting reports directory: {site_config.test_report_directory}")
    if os.path.isdir(site_config.test_report_directory):
        shutil.rmtree(site_config.test_report_directory)

    # Remove dynamic javascript file
    settings_js = os.path.join(site_config.javascript_path, "settings.js")
    logger.info(f"Deleting dynamic javascript file: {settings_js}")
    if os.path.isfile(settings_js):
        os.remove(settings_js)
