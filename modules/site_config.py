import json
import os
from string import Template

from dotenv import load_dotenv

import modules

load_dotenv()

attack_version = ""

# Read versions file for ATT&CK version
with open("data/versions.json", "r", encoding="utf8") as f:
    attack_version = json.load(f)["current"]["name"]

# ATT&CK version
if attack_version.startswith("v"):
    full_attack_version = attack_version
    attack_version = attack_version[1:]

# Domains for stix objects
STIX_LOCATION_ENTERPRISE = os.getenv(
    "STIX_LOCATION_ENTERPRISE",
    "https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json",
)
STIX_LOCATION_MOBILE = os.getenv(
    "STIX_LOCATION_MOBILE", "https://raw.githubusercontent.com/mitre/cti/master/mobile-attack/mobile-attack.json"
)
STIX_LOCATION_ICS = os.getenv(
    "STIX_LOCATION_ICS", "https://raw.githubusercontent.com/mitre/cti/master/ics-attack/ics-attack.json"
)
STIX_LOCATION_PRE = os.getenv(
    "STIX_LOCATION_PRE", "https://raw.githubusercontent.com/mitre/cti/master/pre-attack/pre-attack.json"
)
domains = [
    {"name": "enterprise-attack", "location": STIX_LOCATION_ENTERPRISE, "alias": "Enterprise", "deprecated": False},
    {"name": "mobile-attack", "location": STIX_LOCATION_MOBILE, "alias": "Mobile", "deprecated": False},
    {"name": "ics-attack", "location": STIX_LOCATION_ICS, "alias": "ICS", "deprecated": False},
    {"name": "pre-attack", "location": STIX_LOCATION_PRE, "alias": "PRE-ATT&CK", "deprecated": True},
]

# banner for the website
default_banner_message = "This is a custom instance of the MITRE ATT&CK Website. The official website can be found at <a href='https://attack.mitre.org'>attack.mitre.org</a>."
BANNER_ENABLED = os.getenv("BANNER_ENABLED", True)
BANNER_MESSAGE = os.getenv("BANNER_MESSAGE", default_banner_message)

# Args for modules to use if needed
args = []

# Staged for pelican settings
staged_pelican = {}


def send_to_pelican(key, value):
    """Method to stage key value pairs for pelican use"""
    staged_pelican[key] = value


def check_versions_module():
    """Return if versions module is loaded"""
    if [key["module_name"] for key in modules.run_ptr if key["module_name"] == "versions"]:
        return True
    return False


def check_resources_module():
    """Return if resources module is loaded"""
    if [key["module_name"] for key in modules.run_ptr if key["module_name"] == "resources"]:
        return True
    return False


# Source names for ATT&CK
source_names = ["mitre-attack", "mitre-mobile-attack", "mitre-ics-attack", "mitre-pre-attack"]

# Declare file location of web pages
web_directory = "output"

# Parent web directory name
# leave parent directory name to first level for link tests
parent_web_directory = "output"

# Declare as empty string
subdirectory = ""


def set_subdirectory(subdirectory_str):
    """Method to globally set the subdirectory"""

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

# Static style pelican files directory
static_style_dir = os.path.join("attack-theme", "static", "style/")

# directory for data used in site builds
data_directory = "data"

# Link to instance of the ATT&CK Navigator; change for to a custom location
navigator_link = "https://mitre-attack.github.io/attack-navigator/"

# Content directory
content_dir = "content/"

# Pelican pages directory
pages_dir = "content/pages"

# Pelican docs directory
docs_dir = "content/docs/"

# Markdown path for redirects
redirects_markdown_path = "content/pages/redirects/"

# markdown path for resources
resources_markdown_path = "content/pages/resources/"

# Redirect md string template
redirect_md_index = Template(
    "Title: ${title}\n"
    "Template: general/redirect-index\n"
    "RedirectLink: ${to}\n"
    "save_as: ${from}/index.html"
)
redirect_md = Template(
    "Title: ${title}\n"
    "Template: general/redirect-index\n"
    "RedirectLink: ${to}\n"
    "save_as: ${from}"
)

# Custom_alphabet used to sort list of dictionaries by domain name
# depending on domain ordering
custom_alphabet = ""
rest_of_alphabet = ""

for domain in domains:
    if not domain["deprecated"]:
        # Remove whatever comes after the -
        if "-" in domain["name"]:
            short_domain = domain["name"].split("-")[0]
        else:
            short_domain = domain["name"]

        # Get first character of domain
        custom_alphabet += short_domain.lower()[:1]

        # Add rest of characters, doesn't matter if it is repeated
        rest_of_alphabet += short_domain.lower()[1:]

custom_alphabet += rest_of_alphabet

# Constants used for generated layers
# ----------------------------------------------------------------------------
# usage:
#     domain: "enterprise", "mobile", "ics"
#     path: the path to the object, e.g "software/S1001" or "groups/G2021"
layer_md = Template(
    "Title: ${domain} Techniques\n"
    "Template: general/json\n"
    "save_as: ${path}/${attack_id}-${domain}-layer.json\n"
    "json: "
)
layer_version = "4.4"
navigator_version = "4.8.1"

# Directory for test reports
test_report_directory = "reports"

# Workbench credentials to use if pulling STIX from ATT&CK Workbench version 1.2.0 or later
WORKBENCH_USER = os.getenv("WORKBENCH_USER")
WORKBENCH_API_KEY = os.getenv("WORKBENCH_API_KEY")

GOOGLE_ANALYTICS = os.getenv("GOOGLE_ANALYTICS")
GOOGLE_SITE_VERIFICATION = os.getenv("GOOGLE_SITE_VERIFICATION")
