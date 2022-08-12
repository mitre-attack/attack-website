import collections
import json
import os

from loguru import logger

from modules import util

from . import campaigns_config
from .. import site_config


def generate_campaigns():
    """
    Responsible for verifying campaign directory and starting off campaign markdown generation.
    """

    # Create content pages directory if does not already exist
    util.buildhelpers.create_content_pages_dir()

    # Move templates to templates directory
    util.buildhelpers.move_templates(campaigns_config.module_name, campaigns_config.campaigns_templates_path)

    # Verify if directory exists
    if not os.path.isdir(campaigns_config.campaign_markdown_path):
        os.mkdir(campaigns_config.campaign_markdown_path)

    # Generate redirections
    util.buildhelpers.generate_redirections(
        redirections_filename=campaigns_config.campaigns_redirection_location, redirect_md=site_config.redirect_md
    )

    # Generates the markdown files to be used for page generation
    campaigns_generated = generate_markdown_files()

    if not campaigns_generated:
        util.buildhelpers.remove_module_from_menu(campaigns_config.module_name)


def generate_markdown_files():
    """
    Responsible for generating campaign index page and getting shared data for all campaigns.
    """

    has_campaign = False

    campaign_list = util.relationshipgetters.get_campaign_list()

    campaign_list_no_deprecated_revoked = util.buildhelpers.filter_deprecated_revoked(campaign_list)

    if campaign_list_no_deprecated_revoked:
        has_campaign = True

    if has_campaign:
        data = {}

        # Amount of characters per category
        group_by = 2

        notes = util.relationshipgetters.get_objects_using_notes()
        side_menu_data = util.buildhelpers.get_side_menu_data("Campaigns", "/campaigns/", campaign_list_no_deprecated_revoked)
        data["side_menu_data"] = side_menu_data

        side_menu_mobile_view_data = util.buildhelpers.get_side_menu_mobile_view_data(
            "campaigns", "/campaigns/", campaign_list_no_deprecated_revoked, group_by
        )
        data["side_menu_mobile_view_data"] = side_menu_mobile_view_data

        data["campaigns_table"] = get_campaigns_table_data(campaign_list_no_deprecated_revoked)
        data["campaigns_list_len"] = str(len(campaign_list_no_deprecated_revoked))

        subs = campaigns_config.campaign_index_md + json.dumps(data)

        with open(
            os.path.join(campaigns_config.campaign_markdown_path, "overview.md"), "w", encoding="utf8"
        ) as md_file:
            md_file.write(subs)

        # Create the markdown for the enterprise campaigns in the STIX
        for campaign in campaign_list:
            generate_campaign_md(campaign, side_menu_data, side_menu_mobile_view_data, notes)

    return has_campaign


def generate_campaign_md(campaign, side_menu_data, side_menu_mobile_view_data, notes):
    """Responsible for generating markdown of all campaigns."""

    attack_id = util.buildhelpers.get_attack_id(campaign)

    if attack_id:
        data = {}

        data["attack_id"] = attack_id

        data["side_menu_data"] = side_menu_data
        data["side_menu_mobile_view_data"] = side_menu_mobile_view_data
        data["notes"] = notes.get(campaign["id"])

        # External references
        ext_ref = campaign["external_references"]

        dates = util.buildhelpers.get_created_and_modified_dates(campaign)
        if dates.get("created"):
            data["created"] = dates["created"]
        if dates.get("modified"):
            data["modified"] = dates["modified"]
        if campaign.get("name"):
            data["name"] = campaign["name"]
        if campaign.get("x_mitre_version"):
            data["version"] = campaign["x_mitre_version"]

        campaign_dates = util.buildhelpers.get_first_last_seen_dates(campaign)
        if campaign_dates.get("first_seen"):
            data["first_seen"] = campaign_dates["first_seen"]
        if campaign_dates.get("last_seen"):
            data["last_seen"] = campaign_dates["last_seen"]

        if isinstance(campaign.get("x_mitre_contributors"), collections.Iterable):
            data["contributors_list"] = campaign["x_mitre_contributors"]

        # Get initial reference list
        reference_list = {"current_number": 0}

        # Get initial reference list from campaign object
        reference_list = util.buildhelpers.update_reference_list(reference_list, campaign)

        if campaign.get("description"):
            data["descr"] = campaign["description"]

        if campaign.get("x_mitre_deprecated"):
            data["deprecated"] = True

        # Get technique data for techniques used table
        data["technique_table_data"] = get_techniques_used_by_campaign_data(campaign, reference_list)

        # Get navigator layers for this campaign
        layers = util.buildhelpers.get_navigator_layers(
            data["name"],
            data["attack_id"],
            "campaign",
            data["version"] if "version" in data else None,
            data["technique_table_data"],
        )

        data["layers"] = []
        for layer in layers:
            with open(
                os.path.join(
                    campaigns_config.campaign_markdown_path,
                    "-".join([data["attack_id"], "techniques", layer["domain"]]) + ".md",
                ),
                "w",
                encoding="utf8",
            ) as layer_json:
                subs = site_config.layer_md.substitute(
                    {"attack_id": data["attack_id"], "path": "campaigns/" + data["attack_id"], "domain": layer["domain"]}
                )
                subs = subs + layer["layer"]
                layer_json.write(subs)
            data["layers"].append(
                {
                    "domain": layer["domain"],
                    "filename": "-".join([data["attack_id"], layer["domain"], "layer"]) + ".json",
                    "navigator_link": site_config.navigator_link,
                }
            )

        # Grab software data for Software table
        data["software_data"], data["add_software_ref"] = get_software_table_data(campaign, reference_list)

        if campaign.get("aliases"):
            data["alias_descriptions"] = util.buildhelpers.get_alias_data(campaign["aliases"][1:], ext_ref)

        data["citations"] = reference_list

        if isinstance(campaign.get("aliases"), collections.Iterable):
            data["aliases_list"] = campaign["aliases"][1:]

        data["versioning_feature"] = site_config.check_versions_module()

        subs = campaigns_config.campaign_md.substitute(data)
        subs = subs + json.dumps(data)

        # Write out the markdown file
        with open(
            os.path.join(campaigns_config.campaign_markdown_path, data["attack_id"] + ".md"), "w", encoding="utf8"
        ) as md_file:
            md_file.write(subs)


def get_campaigns_table_data(campaign_list):
    """Responsible for generating campaign table data for the campaign index page"""

    campaigns_table_data = []

    # Now the table on the right, which is made up of campaign data
    for campaign in campaign_list:

        attack_id = util.buildhelpers.get_attack_id(campaign)

        if attack_id:
            row = {}

            row["id"] = attack_id

            if campaign.get("name"):
                row["name"] = campaign["name"]

            if campaign.get("description"):
                row["descr"] = campaign["description"]

                if campaign.get("x_mitre_deprecated"):
                    row["deprecated"] = True

            if isinstance(campaign.get("aliases"), collections.Iterable):
                row["aliases_list"] = campaign["aliases"][1:]

            campaigns_table_data.append(row)

    return campaigns_table_data


def get_techniques_used_by_campaign_data(campaign, reference_list):
    """Given a campaign and its reference list, get the techniques used by the campaign.
    
    Check the reference list for citations, if not found in list, add it.
    """
    technique_list = {}
    techniques_used_by_campaigns = util.relationshipgetters.get_techniques_used_by_campaigns()

    if techniques_used_by_campaigns.get(campaign.get("id")):
        for technique in techniques_used_by_campaigns[campaign["id"]]:
            # Do not add if technique is deprecated
            if not technique["object"].get("x_mitre_deprecated"):
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


def get_software_table_data(campaign, reference_list):
    """Given a campaign, get software table data."""
    software_list = {}
    reference = False

    # Creating map for tools/malware used by campaigns
    # and techniques used by malware/tools
    tools_and_malware = [
        {
            "software": util.relationshipgetters.get_tools_used_by_campaigns(),
            "techniques": util.relationshipgetters.get_techniques_used_by_tools(),
        },
        {
            "software": util.relationshipgetters.get_malware_used_by_campaigns(),
            "techniques": util.relationshipgetters.get_techniques_used_by_malware(),
        },
    ]

    # Get malware or tools used by campaign
    for pairing in tools_and_malware:
        if pairing["software"].get(campaign.get("id")):
            for software in pairing["software"][campaign["id"]]:
                software_id = software["object"]["id"]

                # Check if software not already in software_list dict
                if software_id not in software_list:
                    attack_id = util.buildhelpers.get_attack_id(software["object"])

                    if attack_id:
                        software_list[software_id] = {
                            "id": attack_id,
                            "name": software["object"]["name"]
                        }

                        if software["relationship"].get("description"):
                            if reference == False:
                                reference = True

                            # Get filtered description
                            software_list[software_id]["descr"] = software["relationship"]["description"]
                            # Update reference list
                            reference_list = util.buildhelpers.update_reference_list(
                                reference_list, software["relationship"]
                            )

                        # Check if techniques exists, add techniques used by software
                        if pairing["techniques"].get(software_id):
                            if "techniques" not in software_list[software_id]:
                                software_list[software_id]["techniques"] = []

                            for technique in pairing["techniques"][software_id]:
                                tech_data = {}
                                t_id = util.buildhelpers.get_attack_id(technique["object"])

                                if t_id:
                                    if util.buildhelpers.is_sub_tid(t_id):
                                        tech_data["parent_id"] = util.buildhelpers.get_parent_technique_id(t_id)
                                        tech_data["id"] = util.buildhelpers.get_sub_technique_id(t_id)
                                        tech_data["name"] = util.buildhelpers.get_technique_name(tech_data["parent_id"])
                                        tech_data["sub_name"] = technique["object"]["name"]
                                    else:
                                        tech_data["id"] = t_id
                                        tech_data["name"] = technique["object"]["name"]

                                    software_list[software_id]["techniques"].append(tech_data)

    # Moving it to an array because jinja does not like to loop through dictionaries
    data = []
    for item in software_list:
        if "techniques" in software_list[item]:
            software_list[item]["techniques"] = sorted(
                software_list[item]["techniques"], key=lambda k: k["name"].lower()
            )
        data.append(software_list[item])
    data = sorted(data, key=lambda k: k["name"].lower())

    return data, reference
