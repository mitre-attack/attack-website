import os

from modules import site_config

module_name = "Resources"
priority = 8

# markdown path for updates
updates_markdown_path = "content/pages/updates/"

# General information md
general_information_md = (
    "Title: General Information\n" "Template: resources/resources\n" "save_as: resources/index.html\n" "data: "
)

# Path for templates
resources_templates_path = "modules/resources/templates/"

# Path for docs
docs_path = "modules/resources/docs/"

# ATT&CKcon md
attackcon_md = (
    "Title: ATT&CKcon\n" "Template: resources/attackcon\n" "save_as: resources/attackcon/index.html\n" "data: "
)
# Training md
training_md = (
    "Title: ATT&CK Training\n" "Template: resources/training\n" "save_as: resources/training/index.html\n" "data: "
)

training_cti_md = (
    "Title: ATT&CK For CTI Training\n"
    "Template: resources/training-cti\n"
    "save_as: resources/training/cti/index.html\n"
    "data: "
)

# Excel files / working with ATT&CK
working_with_attack_md = (
    "Title: Working with ATT&CK\n"
    "Template: resources/working-with-attack\n"
    "save_as: resources/working-with-attack/index.html\n"
    "data: "
)

# side navigation for training
training_navigation = {
    "name": "Training",
    "id": "training",
    "path": "/resources/training/",
    "children": [{"name": "CTI Training", "id": "cti", "path": "/resources/training/cti/", "children": []}],
}
