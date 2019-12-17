import json
import os
from . import config
from datetime import datetime

def generate():
    """ Responsible for generating the changelog mardown page """
    generate_markdown_file()

def generate_markdown_file():
    """ Responsible for creating changelog markdown page """
    
    # Read local changelog
    with open("CHANGELOG.md", "r") as f:
        changelog = f.read()
    
    # Append changelog to mardown file
    changelog_md = config.changelog_md + changelog

    with open(os.path.join(config.changelog_markdown_path, "changelog.md"), "w", encoding='utf8') as md_file:
        md_file.write(changelog_md)
