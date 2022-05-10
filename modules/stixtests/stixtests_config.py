import colorama

from modules import util

module_name = "STIX Tests"
priority = 1

# Filenames for test reports
linkbyids_report_filename = "linkbyids-report.md"

combined_reports_filename = "stixtests.html"

# Exit codes:
SUCCESS = 0
FAILURE = 1
WARNING = 2
BROKEN_LINKBYID = -14

# Used to reset text color
RESET = "\033[0m"  # mode 0  = reset

# Testing output statuses
PASSED_STATUS = colorama.Fore.GREEN + "PASSED" + RESET + " " * (util.util_config.status_space - len("PASSED"))
FAILED_STATUS = colorama.Fore.RED + "FAILED" + RESET + " " * (util.util_config.status_space - len("FAILED"))
WARNING_STATUS = colorama.Fore.YELLOW + "WARNING" + RESET + " " * (util.util_config.status_space - len("WARNING"))
