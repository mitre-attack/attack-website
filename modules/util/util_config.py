import colorama
import shutil

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

# Source names for ATT&CK
source_names = [
    "mitre-pre-attack", 
    "mitre-attack", 
    "mitre-mobile-attack"
]

# Used to reset text color
RESET = '\033[0m'  # mode 0  = reset

# Window sizes
# Space for tests report
# Get windows width size and divide it by the three columns
window_size = shutil.get_terminal_size((80, 20))[0]
column_space = int(window_size/3) - 1
status_space = int(float(column_space)*0.80)
other_column_space = int(float(column_space)*1.10)

# Testing output statuses
PASSED_STATUS = colorama.Fore.GREEN + "PASSED" + RESET + \
                                         " " * (status_space - len("PASSED"))
FAILED_STATUS = colorama.Fore.RED + "FAILED" + RESET + \
                                        " " * (status_space - len("FAILED"))
WARNING_STATUS = colorama.Fore.YELLOW + "WARNING" + RESET + \
                                        " " * (status_space - len("WARNING")) 