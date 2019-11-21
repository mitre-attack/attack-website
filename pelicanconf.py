#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import json
import uuid

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
    currNode = root
    for child in root["children"]:
        ret = ret + flatten_tree(child)
    return ret

JINJA_FILTERS = {
    'from_json':json.loads,
    'flatten_tree': flatten_tree,
    'clean_path': clean_path
}