import os
import re

from loguru import logger

from modules import site_config

from . import tests_config

potential_issues_list = ["\(Citation: ?[^)]+\)?"]


def citations_check():
    """Check for broken citations: (Citation: *) in HTML pages"""
    # Hold broken pages information
    broken_pages = []
    okay_files = 0

    for directory, _, files in os.walk(site_config.web_directory):
        # skip previous instances of the code to speed this up
        if "previous" in directory or "versions" in directory:
            continue
        for filename in files:
            problems = []
            if filename == "changelog-detailed.html":
                continue
            if filename.endswith(".html"):
                filepath = os.path.join(directory, filename)
                with open(filepath, "r", encoding="utf8") as f_handle:
                    data = f_handle.read()
                    for issue in potential_issues_list:
                        p = re.compile(issue)
                        check = p.findall(data)
                        for entry in check:
                            if not entry in problems:
                                problems.append(entry)
            if not problems:
                okay_files += 1
            else:
                if site_config.web_directory in filepath:
                    filepath = filepath.split(site_config.web_directory)[1]
                broken_pages.append({"path": filepath, "problems": problems})

    exit_code = write_report(
        report_file=os.path.join(site_config.test_report_directory, tests_config.citations_report_filename),
        report_title="Broken Citations Report",
        broken_pages=broken_pages,
    )

    # Return exit code and file information
    files_info = (okay_files, len(broken_pages))
    return exit_code, files_info


def write_report(report_file, report_title, broken_pages):
    # logger.info(f"Writing report: {report_title}")
    with open(report_file, "w") as f:
        f.write(f"{report_title}:\n\n")

        if broken_pages:
            for page in broken_pages:
                f.write(page["path"] + "\n")
                for problem in page["problems"]:
                    f.write("\t- " + problem + "\n")
            exit_code = tests_config.BROKEN_CITATION
        else:
            f.write("No broken citations found\n")
            exit_code = tests_config.SUCCESS

    return exit_code
