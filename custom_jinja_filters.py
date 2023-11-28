#!/usr/bin/env python
import json
import os
import re

import markdown

from modules import site_config

# Template for HTML references inside of STIX data
reference_marker_template = (
    "<span onclick=scrollToRef('scite-{}') "
    'id="scite-ref-{}-a" class="scite'
    '-citeref-number" '
    'title="{}"'
    'data-reference="{}"><sup><a href="{}" '
    'target="_blank" data-hasqtip="{}" '
    'aria-describedby="qtip-{}">[{}]</a></sup></span>'
)
reference_marker_template_no_url = (
    "<span onclick=scrollToRef('scite-{}') "
    'id="scite-ref-{}-a" '
    'class="scite-citeref-number" '
    'data-reference="{}"'
    'title="{}">'
    "<sup>[{}]</sup></span>"
)

# Pelican settings global variable
pelican_settings = {}

pelican_settings_f = os.path.join(site_config.data_directory, "pelican_settings.json")
with open(pelican_settings_f, "r", encoding="utf8") as json_f:
    pelican_settings = json.load(json_f)

# Custom Jinja Filters


def remove_whitespace(word):
    return "".join(word.split(" "))


def escape_spaces(word):
    return "%20".join(word.split(" "))


def clean_path(path):
    """Remove index.html from end of a path, add / if not at beginning."""
    path = path.split("index.html")[0]
    if not path.startswith("/"):
        path = "/" + path
    if not path.endswith("/"):
        path += "/"
    return path


def flatten_tree(root):
    """Get a flattened tree of the "paths" of all children of a tree of objects. used in sidenav."""
    ret = []
    if root["path"]:
        ret.append(root["path"])
    for child in root["children"]:
        ret = ret + flatten_tree(child)
    return ret


def clean_stix_data(data):
    """Clean stix data from unwanted characters."""
    return data.replace("\n", "").replace("”", '"').replace("“", '"')


def get_citations(data):
    """Given a description, find all of the citations."""
    p = re.compile("\(Citation: (.*?)\)")
    return p.findall(data)


def get_html_citation(citations, citation_name):
    """Given a citation name and the citation list, replace
    the html link with the citation name and update the
    list with the current number plus one
    """
    global reference_marker_template
    global reference_marker_template_no_url

    if "&amp;" in citation_name:
        citation_name = citation_name.replace("&amp;", "&")

    citation = citations.get(citation_name)

    reference_html = ""
    if citation:
        ref_number = None
        description = citation.get("description")
        
        if citation.get("number"):
            ref_number = citation["number"]
        else:
            ref_number = citations["current_number"] + 1
            citations["current_number"] = ref_number
            citation["number"] = ref_number

        if not citation.get("url"):
            reference_html = reference_marker_template_no_url.format(ref_number, ref_number, citation_name, description, ref_number)
        else:
            reference_html = reference_marker_template.format(
                ref_number, ref_number, description, citation_name, citation["url"], ref_number - 1, ref_number - 1, ref_number
            )

    return reference_html


def update_citations(data, citations):
    """Given a data string and the citation list, update citations with the citation names that are held in string."""
    citation_template = "(Citation: {})"

    citation_names = get_citations(data)

    for citation_name in citation_names:
        replace_string = get_html_citation(citations, citation_name)

        if replace_string:
            data = data.replace(citation_template.format(citation_name), replace_string)

    return data


def remove_citations(data):
    """Remove citations from strings."""
    # Get citations names to remove from string
    citation_names = get_citations(data)

    for citation_name in citation_names:
        data = data.replace("(Citation: " + citation_name + ")", "")

    return data


def filter_urls(data):
    """Filters out URLs to return path and not domain."""
    if not pelican_settings["no_stix_link_replacement"]:
        if "https://attack.mitre.org/groups/" in data:
            data = data.replace("https://attack.mitre.org/groups/", "/groups/")
        if "https://attack.mitre.org/software/" in data:
            data = data.replace("https://attack.mitre.org/software/", "/software/")
        if "https://attack.mitre.org/techniques/" in data:
            data = data.replace("https://attack.mitre.org/techniques/", "/techniques/")
        if "https://attack.mitre.org/technique/" in data:
            data = data.replace("https://attack.mitre.org/technique/", "/techniques/")
    return data


def stixToHTML(data, citations, firstParagraphOnly, convert):
    """Clean output of STIX content.

    params:
        data (required, string), the STIX description to format
        citations (optional, object), if not None, add citation markers to the data.
        firstParagraphOnly (optional, boolean), if true, only return the first paragraph of the data in question.
    """
    if (convert):
        # Replace data from markdown format
        data = markdown.markdown(data)

    # Replace url links
    data = filter_urls(data)

    # Get first paragraph from data
    if firstParagraphOnly:
        data = data.split("</p>")[0] + "</p>"
        if data.startswith("<p>") and data.endswith("</p>"):
            data = data[3:-4]

    if citations:
        # Update citations
        data = update_citations(data, citations)
    else:
        # Remove citations
        data = remove_citations(data)

    data = clean_stix_data(data)

    return data


current_version_permalink = None


def permalink(link):
    """Convert from a link to a permalink of that link, e.g /x/y => /versions/v6/x/y
    uses data/versions.json's current object to determine what the current version is for the permalink
    """
    global current_version_permalink
    # load the current version permalink
    if not current_version_permalink:
        with open(os.path.join("data", "versions.json"), "r", encoding="utf8") as f:
            currentVersion = json.load(f)["current"]
            current_version_permalink = (
                currentVersion["path"] if "path" in currentVersion else currentVersion["name"].split(".")[0]
            )
            current_version_permalink = "/versions/" + current_version_permalink
    # remove index.html from the end
    link = link.split("index.html")[0] if link.endswith("index.html") else link
    # strip index.html from path
    return current_version_permalink + "/" + link
