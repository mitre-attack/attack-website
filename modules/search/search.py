import html
import json
import os
import re
from collections import defaultdict

import bleach
from loguru import logger

import modules
from modules import site_config, versions
from modules.util import buildhelpers, relationshipgetters

types = ["software", "groups", "tactics", "techniques"]
sub_types = ["mobile", "enterprise", "ics"]
types_hash = set(types)
sub_types_hash = set(sub_types)
dist_words = 0
domains = ["enterprise", "mobile", "ics"]
domain_source_suffix = "-attack"
object_path_prefixes = {
    "campaign": "campaigns",
    "course-of-action": "mitigations",
    "intrusion-set": "groups",
    "malware": "software",
    "tool": "software",
    "x-mitre-analytic": "analytics",
    "x-mitre-asset": "assets",
    "x-mitre-data-component": "datacomponents",
    "x-mitre-detection-strategy": "detectionstrategies",
}


def generate_index():
    """Generate JSON search indexes from the built website output."""
    logger.info("Creating searchable index for the site")
    index_data = defaultdict(list)
    global_id_counter = 0
    domain_lookup = build_domain_lookup()

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

            if should_skip_search_path(path):
                continue

            file_type = get_page_type(path)

            if not skipindex:
                index_data[file_type].append(
                    {
                        "id": global_id_counter,
                        "title": title,
                        "path": path,
                        "content": cleancontent,
                        "pageType": file_type,
                        "domains": get_domains(title, path, domain_lookup),
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


def get_page_type(path):
    """Get the search page type for a generated site path."""
    if re.match(r"^/techniques/[^/]+/[^/]+/index\.html$", path):
        return "sub-techniques"
    if path.startswith("/mitigations/"):
        return "mitigations"
    if path.startswith("/assets/"):
        return "assets"
    if path.startswith("/matrices/"):
        return "matrices"
    if path.startswith("/groups/"):
        return "groups"
    if path.startswith("/campaigns/"):
        return "campaigns"
    if path.startswith("/datacomponents/"):
        return "datacomponents"
    if path.startswith("/software/"):
        return "software"
    if path.startswith("/tactics/"):
        return "tactics"
    if path.startswith("/techniques/"):
        return "techniques"
    if path.startswith("/detectionstrategies/"):
        return "detectionstrategies"
    if path.startswith("/analytics/"):
        return "analytics"
    if path.startswith("/resources/"):
        return "resources"
    return "misc"


def should_skip_search_path(path):
    """Return whether a generated path is a helper page that should not be searchable."""
    return bool(re.search(r"/sidebar-[^/]+/index\.html$", path))


def get_domains(title, path=None, domain_lookup=None):
    """Get ATT&CK domains for a search result, preferring source metadata before title inference."""
    if path and domain_lookup and path in domain_lookup:
        return sorted(domain_lookup[path], key=domains.index)

    page_domains = set()

    for domain in domains:
        if re.search(rf"(^| - ){domain}( - |$)", title, re.IGNORECASE):
            page_domains.add(domain)

    return sorted(page_domains, key=domains.index)


def build_domain_lookup():
    """Build generated-page path to domain mappings from STIX source bundle membership."""
    domain_lookup = defaultdict(set)

    try:
        memory_stores = relationshipgetters.get_ms()
    except Exception as exc:
        logger.debug(f"Unable to build source-domain lookup for search index: {exc}")
        return domain_lookup

    for domain_config in site_config.domains:
        domain = normalize_domain(domain_config["name"])
        if domain_config["deprecated"] or domain not in domains:
            continue

        memory_store = memory_stores.get(domain_config["name"])
        if not memory_store:
            continue

        for stix_object in memory_store.query():
            object_path = get_object_search_path(stix_object)
            if object_path:
                domain_lookup[object_path].add(domain)

            for explicit_domain in normalize_domains(stix_object.get("x_mitre_domains", [])):
                if object_path:
                    domain_lookup[object_path].add(explicit_domain)

    return domain_lookup


def get_object_search_path(stix_object):
    """Return generated search path for a STIX object when it maps to one searchable detail page."""
    attack_id = buildhelpers.get_attack_id(stix_object)
    if not attack_id:
        return None

    if stix_object.get("type") == "attack-pattern":
        if "." in attack_id:
            parent_id, sub_id = attack_id.split(".", 1)
            return f"/techniques/{parent_id}/{sub_id}/index.html"
        return f"/techniques/{attack_id}/index.html"

    path_prefix = object_path_prefixes.get(stix_object.get("type"))
    if not path_prefix:
        return None

    return f"/{path_prefix}/{attack_id}/index.html"


def normalize_domains(source_domains):
    """Normalize STIX domain names to search filter keys."""
    if isinstance(source_domains, str):
        source_domains = [source_domains]

    normalized_domains = []

    for source_domain in source_domains:
        domain = normalize_domain(source_domain)
        if domain in domains:
            normalized_domains.append(domain)

    return normalized_domains


def normalize_domain(source_domain):
    """Normalize domain source names such as enterprise-attack to enterprise."""
    return str(source_domain).removesuffix(domain_source_suffix).lower()


skiplines = ["breadcrumb-item", "nav-link"]


def skipline(line):
    """Return whether a line should be excluded from indexed search content."""
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
    """Preserve current version."""
    # Check for intermodule dependency
    if [key["module_name"] for key in modules.run_ptr if key["module_name"] == "versions"]:
        versions.versions.deploy_current_version()
