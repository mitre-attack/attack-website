import os
from modules import site_config

module_name = "Resources"
priority = 8

# markdown path for resources
resources_markdown_path = "content/pages/resources/"

# markdown path for updates
updates_markdown_path = "content/pages/updates/"

# General information md
general_information_md = ("Title: General Information\n"
                          "Template: resources/resources\n"
                          "save_as: resources/index.html\n"
                          "data: ")

# Path for templates
resources_templates_path = "modules/resources/templates/"

# FAQ md
faq_md = ("Title: Frequently Asked Questions\n"
          "Template: resources/faq\n"
          "save_as: resources/faq/index.html\n"
          "data: ")

# CHANGELOG md
changelog_md = ("Title: Changelog\n"
                "Template: resources/changelog\n"
                "save_as: resources/changelog.html\n\n")

# ATT&CKcon md
attackcon_md = ("Title: ATT&CKcon\n"
                "Template: resources/attackcon\n"
                "save_as: resources/attackcon/index.html\n"
                "data: ")
# Training md
training_md = ("Title: ATT&CK Training\n"
               "Template: resources/training\n"
               "save_as: resources/training/index.html\n"
               "data: ")

training_cti_md = ("Title: ATT&CK For CTI Training\n"
                   "Template: resources/training-cti\n"
                   "save_as: resources/training/cti/index.html\n"
                   "data: ")

# side navigation for training
training_navigation = {
    "name" : "Training",
    "id" : "training",
    "path" : "/resources/training/",
    "children" : [    
        {
            "name" : "CTI Training",
            "id" : "cti",
            "path" : "/resources/training/cti/",
            "children" : []
        }
    ]
}

prev_versions_path = "versions"
prev_versions_deploy_folder = os.path.join(site_config.web_directory, prev_versions_path)

versions_repo = "https://github.com/mitre-attack/attack-website.git"
versions_directory = "attack-versions"
versions_md = ("Title: Versions of ATT&CK\n"
               "Template: resources/versions\n"
               "save_as: resources/versions/index.html\n"
               "data: ")
versions_markdown_path = "content/pages/resources"