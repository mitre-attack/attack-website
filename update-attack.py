import argparse
import colorama
import json
import os
import time
from string import Template

import modules
from modules import site_config
from modules import util

# argument defaults and options for the CLI
module_choices = ['clean', 'stix_data', 'resources', 'contribute', 'groups', 'search', 'matrices', 'mitigations', 'redirects', 'software', 'tactics', 'techniques', "prev_versions"]
module_defaults = module_choices

test_choices = ['size', 'links', 'external_links', 'citations']
test_defaults = list(filter(lambda t: t != "external_links", test_choices))


# def handle_exit(exit_codes):
#     """Given a exit codes list, exit with 1 on failure and 0 on success
#        for CI
#     """

#     # Check if exit codes list is not empty
#     if exit_codes:
#         # Exit on failure if any of these exit codes are found
#         # Regarding the link checker, only exit on failure if a problem
#         # is found on an internal link
#         if config.BROKEN_CITATION in exit_codes or \
#                 config.BROKEN_LINKS in exit_codes or \
#                 config.SIZE_ERROR in exit_codes:
#             exit(config.FAILURE)
#     # Exit on success
#     exit(config.SUCCESS)

# def update(args):
#     """Run all modules"""

#     exit_codes = []
    
#     # Generate index markdown
#     if args.build:
#         generate.index_md_gen()
    
#     # Pelican update
#     if args.build:
#         generate.pelican_content()
#         # Remove unwanted files created by pelican
#         generate.remove_unwanted_output()
    
#     if args.build:
#         build_end = time.time()
#         build_time = build_end - update_start
    
#     # Tests
#     if (args.build and (sorted(args.build) == sorted(config.build_defaults))) or args.tests:
#         # Start time of tests update
#         test_start = time.time()
#         exit_codes = tests.run_tests(args)
#         test_end = time.time()
#         test_time = test_end - test_start
    
#     if args.build and ((sorted(args.build) == sorted(config.build_defaults)) or args.tests):
#         util.progress_bar("TOTAL Build Time", build_time)
#         util.progress_bar("TOTAL Test Time", test_time)
    
    # if not args.override_exit_status:
    #     handle_exit(exit_codes)

def get_parsed_args():
    """Create argument parser and parse arguments"""

    parser = argparse.ArgumentParser(description=("Build the ATT&CK website.\n"
                                     "To run a complete build, run this script with the -c and -b flags. "))
    parser.add_argument('--refresh', '-r', action='store_true',
                        help='Pull down the current STIX data from the MITRE/CTI GitHub respository')
    parser.add_argument('--no-stix-link-replacement', action='store_true',
                        help="If this flag is absent, links to attack.mitre.org/[page] in the STIX data will be replaced with /[page]. Add this flag to preserve links to attack.mitre.org.")
    
    parser.add_argument('--modules', '-m', nargs='*',
                        type=str,
                        choices=module_choices,
                        help=("Build modules. If no option is specified, "
                              "it will run all modules from the modules directory. "
                              "Run specific modules by selecting from the "
                              "list and leaving one space in "
                              "between them. For example: '-m clean techniques tactics'."))                          
    # parser.add_argument('--test', '-t', nargs='*',
    #                     choices=test_choices,
    #                     dest="tests",
    #                     help="Run tests. If no option is specified, "
    #                           "all choices will be selected except external_links. "
    #                           "Run specific tests "
    #                           "by selecting from the list and leaving "
    #                           "one space in between them. For example: '-t output links'. "
    #                           "Tests: "
    #                           "size (size of output directory against github pages limit); "
    #                           "links (dead internal hyperlinks and relative hyperlinks); "
    #                           "external_links (dead external hyperlinks); "
    #                           "citations (unparsed citation text).")
    
    parser.add_argument('--proxy', help="set proxy")

    parser.add_argument("--print-tests", 
                        dest="print_tests", 
                        action="store_true",
                        help="Force test output to print to stdout even if the results are very long.")

    parser.add_argument("--no-test-exitstatus", 
                        dest="override_exit_status", 
                        action='store_true', 
                        help="Forces application to exit with success status codes even if tests fail.")

    args = parser.parse_args()

    # Set global argument list for modules
    site_config.args = args

    # # If the tests flag was called without params, set to all
    # if (not args.tests and isinstance(args.tests, list)) or (args.build and args.build == config.build_defaults and not args.tests):
    #     args.tests = config.test_defaults
    
    return args

def remove_false_results_from_menu(results):
    """ Given a list of results, remove elements from menu if their result was False """

    def remove_from_menu_list(element, result):
        if element['name'] == result[1]:
            modules.menu_ptr.remove(element)

    for result in results:
        if result[0] == False:
            for module in modules.menu_ptr:
                remove_from_menu_list(module, result)

def remove_from_build(arg_modules):
    """ Given a list of modules from command line, remove modules that appear in module
        directory that are not in list.
    """

    def remove_from_running_pool():
        """ Remove modules from running pool if they are not in modules list from argument """

        for module in modules.run_ptr:
            if module["name"].lower() not in arg_modules:
                modules.run_ptr.remove(module)
    
    def remove_from_menu():
        """ Remove modules from menu if they are not in modules list from argument """

        for module in modules.menu_ptr:
            if module["name"].lower() not in arg_modules:
                modules.menu_ptr.remove(module)
    
    remove_from_running_pool()
    remove_from_menu()

if __name__ == "__main__":
    """Beginning of ATT&CK update module"""

    # Get args
    args = get_parsed_args()

    # If modules flags are called only run modules selected by user
    if args.modules:
        remove_from_build(args.modules)

    # Used to store running modules results
    results = []

    # Start time of update
    update_start = time.time()

    # Init colorama for output
    colorama.init()

    # Get running modules and priorities
    for ptr in modules.run_ptr:
        util.buildhelpers.print_start(ptr['name'])
        start_time = time.time()
        results.append(ptr['run_module']())
        end_time = time.time()
        util.buildhelpers.print_end(ptr['name'], start_time, end_time)

    # Remove false results from menu
    remove_false_results_from_menu(results)

    # Will be part of generate base html module
    with open(os.path.join(site_config.template_dir, "base.bak"), "r", encoding='utf8') as base_template_f:
        base_template = base_template_f.read()
        base_template = Template(base_template)
        subs = base_template.substitute(site_config.base_page_data)

    with open(os.path.join(site_config.template_dir, "base.html"), "w", encoding='utf8') as base_template_f:
        base_template_f.write(subs)

    # Print end of module
    update_end = time.time()
    util.buildhelpers.print_end("TOTAL Update Time", update_start, update_end)

    # # Generate base template for ATT&CK pages
    # generate_base_template()
    