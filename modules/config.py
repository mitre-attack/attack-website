import colorama
import json
import multiprocessing
import os
import shutil
from string import Template
from . import relationshiphelpers as rsh
from . import stixhelpers
from . import util

# Python module for all constants and global variables

# Settings dictionary to build website
settings_dict = {
    "content_version": "6.2",
    "website_version": "1.2.4",
    "changelog_location": "/resources/changelog.html",
    "banner_enabled": "true",
    "banner_message": "<strong><a href='https://collaborate.mitre.org/attackics' target='_blank'>JUST RELEASED: ATT&CK for Industrial Control Systems</a></strong>",
    "domains": ["pre-attack", "enterprise-attack", "mobile-attack"],
    "source_names": [
        "mitre-pre-attack", 
        "mitre-attack", 
        "mitre-mobile-attack"
    ],
    "domain_aliases": [
        ["PRE-ATT&CK", "pre"], 
        ["Enterprise", "enterprise"], 
        ["Mobile", "mobile"]
    ],
    "navigation_menu": [
        ["/matrices/", "matrices", "Matrices"],
        ["/tactics/", "tactics", "Tactics"],
        ["/techniques/", "techniques", "Techniques"],
        ["/mitigations/", "mitigations", "Mitigations"],
        ["/groups/", "groups", "Groups"],
        ["/software/", "software", "Software"],
        ["/resources/", "resources", "Resources"],
        ["https://medium.com/mitre-attack/", "blog", "Blog"],
        ["/resources/contribute", "contribute", "Contribute"]
    ]
}
platform_to_path = {
    "Windows": "enterprise/windows",
    "macOS": "enterprise/macos",
    "Linux": "enterprise/linux",
    "AWS": "enterprise/cloud/aws",
    "GCP": "enterprise/cloud/gcp",
    "Azure": "enterprise/cloud/azure",
    "Azure AD": "enterprise/cloud/azuread",
    "Office 365": "enterprise/cloud/office365",
    "SaaS": "enterprise/cloud/saas",
    "Android": "mobile/android",
    "iOS": "mobile/ios"
}
# config for the matrix shown on the index page
index_matrix = {
    "name": "ATT&CK Matrix for Enterprise",
    "descr": "", # if specified, adds a subtitle to the index page matrix
    "matrix": "enterprise-attack",
    "platforms": ["Windows", "macOS", "Linux"]
}

# The tree of matricies on /matrices/
matrices = [
    {
        "name": "PRE-ATT&CK",
        "type": "local",
        "path": "pre",
        "platforms": [],
        "matrix": "pre-attack",
        "descr": "Below are the tactics and techniques representing the MITRE PRE-ATT&CK Matrix.",
        "subtypes": [],
    },
    {
        "name": "Enterprise",
        "type": "local",
        "path": "enterprise",
        "matrix": "enterprise-attack",
        "platforms": ["Windows","macOS","Linux",
                      "AWS","GCP","Azure","Azure AD",
                      "Office 365","SaaS"],
        "descr": "Below are the tactics and technique representing the MITRE ATT&CK<sup>&reg;</sup> Matrix for Enterprise. ",
        "subtypes": [
            {
                "name": "Windows",
                "type": "local",
                "matrix": "enterprise-attack",
                "path": "enterprise/windows",
                "platforms": ["Windows"],
                "descr": "Below are the tactics and technique representing the MITRE ATT&CK<sup>&reg;</sup> Matrix; for Enterprise. ",
                "subtypes": []
            },
            {
                "name" : "macOS",
                "type": "local",
                "matrix": "enterprise-attack",
                "path": "enterprise/macos",
                "platforms": ["macOS"],
                "descr": "Below are the tactics and technique representing the MITRE ATT&CK<sup>&reg;</sup> Matrix for Enterprise. ",
                "subtypes": []
            },
            {
                "name" : "Linux",
                "type": "local",
                "matrix": "enterprise-attack",
                "platforms": ["Linux"],
                "path": "enterprise/linux",
                "descr": "Below are the tactics and technique representing the MITRE ATT&CK<sup>&reg;</sup> Matrix for Enterprise. ", 
                "subtypes": []
            },
            {
                "name": "Cloud",
                "type": "local",
                "matrix": "enterprise-attack",
                "path": "enterprise/cloud",
                "platforms": ["AWS","GCP","Azure","Azure AD","Office 365","SaaS"],
                "descr": "Below are the tactics and technique representing the MITRE ATT&CK<sup>&reg;</sup> Matrix for Enterprise covering cloud-based techniques. ",
                "subtypes": [
                    {
                        "name" : "AWS",
                        "type": "local",
                        "matrix": "enterprise-attack",
                        "path": "enterprise/cloud/aws",
                        "platforms": ["AWS"],
                        "descr": "Below are the tactics and technique representing the MITRE ATT&CK<sup>&reg;</sup> Matrix for Enterprise covering cloud-based techniques. ",
                        "subtypes": []
                    },
                    {
                        "name" : "GCP",
                        "type": "local",
                        "matrix": "enterprise-attack",
                        "path": "enterprise/cloud/gcp",
                        "platforms": ["GCP"],
                        "descr": "Below are the tactics and technique representing the MITRE ATT&CK<sup>&reg;</sup> Matrix for Enterprise covering cloud-based techniques. ",
                        "subtypes": []
                    },
                    {
                        "name": "Azure",
                        "type": "local",
                        "matrix": "enterprise-attack",
                        "path": "enterprise/cloud/azure",
                        "platforms": ["Azure"],
                        "descr": "Below are the tactics and technique representing the MITRE ATT&CK<sup>&reg;</sup> Matrix for Enterprise covering cloud-based techniques. ",
                        "subtypes": []
                    },
                    { 
                        "name" : "Office 365",
                        "type": "local",
                        "matrix": "enterprise-attack",
                        "path": "enterprise/cloud/office365",
                        "platforms": ["Office 365"],
                        "descr": "Below are the tactics and technique representing the MITRE ATT&CK<sup>&reg;</sup> Matrix for Enterprise covering cloud-based techniques. ",
                        "subtypes": []
                    },
                    {
                        "name" : "Azure AD",
                        "type": "local",
                        "matrix": "enterprise-attack",
                        "path": "enterprise/cloud/azuread",
                        "platforms": ["Azure AD"],
                        "descr": "Below are the tactics and technique representing the MITRE ATT&CK<sup>&reg;</sup> Matrix for Enterprise covering cloud-based techniques. ",
                        "subtypes": []
                    },
                    {
                        "name" : "SaaS",
                        "type": "local",
                        "matrix": "enterprise-attack",
                        "path": "enterprise/cloud/saas",
                        "platforms": ["SaaS"],
                        "descr": "Below are the tactics and technique representing the MITRE ATT&CK<sup>&reg;</sup> Matrix for Enterprise covering cloud-based techniques. ",
                        "subtypes": []
                    }
                ]
            }
        ]
    },
    {
        "name": "Mobile",
        "type": "local",
        "matrix": "mobile-attack",
        "path": "mobile",
        "platforms": ["Android", "iOS"],
        "descr": "Below are the tactics and techniques representing the two MITRE ATT&CK<sup>&reg;</sup> Matrices for Mobile. "
                 "The Matrices cover techniques involving device access and network-based effects that can be used by adversaries without device access. ",
        "subtypes": [
            {
                "name": "Android",
                "type": "local",
                "matrix": "mobile-attack",
                "path": "mobile/android",
                "platforms": ["Android"],
                "descr": "Below are the tactics and techniques representing the two MITRE ATT&CK<sup>&reg;</sup> Matrices for Mobile. "
                         "The Matrices cover techniques involving device access and network-based effects that can be used by adversaries without device access. ",
                "subtypes": []
            },
            {
                "name" : "iOS",
                "type": "local",
                "matrix": "mobile-attack",
                "path": "mobile/ios",
                "platforms": ["iOS"],
                "descr": "Below are the tactics and techniques representing the two MITRE ATT&CK<sup>&reg;</sup> Matrices for Mobile. "
                         "The Matrices cover techniques involving device access and network-based effects that can be used by adversaries without device access. ",
                "subtypes": []
            },
        ]
    }, 
    {
        "name": "ICS",
        "type": "external",
        "path": "https://collaborate.mitre.org/attackics",
        "subtypes": []
    }
]

# argument defaults and options for the CLI
build_choices = ['resources', 'contribute', 'groups', 'search', 'matrices', 'mitigations', 'redirects', 'software', 'tactics', 'techniques', "prev_versions"]
build_defaults = build_choices

test_choices = ['size', 'links', 'external_links', 'citations']
test_defaults = list(filter(lambda t: t != "external_links", test_choices))

# parsed arguments 
args = []

# directory for data used in site builds
data_directory = "data"
# directory for STIX data
stix_directory = data_directory + "/stix"
# STIX bundles for each domain
attack_path = {
    'enterprise-attack': stix_directory + "/enterprise-attack.json",
    'mobile-attack': stix_directory + "/mobile-attack.json",
    'pre-attack': stix_directory + "/pre-attack.json"
}

# Link to instance of the ATT&CK Navigator; change for to a custom location
navigator_link_enterprise = "https://mitre-attack.github.io/attack-navigator"
navigator_link_mobile = "https://mitre-attack.github.io/attack-navigator/mobile"

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

# HTML reference hyperlink inside of software table description
software_table_desc_link = ("<sup><a href=\"{}\" target=\"_blank\" "
                            "data-hasqtip=\"{}\" "
                            "aria-describedby=\"qtip-{}\">[{}]</a></sup>")
software_table_desc_link_no_url = "<sup>[{}]</sup>"

# Constants used by matrix.py
# ----------------------------------------------------------------------------

# Matrix markdown path
matrix_markdown_path = "content/pages/matrices/"

# ATT&CK index markdown path
attack_index_path = "content/pages/index.md"

# Matrix overview string
matrix_overview_md = ("Title: Matrix Overview \n"
                      "Template: general/redirect-index \n"
                      "RedirectLink: /matrices/enterprise/ \n"
                      "save_as: matrices/index.html")

# String template for main domain matrices
matrix_md = Template("Title: Matrix-${domain}\n"
                     "Template: matrices/matrix\n"
                     "save_as: matrices/${path}/index.html\n"
                     "data: ")

# String template for platform matrices
platform_md = Template("Title: Matrix-${domain}-${platform}\n"
                       "Template: matrices/matrix\n"
                       "save_as: matrices/${domain}/${platform_path}/index.html\n"
                       "data: ")

# ATT&CK overview
attack_index_md = ("Title: ATT&CK Overview \n"
                   "Template: general/attack-index \n"
                   "save_as: index.html\n"
                   "data: ")

# Old stix content
last_attack_path = {
    'enterprise-attack': stix_directory + "/enterprise-attack_old.json",
    'mobile-attack': stix_directory + "/mobile-attack_old.json",
    'pre-attack': stix_directory + "/pre-attack_old.json"
}

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
    {'from': 'ics', 'to': 'https://collaborate.mitre.org/attackics'},
    {'from': 'docs/MITRE_ATTACK_Enterprise_Poster_2018.pdf', 'to': '/docs/attack_matrix_poster_2018.pdf'},
    {'from': 'docs/ATTACK_Framework_Board_4x3.pdf', 'to': '/docs/attack_matrix_poster_2020.pdf'},
    {'from': 'docs/attack_roadmap.pdf', 'to': '/docs/attack_roadmap_2020.pdf'}
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

# Constants used in multiple files
# ----------------------------------------------------------------------------

# Not found constant
NOT_FOUND = -1

# Template for HTML references inside of sentences
reference_marker_template = ("<span onclick=scrollToRef('scite-{}') "
                             "id=\"scite-ref-{}-a\" class=\"scite"
                            "-citeref-number\" "
                             "data-reference=\"{}\"><sup><a href=\"{}\" "
                             "target=\"_blank\" data-hasqtip=\"{}\" "
                             "aria-describedby=\"qtip-{}\">[{}]</a></sup></span>")
reference_marker_template_no_url = ("<span onclick=scrollToRef('scite-{}') "
                                    "id=\"scite-ref-{}-a\" "
                                    "class=\"scite-citeref-number\" "
                                    "data-reference=\"{}\">"
                                    "<sup>[{}]</sup></span>")

tech_table_desc_link = ("<sup><a href=\"{}\" target=\"_blank\" "
                        "data-hasqtip=\"{}\" "
                        "aria-describedby=\"qtip-{}\">[{}]</a></sup>")
tech_table_desc_link_no_url = "<sup>[{}]</sup>"

# Exit codes:
SUCCESS = 0
FAILURE = 1
WARNING = 2
BROKEN_CITATION = -8
BROKEN_LINKS = -9
BROKEN_EXTERNAL_LINKS = -10
SIZE_ERROR = -11
UNLINKED_PAGES = -12
RELATIVE_LINKS_FOUND = -13

# Used to reset text color
RESET = '\033[0m'  # mode 0  = reset

# Window sizes
# Space for tests report
# Get windows width size and divide it by the three columns
window_size = shutil.get_terminal_size((80, 20))[0]
column_space = int(window_size/3) - 1
status_space = int(float(column_space)*0.80)
other_column_space = int(float(column_space)*1.10)

# Declare file location of web pages
web_directory = "output"

# Parent web directory name
# leave parent directory name to first level for link tests
parent_web_directory = "output"

# Declare as empty string
subdirectory = ""

def set_subdirectory(subdirectory_str):
    """ Method to globally set the subdirectory """

    global subdirectory
    global web_directory

    subdirectory = subdirectory_str

    # Verify if website directory exists
    if not os.path.isdir(web_directory):
        os.makedirs(web_directory)

    # Add subdirectory to web directory
    web_directory = os.path.join(web_directory, subdirectory)

test_report_directory = "reports"
# Constants used by citationschecker.py
# ----------------------------------------------------------------------------
citations_report_filename = "broken-citations-report.txt"

# Constants used by linkchecker.py
# ----------------------------------------------------------------------------
links_report_filename = "broken-links-report.txt"
unlinked_report_filename = "unlinked-pages-report.txt"
relative_links_report_filename = "relative-links-report.txt"

# Testing output statuses
PASSED_STATUS = colorama.Fore.GREEN + "PASSED" + RESET + \
                                         " " * (status_space - len("PASSED"))
FAILED_STATUS = colorama.Fore.RED + "FAILED" + RESET + \
                                        " " * (status_space - len("FAILED"))
WARNING_STATUS = colorama.Fore.YELLOW + "WARNING" + RESET + \
                                        " " * (status_space - len("WARNING"))   

def run_function(ptr):
    """Given a pointer to a function, run function and return output"""

    return ptr

def init_shared_data():
    """Resposible for initializing shared data between modules"""

    global source_names 
    global domains
    global domain_aliases
    global tools_used_by_groups
    global malware_used_by_groups
    global techniques_used_by_tools
    global techniques_used_by_malware
    global techniques_used_by_groups
    global groups_using_tool
    global groups_using_malware
    global technique_to_domain
    global custom_alphabet
    global relationships
    global technique_list
    global software_list
    global group_list
    global mitigation_list
    global mitigates_techniques
    global technique_mitigated
    global related_techniques
    global tools_using_technique
    global malware_using_technique
    global groups_using_technique
    global ms

    domains = settings_dict["domains"]
    domain_aliases = settings_dict["domain_aliases"]
    source_names = settings_dict["source_names"]

    # Global memory store of all domains
    ms = stixhelpers.get_stix_memory_stores()

    # Grab resources
    resources = stixhelpers.grab_resources(ms)

    # Shared lists
    relationships = resources['relationships']
    group_list = resources['groups']
    software_list = resources['software']
    technique_list = resources['techniques']
    mitigation_list = resources['mitigations']

    # Technique to domain dict 
    technique_to_domain = stixhelpers.get_technique_id_domain_map(ms)

    stix_array = []

    # Custom_alphabet used to sort list of dictionaries by domain name 
    # depending on domain ordering
    custom_alphabet = ""
    rest_of_alphabet = ""

    for domain in domains:
        # Remove whatever comes after the -
        short_domain = domain.split('-')[0]

        # Get first character of domain
        custom_alphabet += short_domain.lower()[:1]

        # Add rest of characters, doesn't matter if it is repeated
        rest_of_alphabet += short_domain.lower()[1:]

        # Append domain to stix
        stix_array.append(attack_path[domain])
    
    custom_alphabet += rest_of_alphabet

    # Source list of domains
    srcs = list(map(lambda url: rsh.load(url), stix_array))

    ptrs = [
        rsh.malware_used_by_groups(srcs),
        rsh.tools_used_by_groups(srcs),
        rsh.techniques_used_by_malware(srcs),
        rsh.techniques_used_by_tools(srcs),
        rsh.techniques_used_by_groups(srcs),
        rsh.groups_using_tool(srcs),
        rsh.groups_using_malware(srcs),
        rsh.mitigation_mitigates_techniques(srcs),
        rsh.technique_mitigated_by_mitigation(srcs),
        rsh.technique_related_to_technique(srcs),
        rsh.tools_using_technique(srcs),
        rsh.malware_using_technique(srcs),
        rsh.groups_using_technique(srcs)
    ]

    number_of_workers = multiprocessing.cpu_count()

    with multiprocessing.Pool(number_of_workers) as p:
        data = p.map(run_function, ptrs)
    
    # Get software used by groups
    malware_used_by_groups = data[0]
    tools_used_by_groups = data[1]

    # Get techniques used by software
    techniques_used_by_malware = data[2]
    techniques_used_by_tools = data[3]

    # Get techniques used by groups
    techniques_used_by_groups = data[4]

    # Groups using software
    groups_using_tool = data[5]
    groups_using_malware = data[6]

    # Mitigations mitigate techniques
    mitigates_techniques = data[7]

    # Technique mitigated by mitigation
    technique_mitigated = data[8]

    # Related techniques
    related_techniques = data[9]

    # Software using technique
    tools_using_technique = data[10]
    malware_using_technique = data[11]

    # Group using technique
    groups_using_technique = data[12]