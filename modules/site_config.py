import colorama
import modules
import os
import shutil

# Settings dictionary to build website
settings_dict = {
    "domains": ["pre-attack", "enterprise-attack", "mobile-attack"]
}

base_page_data = {
    "BANNER_ENABLED": True,
    "BANNER_MESSAGE": "<strong><a href='https://collaborate.mitre.org/attackics' target='_blank'>JUST RELEASED: ATT&CK for Industrial Control Systems</a></strong>",
    "CONTENT_VERSION": "6.2",
    "WEBSITE_VERSION": "1.1.1",
    "CHANGELOG_LOCATION": "/resources/changelog.html",
    "NAVIGATION_MENU": modules.menu_ptr
}

template_folder = os.path.join("attack-theme", "templates", "general/")

# Declare file location of web pages
web_directory = "output"
# Directory for test reports
test_report_directory = "reports"