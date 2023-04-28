import json
import os
import shutil
from datetime import datetime
from pathlib import Path

from loguru import logger
from mitreattack.attackToExcel import attackToExcel

import modules
from modules import site_config, util

from . import resources_config


def generate_resources():
    """Responsible for generating the resources pages"""
    logger.info("Generating Resources")
    # Create content pages directory if does not already exist
    util.buildhelpers.create_content_pages_dir()

    # Verify if resources directory exists
    if not os.path.isdir(site_config.resources_markdown_path):
        os.mkdir(site_config.resources_markdown_path)

    # Verify if resources directory exists
    if not os.path.isdir(resources_config.updates_markdown_path):
        os.mkdir(resources_config.updates_markdown_path)

    # Move templates to templates directory
    util.buildhelpers.move_templates(resources_config.module_name, resources_config.resources_templates_path)
    copy_docs(module_docs_path=resources_config.docs_path)
    generate_working_with_attack()
    generate_general_information()
    generate_training_pages()
    generate_attackcon_page()
    check_menu_versions_module()
    generate_static_pages()


def copy_docs(module_docs_path):
    """Move module specific docs into the website's content directory for pelican."""
    logger.info("Copying files to docs directory")
    if os.path.isdir(module_docs_path):
        # Check that content directory exist
        if not os.path.exists(site_config.content_dir):
            os.mkdir(site_config.content_dir)
        # Check that docs directory exist
        if not os.path.exists(site_config.docs_dir):
            os.mkdir(site_config.docs_dir)

        for doc in os.listdir(module_docs_path):
            if os.path.isdir(os.path.join(module_docs_path, doc)):
                shutil.copytree(os.path.join(module_docs_path, doc), os.path.join(site_config.docs_dir, doc))
            else:
                shutil.copyfile(os.path.join(module_docs_path, doc), os.path.join(site_config.docs_dir, doc))


def generate_general_information():
    """Responsible for compiling resources json into resources markdown files for rendering on the HMTL."""
    logger.info("Generating general information")
    # load presentations list
    with open(os.path.join(site_config.data_directory, "resources.json"), "r", encoding="utf8") as f:
        resources = json.load(f)

    # get presentations in sorted date order
    presentations = sorted(
        resources["presentations"], key=lambda p: datetime.strptime(p["date"], "%B %Y"), reverse=True
    )
    # get markdown
    resources_content = resources_config.general_information_md + json.dumps({"presentations": presentations})
    # write markdown to file
    with open(
        os.path.join(site_config.resources_markdown_path, "general_information.md"), "w", encoding="utf8"
    ) as md_file:
        md_file.write(resources_content)


def generate_training_pages():
    """Responsible for generating the markdown pages of the training pages."""
    logger.info("Generating training pages")
    data = {}

    # Side navigation for training
    data["menu"] = resources_config.training_navigation

    # Training Overview
    training_md = resources_config.training_md + json.dumps(data)

    # write markdown to file
    with open(os.path.join(site_config.resources_markdown_path, "training.md"), "w", encoding="utf8") as md_file:
        md_file.write(training_md)

    # CTI training
    training_cti_md = resources_config.training_cti_md + json.dumps(data)

    # write markdown to file
    with open(os.path.join(site_config.resources_markdown_path, "training_cti.md"), "w", encoding="utf8") as md_file:
        md_file.write(training_cti_md)


def generate_attackcon_page():
    """Responsible for compiling ATT&CKcon json into attackcon markdown file for rendering on the HTML."""
    logger.info("Generating ATT&CKcon page")
    # load ATT&CKcon data
    with open(os.path.join(site_config.data_directory, "attackcon.json"), "r", encoding="utf8") as f:
        attackcon = json.load(f)

    attackcon = sorted(attackcon, key=lambda a: datetime.strptime(a["date"], "%B %Y"), reverse=True)

    attackcon_content = resources_config.attackcon_md + json.dumps(attackcon)
    # write markdown to file
    with open(os.path.join(site_config.resources_markdown_path, "attackcon.md"), "w", encoding="utf8") as md_file:
        md_file.write(attackcon_content)


def check_menu_versions_module():
    """Verify if versions module is in the running pool, if not remove from submenu."""
    if not [key["module_name"] for key in modules.run_ptr if key["module_name"] == "versions"]:
        util.buildhelpers.remove_element_from_sub_menu(resources_config.module_name, "Versions of ATT&CK")


def generate_static_pages():
    """Reads markdown files from the static pages directory and copies them into the markdown directory."""
    logger.info("Generating static pages")
    static_pages_dir = os.path.join("modules", "resources", "static_pages")

    for static_page in os.listdir(static_pages_dir):
        with open(os.path.join(static_pages_dir, static_page), "r", encoding="utf8") as md:
            content = md.read()

            if static_page.startswith("updates-"):
                with open(
                    os.path.join(resources_config.updates_markdown_path, static_page), "w", encoding="utf8"
                ) as md_file:
                    logger.debug(f"{md.name} >>> {md_file.name}")
                    md_file.write(content)
            else:
                with open(
                    os.path.join(site_config.resources_markdown_path, static_page), "w", encoding="utf8"
                ) as md_file:
                    logger.debug(f"{md.name} >>> {md_file.name}")
                    md_file.write(content)


def generate_working_with_attack():
    """Responsible for generating working with ATT&CK and creating excel files."""
    logger.info("Generating Working with ATT&CK page")
    excel_dirs = [
        f"enterprise-attack-{site_config.full_attack_version}",
        f"mobile-attack-{site_config.full_attack_version}",
        f"ics-attack-{site_config.full_attack_version}",
    ]
    files_types = [
        "matrices",
        "mitigations",
        "relationships",
        "software",
        "groups",
        "tactics",
        "techniques",
        "datasources",
        "campaigns",
    ]

    # Verify if directories exists
    if not os.path.isdir(site_config.web_directory):
        os.makedirs(site_config.web_directory)

    docs_dir = os.path.join(site_config.web_directory, "docs")
    if not os.path.isdir(docs_dir):
        os.makedirs(docs_dir)

    for domain in site_config.domains:
        if domain["deprecated"]:
            continue

        # TODO: refactor this to use a function rather than copy/paste from modules/util/stixhelpers.py
        # this can be used because it was called previously in modules/util/stixhelpers.py to download the file
        if domain["location"].startswith("http"):
            download_dir = Path(f"{site_config.web_directory}/stix")
            stix_filename = f"{download_dir}/{domain['name']}.json"
        else:
            stix_filename = domain["location"]

        attackToExcel.export(
            domain=domain["name"],
            version=site_config.full_attack_version,
            output_dir=docs_dir,
            stix_file=stix_filename,
        )

    files_json = {"excel_files": []}
    for excel_dir in excel_dirs:
        excel_json = {"label": f"{excel_dir}.xlsx", "url": f"/docs/{excel_dir}/{excel_dir}.xlsx", "children": []}
        for file_type in files_types:
            child_json = {
                "label": f"{excel_dir}-{file_type}.xlsx",
                "url": f"/docs/{excel_dir}/{excel_dir}-{file_type}.xlsx",
            }
            if os.path.exists(site_config.web_directory + child_json["url"]):
                excel_json["children"].append(child_json)
        files_json["excel_files"].append(excel_json)

    working_with_attack_content = resources_config.working_with_attack_md + json.dumps(files_json)
    # write markdown to file
    with open(
        os.path.join(site_config.resources_markdown_path, "working_with_attack.md"), "w", encoding="utf8"
    ) as md_file:
        md_file.write(working_with_attack_content)
