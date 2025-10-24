#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

# Need to update path with current directory in order to
# read file with custom jinja filters
import sys

sys.path.append(".")
import custom_jinja_filters

AUTHOR = os.environ.get("PELICAN_AUTHOR", "MITRE")
SITENAME = os.environ.get("PELICAN_SITENAME", "ATT&CK")
SITEURL = os.environ.get("PELICAN_SITEURL", "")

PATH = "content"

TIMEZONE = os.environ.get("PELICAN_TIMEZONE", "America/New_York")

DEFAULT_LANG = os.environ.get("PELICAN_DEFAULT_LANG", "en")

THEME = "attack-theme"
ARCHIVES_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
TAGS_SAVE_AS = ""

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False
STATIC_PATHS = ["docs"]
ARTICLE_PATHS = ["pages/updates"]

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

JINJA_FILTERS = {
    "from_json": custom_jinja_filters.json.loads,
    "flatten_tree": custom_jinja_filters.flatten_tree,
    "clean_path": custom_jinja_filters.clean_path,
    "remove_whitespace": custom_jinja_filters.remove_whitespace,
    "escape_spaces": custom_jinja_filters.escape_spaces,
    "stixToHTML": custom_jinja_filters.stixToHTML,
    "permalink": custom_jinja_filters.permalink,
}

MARKDOWN = {
    "extension_configs": {
        # defaults
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        # This is for enabling the TOC generation: https://python-markdown.github.io/extensions/toc/
        "markdown.extensions.toc": {"anchorlink": True},
        # Turns new lines into HTML breaks, like GitHub and StackOverflow: https://python-markdown.github.io/extensions/nl2br/
        "markdown.extensions.nl2br": {},
    },
    "output_format": "html5",
}
