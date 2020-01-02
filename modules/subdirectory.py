import collections
import json
import markdown
import os
import tqdm
import re
from . import config
from . import stixhelpers
from . import relationshiphelpers
from . import util

allowed_in_link = "".join(list(map(lambda s: s.strip(), [
    "   -   ", 
    "   ?   ",
    "   \w   ",
    "   \\   ",
    "   $   ",
    "   \.   ",
    "   !   ",
    "   \*   ",
    "   '   ",
    "   ()   ",
    "   /    ",
]))) 

def replace_links(filepath, subdirectory_name):
    """In the given file, replace the in-site links to reference 
       the correct previous version
    """

    # read file contents
    with open(filepath, mode="r", encoding='utf8') as html:
        html_str = html.read()

    # subdirectory link format
    dest_link_format = f"/{subdirectory_name}\g<1>"

    def substitute(prefix, html_str):
        from_str = f"{prefix}=[\"']([{allowed_in_link}]+)[\"']"
        to_str = f'{prefix}="{dest_link_format}"'
        return re.sub(from_str, to_str, html_str)

    html_str = substitute("src", html_str)
    html_str = substitute("href", html_str)
    html_str = substitute("content=\"0; url", html_str)

    with open(filepath, mode="w", encoding='utf8') as updated_html:
        updated_html.write(html_str)

def replace(subdirectory_name):
    """ Replace local hyperlinks with subdirectory """
    for directory, _, files in os.walk(config.web_directory):
        for filename in filter(lambda f: f.endswith(".html"), files):
            filepath = os.path.join(directory, filename)
            replace_links(filepath, subdirectory_name)