import json
import os
from . import config
from datetime import datetime

def generate():
    """Responsible for generating the resources pages"""
    generate_markdown_files()
    generate_changelog_page()

def generate_markdown_files():
    """Responsible for compiling resources json into resources markdown files
       for rendering on the HMTL
    """
    # load papers and presentations list
    with open(os.path.join(config.data_directory, "resources.json"), "r") as f:
        resources = json.load(f)
    
    # get papers and presentations in sorted date order
    papers = sorted(resources["papers"], key=lambda p: datetime.strptime(p["date"], "%B %Y"), reverse=True)
    presentations = sorted(resources["presentations"], key=lambda p: datetime.strptime(p["date"], "%B %Y"), reverse=True)
    # get markdown
    resources_content = config.resources_md + json.dumps({
        "papers": papers,
        "presentations": presentations
    })
    # write markdown to file
    with open(os.path.join(config.resources_markdown_path, "resources.md"), "w", encoding='utf8') as md_file:
        md_file.write(resources_content)

def generate_changelog_page():
    """Responsible for compiling original changelog markdown into changelog markdown file
       for rendering on the HTML
    """
    
    # Read local changelog
    with open("CHANGELOG.md", "r") as f:
        changelog = f.read()
    
    # Append changelog to mardown file
    changelog_md = config.changelog_md + changelog

    with open(os.path.join(config.changelog_markdown_path, "changelog.md"), "w", encoding='utf8') as md_file:
        md_file.write(changelog_md)