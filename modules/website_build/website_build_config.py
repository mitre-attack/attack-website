import os
from string import Template

import toml

import modules
from modules import site_config

module_name = "website_build"
priority = 16

# Template directory
template_dir = os.path.join("attack-theme", "templates", "general/")

pyproject_toml = toml.load("pyproject.toml")
website_version = pyproject_toml["tool"]["towncrier"]["version"]

# Base page data for website header and footer
# additional keys that are used/set in website_build.py:
#    BANNER_ENABLED
#    BANNER_MESSAGE
#    ATTACK_BRANDING
#    RESOURCES
base_page_data = {
    "CONTENT_VERSION": site_config.attack_version,
    "WEBSITE_VERSION": website_version,
    "CHANGELOG_LOCATION": "/resources/changelog.html",
    "LOGO_HEADER": "/theme/images/mitre_attack_logo.png",
    "LOGO_FOOTER": "/theme/images/mitrelogowhiteontrans.gif",
    "logo_landingpage": "/theme/images/ATT&CK_red.png",
    "NAVIGATION_MENU": modules.menu_ptr,
    "RESOURCE_NAV": site_config.resource_nav,
}

sidebar_page_data = {
    "RESOURCE_NAV": site_config.resource_nav,
}

# config for the matrix shown on the index page
index_matrix = {
    "name": "ATT&CK Matrix for Enterprise",
    "descr": "",  # if specified, adds a subtitle to the index page matrix
    "matrix": "enterprise-attack",
    "platforms": [
        "Windows",
        "macOS",
        "Linux",
        "PRE",
        "Office Suite",
        "Identity Providers",
        "SaaS",
        "IaaS",
        "Network Devices",
        "Containers",
        "ESXi",
    ],
}

# ATT&CK overview
attack_index_md = "Title: ATT&CK Overview \nTemplate: general/attack-index \nsave_as: index.html\ndata: "

# ATT&CK index markdown path
attack_index_path = "content/pages/index.md"

website_build_markdown_path = "content/pages/"

js_dir_settings = Template('var base_url = "${web_directory}";\n')
js_build_uuid = Template('var build_uuid = "${build_uuid}";\n')

# Path for templates
website_build_templates_path = "modules/website_build/templates/"

# CHANGELOG md
changelog_md = "Title: Changelog\nTemplate: website_build/changelog\nsave_as: resources/changelog.html\n\n"
