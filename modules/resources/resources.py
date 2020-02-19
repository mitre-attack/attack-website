import json
import os
from . import resources_config
from . import archives
from modules import site_config
from datetime import datetime

def generate_resources():
    """Responsible for generating the resources pages"""
    generate_general_information()
    generate_getting_started()
    generate_training_pages()
    generate_attackcon_page()
    generate_working_with_attack()
    generate_faq_page()
    generate_updates()
    generate_previous_versions()
    generate_related_projects()
    generate_changelog_page()

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

def generate_getting_started():
    """ Generates getting started markdown file """

    # write markdown to file
    with open(os.path.join(resources_config.resources_markdown_path, "getting_started.md"), "w", encoding='utf8') as md_file:
        md_file.write(resources_config.getting_started_md)

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

def generate_working_with_attack():
    """ Generates working with ATT&CK markdown file """

    # load working with ATT&CK data
    with open(os.path.join(site_config.data_directory, "working-with-attack.json"), "r", encoding='utf8') as f:
        working_with_attack = json.load(f)

    working_with_attack_content = resources_config.working_with_attack_md + working_with_attack['working-with-attack']

    # write markdown to file
    with open(os.path.join(resources_config.resources_markdown_path, "working_with_attack.md"), "w", encoding='utf8') as md_file:
        md_file.write(working_with_attack_content)    

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

def generate_updates():
    """ Generates updates markdown file """

    # write markdown to file
    with open(os.path.join(resources_config.resources_markdown_path, "updates.md"), "w", encoding='utf8') as md_file:
        md_file.write(resources_config.updates_md) 

def generate_previous_versions():
    archives.deploy()

def generate_related_projects():
    """ Generates related projects markdown file """

    # write markdown to file
    with open(os.path.join(resources_config.resources_markdown_path, "related_projects.md"), "w", encoding='utf8') as md_file:
        md_file.write(resources_config.related_projects_md)  

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


