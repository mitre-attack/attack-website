import colorama
import json
import multiprocessing
import shutil
from string import Template
from . import util

# parsed arguments 
args = []

# Constants used for generated layers
# ----------------------------------------------------------------------------
# usage: 
#     domain: "enterprise" or "mobile"
#     path: the path to the object, e.g "software/S1001" or "groups/G2021"
layer_md = Template("Title: ${domain} Techniques\n"
                    "Template: general/json\n"
                    "save_as: ${path}/${attack_id}-${domain}-layer.json\n"
                    "json: ")

# Constants used by contribute.py
# ----------------------------------------------------------------------------

# Markdown path for contribute
contribute_markdown_path = "content/pages/resources"

# String template for contribution index page	
contribute_index_md = ("Title: Contribute\n"
                       "Template: resources/contribute\n"
                       "save_as: resources/contribute/index.html\n"
                       "data: ")

# Constants used by group.py
# ----------------------------------------------------------------------------

# Markdown path for groups
group_markdown_path = "content/pages/groups/"

# String template for group index page	
group_index_md = ("Title: Group overview\n"
                  "Template: groups/groups-index\n"
                  "save_as: groups/index.html\n"
                  "data: ")

# String template for group page
group_md = Template("Title: ${name}\n"
                    "Template: groups/group\n"
                    "save_as: groups/${attack_id}/index.html\n"
                    "data: ")

# Constants used by mitigation.py
# ----------------------------------------------------------------------------

# Markdown path for mitigations
mitigation_markdown_path = "content/pages/mitigations/"

# Mitigation overview string
mitigation_overview_md = ("Title: Mitigation Overview \n"
                          "Template: general/redirect-index \n"
                          "RedirectLink: /mitigations/enterprise/ \n"
                          "save_as: mitigations/index.html \n")

# String template for domains	
mitigation_domain_md = Template("Title: Mitigations\n"
                                "Template: mitigations/mitigations-domain-index\n"
                                "save_as: mitigations/${domain}/index.html\n"
                                "data: ")

# String template for all mitigations
mitigation_md = Template("Title: ${name}-${domain}\n"
                         "Template: mitigations/mitigation\n"
                         "save_as: mitigations/${attack_id}/index.html\n"
                         "data: ")

# Constants used by redirects.py
# ----------------------------------------------------------------------------

# Markdown path for redirects
redirects_markdown_path = "content/pages/wiki/"

# Contributing to ATT&CK md template
contributing_md = ("Title: Contributing_to_MITRE_ATTACK\n"
                   "Template: general/redirect-index\n"
                   "RedirectLink: /resources/contribute\n"
                   "save_as: docs/Contributing_to_MITRE_ATTACK.pdf/index.html\n")

# Training Redirection dictionary
training_redict_dict = [
    {
        "title" : "Training Redirect",
        "redirect_link" : "/resources/training",
        "path" : "training"
    },
    {
        "title" : "CTI Training Redirect",
        "redirect_link" : "/resources/training/cti",
        "path" : "training/cti"
    }
]

# Redirect md string template
redirect_md = Template("Title: ${title}\n"
                       "Template: general/redirect-index\n"
                       "RedirectLink: ${redirect_link}\n"
                       "save_as: ${path}/index.html")

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

# Redirect mapping dictionary
redirects_domain = {
    'enterprise-attack': [
        {'old': "ATT&CK_Matrix", 'new': "/matrices/enterprise"},
        {'old': "ATT&CK_Navigator", 'new': "https://github.com/mitre/attack-navigator"},
        {'old': "Adversary_Emulation_Plans", 'new': "/resources/adversary-emulation-plans"},
        {'old': "All_Techniques", 'new': "/techniques/enterprise"},
        {'old': "Contribute", 'new': "/resources/contribute"},
        {'old': "Cyber_Analytics_Repository", 'new': "https://car.mitre.org"},
        {'old': "Example_queries", 'new': "/resources/working-with-attack"},
        {'old': "Groups", 'new': "/groups"},
        {'old': "Introduction_and_Overview", 'new': "/resources/enterprise-introduction"},
        {'old': "Linux_Technique_Matrix", 'new': "/matrices/enterprise/linux"},
        {'old': "Linux_Techniques", 'new': "/matrices/enterprise/linux"},
        {'old': "MacOS_Techniques", 'new': "/matrices/enterprise/macos"},
        {'old': "Mac_Technique_Matrix", 'new': "/matrices/enterprise/macos"},
        {'old': "Main_Page", 'new': "/"},
        {'old': "Past_Blogs", 'new': "https://medium.com/mitre-attack"},
        {'old': "Past_Updates", 'new': "/resources/updates"},
        {'old': "Related_Efforts", 'new': "/resources/related-efforts"},
        {'old': "Software", 'new': "/software"},
        {'old': "Technique_Matrix", 'new': "/matrices/enterprise"},
        {'old': "Technique_Matrix_Small", 'new': "https://mitre.github.io/attack-navigator"},
        {'old': "Updates_April_2017", 'new': "/resources/updates/updates-april-2017"},
        {'old': "Updates_April_2018", 'new': "/resources/updates/updates-april-2018"},
        {'old': "Updates_January_2018", 'new': "/resources/updates/updates-january-2018"},
        {'old': "Updates_July_2017", 'new': "/resources/updates/updates-july-2017"},
        {'old': "Using_the_API", 'new': "/resources/working-with-attack"},
        {'old': "Windows_Technique_Matrix", 'new': "/matrices/enterprise/windows"},
        {'old': "Windows_Techniques", 'new': "/matrices/enterprise/windows"}
    ],
    'pre-attack': [
        {'old': "All_Techniques", 'new': "/techniques/pre"},
        {'old': "Contribute", 'new': "/resources/contribute"},
        {'old': "Deprecated_Techniques", 'new': "/techniques/pre"},
        {'old': "Groups", 'new': "/groups"},
        {'old': "MITRE", 'new': "/"},
        {'old': "Main_Page", 'new': "/"},
        {'old': "PRE-ATT&CK_Matrix", 'new': "/matrices/pre"},
        {'old': "PRE-ATT&CK_Use_Cases", 'new': "/resources/pre-introduction"},
        {'old': "Past_Updates", 'new': "/resources/updates"},
        {'old': "Tactics", 'new': "/tactics"},
        {'old': "Technique_Matrix", 'new': "/matrices/pre"}
    ],
    'mobile-attack': [
        {'old': "All_Techniques", 'new': "/techniques/mobile"},
        {'old': "ATT&CK_Matrix", 'new': "/matrices/mobile"},
        {'old': "All_Mitigations", 'new': "/mitigations"},
        {'old': "Contribute", 'new': "/resources/contribute"},
        {'old': "Groups", 'new': "/groups"},
        {'old': "Main_Page", 'new': "/"},
        {'old': "Related_Efforts", 'new': "/resources/related-efforts"},
        {'old': "Software", 'new': "/software"},
        {'old': "Software_Technique_usage", 'new': "/software"},
        {'old': "Technique_Matrix", 'new': "/matrices/mobile"},
        {'old': "Technique_Matrix_Small", 'new': "https://mitre.github.io/attack-navigator/mobile"},
        {'old': "Technique_matrix_ID", 'new': "/matrices/mobile"},
        {'old': "Using_the_API", 'new': "/resources/working-with-attack"},
        {'old': "Without_Adversary_Device_Access_Technique_Matrix", 'new': "/matrices/mobile"}
    ]
}

# Images array with dictionaries
redirects_images = [
        {'old': "f/f8/APT3_Adversary_Emulation_Field_Manual.xlsx", 'new': "/docs/APT3_Adversary_Emulation_Field_Manual.xlsx"},
        {'old': "6/6c/APT3_Adversary_Emulation_Plan.pdf", 'new': "/docs/APT3_Adversary_Emulation_Plan.pdf"},
        {'old': "4/4f/MITRE_ATTACK_Enterprise_Poster_2018.pdf", 'new': "/docs/MITRE_ATTACK_Enterprise_Poster_2018.pdf"},
        {'old': "4/46/MITRE_ATTACK_Enterprise_11x17.pdf", 'new': "/docs/MITRE_ATTACK_Enterprise_11x17.pdf"},
        {'old': "7/7d/Contributing_to_MITRE_ATTACK.pdf", 'new': "/docs/Contributing_to_MITRE_ATTACK.pdf"}
]

# Images path
redirects_images_path = "w/img_auth.php/"

# File paths dictionary
redirects_paths = {
    'enterprise-attack': "wiki/", 
    'mobile-attack': "mobile/index.php/", 
    'pre-attack': "pre-attack/index.php/"
}

other_redirects = [
    {'from': 'ics', 'to': 'https://collaborate.mitre.org/attackics'}
]

# Constants used by software.py
# ----------------------------------------------------------------------------

# Markdown path for software
software_markdown_path = "content/pages/software/"  

# String template for software index page	
software_index_md = ("Title: Software overview\n"
                     "Template: software/software-index\n"
                     "save_as: software/index.html\n"
                     "data: ")

# String template for group page
software_md = Template("Title: ${name}\n"
                       "Template: software/software\n"
                       "save_as: software/${attack_id}/index.html\n"
                       "data: ")

# Constants used by tactic.py
# ----------------------------------------------------------------------------

# Markdown path for tactics
tactics_markdown_path = "content/pages/tactics/"

# String template for domains	
tactic_domain_md = Template("Title: Tactics\n"
                            "Template: tactics/tactics-domain-index\n"
                            "save_as: tactics/${domain}/index.html\n"
                            "data: ")

# String template for tactics	
tactic_md = Template("Title: ${name}-${domain}\n"
                     "Template: tactics/tactic\n"
                     "save_as: tactics/${attack_id}/index.html\n"
                     "data: ")

# Tactics overview md template
tactic_overview_md = ("Title: Tactics overview \n"
                      "Template: general/redirect-index \n"
                      "RedirectLink: /tactics/enterprise/ \n"
                      "save_as: tactics/index.html \n")


# Constants used by archives.py
# ----------------------------------------------------------------------------

archives_repo = "https://github.com/mitre-attack/attack-archives.git"
archives_directory = "attack-archives"
previous_md = ("Title: Previous Versions\n"
               "Template: resources/previous-versions\n"
               "save_as: resources/previous-versions/index.html\n"
               "data: ")
previous_markdown_path = "content/pages/resources"

# Constants used by resources.py
# ----------------------------------------------------------------------------

# markdown path for resources
resources_markdown_path = "content/pages/resources/"

# string template for resources.md
resources_md = ("Title: General Information\n"
                "Template: resources/resources\n"
                "save_as: resources/index.html\n"
                "data: ")

# string template for faq.md
faq_md = ("Title: Frequently Asked Questions\n"
          "Template: resources/faq\n"
          "save_as: resources/faq/index.html\n"
          "data: ")

# template for changelog.md
changelog_md = ("Title: Changelog\n"
                "Template: resources/changelog\n"
                "save_as: resources/changelog.html\n\n")

# string template for attackcon.md
attackcon_md = ("Title: ATT&CKcon\n"
                "Template: resources/attackcon\n"
                "save_as: resources/attackcon/index.html\n"
                "data: ")
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

# Constants used by technique.py
# ----------------------------------------------------------------------------

# Markdown path for techniques
techniques_markdown_path = "content/pages/techniques/"	

# String template for all techniques
technique_md = Template("Title: ${name}-${tactics}-${domain}\n"
                        "Template: techniques/technique\n"
                        "save_as: techniques/${attack_id}/index.html\n"
                        "data: ")

# String template for domains	
technique_domain_md = Template("Title: Techniques\n"
                               "Template: techniques/techniques-domain-index\n"
                               "save_as: techniques/${domain}/index.html\n"
                               "data: ")

# Overview md template
technique_overview_md = ("Title: Overview \n"
                         "Template: general/redirect-index \n"
                         "RedirectLink: /techniques/enterprise/ \n"
                         "save_as: techniques/index.html \n")