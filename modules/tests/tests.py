import os
import shutil
from datetime import datetime

import bleach
from loguru import logger

from modules import site_config, util

from . import citationchecker, linkchecker, sizechecker, tests_config


def run_tests():
    """Run tests"""
    error_list = []
    tests = 0

    logger.info("Remove old reports")
    if os.path.isdir(site_config.test_report_directory):
        shutil.rmtree(site_config.test_report_directory)

    logger.info("Running tests:")
    util.buildhelpers.print_test_output("-", "-", "-")
    util.buildhelpers.print_test_output("STATUS", "TEST", "MESSAGE")
    util.buildhelpers.print_test_output("-", "-", "-")

    # Check output size
    if (site_config.args.tests and "size" in site_config.args.tests) or not site_config.args.tests:
        tests += 1
        if check_size() == tests_config.SIZE_ERROR:
            error_list.append(tests_config.SIZE_ERROR)

    # Check internal links
    if (
        site_config.args.tests and ("links" in site_config.args.tests or "external_links" in site_config.args.tests)
    ) or not site_config.args.tests:
        tests += 3
        # Check external and internal links if external link flag was set.
        # Only check internal links if not set
        if site_config.args.tests:
            do_external = "external_links" in site_config.args.tests
        else:
            do_external = False
        exit_codes, broken_links_count, unlinked_pages, relative_links = check_links(do_external)

        for exit_code in exit_codes:
            if exit_code != tests_config.SUCCESS:
                error_list.append(exit_code)

    # Check citations
    if (site_config.args.tests and "citations" in site_config.args.tests) or not site_config.args.tests:
        tests += 1
        exit_code, broken_citations_count = check_citations()
        if exit_code == tests_config.BROKEN_CITATION:
            error_list.append(tests_config.BROKEN_CITATION)

    util.buildhelpers.print_test_output("-", "-", "-")

    # Successful tests vs failed tests
    tests_passed = tests - len(error_list)
    tests_failed = len(error_list)
    logger.info(f"{tests_passed} test(s) passed, {tests_failed} test(s) failed")

    if error_list:
        if tests_config.BROKEN_CITATION in error_list:
            report_file = os.path.join(site_config.test_report_directory, tests_config.citations_report_filename)
            # Print report if less than six broken citations
            if broken_citations_count < 6 or site_config.args.print_tests:
                with open(report_file, "r", encoding="utf-8") as citations_report:
                    print(citations_report.read())
            else:
                logger.info(f"Broken citations report written to {report_file}")

        if tests_config.BROKEN_LINKS in error_list or tests_config.BROKEN_EXTERNAL_LINKS in error_list:
            report_file = os.path.join(site_config.test_report_directory, tests_config.links_report_filename)
            if broken_links_count < 6 or site_config.args.print_tests:
                # Print report if less than six broken citations
                with open(report_file, "r", encoding="utf-8") as links_report:
                    print(links_report.read())
            else:
                logger.info(f"Broken links report written to {report_file}")

        if tests_config.UNLINKED_PAGES in error_list:
            report_file = os.path.join(site_config.test_report_directory, tests_config.unlinked_report_filename)
            # Print report if flag is stated
            if unlinked_pages < 6 or site_config.args.print_tests:
                with open(report_file, "r", encoding="utf-8") as unlinked_report:
                    print(unlinked_report.read())
            else:
                logger.info(f"Unlinked pages report written to {report_file}")

        if tests_config.RELATIVE_LINKS_FOUND in error_list:
            report_file = os.path.join(site_config.test_report_directory, tests_config.relative_links_report_filename)
            # Print report if flag is stated
            if relative_links < 6 or site_config.args.print_tests:
                with open(report_file, "r", encoding="utf-8") as relative_links_report:
                    print(relative_links_report.read())
            else:
                logger.info(f"Relative links report written to {report_file}")

    create_combined_reports_html()

    if not site_config.args.override_exit_status:
        handle_exit(error_list)


def check_links(external_links):
    """Wrapper to check internal and/or external links"""
    # Link test
    TEST = "Links"

    util.buildhelpers.print_test_output("RUNNING", TEST, "-")

    exit_codes, links, unlinked_pages, relative_links = linkchecker.check_links(external_links)

    if tests_config.BROKEN_LINKS in exit_codes:
        STATUS = tests_config.FAILED_STATUS
    elif tests_config.BROKEN_EXTERNAL_LINKS in exit_codes:
        STATUS = tests_config.WARNING_STATUS
    else:
        STATUS = tests_config.PASSED_STATUS

    if external_links:
        TEST = "Internal/External Links"
    else:
        TEST = "Internal Links"

    MSG = ("{} OK - {} broken link(s) ").format(links[0], links[1])

    # Print output
    util.buildhelpers.print_test_output(STATUS, TEST, MSG)

    # Unlinked pages test
    TEST = "Unlinked Pages"

    if tests_config.UNLINKED_PAGES in exit_codes:
        STATUS = tests_config.WARNING_STATUS
    else:
        STATUS = tests_config.PASSED_STATUS

    MSG = ("{} unlinked page(s)").format(unlinked_pages)

    util.buildhelpers.print_test_output(STATUS, TEST, MSG)

    # Unlinked pages test
    TEST = "Relative Links"

    if tests_config.RELATIVE_LINKS_FOUND in exit_codes:
        STATUS = tests_config.WARNING_STATUS
    else:
        STATUS = tests_config.PASSED_STATUS

    MSG = ("{} page(s) with relative link(s) found").format(relative_links)

    util.buildhelpers.print_test_output(STATUS, TEST, MSG)

    return exit_codes, links[1], unlinked_pages, relative_links


def check_citations():
    """Wrapper to check for broken citations"""
    TEST = "Broken Citations"
    util.buildhelpers.print_test_output("RUNNING", TEST, "-")

    exit_code, pages = citationchecker.citations_check()

    if exit_code == tests_config.SUCCESS:
        STATUS = tests_config.PASSED_STATUS
    else:
        STATUS = tests_config.FAILED_STATUS

    if pages[1] == 1:
        MSG = "{} pages OK, {} page broken".format(pages[0], pages[1])
    else:
        MSG = "{} pages OK, {} pages broken".format(pages[0], pages[1])

    util.buildhelpers.print_test_output(STATUS, TEST, MSG)

    return exit_code, pages[1]


def check_size():
    """Wrapper to check output size for Github's limit"""
    TEST = "Output Folder Size"
    util.buildhelpers.print_test_output("RUNNING", TEST, "-")

    MB_TO_GB_CONVERSION = 1000

    exit_code, size_MB = sizechecker.check_output_size()

    if exit_code == tests_config.SUCCESS:
        STATUS = tests_config.PASSED_STATUS
        MSG = f"Size: {size_MB:.2f} MB"

    elif exit_code == tests_config.WARNING:
        STATUS = tests_config.WARNING_STATUS
        MSG = "Approaching 1 GB limit: " + f"{size_MB:.2f} MB"
    else:
        STATUS = tests_config.FAILED_STATUS
        MSG = "Surpassed 1 GB limit: " f"{size_MB/MB_TO_GB_CONVERSION:.3f} GB" + tests_config.RESET

    util.buildhelpers.print_test_output(STATUS, TEST, MSG)

    return exit_code


def create_combined_reports_html():
    reports = os.listdir(site_config.test_report_directory)

    report_sections = []
    for report in reports:
        with open(os.path.join(site_config.test_report_directory, report), "r") as f:
            report_sections.append("<code><pre>\n" + bleach.clean(f.read()) + "\n</pre></code>")

    report_sections = "\n<hr />\n".join(report_sections)
    now = datetime.now().strftime("%m/%d/%Y, %H:%M")

    report_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ATT&CK Test Reports</title>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet"> 
    </head>
    <body>
        <div class="container">
            <h1>ATT&CK Test Reports</h1>
            <p>This page lists the results of the tests run on the ATT&CK STIX data and on the HTML of the built site.</p>
            <p>This report was generated on <b>{now}</b></p>
            <hr />
            {report_sections}
        </div>
    </body>
    <style>
        .container {{
            max-width: 55em;
            margin: 0 auto;
            font-family: 'Roboto', sans-serif;
        }}
        h1 {{
            text-align: center;
            display: flex;
            align-items: center;
        }}
        h1:after, h1:before {{
            flex: 1 0;
            content: '';
            border-bottom: 1px solid black;
        }}
        h1:after {{
            margin-left: 15px;
        }}
        h1:before {{
            margin-right: 15px;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin-bottom: 16px;
        }}
        th {{
            background: rgba(0,0,0, 0.08)
        }}
        th, td {{
            padding: 5px 10px;
            border: 1px solid rgba(0,0,0, 0.12);
            text-align: left;
        }}
    </style>
    </html>
    """

    with open(os.path.join(site_config.test_report_directory, tests_config.combined_reports_filename), "w") as f:
        f.write(report_html)


def handle_exit(exit_codes):
    """Given a exit codes list, exit with 1 on failure and 0 on success for CI."""
    # Check if exit codes list is not empty
    if exit_codes:
        # Exit on failure if any of these exit codes are found
        # Regarding the link checker, only exit on failure if a problem
        # is found on an internal link
        if (
            tests_config.BROKEN_CITATION in exit_codes
            or tests_config.BROKEN_LINKS in exit_codes
            or tests_config.SIZE_ERROR in exit_codes
        ):
            exit(tests_config.FAILURE)
