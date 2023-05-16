from collections.abc import Iterable
import json
import os

from loguru import logger

from modules import util

from . import software_config
from .. import site_config


def generate_software():
    """Responsible for verifying software directory and generating software index markdown."""
    # Create content pages directory if does not already exist
    util.buildhelpers.create_content_pages_dir()

    # Move templates to templates directory
    util.buildhelpers.move_templates(software_config.module_name, software_config.software_templates_path)

    # Verify if directory exists
    if not os.path.isdir(software_config.software_markdown_path):
        os.mkdir(software_config.software_markdown_path)

    # TODO resolve infinite redirect loop when run locally. Needs further testing before code removal.
    # Generate redirections
    util.buildhelpers.generate_redirections(
        redirections_filename=software_config.software_redirection_location, redirect_md=site_config.redirect_md
    )

    # Generates the markdown files to be used for page generation and verifies if a software was generated
    software_generated = generate_markdown_files()

    if not software_generated:
        util.buildhelpers.remove_module_from_menu(software_config.module_name)


def generate_markdown_files():
    """Responsible for generating the shared data for all software and kicking off markdown generation."""
    data = {}

    has_software = False

    # Amount of characters per category
    group_by = 2

    software_list = util.relationshipgetters.get_software_list()

    software_list_no_deprecated_revoked = util.buildhelpers.filter_deprecated_revoked(software_list)

    if software_list_no_deprecated_revoked:
        has_software = True

    if has_software:
        data["software_list_len"] = str(len(software_list_no_deprecated_revoked))

        notes = util.relationshipgetters.get_objects_using_notes()

        side_menu_data = util.buildhelpers.get_side_menu_data(
            "software", "/software/", software_list_no_deprecated_revoked
        )
        data["side_menu_data"] = side_menu_data

        side_menu_mobile_view_data = util.buildhelpers.get_side_menu_mobile_view_data(
            "software", "/software/", software_list_no_deprecated_revoked, group_by
        )
        data["side_menu_mobile_view_data"] = side_menu_mobile_view_data

        data["software_table"] = get_software_table_data(software_list_no_deprecated_revoked)

        subs = software_config.software_index_md + json.dumps(data)

        with open(os.path.join(software_config.software_markdown_path, "overview.md"), "w", encoding="utf8") as md_file:
            md_file.write(subs)

        # Create the markdown for the enterprise groups in the stix
        for software in software_list:
            generate_software_md(software, side_menu_data, side_menu_mobile_view_data, notes)

    return has_software


def generate_software_md(software, side_menu_data, side_menu_mobile_view_data, notes):
    """Responsible for generating given software markdown"""
    attack_id = util.buildhelpers.get_attack_id(software)

    # If software has id generate software data
    if attack_id:
        data = {}

        data["attack_id"] = attack_id

        data["side_menu_data"] = side_menu_data
        data["side_menu_mobile_view_data"] = side_menu_mobile_view_data
        data["notes"] = notes.get(software["id"])

        dates = util.buildhelpers.get_created_and_modified_dates(software)

        if dates.get("created"):
            data["created"] = dates["created"]

        if dates.get("modified"):
            data["modified"] = dates["modified"]

        # Get name
        if software.get("name"):
            data["name"] = software["name"]

        # Get type
        if software.get("type"):
            data["type"] = software["type"].upper()

        # Get version
        if software.get("x_mitre_version"):
            data["version"] = software["x_mitre_version"]

        ext_ref = software["external_references"]

        # Get initial reference list
        reference_list = {"current_number": 0}

        # Get initial reference list from software object
        reference_list = util.buildhelpers.update_reference_list(reference_list, software)

        # Get description
        if software.get("description"):
            data["descr"] = software["description"]

            if software.get("x_mitre_deprecated"):
                data["deprecated"] = True

        # Get techniques used by software
        data["technique_table_data"] = get_techniques_used_by_software_data(software, reference_list)

        # Get campaigns that use this software
        data["campaign_data"] = get_campaign_table_data(software, reference_list)

        # Get navigator layers for this group
        layers = util.buildhelpers.get_navigator_layers(
            data["name"],
            data["attack_id"],
            "software",
            data["version"] if "version" in data else None,
            data["technique_table_data"],
        )

        data["layers"] = []
        for layer in layers:
            with open(
                os.path.join(
                    software_config.software_markdown_path,
                    "-".join([data["attack_id"], "techniques", layer["domain"]]) + ".md",
                ),
                "w",
                encoding="utf8",
            ) as layer_json:
                subs = site_config.layer_md.substitute(
                    {"attack_id": data["attack_id"], "path": "software/" + data["attack_id"], "domain": layer["domain"]}
                )
                subs = subs + layer["layer"]
                layer_json.write(subs)
            data["layers"].append(
                {
                    "domain": layer["domain"],
                    "name": layer["name"],
                    "filename": layer["filename"],
                    "navigator_link": site_config.navigator_link,
                }
            )

        # Get aliases descriptions
        if software.get("x_mitre_aliases"):
            data["alias_descriptions"] = util.buildhelpers.get_alias_data(software["x_mitre_aliases"][1:], ext_ref)

        # Get group data of groups that use software
        data["groups"] = get_groups_using_software(software, reference_list)

        # Get aliases list
        if isinstance(software.get("x_mitre_aliases"), Iterable):
            data["aliases_list"] = software["x_mitre_aliases"][1:]

        # Get contributors
        if isinstance(software.get("x_mitre_contributors"), Iterable):
            data["contributors_list"] = software["x_mitre_contributors"]

        # Get platform list
        if isinstance(software.get("x_mitre_platforms"), Iterable):
            data["platform_list"] = software["x_mitre_platforms"]

        data["citations"] = reference_list
        data["versioning_feature"] = site_config.check_versions_module()

        subs = software_config.software_md.substitute(data)
        subs = subs + json.dumps(data)

        # Write out the markdown file
        with open(
            os.path.join(software_config.software_markdown_path, data["attack_id"] + ".md"), "w", encoding="utf8"
        ) as md_file:
            md_file.write(subs)


def get_software_table_data(software_list):
    """Responsible for generating software table data for the software index page."""
    software_table_data = []

    for software in software_list:
        if software.get("name"):
            row = {}

            row["name"] = software["name"]

            if software.get("description"):
                row["descr"] = software["description"]
                if software.get("x_mitre_deprecated"):
                    row["deprecated"] = True

            attack_id = util.buildhelpers.get_attack_id(software)

            if attack_id:
                row["id"] = attack_id

            if isinstance(software.get("x_mitre_aliases"), Iterable):
                row["aliases_list"] = software["x_mitre_aliases"][1:]

            software_table_data.append(row)

    return software_table_data


def get_groups_using_software(software, reference_list):
    """Given a software object, return group list with id and name of groups."""
    if software.get("type").lower() == "malware":
        groups_using_software = util.relationshipgetters.get_groups_using_malware().get(software["id"])
        groups_attributed_to_campaigns = {
            "campaigns": util.relationshipgetters.get_campaigns_using_malware(),
            "groups": util.relationshipgetters.get_groups_attributed_to_campaigns(),
        }
    else:
        groups_using_software = util.relationshipgetters.get_groups_using_tool().get(software["id"])
        groups_attributed_to_campaigns = {
            "campaigns": util.relationshipgetters.get_campaigns_using_tool(),
            "groups": util.relationshipgetters.get_groups_attributed_to_campaigns(),
        }

    groups = []
    seen_attack_ids = {}

    if groups_using_software:
        # Get name, id of group
        for group in groups_using_software:
            attack_id = util.buildhelpers.get_attack_id(group["object"])

            if attack_id:
                if attack_id in seen_attack_ids:
                    software_attack_id = util.buildhelpers.get_attack_id(software)
                    logger.debug(
                        f"Skipping extra use of [{attack_id}] {group['object']['name']} for {software_attack_id}"
                    )
                    continue

                row = {"id": attack_id, "name": group["object"]["name"]}

                if group["relationship"].get("description"):
                    # Get filtered description
                    row["descr"] = group["relationship"]["description"]
                    reference_list = util.buildhelpers.update_reference_list(reference_list, group["relationship"])

                seen_attack_ids[attack_id] = True
                groups.append(row)

    if groups_attributed_to_campaigns["campaigns"].get(software.get("id")):
        # campaigns related to this software
        for campaign in groups_attributed_to_campaigns["campaigns"][software["id"]]:
            campaign_id = campaign["object"]["id"]

            if groups_attributed_to_campaigns["groups"].get(campaign_id):
                # groups related to this campaign
                for group in groups_attributed_to_campaigns["groups"][campaign_id]:
                    attack_id = util.buildhelpers.get_attack_id(group["object"])

                    descr = None
                    if group["relationship"].get("description"):
                        descr = group["relationship"]["description"]
                        reference_list = util.buildhelpers.update_reference_list(reference_list, group["relationship"])

                    if attack_id in seen_attack_ids:
                        # group already in table, concatenate descriptions
                        r = next(row for row in groups if row["id"] == attack_id)

                        if r["descr"] and descr:  # concatenate descriptions
                            # get unique set of references
                            r["descr"] = util.buildhelpers.get_reference_set([r["descr"], descr])
                        elif descr:
                            r["descr"] = descr
                    else:  # new group seen, add row
                        row = {"id": attack_id, "name": group["object"]["name"]}

                        if descr:
                            row["descr"] = descr

                        seen_attack_ids[attack_id] = True
                        groups.append(row)

    return groups


def get_techniques_used_by_software_data(software, reference_list):
    """Given a software and its reference list, get the techniques used by the
    software. Check the reference list for citations, if not found
    in list, add it.
    """
    if software.get("type").lower() == "malware":
        techniques_used_by_software = util.relationshipgetters.get_techniques_used_by_malware().get(software["id"])
    else:
        techniques_used_by_software = util.relationshipgetters.get_techniques_used_by_tools().get(software["id"])

    technique_list = {}
    if techniques_used_by_software:
        for technique in techniques_used_by_software:
            # Do not add if technique is deprecated
            if technique["object"].get("x_mitre_deprecated"):
                continue

            technique_list = util.buildhelpers.technique_used_helper(technique_list, technique, reference_list)

    technique_data = []
    for item in technique_list:
        technique_data.append(technique_list[item])
    # Sort by technique name
    technique_data = sorted(technique_data, key=lambda k: k["name"].lower())

    # Sort by domain name
    technique_data = sorted(
        technique_data, key=lambda k: [site_config.custom_alphabet.index(c) for c in k["domain"].lower()]
    )
    return technique_data


def get_campaign_table_data(software, reference_list):
    """Given a software, get the campaign table data."""
    if software.get("type").lower() == "malware":
        campaigns_using_software = util.relationshipgetters.get_campaigns_using_malware().get(software["id"])
    else:
        campaigns_using_software = util.relationshipgetters.get_campaigns_using_tool().get(software["id"])

    campaign_list = {}  # campaign stix id => {attack id, name, description}
    if campaigns_using_software:
        for campaign in campaigns_using_software:
            campaign_id = campaign["object"]["id"]
            if campaign_id not in campaign_list:
                attack_id = util.buildhelpers.get_attack_id(campaign["object"])
                campaign_list[campaign_id] = {"id": attack_id, "name": campaign["object"]["name"]}

                if campaign["relationship"].get("description"):
                    campaign_list[campaign_id]["desc"] = campaign["relationship"]["description"]

                    # update reference list
                    reference_list = util.buildhelpers.update_reference_list(reference_list, campaign["relationship"])

    campaign_data = [campaign_list[item] for item in campaign_list]
    campaign_data = sorted(campaign_data, key=lambda k: k["name"].lower())
    return campaign_data
