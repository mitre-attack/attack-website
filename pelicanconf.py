#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import json
import markdown
import uuid
import sys
import re

# import plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['assets']

AUTHOR = 'MITRE'
SITENAME = 'ATT&CK'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

THEME = 'attack-theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False
STATIC_PATHS = ['docs']
ARTICLE_PATHS = ['pages/updates']

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

# Custom Jinja Filters

# Template for HTML references inside of STIX data
reference_marker_template = ("<span onclick=scrollToRef('scite-{}') "
                             "id=\"scite-ref-{}-a\" class=\"scite"
                            "-citeref-number\" "
                             "data-reference=\"{}\"><sup><a href=\"{}\" "
                             "target=\"_blank\" data-hasqtip=\"{}\" "
                             "aria-describedby=\"qtip-{}\">[{}]</a></sup></span>")
reference_marker_template_no_url = ("<span onclick=scrollToRef('scite-{}') "
                                    "id=\"scite-ref-{}-a\" "
                                    "class=\"scite-citeref-number\" "
                                    "data-reference=\"{}\">"
                                    "<sup>[{}]</sup></span>")

def clean_path(path):
    """ remove index.html from end of a path, add / if not at beginning """

    path = path.split("index.html")[0]
    if not path.startswith("/"): path = "/" + path
    if not path.endswith("/"): path += "/"
    return path

def flatten_tree(root):
    """ get a flattened tree of the "paths" of all children of a tree of objects.
        used in sidenav
    """
    ret = []
    if root["path"]: ret.append(root["path"])
    for child in root["children"]:
        ret = ret + flatten_tree(child)
    return ret

def clean_stix_data(data):
    """ Clean stix data from unwanted characters """

    return data.replace("\n", "")\
               .replace("{", "{{")\
               .replace("}", "}}")\
               .replace("”","\"")\
               .replace("“","\"")

def get_citations(data):
    """ Given a description, find all of the citations """

    p = re.compile('\(Citation: (.*?)\)')
    return p.findall(data)

def get_html_citation(citations, citation_name):
    """ Given a citation name and the citation list, replace
        the html link with the citation name and update the 
        list with the current number plus one
    """

    global reference_marker_template
    global reference_marker_template_no_url

    citation = citations.get(citation_name)

    reference_html = ""
    if citation:
        ref_number = None

        if citation.get('number'):
            ref_number = citation['number']
        else:
            ref_number = citations['current_number'] + 1
            citations['current_number'] = ref_number
            citation['number'] = ref_number

        if not citation.get('url'):
            reference_html = reference_marker_template_no_url.format(ref_number,ref_number,citation_name,ref_number)
        else:
            reference_html = reference_marker_template.format(ref_number,ref_number,citation_name,citation['url'],ref_number - 1, ref_number - 1, ref_number)
        
    return reference_html

def update_citations(data, citations):
    """ Given a data string and the citation list, update
        citations with the citation names that are held in string
    """

    citation_template = "(Citation: {})"

    citation_names = get_citations(data)
    
    for citation_name in citation_names:
        replace_string = get_html_citation(citations, citation_name)

        if replace_string:
            data = data.replace(citation_template.format(citation_name), replace_string)
    
    return data

def remove_citations(data):
    """ Remove citations from strings """

    # Get citations names to remove from string
    citation_names = get_citations(data)

    for citation_name in citation_names:
        data = data.replace("(Citation: " + citation_name + ")","")

    return data

def stixToHTML(data, citations, firstParagraphOnly):
    """ Clean output of STIX content.
        params:
            data (required, string), the STIX description to format
            citations (optional, object), if not None, add citation markers to the data.
            firstParagraphOnly (optional, boolean), if true, only return the first paragraph of the data in question.
    """

    # Replace data from markdown format
    data = markdown.markdown(data)

    # Get first paragraph from data
    if firstParagraphOnly:
        data = data.split('</p>')[0] + '</p>'
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

JINJA_FILTERS = {
    'from_json':json.loads,
    'flatten_tree': flatten_tree,
    'clean_path': clean_path,
    'stixToHTML': stixToHTML
}