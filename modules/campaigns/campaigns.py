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

    # TODO resolve infinite redirect loop when run locally. Needs further testing before code removal.
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
        side_menu_data = util.buildhelpers.get_side_menu_data(
            "Campaigns", "/campaigns/", campaign_list_no_deprecated_revoked
        )
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

        campaign_date_citations = util.buildhelpers.get_first_last_seen_citations(campaign)
        if campaign_date_citations.get("first_seen_citation"):
            data["first_seen_citation"] = campaign_date_citations["first_seen_citation"]
        if campaign_date_citations.get("last_seen_citation"):
            data["last_seen_citation"] = campaign_date_citations["last_seen_citation"]

        if isinstance(campaign.get("x_mitre_contributors"), collections.abc.Iterable):
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
                    {
                        "attack_id": data["attack_id"],
                        "path": "campaigns/" + data["attack_id"],
                        "domain": layer["domain"],
                    }
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

        # Get group data for Group table
        data["group_data"] = get_group_table_data(campaign, reference_list)

        # Grab software data for Software table
        data["software_data"] = get_software_table_data(campaign, reference_list)

        if campaign.get("aliases"):
            data["alias_descriptions"] = util.buildhelpers.get_alias_data(campaign["aliases"][1:], ext_ref)

        data["citations"] = reference_list

        if isinstance(campaign.get("aliases"), collections.abc.Iterable):
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
            campaign_dates = util.buildhelpers.get_first_last_seen_dates(campaign)
            row = {
                "id": attack_id,
                "name": campaign["name"] if campaign.get("name") else attack_id,
                "first_seen": campaign_dates["first_seen"] if campaign_dates.get("first_seen") else "",
                "last_seen": campaign_dates["last_seen"] if campaign_dates.get("last_seen") else "",
            }

            if campaign.get("description"):
                row["descr"] = campaign["description"]

                if campaign.get("x_mitre_deprecated"):
                    row["deprecated"] = True

            if isinstance(campaign.get("aliases"), collections.abc.Iterable):
                row["aliases_list"] = campaign["aliases"][1:]

            campaigns_table_data.append(row)

    return campaigns_table_data


def get_group_table_data(campaign, reference_list):
    """Given a campaign, get the group table data."""
    group_list = {}  # group stix_id => {attack_id, name, description}
    groups_attributed_to_campaign = util.relationshipgetters.get_groups_attributed_to_campaigns()

    if groups_attributed_to_campaign.get(campaign.get("id")):
        for group in groups_attributed_to_campaign[campaign["id"]]:
            group_id = group["object"]["id"]
            if group_id not in group_list:
                attack_id = util.buildhelpers.get_attack_id(group["object"])
                group_list[group_id] = {"id": attack_id, "name": group["object"]["name"]}

                if group["relationship"].get("description"):
                    group_list[group_id]["desc"] = group["relationship"]["description"]

                    # update reference list
                    reference_list = util.buildhelpers.update_reference_list(reference_list, group["relationship"])

    group_data = [group_list[item] for item in group_list]
    group_data = sorted(group_data, key=lambda k: k["name"].lower())
    return group_data


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
    software_list = {}  # software stix_id => {attack_id, name, description}

    # Creating map for tools/malware used by campaigns
    software_used_by_campaign = [
        util.relationshipgetters.get_tools_used_by_campaigns(),
        util.relationshipgetters.get_malware_used_by_campaigns(),
    ]

    for res in software_used_by_campaign:
        if res.get(campaign.get("id")):
            for software in res[campaign["id"]]:
                software_id = software["object"]["id"]
                if software_id not in software_list:
                    attack_id = util.buildhelpers.get_attack_id(software["object"])
                    software_list[software_id] = {"id": attack_id, "name": software["object"]["name"]}
                    if software["relationship"].get("description"):
                        software_list[software_id]["desc"] = software["relationship"]["description"]

                        # update reference list
                        reference_list = util.buildhelpers.update_reference_list(
                            reference_list, software["relationship"]
                        )

    software_data = [software_list[item] for item in software_list]
    software_data = sorted(software_data, key=lambda k: k["name"].lower())
    return software_data
