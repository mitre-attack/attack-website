import json
import os
from . import config
from datetime import datetime

def generate():
    """Responsible for generating the resources pages"""
    generate_markdown_files()
    generate_training_pages()

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

def generate_training_pages():
    """ Responsible for generating the markdown pages of the training pages """

