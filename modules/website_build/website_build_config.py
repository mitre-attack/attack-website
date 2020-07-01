import os
import modules
from string import Template

module_name = "website_build"
priority = 16

# Template directory
template_dir = os.path.join("attack-theme", "templates", "general/")

# Base page data for website header and footer
base_page_data = {
    "BANNER_ENABLED": True,
    "BANNER_MESSAGE": "<strong><a href='https://collaborate.mitre.org/attackics' target='_blank'>JUST RELEASED: ATT&CK for Industrial Control Systems</a></strong>",
    "CONTENT_VERSION": "6.3",
    "WEBSITE_VERSION": "1.2.4",
    "CHANGELOG_LOCATION": "/resources/changelog.html",
    "LOGO_HEADER": "/theme/images/mitre_attack_logo.png",
    "LOGO_FOOTER": "/theme/images/mitrelogowhiteontrans.gif",
    "logo_landingpage": "/theme/images/ATT&CK_red.png",
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

# js_dir_settings = Template("var base_url = \"${web_directory}\";\nvar build_uuid = \"" + str(uuid.uuid4()) + "\";\n")
js_dir_settings = Template("var base_url = \"${web_directory}\";\n")
js_build_uuid = Template("var build_uuid = \"${build_uuid}\";\n")

