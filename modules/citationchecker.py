import re
import os
from . import config

potential_issues_list = ['[(]Citation:[^ ][^)]+[)]']

def citations_check():
    """Check for broken citations: (Citation: *) in HTML pages"""

    # Hold broken pages information
    broken_pages = []

    okay_files = 0

    for directory, _, files in os.walk(config.web_directory):
        # skip previous instances of the code to speed this up
        if 'previous' in directory or 'versions' in directory: 
            continue
        for filename in files:
            problems = []
            if filename.endswith('.html'):
                filepath = os.path.join(directory,filename)
                with open(
                        filepath,'r', 
                        encoding='utf8') as f_handle:
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
                if config.web_directory in filepath:
                    filepath = filepath.split(config.web_directory)[1]
                broken_pages.append({"path": filepath, "problems": problems})
    
    if broken_pages:
        if not (os.path.isdir(config.test_report_directory)):
            os.mkdir(config.test_report_directory)
        with open(os.path.join(config.test_report_directory, config.citations_report_filename), 'w') as f:
            f.write("Broken Citations Report:\n\n")
            for page in broken_pages:
                f.write(page["path"] + "\n")
                for problem in page["problems"]:
                    f.write("\t- " + problem + "\n")
        exit_code = config.BROKEN_CITATION
    else:
        exit_code = config.SUCCESS

    # Return exit code and file information
    files_info = (okay_files, len(broken_pages))
    return exit_code, files_info