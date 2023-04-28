from collections.abc import Iterable
import json
import os

from modules import util
from modules.util import relationshipgetters as rsg

from . import datasources_config
from .. import site_config


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
    datasource_list_no_deprecated_revoked = util.buildhelpers.filter_deprecated_revoked(datasource_list)

    if datasource_list_no_deprecated_revoked:
        has_datasource = True

    if has_datasource:
        data = {}

        # Amount of characters per category
        group_by = 2

        notes = rsg.get_objects_using_notes()
        side_menu_data = get_datasources_side_nav_data(datasource_list_no_deprecated_revoked)
        data["side_menu_data"] = side_menu_data

        side_menu_mobile_view_data = util.buildhelpers.get_side_menu_mobile_view_data(
            datasources_config.module_name, "/datasources/", datasource_list_no_deprecated_revoked, group_by
        )
        data["side_menu_mobile_view_data"] = side_menu_mobile_view_data

        data["datasources_table"] = get_datasources_table_data(datasource_list_no_deprecated_revoked)
        data["datasources_list_len"] = str(len(datasource_list_no_deprecated_revoked))

        subs = datasources_config.datasource_index_md + json.dumps(data)

        with open(
            os.path.join(datasources_config.datasource_markdown_path, "overview.md"), "w", encoding="utf8"
        ) as md_file:
            md_file.write(subs)

        # Create the markdown for the enterprise datasources in the STIX
        for datasource in datasource_list:
            generate_datasource_md(datasource, side_menu_data, side_menu_mobile_view_data, notes)

    return has_datasource


def generate_datasource_md(datasource, side_menu_data, side_menu_mobile_view_data, notes):
    """Responsible for generating markdown of all datasources."""
    attack_id = util.buildhelpers.get_attack_id(datasource)

    if attack_id:
        data = {}

        data["attack_id"] = attack_id

        data["side_menu_data"] = side_menu_data
        data["side_menu_mobile_view_data"] = side_menu_mobile_view_data
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

        # Get data components of data source and the technique relationships
        data["datacomponents_list"] = get_datacomponents_data(datasource, reference_list)

        data["citations"] = reference_list

        if datasource.get("x_mitre_deprecated"):
            data["deprecated"] = True

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

    # Get data components of data source
    datacomponent_of = rsg.get_datacomponent_of()
    technique_to_domain = rsg.get_technique_to_domain()
    techniques_detected_by_datacomponent = rsg.get_techniques_detected_by_datacomponent()

    def get_domains_of_datacomponent(datacomponent):
        """Retrives domains of given data component"""
        domains_of_datacomponent = []

        # get data components to techniques mapping to find domains
        techniques_of_datacomp = techniques_detected_by_datacomponent.get(datacomponent["id"])
        if techniques_of_datacomp:
            technique_list = {}
            for technique_rel in techniques_of_datacomp:
                attack_id = util.buildhelpers.get_attack_id(technique_rel["object"])
                if attack_id:
                    domain = technique_to_domain[attack_id].split("-")[0]
                    if not domain in domains_of_datacomponent:
                        domains_of_datacomponent.append(domain)

        return domains_of_datacomponent

    # Loop through data sources
    for datasource in datasources:
        attack_id = util.buildhelpers.get_attack_id(datasource)

        if attack_id:
            domains_of_datasource = []
            datasource_data = {
                "name": datasource["name"],
                "id": attack_id,
                "path": "/datasources/{}/".format(attack_id),
                "children": [],
            }

            if datacomponent_of.get(datasource["id"]):
                for datacomponent in datacomponent_of[datasource["id"]]:
                    if not datacomponent.get("x_mitre_deprecated") and not datacomponent.get("revoked"):
                        # get data component detections
                        techniques_of_datacomp = techniques_detected_by_datacomponent.get(datacomponent["id"])
                        if techniques_of_datacomp:
                            domains_of_datacomponent = get_domains_of_datacomponent(datacomponent)
                            # Add missing domains to data source
                            for domain in domains_of_datacomponent:
                                if not domain in domains_of_datasource:
                                    domains_of_datasource.append(domain)

                            datacomponent_data = {
                                "name": datacomponent["name"],
                                "id": datacomponent["name"],
                                "path": "/datasources/{}/#{}".format(attack_id, datacomponent["name"]),
                                "domains": domains_of_datacomponent,
                                "children": [],
                            }

                            # Add data component data to data source
                            datasource_data["children"].append(datacomponent_data)

                    # Sort subtechniques by ATT&CK ID
                    if datasource_data["children"]:
                        datasource_data["children"] = sorted(
                            datasource_data["children"], key=lambda k: k["name"].lower()
                        )

        datasource_data["domains"] = domains_of_datasource
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

    # Now the table on the right, which is made up of datasource data
    for datasource in datasource_list:
        attack_id = util.buildhelpers.get_attack_id(datasource)

        if attack_id:
            row = {}

            row["id"] = attack_id

            if datasource.get("name"):
                row["name"] = datasource["name"]

            if datasource.get("description"):
                row["descr"] = datasource["description"]

                if datasource.get("x_mitre_deprecated"):
                    row["deprecated"] = True

            datasources_table_data.append(row)

    # Sort by data source name
    datasources_table_data = sorted(datasources_table_data, key=lambda k: k["name"].lower())

    return datasources_table_data


def get_datacomponents_data(datasource, reference_list):
    """Given a data source and its reference list, get a list of data components of the data source.

    Add techniques detected by data components. Check the reference list for citations, if not found in list, add it.
    """
    datacomponents_data = []

    # Get data components of data source
    datacomponent_of = rsg.get_datacomponent_of()
    technique_to_domain = rsg.get_technique_to_domain()
    techniques_detected_by_datacomponent = rsg.get_techniques_detected_by_datacomponent()

    if datacomponent_of.get(datasource["id"]):
        for datacomponent in datacomponent_of[datasource["id"]]:
            if not datacomponent.get("x_mitre_deprecated") and not datacomponent.get("revoked"):
                # get data component detections
                techniques_of_datacomp = techniques_detected_by_datacomponent.get(datacomponent["id"])

                # skip if no detections
                if not techniques_of_datacomp:
                    continue

                reference = False
                datacomponent_data = {"name": datacomponent["name"], "descr": datacomponent["description"]}

                # update reference list
                reference_list = util.buildhelpers.update_reference_list(reference_list, datacomponent)

                # get data components to techniques mapping
                datacomponent_data["techniques"] = []
                domains_of_datacomponent = []
                technique_list = {}
                for technique_rel in techniques_of_datacomp:
                    # Do not add if technique is deprecated
                    if not technique_rel["object"].get("x_mitre_deprecated"):
                        technique_list = util.buildhelpers.technique_used_helper(
                            technique_list, technique_rel, reference_list
                        )

                        # Get domain of technique
                        attack_id = util.buildhelpers.get_attack_id(technique_rel["object"])
                        if attack_id:
                            domain = technique_to_domain[attack_id].split("-")[0]
                            if not domain in domains_of_datacomponent:
                                domains_of_datacomponent.append(domain)

                        technique_data = []
                        for item in technique_list:
                            if technique_list[item].get("descr"):
                                if reference == False:
                                    reference = True
                            technique_data.append(technique_list[item])

                        # Sort by technique name
                        technique_data = sorted(technique_data, key=lambda k: k["name"].lower())

                        datacomponent_data["techniques"] = technique_data
                        datacomponent_data["add_datacomponent_ref"] = reference

                datacomponent_data["domains"] = domains_of_datacomponent
                datacomponents_data.append(datacomponent_data)

    # Sort output by data component name
    datacomponents_data = sorted(datacomponents_data, key=lambda k: k["name"].lower())

    return datacomponents_data
