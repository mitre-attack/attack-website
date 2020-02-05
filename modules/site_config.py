import colorama
import modules
import os
import shutil
from modules import util

# Domains for stix objects
domains = ["pre-attack", "enterprise-attack", "mobile-attack"]

# Source names for ATT&CK
source_names = [
    "mitre-pre-attack", 
    "mitre-attack", 
    "mitre-mobile-attack"
]

# Base page data for website header and footer
base_page_data = {
    "BANNER_ENABLED": True,
    "BANNER_MESSAGE": "<strong><a href='https://collaborate.mitre.org/attackics' target='_blank'>JUST RELEASED: ATT&CK for Industrial Control Systems</a></strong>",
    "CONTENT_VERSION": "6.2",
    "WEBSITE_VERSION": "1.1.1",
    "CHANGELOG_LOCATION": "/resources/changelog.html",
    "NAVIGATION_MENU": modules.menu_ptr
}

# Template directory
template_dir = os.path.join("attack-theme", "templates", "general/")

# Declare file location of web pages
web_directory = "output"
# Directory for test reports
test_report_directory = "reports"

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