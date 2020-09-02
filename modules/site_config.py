import colorama
import modules
import os
import shutil
from modules import util
from string import Template

# Domains for stix objects
domains = ["pre-attack", "enterprise-attack", "mobile-attack"]

# Domain aliases
domain_aliases = [
    ["PRE-ATT&CK", "pre"], 
    ["Enterprise", "enterprise"], 
    ["Mobile", "mobile"] 
]

# Args for modules to use if needed
args = []

# Source names for ATT&CK
source_names = [
    "mitre-pre-attack", 
    "mitre-attack", 
    "mitre-mobile-attack"
]

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

# Location of html templates
templates_directory = "attack-theme/templates/"

javascript_path = "attack-theme/static/scripts/"

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
navigator_link_enterprise = "https://mitre-attack.github.io/attack-navigator/enterprise"
navigator_link_mobile = "https://mitre-attack.github.io/attack-navigator/mobile"

# Markdown path for redirects
redirects_markdown_path = "content/pages/redirects/"

# Redirect md string template
redirect_md = Template("Title: ${title}\n"
                       "Template: general/redirect-index\n"
                       "RedirectLink: ${to}\n"
                       "save_as: ${from}")

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
srcs = list(map(lambda url: util.relationshiphelpers.load(url), stix_array))

# Constants used for generated layers
# ----------------------------------------------------------------------------
# usage: 
#     domain: "enterprise" or "mobile"
#     path: the path to the object, e.g "software/S1001" or "groups/G2021"
layer_md = Template("Title: ${domain} Techniques\n"
                    "Template: general/json\n"
                    "save_as: ${path}/${attack_id}-${domain}-layer.json\n"
                    "json: ")
no_stix_link_replacement = ""
