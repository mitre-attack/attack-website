#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

# Need to update path with current directory in order to
# read file with custom jinja filters 
import sys
sys.path.append('.')
import custom_jinja_filters

# import plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['assets']

AUTHOR = os.environ.get('PELICAN_AUTHOR', 'MITRE')
SITENAME = os.environ.get('PELICAN_SITENAME', 'ATT&CK')
SITEURL = os.environ.get('PELICAN_SITEURL', '')

PATH = 'content'

TIMEZONE = os.environ.get('PELICAN_TIMEZONE', 'America/New_York')

DEFAULT_LANG = os.environ.get('PELICAN_DEFAULT_LANG','en')

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
    'remove_whitespace': custom_jinja_filters.remove_whitespace,
    'escape_spaces': custom_jinja_filters.escape_spaces,
    'stixToHTML': custom_jinja_filters.stixToHTML,
    'permalink': custom_jinja_filters.permalink
}
