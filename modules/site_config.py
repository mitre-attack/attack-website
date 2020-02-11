import colorama
import modules
import os
import shutil
from modules import util

# Domains for stix objects
domains = ["pre-attack", "enterprise-attack", "mobile-attack"]

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

# Old stix content
last_attack_path = {
    'enterprise-attack': stix_directory + "/enterprise-attack_old.json",
    'mobile-attack': stix_directory + "/mobile-attack_old.json",
    'pre-attack': stix_directory + "/pre-attack_old.json"
}

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

# Source list of domains
srcs = list(map(lambda url: util.relationshiphelpers.load(url), stix_array))

no_stix_link_replacement = ""