import json
import os

from modules import util
from loguru import logger

from .. import site_config
from . import datacomponents_config


def generate_datacomponents():
    """Responsible for verifying data component directory and starting off data component markdown generation."""
    # Create content pages directory if does not already exist
    util.buildhelpers.create_content_pages_dir()

    # Move templates to templates directory
    util.buildhelpers.move_templates(
        datacomponents_config.module_name_no_spaces, datacomponents_config.datacomponents_templates_path
    )

    # Create content pages directory if does not already exist
    util.buildhelpers.create_content_pages_dir()

    # Verify if directory exists
    if not os.path.isdir(datacomponents_config.datacomponent_markdown_path):
        os.mkdir(datacomponents_config.datacomponent_markdown_path)

    # Generates the markdown files to be used for page generation
    datacomponent_generated = generate_markdown_files()

    if not datacomponent_generated:
        util.buildhelpers.remove_module_from_menu(datacomponents_config.module_name_no_spaces)


def generate_markdown_files():
    """Responsible for generating datacomponent index page and getting shared data for all datacomponents."""
    has_datacomponents = False

    datacomponent_list = util.relationshipgetters.get_datacomponent_list()
    active_datacomponent_list = util.buildhelpers.filter_deprecated_revoked(datacomponent_list)

    # sidebar
    datacomponents = {}
    ms = util.relationshipgetters.get_ms()
    for domain in site_config.domains:
        if domain["deprecated"]:
            continue
        # Reads the STIX and creates a list of the ATT&CK data components filtered by domain
        datacomponents[domain["name"]] = util.stixhelpers.get_datacomponent_list_from_src(ms[domain["name"]])

    if active_datacomponent_list:
        has_datacomponents = True
    else:
        logger.debug("No detection strategies found")

    if has_datacomponents:
        notes = util.relationshipgetters.get_objects_using_notes()

        # generate sidebar
        sidebar_data = util.buildhelpers.get_side_nav_domains_data("data components", datacomponents, False)
        generate_sidebar_datacomponents(sidebar_data)

        data = {
            "total_count": str(len(active_datacomponent_list)),
            "datacomponent_table": get_datacomponent_table(active_datacomponent_list)
        }

        subs = datacomponents_config.datacomponent_index_md + json.dumps(data)
        with open(
            os.path.join(datacomponents_config.datacomponent_markdown_path, "overview.md"), "w", encoding="utf8"
        ) as md_file:
            md_file.write(subs)

        # Create the markdown for the enterprise datacomponents in the STIX
        for datacomponent in datacomponent_list:
            generate_datacomponent_md(datacomponent, notes)

    return has_datacomponents


def get_datacomponent_table(datacomponent_list):
    """Generate data component table for the overview page."""
    datacomponent_table = []

    for datacomponent in datacomponent_list:
        attack_id = util.buildhelpers.get_attack_id(datacomponent)
        if not attack_id:
            continue

        domains = datacomponent.get("x_mitre_domains", [])
        domain_names = [util.buildhelpers.get_domain_display_name(domain) for domain in domains]
        row = {
            "id": attack_id,
            "name": datacomponent.get("name"),
            "domains": domain_names,
            "description": datacomponent.get("description"),
            "deprecated": datacomponent.get("x_mitre_deprecated", False),
        }
        datacomponent_table.append(row)
    
    # sort by detection strategy name
    return sorted(datacomponent_table, key=lambda k: k["name"].lower())


def generate_sidebar_datacomponents(sidebar_data):
    """Responsible for generating the sidebar for the data component pages."""
    logger.info("Generating data components sidebar")
    data = { "menu": sidebar_data }

    # Sidebar Overview
    sidebar_md = datacomponents_config.sidebar_datacomponents_md + json.dumps(data)

    # write markdown to file
    with open(
        os.path.join(datacomponents_config.datacomponent_markdown_path, "sidebar_datacomponents.md"), "w", encoding="utf8"
    ) as md_file:
        md_file.write(sidebar_md)


def generate_datacomponent_md(datacomponent, notes):
    """Generate markdown for individual data components."""
    attack_id = util.buildhelpers.get_attack_id(datacomponent)
    if not attack_id:
        return
    
    dates = util.buildhelpers.get_created_and_modified_dates(datacomponent)

    # build reference list
    reference_list = { "current_number": 0 }
    reference_list = util.buildhelpers.update_reference_list(reference_list, datacomponent)

    domains = datacomponent.get("x_mitre_domains", [])
    domain_names = [util.buildhelpers.get_domain_display_name(domain) for domain in domains]
    data = {
        "attack_id": attack_id,
        "created": dates.get("created"),
        "modified": dates.get("modified"),
        "name": datacomponent.get("name"),
        "description": datacomponent.get("description"),
        "domains": domain_names,
        "version": datacomponent.get("x_mitre_version"),
        "deprecated": datacomponent.get("x_mitre_deprecated", False),
        "log_sources": sorted(
            datacomponent.get("x_mitre_log_sources", []),
            key=lambda x: x["name"].lower()
        ),
        "citations": reference_list,
        "notes": notes.get(datacomponent["id"])
    }

    subs = datacomponents_config.datacomponent_md.substitute(data)
    subs += json.dumps(data)

    # Write the markdown file
    with open(os.path.join(datacomponents_config.datacomponent_markdown_path, attack_id + ".md"), "w", encoding="utf8") as md_file:
        md_file.write(subs)