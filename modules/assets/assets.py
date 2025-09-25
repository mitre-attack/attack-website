import collections
import json
import os

from modules import util

from .. import site_config
from . import assets_config


def generate_assets():
    """Responsible for verifying asset directory and starting off asset markdown generation."""
    # Create content pages directory if does not already exist
    util.buildhelpers.create_content_pages_dir()

    # Move templates to templates directory
    util.buildhelpers.move_templates(assets_config.module_name, assets_config.assets_templates_path)

    # Verify if directory exists
    if not os.path.isdir(assets_config.asset_markdown_path):
        os.mkdir(assets_config.asset_markdown_path)

    # Generates the markdown files to be used for page generation
    assets_generated = generate_markdown_files()

    if not assets_generated:
        util.buildhelpers.remove_module_from_menu(assets_config.module_name)


def generate_markdown_files():
    """Responsible for generating asset index page and getting shared data for all assets."""
    has_asset = False

    asset_list = util.relationshipgetters.get_asset_list()

    asset_list_no_deprecated_revoked = util.buildhelpers.filter_deprecated_revoked(asset_list)

    if asset_list_no_deprecated_revoked:
        has_asset = True

    if has_asset:
        data = {}

        notes = util.relationshipgetters.get_objects_using_notes()
        side_menu_data = util.buildhelpers.get_side_menu_data("Assets", "/assets/", asset_list_no_deprecated_revoked)
        data["side_menu_data"] = side_menu_data
        data["assets_table"] = get_assets_table_data(asset_list_no_deprecated_revoked)
        data["assets_list_len"] = str(len(asset_list_no_deprecated_revoked))

        subs = assets_config.asset_index_md + json.dumps(data)

        with open(os.path.join(assets_config.asset_markdown_path, "overview.md"), "w", encoding="utf8") as md_file:
            md_file.write(subs)

        # Create the markdown for assets
        for asset in asset_list:
            generate_asset_md(asset, side_menu_data, notes)

    return has_asset


def generate_asset_md(asset, side_menu_data, notes):
    """Responsible for generating markdown of all assets."""
    attack_id = util.buildhelpers.get_attack_id(asset)

    if not attack_id:
        return

    data = {}
    data["attack_id"] = attack_id
    data["side_menu_data"] = side_menu_data
    data["notes"] = notes.get(asset["id"])

    dates = util.buildhelpers.get_created_and_modified_dates(asset)
    if dates.get("created"):
        data["created"] = dates["created"]
    if dates.get("modified"):
        data["modified"] = dates["modified"]
    if asset.get("name"):
        data["name"] = asset["name"]
    if asset.get("x_mitre_version"):
        data["version"] = asset["x_mitre_version"]

    if isinstance(asset.get("x_mitre_contributors"), collections.abc.Iterable):
        data["contributors_list"] = asset["x_mitre_contributors"]

    if asset.get("x_mitre_platforms"):
        asset["x_mitre_platforms"].sort()
        data["platforms"] = ", ".join(asset["x_mitre_platforms"])

    if asset.get("x_mitre_sectors"):
        asset["x_mitre_sectors"].sort()
        data["sectors"] = ", ".join(asset["x_mitre_sectors"])

    # Get initial reference list
    reference_list = {"current_number": 0}

    # Get initial reference list from asset object
    reference_list = util.buildhelpers.update_reference_list(reference_list, asset)

    if asset.get("description"):
        data["descr"] = asset["description"]
    if asset.get("x_mitre_deprecated"):
        data["deprecated"] = True

    # Get technique data for technique table
    data["technique_table_data"] = get_techniques_targeting_asset_data(asset, reference_list)

    # Get navigator layers for this asset
    layers = util.buildhelpers.get_navigator_layers(
        data["name"],
        data["attack_id"],
        "asset",
        "targeted by",
        data["version"] if "version" in data else None,
        data["technique_table_data"],
    )

    data["layers"] = []
    for layer in layers:
        with open(
            os.path.join(
                assets_config.asset_markdown_path,
                "-".join([data["attack_id"], "techniques", layer["domain"]]) + ".md",
            ),
            "w",
            encoding="utf8",
        ) as layer_json:
            subs = site_config.layer_md.substitute(
                {
                    "attack_id": data["attack_id"],
                    "path": "assets/" + data["attack_id"],
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

    if asset.get("x_mitre_related_assets"):
        data["related_assets_table"] = get_related_asset_data(asset["x_mitre_related_assets"])

    data["citations"] = reference_list
    data["versioning_feature"] = site_config.check_versions_module()

    subs = assets_config.asset_md.substitute(data)
    subs = subs + json.dumps(data)

    # Write out the markdown file
    with open(
        os.path.join(assets_config.asset_markdown_path, data["attack_id"] + ".md"), "w", encoding="utf8"
    ) as md_file:
        md_file.write(subs)


def get_assets_table_data(asset_list):
    """Responsible for generating asset table data for the asset index page"""
    assets_table_data = []
    for asset in asset_list:
        attack_id = util.buildhelpers.get_attack_id(asset)
        if not attack_id:
            continue

        domain_list = util.buildhelpers.get_domain_name(asset)
        row = {
            "id": attack_id,
            "name": asset["name"] if asset.get("name") else attack_id,
        }

        for domain_idx in range(len(domain_list)):
            domain_list[domain_idx] = domain_list[domain_idx].replace("-attack", "")
            if domain_list[domain_idx] == "ics":
                domain_list[domain_idx] = domain_list[domain_idx].upper()
            else:
                domain_list[domain_idx] = domain_list[domain_idx].capitalize()
        row["domains"] = domain_list

        if asset.get("description"):
            row["descr"] = asset["description"]

        if asset.get("x_mitre_deprecated"):
            row["deprecated"] = True

        assets_table_data.append(row)

    return assets_table_data


def get_related_asset_data(related_assets):
    if not related_assets:
        return []

    related_asset_data = []
    for related_asset in related_assets:
        row = {
            "name": related_asset["name"],  # required
        }
        if related_asset.get("related_asset_sectors"):
            related_asset["related_asset_sectors"].sort()
            row["sectors"] = ", ".join(related_asset["related_asset_sectors"])
        if related_asset.get("description"):
            row["descr"] = related_asset["description"]
        related_asset_data.append(row)
    return related_asset_data


def get_techniques_targeting_asset_data(asset, reference_list):
    """Given an asset and its reference list, get the techniques targeting the asset.
    Check the reference list for citations, if not found in list, add it.
    """
    technique_list = {}
    techniques_targeting_assets = util.relationshipgetters.get_techniques_targeting_assets()

    if techniques_targeting_assets.get(asset.get("id")):
        for technique in techniques_targeting_assets[asset["id"]]:
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
