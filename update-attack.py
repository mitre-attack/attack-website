import argparse
import time

import colorama
from dotenv import load_dotenv
from loguru import logger

import modules
from modules import site_config, util

load_dotenv()

# argument defaults and options for the CLI
module_choices = [
    "clean",
    "datasources",
    "groups",
    "search",
    "matrices",
    "mitigations",
    "software",
    "tactics",
    "techniques",
    "campaigns",
    "assets",
    "tour",
    "website_build",
    "random_page",
    "redirections",
    "subdirectory",
    "tests",
]
extras = ["resources", "versions", "blog", "stixtests", "benefactors"]
test_choices = ["size", "links", "external_links", "citations"]


def validate_subdirectory_string(subdirectory_str):
    """Validate subdirectory string."""
    if not subdirectory_str.isascii():
        raise argparse.ArgumentTypeError(f"{subdirectory_str} contains non ascii characters")

    # Remove leading and trailing /
    if subdirectory_str.startswith("/"):
        subdirectory_str = subdirectory_str[1:]
    if subdirectory_str.endswith("/"):
        subdirectory_str = subdirectory_str[:-1]

    site_config.set_subdirectory(subdirectory_str)

    return subdirectory_str


def get_parsed_args():
    """Create argument parser and parse arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Build the ATT&CK website.\n"
            "All flags are optional. If you run the build without flags, "
            "the modules that pertain to the ATT&CK dataset will be ran. "
            "If you would like to run extra modules, opt-in these modules with the"
            "--extras flag."
        )
    )
    parser.add_argument(
        "--no-stix-link-replacement",
        action="store_true",
        help="If this flag is absent, links to attack.mitre.org/[page] in the STIX data will be replaced with /[page]. Add this flag to preserve links to attack.mitre.org.",
    )
    parser.add_argument(
        "--modules",
        "-m",
        nargs="+",
        type=str,
        choices=module_choices,
        help=(
            "Run specific modules by selecting from the "
            "list and leaving one space in "
            "between them. For example: '-m clean techniques tactics'."
            "Will run all the modules if flag is not called, or selected "
            "without arguments."
        ),
    )
    parser.add_argument(
        "--extras",
        "-e",
        nargs="*",
        type=str,
        choices=extras,
        help=(
            "Run extra modules that do not pertain to the ATT&CK dataset. "
            "Select from the list and leaving one space in "
            "between them. For example: '-m resources blog'.\n"
            "These modules will only run if the user adds this flag. "
            "Calling this flag without arguments will select all the extra modules."
        ),
    )
    parser.add_argument(
        "--test",
        "-t",
        nargs="+",
        choices=test_choices,
        dest="tests",
        help=(
            "Run specific tests by selecting from the list and leaving "
            "one space in between them. For example: '-t output links'. "
            "Tests: "
            "size (size of output directory against github pages limit); "
            "links (dead internal hyperlinks and relative hyperlinks); "
            "external_links (dead external hyperlinks); "
            "citations (unparsed citation text)."
        ),
    )
    parser.add_argument(
        "--attack-brand", action="store_true", help="Applies ATT&CK brand colors. See also the --extras flag."
    )
    parser.add_argument("--proxy", help="set proxy")
    parser.add_argument(
        "--subdirectory",
        help="If you intend to host the site from a sub-directory, specify the directory using this flag.",
        type=validate_subdirectory_string,
    )
    parser.add_argument(
        "--print-tests",
        dest="print_tests",
        action="store_true",
        help="Force test output to print to stdout even if the results are very long.",
    )
    parser.add_argument(
        "--no-test-exitstatus",
        dest="override_exit_status",
        action="store_true",
        help="Forces application to exit with success status codes even if tests fail.",
    )
    parser.add_argument(
        "--banner",
        type=str,
        help=(
            "If specified, sets the banner for the site to this string. "
            "If left out and the banner is enabled, the text will come from either "
            "the modules/site_config.py BANNER_MESSAGE variable or the BANNER_MESSAGE environment variable in that order."
        ),
    )
    parser.add_argument(
        "--banner-disable",
        action="store_true",
        help=(
            "Explicitly disable the banner when building the website. "
            "Default behavior without this flag is to have a banner generated on the site."
        ),
    )
    parser.add_argument(
        "--google-analytics",
        type=str,
        help=("If a Google Analytics ID is provided, then the site will include it on all pages."),
    )
    parser.add_argument(
        "--google-site-verification",
        type=str,
        help=("If a Google site verification code is provided, then the site will include it on all pages."),
    )

    args = parser.parse_args()

    # If modules is empty, means all modules will be ran
    if not args.modules:
        args.modules = module_choices

    # If the extras flag was called without params, set to all
    if not args.extras and isinstance(args.extras, list):
        args.extras = extras

    # Set global argument list for modules
    site_config.args = args

    return args


def remove_from_build(arg_modules, arg_extras):
    """Given a list of modules from command line, remove modules that appear in module directory that are not in list."""

    def remove_from_running_pool():
        """Remove modules from running pool if they are not in modules list from argument"""
        copy_of_modules = []

        for module in modules.run_ptr:
            if module["module_name"].lower() in arg_modules:
                copy_of_modules.append(module)

        modules.run_ptr = copy_of_modules

    def remove_from_menu():
        """Remove modules from menu if they are not in modules list from argument"""
        copy_of_menu = []

        for module in modules.menu_ptr:
            if module["module_name"].lower() in arg_modules:
                copy_of_menu.append(module)

        modules.menu_ptr = copy_of_menu

    # Only add extra modules if argument flag was used
    if arg_extras:
        arg_modules = arg_modules + arg_extras

    remove_from_running_pool()
    remove_from_menu()


if __name__ == "__main__":
    """Beginning of ATT&CK update module"""
    # Get args
    args = get_parsed_args()

    # Remove modules from build
    remove_from_build(args.modules, args.extras)

    # Arguments used for pelican
    site_config.send_to_pelican("no_stix_link_replacement", args.no_stix_link_replacement)

    # Start time of update
    update_start = time.time()

    # Init colorama for output
    colorama.init()

    # Get running modules and priorities
    for ptr in modules.run_ptr:
        util.buildhelpers.print_start(ptr["module_name"])
        start_time = time.time()
        ptr["run_module"]()
        end_time = time.time()
        util.buildhelpers.print_end(ptr["module_name"], start_time, end_time)
    
    # Print end of module
    update_end = time.time()
    util.buildhelpers.print_end("TOTAL Update Time", update_start, update_end)
