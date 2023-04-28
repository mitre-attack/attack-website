import html
import json
import os
import re
from collections import defaultdict

import bleach
from loguru import logger

import modules
from modules import site_config, versions

types = ["software", "datasources", "groups", "tactics", "techniques"]
sub_types = ["mobile", "enterprise", "ics"]
types_hash = set(types)
sub_types_hash = set(sub_types)
dist_words = 0


def generate_index():
    logger.info("Creating searchable index for the site")
    index_data = defaultdict(list)
    global_id_counter = 0

    for root, __, files in os.walk(site_config.web_directory):
        skip = False
        for versions_dir in ["previous", "versions"]:
            if root.startswith(os.path.join(site_config.web_directory, versions_dir)):
                skip = True
        if skip:
            continue

        for html_file in filter(lambda filename: filename.endswith(".html"), files):
            absolute_path = os.path.join(root, html_file)
            cleancontent, skipindex, title = clean(absolute_path)

            path = absolute_path[6:]

            if path.startswith("/mitigations/"):
                file_type = "mitigations"
            elif path.startswith("/matrices/"):
                file_type = "matrices"
            elif path.startswith("/groups/"):
                file_type = "groups"
            elif path.startswith("/campaigns/"):
                file_type = "campaigns"
            elif path.startswith("/datasources/"):
                file_type = "datasources"
            elif path.startswith("/software/"):
                file_type = "software"
            elif path.startswith("/tactics/"):
                file_type = "tactics"
            elif path.startswith("/techniques/"):
                file_type = "techniques"
            else:
                file_type = "misc"

            if not skipindex:
                index_data[file_type].append(
                    {
                        "id": global_id_counter,
                        "title": title,
                        "path": path,
                        "content": cleancontent,
                    }
                )
                global_id_counter += 1

    if not os.path.isdir(site_config.web_directory):
        os.makedirs(site_config.web_directory)

    searchable_pages = os.path.join(site_config.web_directory, "search")

    # create the subdirectory if it doesn't exist
    if not os.path.exists(searchable_pages):
        os.makedirs(searchable_pages)

    for file_type, data in index_data.items():
        json.dump(data, open(os.path.join(searchable_pages, f"{file_type}.json"), mode="w", encoding="utf8"), indent=0)

    if site_config.subdirectory:
        search_file_path = os.path.join(site_config.web_directory, "theme", "scripts", "search_bundle.js")

        if os.path.exists(search_file_path):
            search_contents = ""

            with open(search_file_path, mode="r", encoding="utf8") as search_file:
                search_contents = search_file.read()
                search_contents = re.sub(
                    'site_base_url ?= ? ""', f'site_base_url = "/{site_config.subdirectory}/"', search_contents
                )

            with open(search_file_path, mode="w", encoding="utf8") as search_file:
                search_file.write(search_contents)

    preserve_current_version()


skiplines = ["breadcrumb-item", "nav-link"]


def skipline(line):
    for skip in skiplines:
        if skip in line:
            return True
    return False


def clean_line(line):
    """Clean unicode spaces from line."""
    # Replace unicode spaces
    line = line.replace("\u00a0", " ")
    line = line.replace("\u202f", " ")
    line = line.replace("&nbsp;", " ")
    line = line.replace("&nbsp", " ")

    return line


def clean(filepath):
    """Clean the file of all HTML tags and unnecessary data."""
    with open(filepath, mode="r", encoding="utf8") as f:
        lines = f.readlines()

    content = ""
    count = 0
    title = ""
    skipindex = False
    indexing = False

    for line in lines:
        if (not skipline(line)) and indexing:
            content += clean_line(line) + "\n"
        if "<!--start-indexing-for-search-->" in line:
            indexing = True
        if "<!--stop-indexing-for-search-->" in line:
            indexing = False
        if "<title>" in line:
            # e.g [Credential Access - Enterprise | MITRE ATT&CK&trade;] becomes [Credential Access - Enterprise]
            match = re.search(r"<title>(.*)\|.*</title>", line)
            if match:
                title = match.group(1).strip()
        if 'http-equiv="refresh"' in line:
            skipindex = True
            break
        if '<h5 class="mb-0">Deprecation Warning</h5>' in line:
            skipindex = True
            break

    # content = ps.stem(content)
    out = bleach.clean(content, tags=[], strip=True)  # remove tags
    out = re.sub(r"[\n ]+", " ", out)  # remove extra newlines, smush to 1 line
    out = html.unescape(out)  # fix &amp and &#nnn unicode escaping
    skipindex = skipindex or out == "" or out == " "
    count = count + 1
    return out, skipindex, title


def preserve_current_version():
    """Preserve current version"""

    # Check for intermodule dependency
    if [key["module_name"] for key in modules.run_ptr if key["module_name"] == "versions"]:
        versions.versions.deploy_current_version()
