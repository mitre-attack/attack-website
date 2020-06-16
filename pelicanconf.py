#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import json
import uuid
import sys
import os

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

current_version_permalink = None
def permalink(link):
    """convert from a link to a permalink of that link, e.g /x/y => /versions/v6/x/y
       uses data/versions.json's current object to determine what the current version is for the permalink
    """

    global current_version_permalink
    # load the current version permalink
    if not current_version_permalink:
        with open(os.path.join("data", "versions.json"), "r") as f:
            current_version_permalink = "/versions/" + json.load(f)["current"]["name"].split(".")[0]
    # remove index.html from the end
    link = link.split("index.html")[0] if link.endswith("index.html") else link
    # strip index.html from path
    return current_version_permalink + "/" + link


JINJA_FILTERS = {
    'from_json':json.loads,
    'flatten_tree': flatten_tree,
    'clean_path': clean_path,
    'permalink': permalink
}