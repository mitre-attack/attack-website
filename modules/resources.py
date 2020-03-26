import json
import os
from . import config
from datetime import datetime

def generate():
    """Responsible for generating the resources pages"""
    generate_faq_page()
    generate_changelog_page()
    generate_resources_page()
    generate_attackcon_page()
    generate_training_pages()

def generate_resources_page():
    """Responsible for compiling resources json into resources markdown files
       for rendering on the HMTL
    """
    # load papers and presentations list
    with open(os.path.join(config.data_directory, "resources.json"), "r", encoding='utf8') as f:
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

def generate_faq_page():
    """Responsible for compiling faq json into faq markdown file
       for rendering on the HMTL
    """
    # load faq data from json
    with open(os.path.join(config.data_directory, "faq.json"), "r", encoding='utf8') as f:
        faqdata = json.load(f)
    # add unique IDs
    for i,section in enumerate(faqdata["sections"]):
        for j,item in enumerate(section["questions"]):
            item["id"] = f"faq-{i}-{j}"
    
    # get markdown
    faq_content = config.faq_md + json.dumps(faqdata)
    # write markdown to file
    with open(os.path.join(config.resources_markdown_path, "faq.md"), "w", encoding='utf8') as md_file:
        md_file.write(faq_content)

def generate_changelog_page():
    """Responsible for compiling original changelog markdown into changelog markdown file
       for rendering on the HTML
    """
    
    # Read local changelog
    with open("CHANGELOG.md", "r", encoding='utf8') as f:
        changelog = f.read()
    
    # Append changelog to mardown file
    changelog_md = config.changelog_md + changelog

    with open(os.path.join(config.resources_markdown_path, "changelog.md"), "w", encoding='utf8') as md_file:
        md_file.write(changelog_md)

def generate_attackcon_page():
    """Responsible for compiling ATT&CKcon json into attackcon markdown file
       for rendering on the HTML
    """
    # load ATT&CKcon data
    with open(os.path.join(config.data_directory, "attackcon.json"), "r", encoding='utf8') as f:
        attackcon = json.load(f)

    attackcon = sorted(attackcon, key=lambda a: datetime.strptime(a["date"], "%B %Y"), reverse=True)

    attackcon_content = config.attackcon_md + json.dumps(attackcon)
    # write markdown to file
    with open(os.path.join(config.resources_markdown_path, "attackcon.md"), "w", encoding='utf8') as md_file:
        md_file.write(attackcon_content)
    
def generate_training_pages():
    """ Responsible for generating the markdown pages of the training pages """

    data = {}
    
    # Side navigation for training
    data['menu'] = config.training_navigation

    # Training Overview
    training_md = config.training_md + json.dumps(data)

    # write markdown to file
    with open(os.path.join(config.resources_markdown_path, "training.md"), "w", encoding='utf8') as md_file:
        md_file.write(training_md)

    # CTI training
    training_cti_md = config.training_cti_md + json.dumps(data)

    # write markdown to file
    with open(os.path.join(config.resources_markdown_path, "training_cti.md"), "w", encoding='utf8') as md_file:
        md_file.write(training_cti_md)


