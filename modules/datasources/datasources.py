import json
import os
from collections.abc import Iterable

from modules import util
from modules.util import relationshipgetters as rsg

from .. import site_config
from . import datasources_config


def generate_datasources():
    """Responsible for verifying data source directory and starting off data source markdown generation."""
    # Create content pages directory if does not already exist
    util.buildhelpers.create_content_pages_dir()

    # Move templates to templates directory
    util.buildhelpers.move_templates(
        datasources_config.module_name_no_spaces, datasources_config.datasources_templates_path
    )

    # Create content pages directory if does not already exist
    util.buildhelpers.create_content_pages_dir()

    # Verify if directory exists
    if not os.path.isdir(datasources_config.datasource_markdown_path):
        os.mkdir(datasources_config.datasource_markdown_path)

    # Generates the markdown files to be used for page generation
    datasource_generated = generate_markdown_files()

    if not datasource_generated:
        util.buildhelpers.remove_module_from_menu(datasources_config.module_name_no_spaces)


def generate_markdown_files():
    """Responsible for generating datasource index page and getting shared data for all datasources."""
    has_datasource = False

    datasource_list = rsg.get_datasource_list()

    if datasource_list:
        has_datasource = True

    if has_datasource:
        side_menu_data = get_datasources_side_nav_data(datasource_list)
        data = {
            "datasources_table": get_datasources_table_data(datasource_list),
            "datasources_list_len": str(len(datasource_list)),
            "side_menu_data": side_menu_data,
        }
        subs = datasources_config.datasource_index_md + json.dumps(data)

        with open(
            os.path.join(datasources_config.datasource_markdown_path, "overview.md"), "w", encoding="utf8"
        ) as md_file:
            md_file.write(subs)

        # Create the markdown for the enterprise datasources in the STIX
        notes = rsg.get_objects_using_notes()
        for datasource in datasource_list:
            generate_datasource_md(datasource, side_menu_data, notes)

    return has_datasource


def generate_datasource_md(datasource, side_menu_data, notes):
    """Responsible for generating markdown of all datasources."""
    attack_id = util.buildhelpers.get_attack_id(datasource)

    if attack_id:
        data = {}
        data["attack_id"] = attack_id
        data["side_menu_data"] = side_menu_data
        data["notes"] = notes.get(datasource["id"])

        # Get initial reference list
        reference_list = {"current_number": 0}

        # Get initial reference list from group object
        reference_list = util.buildhelpers.update_reference_list(reference_list, datasource)

        dates = util.buildhelpers.get_created_and_modified_dates(datasource)

        if dates.get("created"):
            data["created"] = dates["created"]

        if dates.get("modified"):
            data["modified"] = dates["modified"]

        if datasource.get("name"):
            data["name"] = datasource["name"]

        if datasource.get("x_mitre_version"):
            data["version"] = datasource["x_mitre_version"]

        if isinstance(datasource.get("x_mitre_contributors"), Iterable):
            data["contributors_list"] = datasource["x_mitre_contributors"]

        if datasource.get("description"):
            data["descr"] = datasource["description"]

        if datasource.get("x_mitre_platforms"):
            datasource["x_mitre_platforms"].sort()
            data["platforms"] = ", ".join(datasource["x_mitre_platforms"])

        if datasource.get("x_mitre_collection_layers"):
            datasource["x_mitre_collection_layers"].sort()
            data["collection_layers"] = ", ".join(datasource["x_mitre_collection_layers"])

        data["citations"] = reference_list

        data["deprecated"] = datasource.get("x_mitre_deprecated", False)

        data["versioning_feature"] = site_config.check_versions_module()

        datasource_data_md = datasources_config.datasource_md.substitute(data)
        datasource_data_md = datasource_data_md + json.dumps(data)

        # Write out the markdown file
        with open(
            os.path.join(datasources_config.datasource_markdown_path, data["attack_id"] + ".md"), "w", encoding="utf8"
        ) as md_file:
            md_file.write(datasource_data_md)


def get_datasources_side_nav_data(datasources):
    """Responsible for generating the links that are located on the left side of individual data sources domain pages."""
    side_nav_data = []

    # Loop through data sources
    for datasource in datasources:
        attack_id = util.buildhelpers.get_attack_id(datasource)

        if attack_id:
            domains = datasource.get("x_mitre_domains", [])
            domain_names = [util.buildhelpers.get_domain_display_name(domain) for domain in domains]
            datasource_data = {
                "name": datasource["name"],
                "id": attack_id,
                "path": "/datasources/{}/".format(attack_id),
                "domains": domain_names,
                "children": [],
            }
            # add data source and children to the side navigation
            side_nav_data.append(datasource_data)

    side_nav_data = sorted(side_nav_data, key=lambda k: k["name"].lower())

    return {
        "name": "Data Sources",
        "id": "datasources",
        "path": None,  # root level doesn't get a path
        "children": side_nav_data,
    }


def get_datasources_table_data(datasource_list):
    """Responsible for generating datasource table data for the datasource index page."""
    datasources_table_data = []
    for datasource in datasource_list:
        attack_id = util.buildhelpers.get_attack_id(datasource)

        if attack_id:
            domains = datasource.get("x_mitre_domains", [])
            domain_names = [util.buildhelpers.get_domain_display_name(domain) for domain in domains]
            row = {
                "id": attack_id,
                "name": datasource.get("name"),
                "domains": domain_names,
                "descr": datasource.get("description", ""),
                "deprecated": datasource.get("x_mitre_deprecated", False),
            }
            datasources_table_data.append(row)

    # Sort by data source name
    datasources_table_data = sorted(datasources_table_data, key=lambda k: k["name"].lower())
    return datasources_table_data
