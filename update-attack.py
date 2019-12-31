import argparse
import colorama
import json
import os
import requests
import time
from modules import generate
from modules import config
from modules import tests
from modules import util
from string import Template

def get_stix_data(args):
    """Set up proxy if any and get STIX data"""

    # Set proxy
    proxy  = ""
    if args.proxy is not None:
        proxy = args.proxy
    proxyDict = { 
        "http"  : proxy,
        "https" : proxy
    }

    use_local_stix = True
    for domain in config.settings_dict['domains']:
        if not (os.path.isfile('{0}/{1}.json'.format(config.stix_directory, domain))):
            use_local_stix = False

    if (not os.path.isdir(config.stix_directory)):
        os.mkdir(config.stix_directory)
    try:
        util.progress_bar("Downloading STIX Data")
        start_time = time.time()

        for domain in config.settings_dict['domains']:
            r = requests.get(f"https://raw.githubusercontent.com/mitre/cti/master/{domain}/{domain}.json", 
            verify=False, proxies=proxyDict)
            
            with open(os.path.join(config.stix_directory, domain + "_old.json"), 'w+') as f:
                f.write(json.dumps(r.json()))
                
                if (args.refresh or not os.path.isdir(config.stix_directory) or not use_local_stix):
                    with open(os.path.join(config.stix_directory, domain + ".json"), 'w+') as f:
                        f.write(json.dumps(r.json()))

        end_time = time.time()
        util.progress_bar("Downloading STIX Data", end_time - start_time)
    except:
        end_time = time.time()
        util.progress_bar("Downloading STIX Data", end_time - start_time)
        print("Unable to reach stix repository. Are you behind a (--proxy)?")

def handle_exit(exit_codes):
    """Given a exit codes list, exit with 1 on failure and 0 on success
       for CI
    """

    # Check if exit codes list is not empty
    if exit_codes:
        # Exit on failure if any of these exit codes are found
        # Regarding the link checker, only exit on failure if a problem
        # is found on an internal link
        if config.BROKEN_CITATION in exit_codes or \
                config.BROKEN_LINKS in exit_codes or \
                config.SIZE_ERROR in exit_codes:
            exit(config.FAILURE)
    # Exit on success
    exit(config.SUCCESS)

def update(args):
    """Run all modules"""

    exit_codes = []

    # Start time of update
    update_start = time.time()

    # Clean output/content directory if flag is set
    if args.clean:
        generate.clean_website()    

    # Grab shared resources and stix data
    if args.build:
        get_stix_data(args)
        generate.grab_resources()
    
    # Generate index markdown
    if args.build:
        generate.index_md_gen()

    # Generate group markdowns
    if args.build:
        if 'groups' in args.build:
            generate.group_md_gen()

    # Software markdown generation
    if args.build:
        if 'software' in args.build:
            generate.software_md_gen()

    # Generate technique markdowns
    if args.build:
        if 'techniques' in args.build:
            generate.technique_md_gen()

    # Generate matrix markdowns
    if args.build:
        if 'matrices' in args.build:
            generate.matrix_md_gen()

    # Generate tactic markdowns
    if args.build:
        if 'tactics' in args.build:
            generate.tactic_md_gen()

    # Generate mitigation markdowns
    if args.build:
        if 'mitigations' in args.build:
            generate.mitigation_md_gen()

    # Generate contribute markdowns
    if args.build:
        if 'contribute' in args.build:
            generate.contribute_md_gen()
    
    # Generate resources markdowns
    if args.build:
        if 'resources' in args.build:
            generate.resources_md_gen()
        
    # Generate redirects markdowns
    if args.build:
        if 'redirects' in args.build:
            generate.redirects_md_gen()

    # Generate Index
    if args.build:
        if 'search' in args.build:
    	    generate.generate_search_index()

    # Deploy previous version
    if args.build:
        if 'prev_versions' in args.build:
    	    generate.previous_versions_gen()
    
    # Pelican update
    if args.build:
        generate.pelican_content()
        # Remove unwanted files created by pelican
        generate.remove_unwanted_output()
    
    if args.build:
        build_end = time.time()
        build_time = build_end - update_start
    
    # Tests
    if (args.build and (sorted(args.build) == sorted(config.build_defaults))) or args.tests:
        # Start time of tests update
        test_start = time.time()
        exit_codes = tests.run_tests(args)
        test_end = time.time()
        test_time = test_end - test_start
    
    if args.build and ((sorted(args.build) == sorted(config.build_defaults)) or args.tests):
        util.progress_bar("TOTAL Build Time", build_time)
        util.progress_bar("TOTAL Test Time", test_time)
    
    update_end = time.time()
    util.progress_bar("TOTAL Update Time", update_end - update_start)

    if not args.override_exit_status:
        handle_exit(exit_codes)

def get_parsed_args():
    """Create argument parser and parse arguments"""

    parser = argparse.ArgumentParser(description=("Build the ATT&CK website.\n"
                                     "To run a complete build, run this script with the -c and -b flags. "))
    parser.add_argument('--clean', '-c', action='store_true',
                        help='Clean files from previous builds')
    parser.add_argument('--refresh', '-r', action='store_true',
                        help='Pull down the current STIX data from the MITRE/CTI GitHub respository')
    parser.add_argument('--no-stix-link-replacement', action='store_true',
                        help="If this flag is absent, links to attack.mitre.org/[page] in the STIX data will be replaced with /[page]. Add this flag to preserve links to attack.mitre.org.")
    
    parser.add_argument('--build', '-b', nargs='*',
                        type=str,
                        choices=config.build_choices,
                        help=("Build modules. If no option is specified, "
                              "all choices will be selected. "
                              "Run specific modules by selecting from the "
                              "list and leaving one space in "
                              "between them. For example: '-b techniques'."))                          
    
    parser.add_argument('--test', '-t', nargs='*',
                        choices=config.test_choices,
                        dest="tests",
                        help="Run tests. If no option is specified, "
                              "all choices will be selected except external_links. "
                              "Run specific tests "
                              "by selecting from the list and leaving "
                              "one space in between them. For example: '-t output links'. "
                              "Tests: "
                              "size (size of output directory against github pages limit); "
                              "links (dead internal hyperlinks and relative hyperlinks); "
                              "external_links (dead external hyperlinks); "
                              "citations (unparsed citation text).")
    
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

    if (not args.clean) and (not args.refresh) and (args.build is None) and (args.tests is None):
        parser.print_help()
        exit(0)

    # If the build flag was called without params, set to all
    if not args.build and isinstance(args.build, list):
        args.build = config.build_defaults

    # If the tests flag was called without params, set to all
    if (not args.tests and isinstance(args.tests, list)) or (args.build and args.build == config.build_defaults and not args.tests):
        args.tests = config.test_defaults

    config.args = args
    
    return args

def generate_base_template():
    """Generate base template with settings stored in config.py"""

    # String template for base template	
    base_template = Template("{% set BANNER_ENABLED = \"${banner_enabled}\" %}\n"
                             "{% set BANNER_MESSAGE = \"${banner_message}\" %}\n"
                             "{% set NAVIGATION_MENU = ${navigation} -%}\n"
                             "{% set DOMAINS = ${domains} -%}\n"
                             "{% set CONTENT_VERSION = \"${content_version}\" -%}\n"
                             "{% set WEBSITE_VERSION = \"${website_version}\" -%}\n"
                             "{% set CHANGELOG_LOCATION = \"${changelog_location}\" -%}\n"
                             "{% set active_page = active_page|"
                             "default('index') -%}\n")
    
    base_template_path = "./attack-theme/templates/general/base.html"

    with open(base_template_path, 'r') as f:
        base_dict = {}

        base_html = f.read()
        base_html = base_html.split("{% set active_page = active_page|"
                                            "default('index') -%}\n")[-1] 
        base_dict['banner_enabled'] = config.settings_dict['banner_enabled']
        base_dict['banner_message'] = config.settings_dict['banner_message'].\
                                                            replace("\"", "'")
        base_dict['navigation'] = config.settings_dict['navigation_menu']
        base_dict['domains'] = config.settings_dict['domain_aliases']
        base_dict['content_version'] = config.settings_dict['content_version']
        base_dict['website_version'] = config.settings_dict['website_version']
        base_dict['changelog_location'] = config.settings_dict['changelog_location']
        jinja_settings = base_template.substitute(base_dict)
  
    with open(base_template_path, 'w+') as f:
        f.write(jinja_settings + base_html)

if __name__ == "__main__":
    """Beginning of ATT&CK update module"""

    # Get args
    args = get_parsed_args()

    # Generate base template for ATT&CK pages
    generate_base_template()

    # Init colorama for output
    colorama.init()
    
    # Update ATT&CK
    update(args)
