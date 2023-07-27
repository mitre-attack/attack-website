import os
import json 

from modules import site_config
import modules
from modules import site_config, util
from datetime import datetime

def generate_updates_list():
    """Reads markdown files from the static pages directory and copies them into the markdown directory."""
    static_pages_dir = os.path.join("modules", "resources", "static_pages")
    data = []
    updates_names = []
    for static_page in os.listdir(static_pages_dir):
        with open(os.path.join(static_pages_dir, static_page), "r", encoding="utf8") as md:
            content = md.read()

            if static_page.startswith("updates-"):
                temp_string = static_page.replace('.md','')
                temp_string = temp_string.split('-')
                temp_string = temp_string[1].capitalize() + ' ' + temp_string[2]
                data.append(temp_string)
                temp_string = static_page.replace('.md','')
                updates_names.append("/resources/updates/" + temp_string)
    data.sort(key=lambda date: datetime.strptime(date, "%B %Y"), reverse=True)
    updates_names.sort(key=lambda date: datetime.strptime(date, "/resources/updates/updates-%B-%Y"), reverse=True)
    return(data, updates_names)

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
    "Title: ATT&CK Training\n" "Template: resources/training\n" "save_as: resources/training/index.html\n"
)

training_cti_md = (
    "Title: ATT&CK For CTI Training\n"
    "Template: resources/training-cti\n"
    "save_as: resources/training/cti/index.html\n"
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

resources_navigation = {
        "name": "Resources",
        "id": "resources",
        "children": [
        {"name": "General Information",
        "id": "general-info",
        "path": "/resources/",
        "children": []
        },
        {"name": "Getting Started",
        "id": "getting-started",
        "path": "/resources/getting-started",
        "children": [] 
        },
        {
        "name": "Training",
        "id": "training",
        "path": "/resources/training/",
        "children": [{"name": "CTI Training", "id": "cti", "path": "/resources/training/cti/", "children": []}],
        },
        {
        "name": "ATT&CKcon",
        "id": "attackcon",
        "path": "/resources/attackcon/",
        "children": []
        },
        {
        "name": "Working with ATT&CK",
        "id": "working-with-attack",
        "path": "/resources/working-with-attack/",
        "children": []
        },
        {
        "name": "FAQ",
        "id": "faq",
        "path": "/resources/faq/",
        "children": []
        },
        {
        "name": "Updates",
        "id": "updates",
        "path": "/resources/updates/",
        "children": []
        },
        {
        "name": "Related Projects",
        "id": "related-projects",
        "path": "/resources/related-projects/",
        "children": []
        }
        ]
    }

test, yy = generate_updates_list()
temp_dict = {}
for i in range(len(test)):
    temp_dict["name"] = test[i]
    temp_dict["path"] = yy[i]
    temp_dict["children"] = []
    resources_navigation["children"][6]["children"].append(temp_dict.copy())
    temp_dict = {}

with open("data/resources_navigation.json", "r", encoding="utf8") as i:
    res_nav = json.load(i)
test, yy = generate_updates_list()
temp_dict = {}
for i in range(len(test)):
    temp_dict["name"] = test[i]
    temp_dict["path"] = yy[i]
    temp_dict["children"] = []
    res_nav["children"][5]["children"].append(temp_dict.copy())
    temp_dict = {}