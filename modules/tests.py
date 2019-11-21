import shutil
from . import citationchecker
from . import config
from . import linkchecker
from . import sizechecker
from . import util
import os 

def run_tests(args):
    """Run tests"""

    error_list = []
    tests = 0

    print("\nRunning tests:")
    util.print_test_output("-"*(config.status_space-1), 
                           "-"*(config.other_column_space-1), 
                           "-"*(config.other_column_space-1))
    util.print_test_output("STATUS","TEST","MESSAGE")
    util.print_test_output("-"*(config.status_space-1), 
                           "-"*(config.other_column_space-1), 
                           "-"*(config.other_column_space-1))

    # Check output size
    if (config.build_defaults == args.build) or \
       ('size' in args.tests):
        tests += 1
        if check_size() == config.SIZE_ERROR:
            error_list.append(config.SIZE_ERROR)

    # Check internal links
    if (config.build_defaults == args.build) or \
       ('links' in args.tests or 'external_links' in args.tests):
        tests += 3
        # Check external and internal links if external link flag was set. 
        # Only check internal links if not set
        do_external = "external_links" in args.tests
        exit_codes, broken_links_count, unlinked_pages, relative_links = check_links(do_external)

        for exit_code in exit_codes:
            if exit_code != config.SUCCESS:
                error_list.append(exit_code)
        
    # Check citations
    if (config.build_defaults == args.build) or \
       ('citations' in args.tests):
        tests += 1
        exit_code, broken_citations_count = check_citations()
        if exit_code == config.BROKEN_CITATION:
            error_list.append(config.BROKEN_CITATION)
    
    util.print_test_output("-"*(config.status_space-1), 
                           "-"*(config.other_column_space-1), 
                           "-"*(config.other_column_space-1))
    
    # Successful tests vs failed tests
    if (tests - len(error_list)) == 1:
        if len(error_list) == 1:
            print("\n{} test passed, {} test failed\n".format(
                tests - len(error_list), len(error_list)))
        else:
            print("\n{} test passed, {} tests failed\n".format(
                tests - len(error_list), len(error_list)))
    else:
        if len(error_list) == 1:
            print("\n{} tests passed, {} test failed\n".format(
                tests - len(error_list), len(error_list)))
        else:
            print("\n{} tests passed, {} tests failed\n".format(
                tests - len(error_list), len(error_list)))
    
    if error_list:
        if config.BROKEN_CITATION in error_list:
            # Print report if less than six broken citations
            if broken_citations_count < 6 or args.print_tests:
                with open(
                        os.path.join(config.test_report_directory, config.citations_report_filename), "r", 
                        encoding='utf-8') as citations_report:
                    print(citations_report.read())
            else:
                print("Broken citations report written to {}".format(
                    os.path.join(config.test_report_directory, config.citations_report_filename)))

        if config.BROKEN_LINKS in error_list or config.BROKEN_EXTERNAL_LINKS in error_list:
            if broken_links_count < 6 or args.print_tests:
                # Print report if less than six broken citations
                with open(
                        os.path.join(config.test_report_directory, config.links_report_filename), "r", 
                        encoding='utf-8') as links_report:
                    print(links_report.read())
            else:
                print("Broken links report written to {}".format(
                      os.path.join(config.test_report_directory, config.links_report_filename)))

        if config.UNLINKED_PAGES in error_list:
            # Print report if flag is stated
            if unlinked_pages < 6 or args.print_tests:
                with open(
                        os.path.join(config.test_report_directory, config.unlinked_report_filename), "r", 
                        encoding='utf-8') as unlinked_report:
                    print(unlinked_report.read())
            else:
                print("Unlinked pages report written to {}".format(
                    os.path.join(config.test_report_directory, config.unlinked_report_filename)))
        if config.RELATIVE_LINKS_FOUND in error_list:
            # Print report if flag is stated
            if relative_links < 6 or args.print_tests:
                with open(
                        os.path.join(config.test_report_directory, config.relative_links_report_filename), "r", 
                        encoding='utf-8') as relative_links_report:
                    print(relative_links_report.read())
            else:
                print("Unlinked pages report written to {}".format(
                    os.path.join(config.test_report_directory, config.relative_links_report_filename)))
    
    return error_list

def check_links(external_links):
    """Wrapper to check internal and/or external links"""

    # Link test

    TEST = "Links"

    util.print_test_output("RUNNING",TEST,"-")

    exit_codes, links, unlinked_pages, relative_links = linkchecker.check_links(external_links)

    if config.BROKEN_LINKS in exit_codes:
        STATUS = config.FAILED_STATUS
    elif config.BROKEN_EXTERNAL_LINKS in exit_codes:
        STATUS = config.WARNING_STATUS
    else:
        STATUS = config.PASSED_STATUS

    if external_links:
        TEST = "Internal/External Links"
    else:
        TEST = "Internal Links"

    MSG = ("{} OK - {} broken link(s) ").format(links[0], links[1])

    # Print output
    util.print_test_output(STATUS,TEST,MSG)

    # Unlinked pages test
    TEST = "Unlinked Pages"

    if config.UNLINKED_PAGES in exit_codes:
        STATUS = config.WARNING_STATUS
    else:
        STATUS = config.PASSED_STATUS

    MSG = ("{} unlinked page(s)").format(unlinked_pages)

    util.print_test_output(STATUS,TEST,MSG)

    # Unlinked pages test
    TEST = "Relative Links"

    if config.RELATIVE_LINKS_FOUND in exit_codes:
        STATUS = config.WARNING_STATUS
    else:
        STATUS = config.PASSED_STATUS

    MSG = ("{} page(s) with relative link(s) found").format(relative_links)

    util.print_test_output(STATUS,TEST,MSG)

    return exit_codes, links[1], unlinked_pages, relative_links

def check_citations():
    """Wrapper to check for broken citations"""

    TEST = "Broken Citations"

    util.print_test_output("RUNNING",TEST,"-")

    exit_code, pages = citationchecker.citations_check()

    if exit_code == config.SUCCESS:
        STATUS = config.PASSED_STATUS
    else:
        STATUS = config.FAILED_STATUS

    if pages[1] == 1:
        MSG = "{} pages OK, {} page broken".format(pages[0],pages[1])
    else:
        MSG = "{} pages OK, {} pages broken".format(pages[0],pages[1])

    util.print_test_output(STATUS,TEST,MSG)

    return exit_code, pages[1]

def check_size():
    """Wrapper to check output size for Github's limit"""

    TEST = "Output Folder Size"

    util.print_test_output("RUNNING",TEST,"-")

    MB_TO_GB_CONVERSION = 1000
    
    exit_code, size_MB = sizechecker.check_output_size()

    if exit_code == config.SUCCESS:
        STATUS = config.PASSED_STATUS
        MSG = f"Size: {size_MB:.2f} MB"

    elif exit_code == config.WARNING:
        STATUS = config.WARNING_STATUS
        MSG = "Approaching 1 GB limit: " + f"{size_MB:.2f} MB"
    else:
        STATUS = config.FAILED_STATUS
        MSG = "Surpassed 1 GB limit: " \
                f"{size_MB/MB_TO_GB_CONVERSION:.3f} GB" + config.RESET

    util.print_test_output(STATUS,TEST,MSG)

    return exit_code