import colorama
import json
import multiprocessing
import shutil
from string import Template
from . import util

# parsed arguments 
args = []

# Constants used by contribute.py
# ----------------------------------------------------------------------------

# Markdown path for contribute
contribute_markdown_path = "content/pages/resources"

# String template for contribution index page	
contribute_index_md = ("Title: Contribute\n"
                       "Template: resources/contribute\n"
                       "save_as: resources/contribute/index.html\n"
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