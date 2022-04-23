import os

from modules import site_config

module_name = "Versions"
priority = 8.1

# markdown path for versions
versions_markdown_path = "content/pages/resources"

# Path for templates
versions_templates_path = "modules/versions/templates/"

prev_versions_path = "versions"
prev_versions_deploy_folder = ""

versions_repo = "https://github.com/mitre-attack/attack-website.git"
versions_directory = "attack-versions"
versions_md = (
    "Title: Versions of ATT&CK\n" "Template: versions/versions\n" "save_as: resources/versions/index.html\n" "data: "
)
