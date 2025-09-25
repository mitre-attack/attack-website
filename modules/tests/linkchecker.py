import os
import re
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from loguru import logger

import modules
from modules import site_config

from . import tests_config

# STATIC PROPERTIES

IGNORED_LINKS = ["full-coverage.html", "macro-technique-refinement.html"]

ALLOWED_IN_LINK_INTERNAL = r"-?\w\$\.!\*'()/"
ALLOWED_IN_LINK_EXTERNAL = r"-?\w\$\.!\*'()/:"
LINK_POSTFIX = r']+)["\']'

# Pre-compiled regex patterns
LINK_REGEXES = {
    "href_internal": re.compile(r'href\s?=\s?["\']([' + ALLOWED_IN_LINK_INTERNAL + LINK_POSTFIX),
    "href_external": re.compile(r'href\s?=\s?["\']([' + ALLOWED_IN_LINK_EXTERNAL + LINK_POSTFIX),
    "src_internal": re.compile(r'src\s?=\s?["\']([' + ALLOWED_IN_LINK_INTERNAL + LINK_POSTFIX),
    "src_external": re.compile(r'src\s?=\s?["\']([' + ALLOWED_IN_LINK_EXTERNAL + LINK_POSTFIX),
    "cache_bust": re.compile(r"(css|js)\?\w+"),
}

# Caches
file_exists_cache = {}
get_correct_link_cache = {}
relative_link_cache = {}

links_list = {}
in_use_links = {}

internal_problem = False

# Google Chrome headers
headers = {
    "pragma": "no-cache",
    "cache-control": "no-cache",
    "user-agent": "Mozilla/5.0 "
    "(Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/76.0.3809.100 Safari/537.36",
    "sec-fetch-mode": "navigate",
    "accept": "text/html,application/xhtml+xml,application/xml;"
    "q=0.9,image/webp,image/apng,"
    "*/*;q=0.8,application/signed-exchange;v=b3",
    "sec-fetch-site": "none",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
}


def remove_extra_from_path(filepath):
    """Given a path, remove unwanted path from a website link."""
    return filepath.split(site_config.parent_web_directory)[1]


def get_correct_link(path):
    """Given a path, return the correct path by adding index.html or removing cache-disabling query string suffix."""
    # Use cache to avoid redundant work
    if path in get_correct_link_cache:
        return get_correct_link_cache[path]

    # Ignore if it starts with http
    if path.startswith("http"):
        get_correct_link_cache[path] = path
        return path

    # All paths need to start with /
    if not path.startswith("/"):
        path = "/" + path

    # Check if path is directory
    sort_of_extension = path.split(".")[-1]
    if sort_of_extension not in [
        "html",
        "css",
        "htm",
        "gif",
        "jpg",
        "png",
        "js",
        "json",
        "ico",
        "jpeg",
        "svg",
        "pdf",
        "xlsx",
        "docx",
        "rtf",
    ]:
        if LINK_REGEXES["cache_bust"].search(sort_of_extension):
            # CSS & JavaScript: check for cache-disabling query string suffix, e.g style.min.css?f8be4c06
            path = path.split("?")[0]  # remove suffix
        else:
            # is referring to a directory, not a file; webserver would
            # serve index.html if you fetch the directory without
            # serving a file add index.html to replicate webserver
            # functionality
            if not path.endswith("/"):
                path += "/"
            path += "index.html"

    get_correct_link_cache[path] = path
    return path


def check_if_link_in_use(filepath, link):
    """Given a filepath and a link, check if the link is already linked by another page.

    If not, verify that the link is not the same as the filepath and add it to the in use links map.
    """
    if "previous" not in link and "versions" not in link:
        if not in_use_links.get(link):
            new_file_name = remove_extra_from_path(filepath)

            if new_file_name.startswith("\\"):
                new_file_name = new_file_name.replace("\\", "/")

            if new_file_name != link:
                in_use_links[link] = True


def internal_link_test(link):
    """Given a link, make sure that that it exists on the file system."""
    if site_config.subdirectory:
        web_dir = site_config.web_directory.split(site_config.subdirectory)[0]
    else:
        web_dir = site_config.web_directory

    # Get correct link path
    path = web_dir + get_correct_link(link)

    # e.g: contacts.html -> contacts/index.html
    to_index_path = path
    if path.endswith(".html") and not path.endswith("index.html"):
        to_index_path = path.split(".html")
        to_index_path = to_index_path[0] + "/" + "index.html"

    # e.g: contacts/index.html -> contacts.html
    from_index_path = path
    if path.endswith("/index.html"):
        from_index_path = path.split("/index.html")
        from_index_path = from_index_path[0] + ".html"

    # Use cache for file existence checks
    for test_path in (path, to_index_path, from_index_path):
        if test_path in file_exists_cache:
            if file_exists_cache[test_path]:
                return False
        else:
            exists = os.path.exists(test_path)
            file_exists_cache[test_path] = exists
            if exists:
                return False
    return True


def check_if_relative_link(link):
    """Given a link, return true if it is a relative path."""
    if link in relative_link_cache:
        return relative_link_cache[link]
    result = not link.startswith("http") and not link.startswith("/")
    relative_link_cache[link] = result
    return result


def internal_external_link_checker(filepath, html_str):
    """Check internal and external links."""
    # Flag to determine if internal link is broken
    internal_link_error = False

    # Array to store problems found
    problems = []
    relative_links = []

    # find all links
    for prefix in ["href", "src"]:
        # Regular expression includes http: and https:
        if (
            "/versions/" in filepath
        ):  # don't check links with data-test-ignore attribute, or live version link name, when on previous versions
            linkregex = rf'{prefix}\s?=\s?["\']([{ALLOWED_IN_LINK_EXTERNAL}]+)["\'](?! ?data-test-ignore="true")(?!>live version)'
        else:
            linkregex = rf"{prefix}\s?=\s?[\"']([{ALLOWED_IN_LINK_EXTERNAL}]+)[\"']"
        links = re.findall(linkregex, html_str)

        # check if link has a dest
        for link in links:
            # Check if link is relative path
            is_relative = check_if_relative_link(link)

            # Add to relative links list if relative
            if is_relative:
                if link not in relative_links:
                    relative_links.append(link)

            # Get correct path
            link = get_correct_link(link)
            # Check if link is in use
            check_if_link_in_use(filepath, link)

            if link in links_list:
                # If problem detected, add to problem list
                if links_list[link]:
                    if link not in problems:
                        problems.append(f"[{links_list[link]}] {link}")
            elif link.startswith("http"):
                # Consider status 404 and unreachable as broken.
                # Unreachable will be triggered by the except clause
                try:
                    r = requests.head(link, headers=headers, timeout=5)
                    if r.status_code != 200:
                        links_list[link] = r.status_code
                        problems.append(f"[{r.status_code}] {link}")
                    else:
                        links_list[link] = None
                except Exception as ex:
                    links_list[link] = f"external link {type(ex).__name__}"
                    problems.append(f"[external link {type(ex).__name__}] {link}")
            else:
                if internal_link_test(link):
                    problems.append(f"[internal page missing] {link}")
                    links_list[link] = "internal page missing"

                    if not internal_link_error:
                        internal_link_error = True
                else:
                    links_list[link] = None

    return problems, relative_links, internal_link_error


def internal_link_checker(filepath, html_str):
    """Given an html page as a string, check if there are broken internal links."""
    # Flag to determine if internal link is broken
    internal_link_error = False

    problems = []
    relative_links = []

    # find all links
    for prefix in ["href", "src"]:
        links = re.findall(rf"{prefix}\s?=\s?[\"']([{ALLOWED_IN_LINK_INTERNAL}]+)[\"']", html_str)
        # check if link has a dest
        for link in links:
            # Check if link is relative path
            is_relative = check_if_relative_link(link)

            # Add to relative links list if relative
            if is_relative:
                if link not in relative_links:
                    relative_links.append(link)

            # Get correct path
            link = get_correct_link(link)

            for ignored_link in IGNORED_LINKS:
                if ignored_link in link:
                    logger.debug(f"Ignoring link: {link}")
                    links_list[link] = None

            # Check if link is in use
            check_if_link_in_use(filepath, link)

            if link in links_list:
                if links_list[link]:
                    if link not in problems:
                        problems.append(f"[{links_list[link]}] {link}")
            else:
                if internal_link_test(link):
                    problems.append(f"[internal page missing] {link}")
                    links_list[link] = "internal page missing"

                    if not internal_link_error:
                        internal_link_error = True
                else:
                    links_list[link] = None

    return problems, relative_links, internal_link_error


def check_if_file_is_deprecated(filename):
    """Given a filename, verify if it is deprecated.

    Return True if it is deprecated, False if not.
    """
    with open(filename, "r", encoding="utf8") as f:
        lines = f.readlines()
        for line in lines:
            if '<meta name="robots" content="noindex, nofollow">' in line:
                return True
    return False


def check_unlinked_pages(filenames):
    """Given a list of filenames, check if they where linked from another page.

    Add the files that are not linked to a list a return the list.
    """
    unlinked_pages = []
    for filename in filenames:
        if "previous" not in filename and "versions" not in filename:
            # Check if it is deprecated
            if check_if_file_is_deprecated(filename):
                continue

            # Remove unused filepath from filename
            filename = remove_extra_from_path(filename)

            if filename.startswith("\\"):
                filename = filename.replace("\\", "/")

            # Ignore 404 html page
            if filename.endswith("/404.html"):
                continue

            if "sidebar" in filename:
                continue

            # e.g: contacts.html -> contacts/index.html
            to_index_path = filename
            if filename.endswith(".html") and not filename.endswith("index.html"):
                to_index_path = filename.split(".html")
                to_index_path = to_index_path[0] + "/" + "index.html"

            # e.g: contacts/index.html -> contacts.html
            from_index_path = filename
            if filename.endswith("/index.html"):
                from_index_path = filename.split("/index.html")
                from_index_path = from_index_path[0] + ".html"

            if (
                not in_use_links.get(filename)
                and not in_use_links.get(to_index_path)
                and not in_use_links.get(from_index_path)
            ):
                unlinked_pages.append(filename)
    return unlinked_pages


def check_links_on_page(filepath, check_external_links=False):
    """Return whether the links on the given file are all valid."""
    # Declare just in case there is a problem opening the file
    problems = []
    relative_links = []
    internal_problem = False

    with open(filepath, mode="r", encoding="utf8") as html:
        html_str = html.read()

        if "previous" not in filepath and "versions" not in filepath:
            # Add redirects to in-use to avoid false positives
            if html_str.startswith('<meta http-equiv="refresh"'):
                corrected_path = remove_extra_from_path(filepath)

                if corrected_path.startswith("\\"):
                    corrected_path = corrected_path.replace("\\", "/")

                if not in_use_links.get(corrected_path):
                    in_use_links[corrected_path] = True

        if check_external_links:
            problems, relative_links, internal_problem = internal_external_link_checker(filepath, html_str)
        else:
            problems, relative_links, internal_problem = internal_link_checker(filepath, html_str)

    filepath = remove_extra_from_path(filepath)
    return {
        "path": filepath,
        "problems": problems,
        "relative_links": relative_links,
        "internal_problem": internal_problem,
    }


def check_links(external_links=False):
    """Check all links on the site to make sure that they have a valid destination."""
    broken_pages = []
    relative_links = []
    filenames = []
    internal_problem = False

    html_filepaths = []
    for directory, _, files in os.walk(site_config.web_directory):
        for filename in filter(lambda f: f.endswith(".html"), files):
            filepath = os.path.join(directory, filename)
            filenames.append(filepath)
            html_filepaths.append(filepath)

    # Parallelize link checking
    max_workers = min(32, os.cpu_count() or 4)
    lock = threading.Lock()
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_filepath = {}
        for filepath in html_filepaths:
            if external_links and "previous" not in filepath and "versions" not in filepath:
                future = executor.submit(check_links_on_page, filepath, True)
            else:
                future = executor.submit(check_links_on_page, filepath)
            future_to_filepath[future] = filepath

        for future in as_completed(future_to_filepath):
            report = future.result()
            with lock:
                # Set internal problem flag to true if internal link is broken
                if not internal_problem and report.get("internal_problem"):
                    internal_problem = True
                if report.get("problems"):
                    broken_pages.append(report)
                if report.get("relative_links"):
                    relative_links_report = {
                        "path": report["path"],
                        "relative_links": report["relative_links"],
                    }
                    relative_links.append(relative_links_report)

    # Get unlinked pages list
    unlinked_pages = check_unlinked_pages(filenames)

    # logger.info(f"Writing report: unlinked pages")
    with open(os.path.join(site_config.test_report_directory, tests_config.unlinked_report_filename), "w") as f:
        f.write("Unlinked pages report:\n\n")
        if unlinked_pages:
            f.write("Pages listed were not linked from another page\n\n")
            for page in unlinked_pages:
                f.write(page + "\n")
        else:
            f.write("No unlinked pages found\n")

    # logger.info(f"Writing report: broken links")
    broken_count = 0
    with open(os.path.join(site_config.test_report_directory, tests_config.links_report_filename), "w") as f:
        f.write("Broken links report:\n\n")
        build_versions_module = False
        for module_info in modules.run_ptr:
            if module_info["module_name"] == "versions":
                build_versions_module = True
        if broken_pages:
            for page in broken_pages:
                f.write(page["path"] + "\n")
                for problem in page["problems"]:
                    if "versions" in problem:
                        if build_versions_module:
                            f.write("\t- " + problem + "\n")
                            broken_count += 1
                    else:
                        f.write("\t- " + problem + "\n")
                        broken_count += 1
        else:
            f.write("No broken links found\n")

    # logger.info(f"Writing report: relative links")
    with open(os.path.join(site_config.test_report_directory, tests_config.relative_links_report_filename), "w") as f:
        f.write("Relative links report:\n\n")
        if relative_links:
            for page in relative_links:
                f.write(page["path"] + "\n")
                for relative_link in page["relative_links"]:
                    f.write("\t- " + relative_link + "\n")
        else:
            f.write("No relative links found\n")

    links = (len(links_list) - broken_count, broken_count)

    exit_codes = []

    # Add exit codes depending on problems found
    if broken_count and internal_problem:
        exit_codes.append(tests_config.BROKEN_LINKS)
    elif broken_count:
        exit_codes.append(tests_config.BROKEN_EXTERNAL_LINKS)
    if unlinked_pages:
        exit_codes.append(tests_config.UNLINKED_PAGES)
    if relative_links:
        exit_codes.append(tests_config.RELATIVE_LINKS_FOUND)

    if not exit_codes:
        exit_codes.append(tests_config.SUCCESS)

    return exit_codes, links, len(unlinked_pages), len(relative_links)
