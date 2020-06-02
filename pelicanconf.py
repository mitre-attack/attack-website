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

# custom jinja filters
# remove index.html from end of a path, add / if not at beginning
def clean_path(path): 
    path = path.split("index.html")[0]
    if not path.startswith("/"): path = "/" + path
    if not path.endswith("/"): path += "/"
    return path
# get a flattened tree of the "paths" of all children of a tree of objects.
# used in sidenav
def flatten_tree(root):
    ret = []
    if root["path"]: ret.append(root["path"])
    for child in root["children"]:
        ret = ret + flatten_tree(child)
    return ret

# Clean stix data from unwanted characters
def clean_stix_data(data):
    return data.replace("\n", "")\
               .replace("{", "{{")\
               .replace("}", "}}")\
               .replace("”","\"")\
               .replace("“","\"")

# Template for HTML references inside of sentences
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

def get_citations(data):
    """Given a description, find all of the citations"""

    p = re.compile('\(Citation: (.*?)\)')
    return p.findall(data)

def get_string_to_replace(citations, citation_name):

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

    citation_template = "(Citation: {})"

    citation_names = get_citations(data)
    
    for citation_name in citation_names:
        replace_string = get_string_to_replace(citations, citation_name)

        if replace_string:
            data = data.replace(citation_template.format(citation_name), replace_string)
    
    return data

def remove_citations(data):

    # Get citations names to remove from string
    citation_names = get_citations(data)

    for citation_name in citation_names:
        data = data.replace("(Citation: " + citation_name + ")","")

    return data

def stixToHTML(data, citations, firstParagraphOnly):

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