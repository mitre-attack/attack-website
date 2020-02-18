import os

module_name = "Resources"
priority = 8

# markdown path for resources
resources_markdown_path = "content/pages/resources/"

# General information md
general_information_md = ("Title: General Information\n"
                          "Template: resources/resources\n"
                          "save_as: resources/index.html\n"
                          "data: ")

# Getting started md
getting_started_md = ("Title: Getting Started\n"
                      "Template: resources/getting-started\n"
                      "save_as: resources/getting-started/index.html\n")

# Working with attack md
working_with_attack_md = ("Title: Interfaces for Working with ATT&CK\n"
                          "Template: general/intro-overview\n"
                          "save_as: resources/working-with-attack/index.html\n\n")

# FAQ md
faq_md = ("Title: Frequently Asked Questions\n"
          "Template: resources/faq\n"
          "save_as: resources/faq/index.html\n"
          "data: ")

# Updates md
updates_md = ("Title: Updates\n"
              "Template: resources/updates-index\n"
              "save_as: resources/updates/index.html")

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

prev_versions_deploy_folder = os.path.join("output", "previous")

archives_repo = "https://github.com/mitre-attack/attack-archives.git"
archives_directory = "attack-archives"
previous_md = ("Title: Previous Versions\n"
               "Template: resources/previous-versions\n"
               "save_as: resources/previous-versions/index.html\n"
               "data: ")
previous_markdown_path = "content/pages/resources"

# Related projects md
related_projects_md = ("Title: Related Projects\n"
                       "Template: resources/related-projects\n"
                       "save_as: resources/related-projects/index.html")