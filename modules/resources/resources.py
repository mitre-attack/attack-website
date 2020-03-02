import json
import os
from . import resources_config
from . import archives
from modules import site_config
from modules import util
from datetime import datetime

def generate_resources():
    """Responsible for generating the resources pages"""

    # Verify if resources directory exists
    if not os.path.isdir(resources_config.resources_markdown_path):
        os.mkdir(resources_config.resources_markdown_path)

    # Verify if resources directory exists
    if not os.path.isdir(resources_config.updates_markdown_path):
        os.mkdir(resources_config.updates_markdown_path)

    generate_general_information()
    generate_training_pages()
    generate_attackcon_page()
    generate_faq_page()
    generate_previous_versions()
    generate_changelog_page()
    generate_static_pages()

def generate_general_information():
    """Responsible for compiling resources json into resources markdown files
       for rendering on the HMTL
    """
    # load papers and presentations list
    with open(os.path.join(site_config.data_directory, "resources.json"), "r", encoding='utf8') as f:
        resources = json.load(f)
    
    # get papers and presentations in sorted date order
    papers = sorted(resources["papers"], key=lambda p: datetime.strptime(p["date"], "%B %Y"), reverse=True)
    presentations = sorted(resources["presentations"], key=lambda p: datetime.strptime(p["date"], "%B %Y"), reverse=True)
    # get markdown
    resources_content = resources_config.general_information_md + json.dumps({
        "papers": papers,
        "presentations": presentations
    })
    # write markdown to file
    with open(os.path.join(resources_config.resources_markdown_path, "general_information.md"), "w", encoding='utf8') as md_file:
        md_file.write(resources_content)

def generate_training_pages():
    """ Responsible for generating the markdown pages of the training pages """

    data = {}
    
    # Side navigation for training
    data['menu'] = resources_config.training_navigation

    # Training Overview
    training_md = resources_config.training_md + json.dumps(data)

    # write markdown to file
    with open(os.path.join(resources_config.resources_markdown_path, "training.md"), "w", encoding='utf8') as md_file:
        md_file.write(training_md)

    # CTI training
    training_cti_md = resources_config.training_cti_md + json.dumps(data)

    # write markdown to file
    with open(os.path.join(resources_config.resources_markdown_path, "training_cti.md"), "w", encoding='utf8') as md_file:
        md_file.write(training_cti_md)

def generate_attackcon_page():
    """Responsible for compiling ATT&CKcon json into attackcon markdown file
       for rendering on the HTML
    """
    # load ATT&CKcon data
    with open(os.path.join(site_config.data_directory, "attackcon.json"), "r", encoding='utf8') as f:
        attackcon = json.load(f)

    attackcon = sorted(attackcon, key=lambda a: datetime.strptime(a["date"], "%B %Y"), reverse=True)

    attackcon_content = resources_config.attackcon_md + json.dumps(attackcon)
    # write markdown to file
    with open(os.path.join(resources_config.resources_markdown_path, "attackcon.md"), "w", encoding='utf8') as md_file:
        md_file.write(attackcon_content)

def generate_faq_page():
    """Responsible for compiling faq json into faq markdown file
       for rendering on the HMTL
    """
    # load faq data from json
    with open(os.path.join(site_config.data_directory, "faq.json"), "r", encoding='utf8') as f:
        faqdata = json.load(f)
    # add unique IDs
    for i,section in enumerate(faqdata["sections"]):
        for j,item in enumerate(section["questions"]):
            item["id"] = f"faq-{i}-{j}"
    
    # get markdown
    faq_content = resources_config.faq_md + json.dumps(faqdata)
    # write markdown to file
    with open(os.path.join(resources_config.resources_markdown_path, "faq.md"), "w", encoding='utf8') as md_file:
        md_file.write(faq_content)

def generate_previous_versions():
    archives.deploy()

def generate_changelog_page():
    """Responsible for compiling original changelog markdown into changelog markdown file
       for rendering on the HTML
    """
    
    # Read local changelog
    with open("CHANGELOG.md", "r", encoding='utf8') as f:
        changelog = f.read()
    
    # Append changelog to mardown file
    changelog_md = resources_config.changelog_md + changelog

    with open(os.path.join(resources_config.resources_markdown_path, "changelog.md"), "w", encoding='utf8') as md_file:
        md_file.write(changelog_md)

def generate_static_pages():
    """ Reads markdown files from the static pages directory and copies them into 
        the markdown directory
    """

    static_pages_dir = os.path.join('modules', resources_config.module_name, 'static_pages')

    for static_page in os.listdir(static_pages_dir):

        with open(os.path.join(static_pages_dir, static_page), "r", encoding='utf8') as md:
            content = md.read()

            if static_page.startswith("updates-"):
                with open(os.path.join(resources_config.updates_markdown_path, static_page), "w", encoding='utf8') as md_file:
                    md_file.write(content)
            else:
                with open(os.path.join(resources_config.resources_markdown_path, static_page), "w", encoding='utf8') as md_file:
                    md_file.write(content)