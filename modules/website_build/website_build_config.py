import os
import modules

module_name = "website_build"
priority = 15

# Template directory
template_dir = os.path.join("attack-theme", "templates", "general/")

# Base page data for website header and footer
base_page_data = {
    "BANNER_ENABLED": True,
    "BANNER_MESSAGE": "<strong><a href='https://collaborate.mitre.org/attackics' target='_blank'>JUST RELEASED: ATT&CK for Industrial Control Systems</a></strong>",
    "CONTENT_VERSION": "6.2",
    "WEBSITE_VERSION": "1.1.1",
    "CHANGELOG_LOCATION": "/resources/changelog.html",
    "NAVIGATION_MENU": modules.menu_ptr
}

# config for the matrix shown on the index page
index_matrix = {
    "name": "ATT&CK Matrix for Enterprise",
    "descr": "", # if specified, adds a subtitle to the index page matrix
    "matrix": "enterprise-attack",
    "platforms": ["Windows", "macOS", "Linux"]
}

# ATT&CK overview
attack_index_md = ("Title: ATT&CK Overview \n"
                   "Template: general/attack-index \n"
                   "save_as: index.html\n"
                   "data: ")

# ATT&CK index markdown path
attack_index_path = "content/pages/index.md"

website_build_markdown_path = "content/pages/"