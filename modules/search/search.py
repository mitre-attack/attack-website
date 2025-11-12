import html
import json
import os
import re
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed

from loguru import logger

import modules
from modules import site_config, versions

types = ["software", "groups", "tactics", "techniques"]
sub_types = ["mobile", "enterprise", "ics"]
types_hash = set(types)
sub_types_hash = set(sub_types)
dist_words = 0

# Compile regex patterns for performance
HTML_TAG_PATTERN = re.compile(r"<[^>]+>")
WHITESPACE_PATTERN = re.compile(r"[\n ]+")
TITLE_PATTERN = re.compile(r"<title>(.*?)\|.*?</title>", re.DOTALL)
UNICODE_SPACE_PATTERN = re.compile(r"[\u00a0\u202f]|&nbsp;?")

# Path prefix to file type mapping for faster lookup
PATH_TYPE_MAP = {
    "/mitigations/": "mitigations",
    "/assets/": "assets",
    "/matrices/": "matrices",
    "/groups/": "groups",
    "/campaigns/": "campaigns",
    "/datacomponents/": "datacomponents",
    "/software/": "software",
    "/tactics/": "tactics",
    "/techniques/": "techniques",
    "/detectionstrategies/": "detectionstrategies",
    "/analytics/": "analytics",
}


def process_html_file(file_info):
    """Process a single HTML file and return index entry."""
    absolute_path, web_dir_len = file_info
    cleancontent, skipindex, title = clean(absolute_path)

    if skipindex:
        return None

    # Get relative path
    path = absolute_path[web_dir_len:]

    # Determine file type using path prefix map (faster than if/elif chain)
    file_type = "misc"
    for prefix, ftype in PATH_TYPE_MAP.items():
        if path.startswith(prefix):
            file_type = ftype
            break

    return {"title": title, "path": path, "content": cleancontent, "file_type": file_type}


def generate_index():
    logger.info("Creating searchable index for the site")
    index_data = defaultdict(list)

    # Collect all HTML files first
    html_files = []
    web_dir_len = len(site_config.web_directory) - 1  # -1 to keep leading slash in path

    for root, __, files in os.walk(site_config.web_directory):
        # Skip version directories
        skip = False
        for versions_dir in ["previous", "versions"]:
            if root.startswith(os.path.join(site_config.web_directory, versions_dir)):
                skip = True
                break
        if skip:
            continue

        for html_file in files:
            if html_file.endswith(".html"):
                absolute_path = os.path.join(root, html_file)
                html_files.append((absolute_path, web_dir_len))

    logger.info(f"Found {len(html_files)} HTML files to index")

    # Process files in parallel for better performance
    # Use ThreadPoolExecutor since this is I/O bound
    results = []
    max_workers = min(8, len(html_files)) if len(html_files) > 0 else 1

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_file = {executor.submit(process_html_file, file_info): file_info for file_info in html_files}

        for future in as_completed(future_to_file):
            result = future.result()
            if result:
                results.append(result)

    # Assign IDs and group by file type
    for idx, result in enumerate(results):
        file_type = result.pop("file_type")
        result["id"] = idx
        index_data[file_type].append(result)

    logger.info(f"Indexed {len(results)} pages across {len(index_data)} categories")

    # Create search directory
    if not os.path.isdir(site_config.web_directory):
        os.makedirs(site_config.web_directory)

    searchable_pages = os.path.join(site_config.web_directory, "search")
    if not os.path.exists(searchable_pages):
        os.makedirs(searchable_pages)

    # Write index files
    for file_type, data in index_data.items():
        output_path = os.path.join(searchable_pages, f"{file_type}.json")
        with open(output_path, mode="w", encoding="utf8") as f:
            json.dump(data, f, indent=0)

    # Update search bundle if using subdirectory
    if site_config.subdirectory:
        search_file_path = os.path.join(site_config.web_directory, "theme", "scripts", "search_bundle.js")

        if os.path.exists(search_file_path):
            with open(search_file_path, mode="r", encoding="utf8") as search_file:
                search_contents = search_file.read()

            search_contents = re.sub(
                'site_base_url ?= ? ""', f'site_base_url = "/{site_config.subdirectory}/"', search_contents
            )

            with open(search_file_path, mode="w", encoding="utf8") as search_file:
                search_file.write(search_contents)

    preserve_current_version()


skiplines = ["breadcrumb-item", "nav-link"]


def clean(filepath):
    """Clean the file of all HTML tags and unnecessary data. Optimized version."""
    try:
        # Read entire file at once (faster than line-by-line)
        with open(filepath, mode="r", encoding="utf8", errors="ignore") as f:
            file_content = f.read()
    except Exception as e:
        logger.warning(f"Error reading {filepath}: {e}")
        return "", True, ""

    # Quick checks for skip conditions
    if 'http-equiv="refresh"' in file_content or '<h5 class="mb-0">Deprecation Warning</h5>' in file_content:
        return "", True, ""

    # Extract title using compiled regex
    title = ""
    title_match = TITLE_PATTERN.search(file_content)
    if title_match:
        title = title_match.group(1).strip()

    # Extract indexable content between markers
    start_marker = "<!--start-indexing-for-search-->"
    stop_marker = "<!--stop-indexing-for-search-->"

    content_parts = []
    start_idx = 0

    while True:
        start_pos = file_content.find(start_marker, start_idx)
        if start_pos == -1:
            break

        stop_pos = file_content.find(stop_marker, start_pos)
        if stop_pos == -1:
            # If no stop marker, take till end
            stop_pos = len(file_content)

        # Extract content between markers
        section = file_content[start_pos + len(start_marker) : stop_pos]

        # Filter out lines with skip patterns
        section_lines = []
        for line in section.split("\n"):
            if not any(skip in line for skip in skiplines):
                section_lines.append(line)

        if section_lines:
            content_parts.append("\n".join(section_lines))

        start_idx = stop_pos + len(stop_marker)

    if not content_parts:
        return "", True, ""

    content = "\n".join(content_parts)

    # Clean unicode spaces using compiled regex (faster than multiple replace calls)
    content = UNICODE_SPACE_PATTERN.sub(" ", content)

    # Remove HTML tags using compiled regex (much faster than bleach for this use case)
    content = HTML_TAG_PATTERN.sub("", content)

    # Collapse whitespace using compiled regex
    content = WHITESPACE_PATTERN.sub(" ", content)

    # Unescape HTML entities
    content = html.unescape(content)

    # Trim
    content = content.strip()

    skipindex = not content

    return content, skipindex, title


def preserve_current_version():
    """Preserve current version."""
    # Check for intermodule dependency
    if [key["module_name"] for key in modules.run_ptr if key["module_name"] == "versions"]:
        versions.versions.deploy_current_version()
