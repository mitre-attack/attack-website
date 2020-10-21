#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Need to update path with current directory in order to
# read file with custom jinja filters 
import sys
sys.path.append('.')
import custom_jinja_filters

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

JINJA_FILTERS = {
    'from_json': custom_jinja_filters.json.loads,
    'flatten_tree': custom_jinja_filters.flatten_tree,
    'clean_path': custom_jinja_filters.clean_path,
    'stixToHTML': custom_jinja_filters.stixToHTML,
    'permalink': custom_jinja_filters.permalink
}