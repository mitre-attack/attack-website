import colorama

from modules import util

module_name = "Tests"
priority = 21

# Filenames for test reports
citations_report_filename = "broken-citations-report.txt"
links_report_filename = "broken-links-report.txt"
unlinked_report_filename = "unlinked-pages-report.txt"
relative_links_report_filename = "relative-links-report.txt"
linkbyids_report_filename = "linkbyids-report.md"

combined_reports_filename = "tests.html"

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
BROKEN_LINKBYID = -14

# Used to reset text color
RESET = "\033[0m"  # mode 0  = reset

# Testing output statuses
PASSED_STATUS = colorama.Fore.GREEN + "PASSED" + RESET + " " * (util.util_config.status_space - len("PASSED"))
FAILED_STATUS = colorama.Fore.RED + "FAILED" + RESET + " " * (util.util_config.status_space - len("FAILED"))
WARNING_STATUS = colorama.Fore.YELLOW + "WARNING" + RESET + " " * (util.util_config.status_space - len("WARNING"))
