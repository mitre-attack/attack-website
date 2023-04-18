import os
from datetime import datetime
from pathlib import Path

import bleach
import markdown
import stix2validator
from loguru import logger

from modules import site_config, util

from . import linkbyidchecker, stixtests_config


def run_tests():
    """Run tests"""
    error_list = []
    tests = 0

    logger.info("Removing old reports")
    reports = [stixtests_config.linkbyids_report_filename]
    for report in reports:
        Path(f"{site_config.test_report_directory}/{report}").unlink(missing_ok=True)

    logger.info("Creating reports directory")
    Path(site_config.test_report_directory).mkdir(parents=True, exist_ok=True)

    logger.info("Running tests:")

    # using this to download STIX if needed
    util.relationshipgetters.get_ms()

    options = stix2validator.ValidationOptions(version="2.0", disabled=["all"])
    for domain in site_config.domains:
        if domain["deprecated"]:
            logger.debug(f"Skipping validation for {domain['name']} because it is deprecated")
            continue

        # TODO: refactor this to use a function rather than copy/paste from modules/util/stixhelpers.py
        # this can be used because it was called previously in modules/util/stixhelpers.py to download the file
        if domain["location"].startswith("http"):
            download_dir = Path(f"{site_config.web_directory}/stix")
            stix_filename = f"{download_dir}/{domain['name']}.json"
        else:
            stix_filename = domain["location"]

        logger.info(f"Validating STIX for domain: {domain['name']}")
        results = stix2validator.validate_file(fn=stix_filename, options=options)
        if results.is_valid:
            logger.info(f"File {stix_filename} is valid")
        else:
            logger.error(f"File {stix_filename} is invalid:")

            stix2validator.print_results(results)

            # TODO: implement this once this GitHub issue is resolved
            # https://github.com/oasis-open/cti-stix-validator/issues/192

            # error_file = f"{site_config.test_report_directory}/{stix_filename}-stix-errors.txt"
            # with open(error_file, "w") as error_f:
            #     error_f.write(results)

    #################
    # Check LinkByIds
    #################
    if (site_config.args.tests and "linkbyid" in site_config.args.tests) or not site_config.args.tests:
        tests += 1
        exit_code, broken_linkbyids_count = check_linkbyids()
        if exit_code == stixtests_config.BROKEN_LINKBYID:
            error_list.append(stixtests_config.BROKEN_LINKBYID)

    create_combined_reports_html()

    # Successful tests vs failed tests
    tests_passed = tests - len(error_list)
    tests_failed = len(error_list)
    logger.info(f"{tests_passed} test(s) passed, {tests_failed} test(s) failed")

    if error_list:
        if stixtests_config.BROKEN_LINKBYID in error_list:
            display_error_report(
                report_file=os.path.join(site_config.test_report_directory, stixtests_config.linkbyids_report_filename),
                error_count=broken_linkbyids_count,
                error_type="Broken LinkByIds",
            )

    if not site_config.args.override_exit_status:
        handle_exit(error_list)


def display_error_report(report_file, error_count, error_type):
    if error_count < 6 or site_config.args.print_tests:
        with open(report_file, "r", encoding="utf-8") as error_report:
            logger.warning(error_report.read())
    else:
        logger.warning(f"{error_type} report written to {report_file}")


def check_linkbyids():
    """Wrapper to check for broken LinkById's"""
    TEST = "Broken LinkByIds"
    logger.info(f"Running {TEST}")

    exit_code, broken_linkbyids_count = linkbyidchecker.linkbyid_check()

    if exit_code == stixtests_config.SUCCESS:
        STATUS = stixtests_config.PASSED_STATUS
    else:
        STATUS = stixtests_config.FAILED_STATUS

    MSG = f"{broken_linkbyids_count} broken LinkByIds"

    logger.debug(f"STATUS {STATUS} TEST {TEST} MSG {MSG}")
    return exit_code, broken_linkbyids_count


def create_combined_reports_html():
    reports = os.listdir(site_config.test_report_directory)

    report_sections = []
    for report in reports:
        with open(os.path.join(site_config.test_report_directory, report), "r") as f:
            if report.endswith(".md"):
                report_sections.append(markdown.markdown(f.read(), extensions=["tables"]))
            else:
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

    with open(os.path.join(site_config.test_report_directory, stixtests_config.combined_reports_filename), "w") as f:
        f.write(report_html)


def handle_exit(exit_codes):
    """Given a exit codes list, exit with 1 on failure and 0 on success for CI."""
    # Check if exit codes list is not empty
    if exit_codes:
        # Exit on failure if any of these exit codes are found
        # Regarding the link checker, only exit on failure if a problem
        # is found on an internal link
        if stixtests_config.BROKEN_LINKBYID in exit_codes:
            exit(stixtests_config.FAILURE)
