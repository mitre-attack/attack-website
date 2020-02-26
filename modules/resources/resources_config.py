import os

module_name = "Resources"
priority = 8

# markdown path for resources
resources_markdown_path = "content/pages/resources/"

# markdown path for updates
updates_markdown_path = "content/pages/updates/"

# Resources redirection json location
resources_redirection_location = "modules/resources/resources_redirections.json"

# General information md
general_information_md = ("Title: General Information\n"
                          "Template: resources/resources\n"
                          "save_as: resources/index.html\n"
                          "data: ")

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
        
prev_versions_deploy_folder = os.path.join("output", "previous")

archives_repo = "https://github.com/mitre-attack/attack-archives.git"
archives_directory = "attack-archives"
previous_md = ("Title: Previous Versions\n"
               "Template: resources/previous-versions\n"
               "save_as: resources/previous-versions/index.html\n"
               "data: ")
previous_markdown_path = "content/pages/resources"

# General redirects
general_redirects_dict = {
    "attack-pattern": {"old": "Technique", "new": "techniques"}, 
    "malware": {"old": "Software", "new": "software"},
    "tool": {"old": "Software", "new": "software"},
    "intrusion-set": {"old": "Group", "new": "groups"}
}

# Mobile redirects
mobile_redirect_dict = {
    "course-of-action": {
        "old": "Mitigation", 
        "new": "mitigations"
    }
}

# File paths dictionary
redirects_paths = {
    'enterprise-attack': "wiki/", 
    'mobile-attack': "mobile/index.php/", 
    'pre-attack': "pre-attack/index.php/"
}