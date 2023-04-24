import json
import os
import re

from loguru import logger

from modules import site_config, util

from . import techniques_config


def generate_techniques():
    """Generate techniques, return True if technique was generated, False if nothing was generated."""
    # Create content pages directory if does not already exist
    util.buildhelpers.create_content_pages_dir()

    # Move templates to templates directory
    util.buildhelpers.move_templates(techniques_config.module_name, techniques_config.techniques_templates_path)

    # Verify if directory exists
    if not os.path.isdir(techniques_config.techniques_markdown_path):
        os.mkdir(techniques_config.techniques_markdown_path)

    # TODO resolve infinite redirect loop when run locally. Needs further testing before code removal.
    # Generate redirections
    util.buildhelpers.generate_redirections(
        redirections_filename=techniques_config.techniques_redirection_location, redirect_md=site_config.redirect_md
    )

    # Write the technique index.html page
    with open(os.path.join(techniques_config.techniques_markdown_path, "overview.md"), "w", encoding="utf8") as md_file:
        md_file.write(techniques_config.technique_overview_md)

    # To verify if a technique was generated
    technique_generated = False

    techniques_no_sub = {}
    tactics = {}

    ms = util.relationshipgetters.get_ms()

    notes = util.relationshipgetters.get_objects_using_notes()

    for domain in site_config.domains:
        # Reads the STIX and creates a list of the ATT&CK Techniques
        techniques_no_sub[domain["name"]] = util.buildhelpers.filter_out_subtechniques(
            util.stixhelpers.get_techniques(ms[domain["name"]], domain["name"])
        )
        tactics[domain["name"]] = util.stixhelpers.get_tactic_list(src=ms[domain["name"]], domain=domain["name"])

    side_nav_data = get_technique_side_nav_data(techniques_no_sub, tactics)

    for domain in site_config.domains:
        deprecated = True if domain["deprecated"] else False
        check_if_generated = generate_domain_markdown(
            domain["name"], techniques_no_sub, tactics, side_nav_data, notes, deprecated
        )
        if not technique_generated:
            if check_if_generated:
                technique_generated = True

    if not technique_generated:
        util.buildhelpers.remove_module_from_menu(techniques_config.module_name)


def generate_domain_markdown(domain, techniques_no_sub, tactics, side_nav_data, notes, deprecated=None):
    """Generate technique index markdown for each domain and generates shared data for techniques."""
    # Check if there is at least one technique
    if techniques_no_sub[domain]:
        technique_list_no_sub_no_deprecated = util.buildhelpers.filter_deprecated_revoked(techniques_no_sub[domain])

        data = {}

        data["domain"] = domain.split("-")[0]

        # Get technique table data and number of techniques
        data["technique_table"] = util.buildhelpers.get_technique_table_data(None, technique_list_no_sub_no_deprecated)
        data["technique_list_len"] = str(len(technique_list_no_sub_no_deprecated))
        data["subtechniques_len"] = util.buildhelpers.get_subtechnique_count(technique_list_no_sub_no_deprecated)

        # Get tactic-techniques table
        data["menu"] = side_nav_data

        if deprecated:
            data["deprecated"] = deprecated

        subs = techniques_config.technique_domain_md.substitute(data)
        subs = subs + json.dumps(data)

        techniques_markdown = os.path.join(
            techniques_config.techniques_markdown_path, f"{data['domain']}-techniques.md"
        )
        with open(techniques_markdown, "w", encoding="utf8") as md_file:
            md_file.write(subs)

        # Create the markdown for techniques in the STIX
        for technique in techniques_no_sub[domain]:
            if "revoked" not in technique or technique["revoked"] is False:
                generate_technique_md(technique, domain, side_nav_data, tactics[domain], notes)

        return True

    return False


def generate_technique_md(technique, domain, side_nav_data, tactic_list, notes):
    """Generetes markdown data for given technique."""
    attack_id = util.buildhelpers.get_attack_id(technique)

    # Only add technique if the attack id was found
    if attack_id:
        subtechniques_of = util.relationshipgetters.get_subtechniques_of()

        technique_dict = {}

        technique_dict["attack_id"] = attack_id
        technique_dict["domain"] = domain.split("-")[0]
        technique_dict["menu"] = side_nav_data
        technique_dict["name"] = technique.get("name")
        technique_dict["notes"] = notes.get(technique["id"])

        # Get subtechniques (not deprecated/revoked)
        technique_dict["subtechniques"] = get_subtechniques(technique)

        # Generate data for technique
        technique_dict = generate_data_for_md(technique_dict, technique, tactic_list)

        subs = techniques_config.technique_md.substitute(technique_dict)
        path = technique_dict["attack_id"]

        subs = subs + json.dumps(technique_dict)

        # Write out the technique markdown file
        with open(
            os.path.join(techniques_config.techniques_markdown_path, path + ".md"), "w", encoding="utf8"
        ) as md_file:
            md_file.write(subs)

        # Generate data for sub-techniques
        if technique_dict["subtechniques"]:
            # Generate sub-technique markdown file for each sub technique
            subtechniques = subtechniques_of[technique["id"]]
            for subtechnique in subtechniques:
                sub_tech_dict = {}

                sub_tech_dict["domain"] = domain.split("-")[0]
                sub_tech_dict["menu"] = side_nav_data
                sub_tech_dict["parent_id"] = technique_dict["attack_id"]
                sub_tech_dict["parent_name"] = technique.get("name")
                sub_tech_dict["subtechniques"] = technique_dict["subtechniques"]

                sub_tech_dict = generate_data_for_md(sub_tech_dict, subtechnique["object"], tactic_list, True)

                if sub_tech_dict.get("sub_number"):
                    subs = techniques_config.sub_technique_md.substitute(sub_tech_dict)
                    path = sub_tech_dict["parent_id"] + "-" + sub_tech_dict["sub_number"]

                    subs = subs + json.dumps(sub_tech_dict)

                    # Write out the technique markdown file
                    with open(
                        os.path.join(techniques_config.techniques_markdown_path, path + ".md"), "w", encoding="utf8"
                    ) as md_file:
                        md_file.write(subs)


def generate_data_for_md(technique_dict, technique, tactic_list, is_sub_technique=False):
    """Given a technique or subtechnique, fill technique dictionary to create markdown file."""
    technique_dict["name"] = technique.get("name")

    if is_sub_technique:
        technique_dict["attack_id"] = util.buildhelpers.get_attack_id(technique)
        if technique_dict["attack_id"]:
            technique_dict["sub_number"] = technique_dict["attack_id"].split(".")[1]
        technique_dict["is_subtechnique"] = True

    if technique_dict["attack_id"]:
        # Get capecs and mtcs
        for ref in technique["external_references"]:
            if ref.get("source_name"):
                if ref["source_name"] == "capec":
                    if technique_dict.get("capecs") is None:
                        technique_dict["capecs"] = []
                    capec_dict = {"id": ref["external_id"], "url": ref["url"]}
                    technique_dict["capecs"].append(capec_dict)

                if ref["source_name"] == "NIST Mobile Threat Catalogue":
                    if technique_dict.get("mtcs") is None:
                        technique_dict["mtcs"] = []

                    mtcs_dict = {"id": ref["external_id"], "url": ref["url"]}
                    technique_dict["mtcs"].append(mtcs_dict)

        # Get initial reference list
        reference_list = {"current_number": 0}

        # Get initial reference list from technique object
        reference_list = util.buildhelpers.update_reference_list(reference_list, technique)

        dates = util.buildhelpers.get_created_and_modified_dates(technique)

        if dates.get("created"):
            technique_dict["created"] = dates["created"]

        if dates.get("modified"):
            technique_dict["modified"] = dates["modified"]

        if technique.get("x_mitre_deprecated"):
            technique_dict["deprecated"] = True
        else:
            technique_dict["deprecated"] = False

        # Get technique description with citations
        if technique.get("description") and not technique_dict["deprecated"]:
            technique_dict["descr"] = technique["description"]

            # Get mitigation table
            technique_dict["mitigation_table"] = get_mitigations_table_data(technique, reference_list)

            # Get examples
            technique_dict["examples_table"] = get_examples_table_data(technique, reference_list)

            # Get technique version
            if technique.get("x_mitre_version"):
                technique_dict["version"] = technique["x_mitre_version"]

            # Get tactics of technique
            if technique.get("kill_chain_phases"):
                technique_dict["tactics"] = []
                for elem in technique["kill_chain_phases"]:
                    # Get tactic from tactic_list
                    phase_name = elem["phase_name"]

                    tmp_tactic_list = []
                    for _tactic in tactic_list:
                        shortname = _tactic["x_mitre_shortname"]
                        if shortname == phase_name:
                            tmp_tactic_list.append(_tactic)

                    if not tmp_tactic_list:
                        logger.error(
                            f"Technique: {technique_dict['name']} is in Tactic: {phase_name}, but that is an unknown Tactic for domain: {technique_dict['domain']}!"
                        )
                        continue
                    tactic = tmp_tactic_list[0]

                    tactic_info = {"name": tactic["name"], "id": util.buildhelpers.get_attack_id(tactic)}
                    technique_dict["tactics"].append(tactic_info)

            # Get platforms that technique uses
            if technique.get("x_mitre_platforms"):
                technique["x_mitre_platforms"].sort()
                technique_dict["platforms"] = ", ".join(technique["x_mitre_platforms"])

            # Get system requirements
            if technique.get("x_mitre_system_requirements"):
                technique["x_mitre_system_requirements"].sort()
                technique_dict["sysreqs"] = ", ".join(technique["x_mitre_system_requirements"])
                technique_dict["sysreqs"] = re.sub("\.?\\n+", "; ", technique_dict["sysreqs"])

            # Get permissions required
            if technique.get("x_mitre_permissions_required"):
                technique["x_mitre_permissions_required"].sort()
                technique_dict["perms"] = ", ".join(technique["x_mitre_permissions_required"])

            # Get effective permissions
            if technique.get("x_mitre_effective_permissions"):
                technique["x_mitre_effective_permissions"].sort()
                technique_dict["eff_perms"] = ", ".join(technique["x_mitre_effective_permissions"])

            # Get data sources and components
            (
                technique_dict["datasources"],
                technique_dict["show_descriptions"],
            ) = get_datasources_and_components_of_technique(technique, reference_list)

            # Get if technique supports remote
            if technique.get("x_mitre_remote_support"):
                if technique["x_mitre_remote_support"]:
                    technique_dict["supports_remote"] = " Yes"
                else:
                    technique_dict["supports_remote"] = " No"

            # Get network requirements
            if technique.get("x_mitre_network_requirements"):
                if technique["x_mitre_network_requirements"]:
                    technique_dict["network_reqs"] = " Yes"
                else:
                    technique_dict["network_reqs"] = " No"

            # Get list of impacts
            if technique.get("x_mitre_impact_type"):
                technique["x_mitre_impact_type"].sort()
                technique_dict["impact_type"] = ", ".join(technique["x_mitre_impact_type"])

            # Get list of defenses bypassed
            if technique.get("x_mitre_defense_bypassed"):
                technique["x_mitre_defense_bypassed"].sort()
                technique_dict["def_bypass"] = ", ".join(technique["x_mitre_defense_bypassed"])

            # Get list of contributors
            if technique.get("x_mitre_contributors"):
                technique["x_mitre_contributors"].sort()
                technique_dict["contributors"] = "; ".join(technique["x_mitre_contributors"])

            # Get list of tactic types
            if technique.get("x_mitre_tactic_type"):
                technique["x_mitre_tactic_type"].sort()
                technique_dict["tactic_type"] = ", ".join(technique["x_mitre_tactic_type"])

            # Get detection data
            if technique.get("x_mitre_detection"):
                technique_dict["detection"] = technique["x_mitre_detection"]

            # Get if technique is detectable by common defenses
            if technique.get("x_mitre_detectable_by_common_defenses"):
                technique_dict["detectable"] = technique.get("x_mitre_detectable_by_common_defenses")

            # Get explanation of detecatable by common defenses
            if technique.get("x_mitre_detectable_by_common_defenses_explanation"):
                technique_dict["detectable_exp"] = util.buildhelpers.replace_html_chars(
                    technique["x_mitre_detectable_by_common_defenses_explanation"]
                )

            # Get diffulty for adversaries
            if technique.get("x_mitre_difficulty_for_adversary"):
                technique_dict["diff_for_adv"] = technique["x_mitre_difficulty_for_adversary"]

            # Get explanation of difficulty for adversaries
            if technique.get("x_mitre_difficulty_for_adversary_explanation"):
                technique_dict["diff_for_adv_exp"] = util.buildhelpers.replace_html_chars(
                    technique["x_mitre_difficulty_for_adversary_explanation"]
                )

            technique_dict["citations"] = reference_list

            technique_dict["versioning_feature"] = site_config.check_versions_module()

        else:
            if technique_dict["deprecated"]:
                technique_dict["descr"] = technique.get("description")

    return technique_dict


def get_mitigations_table_data(technique, reference_list):
    """Given a technique a reference list, find mitigations that mitigate
    technique and return list with mitigation data. Also modifies the
    reference list if it finds a reference that is not on the list
    """
    mitigation_data = []

    # Check if technique has mitigations
    if util.relationshipgetters.get_technique_mitigated_by_mitigation().get(technique["id"]):
        # Iterate through technique mitigations
        for mitigation in util.relationshipgetters.get_technique_mitigated_by_mitigation()[technique["id"]]:
            # Do not add deprecated mitigation to table
            if not mitigation["object"].get("x_mitre_deprecated"):
                attack_id = util.buildhelpers.get_attack_id(mitigation["object"])

                # Only add if mitigation attack id is found
                if attack_id:
                    row = {}
                    row["mid"] = attack_id
                    row["name"] = mitigation["object"]["name"]
                    if mitigation["relationship"].get("description"):
                        # Get filtered description
                        reference_list = util.buildhelpers.update_reference_list(
                            reference_list, mitigation["relationship"]
                        )
                        row["descr"] = mitigation["relationship"]["description"]

                    mitigation_data.append(row)

    if mitigation_data:
        mitigation_data = sorted(mitigation_data, key=lambda k: k["name"].lower())
    return mitigation_data


def get_examples_table_data(technique, reference_list):
    """Given a technique object, find examples in malware using technique,
    tools using technique and groups using technique. Return list with
    example data
    """
    # Creating map to avoid repeating the code multiple times
    examples_map = [
        {"example_type": util.relationshipgetters.get_tools_using_technique()},
        {"example_type": util.relationshipgetters.get_malware_using_technique()},
        {"example_type": util.relationshipgetters.get_groups_using_technique()},
        {"example_type": util.relationshipgetters.get_campaigns_using_technique()},
    ]

    example_data = []

    # Get malware, tools, or campaigns used by group
    for examples in examples_map:
        if examples["example_type"].get(technique.get("id")):
            for example in examples["example_type"][technique["id"]]:
                attack_id = util.buildhelpers.get_attack_id(example["object"])

                # Only add example data if the attack id is found
                if attack_id:
                    row = {}

                    row["id"] = attack_id

                    row["path"] = get_path_from_type(example["object"])

                    row["name"] = example["object"]["name"]

                    if example["relationship"].get("description"):
                        # Get filtered description
                        reference_list = util.buildhelpers.update_reference_list(
                            reference_list, example["relationship"]
                        )
                        row["descr"] = example["relationship"]["description"]

                    example_data.append(row)

    if example_data:
        example_data = sorted(example_data, key=lambda k: k["name"].lower())
    return example_data


def get_path_from_type(object):
    """Given an object, return the path"""
    path_map = {"intrusion-set": "groups", "malware": "software", "tool": "software", "campaign": "campaigns"}
    return path_map[object.get("type")]


def get_technique_side_nav_data(techniques, tactics):
    """Responsible for generating the links that are located on the left side of individual technique domain pages."""
    side_nav_data = []

    subtechniques_of = util.relationshipgetters.get_subtechniques_of()

    for domain in site_config.domains:
        if domain["deprecated"]:
            continue

        domain_data = {
            "name": domain["alias"],
            "id": domain["name"].split("-")[0],
            "path": "/techniques/{}/".format(domain["name"].split("-")[0]),  # root level doesn't get a path
            "children": [],
        }

        technique_list = get_techniques_list(techniques[domain["name"]])

        for tactic in tactics[domain["name"]]:
            tactic_row = {}

            tactic_row["name"] = tactic["name"]
            tactic_row["id"] = util.buildhelpers.get_attack_id(tactic)
            tactic_row["path"] = "/tactics/{}".format(util.buildhelpers.get_attack_id(tactic))

            tactic_row["children"] = []

            # Skip tactic if it does not have techniques
            if not technique_list.get(tactic["x_mitre_shortname"]):
                continue
            for technique in technique_list[tactic["x_mitre_shortname"]]:
                technique_row = {}
                # Get technique id and name for each technique
                technique_row["name"] = technique["name"]
                technique_row["id"] = technique["id"]
                technique_row["path"] = "/techniques/{}/".format(technique["id"])
                technique_row["children"] = []

                # Add subtechniques as children if they are found:
                if technique["stix_id"] in subtechniques_of:
                    subtechniques = subtechniques_of[technique["stix_id"]]
                    for subtechnique in subtechniques:
                        child = {}
                        child["id"] = util.buildhelpers.get_attack_id(subtechnique["object"])
                        if child["id"]:
                            child["name"] = subtechnique["object"]["name"]
                            sub_number = child["id"].split(".")[1]
                            child["path"] = "/techniques/{}/{}/".format(technique["id"], sub_number)
                            child["children"] = []
                            technique_row["children"].append(child)

                    # Sort subtechniques by ATT&CK ID
                    if technique_row["children"]:
                        technique_row["children"] = sorted(technique_row["children"], key=lambda k: k["id"])

                # Add technique data to tactic
                tactic_row["children"].append(technique_row)
            # Add tactic to domain
            domain_data["children"].append(tactic_row)
        # add domain to the table
        side_nav_data.append(domain_data)

    return {
        "name": "techniques",
        "id": "techniques",
        "path": None,  # root level doesn't get a path
        "children": side_nav_data,
    }


def get_techniques_list(techniques):
    """This method is used to generate a list of techniques."""
    technique_list = {}

    for technique in techniques:
        if not technique.get("revoked") and not technique.get("x_mitre_deprecated"):
            attack_id = util.buildhelpers.get_attack_id(technique)

            if attack_id:
                technique_dict = {}
                technique_dict["id"] = attack_id
                technique_dict["stix_id"] = technique["id"]
                technique_dict["name"] = technique["name"]
                technique_dict["description"] = technique["description"]

                if technique.get("kill_chain_phases"):
                    for elem in technique["kill_chain_phases"]:
                        # Fill dict
                        if elem["phase_name"] not in technique_list:
                            technique_list[elem["phase_name"]] = []

                        technique_list[elem["phase_name"]].append(technique_dict)

    for key, __ in technique_list.items():
        technique_list[key] = sorted(technique_list[key], key=lambda k: k["name"].lower())

    return technique_list


def get_subtechniques(technique):
    """Given a technique, return the ID and name of the subtechnique."""
    subtechs = []
    attack_id = util.buildhelpers.get_attack_id(technique)

    subtechniques_of = util.relationshipgetters.get_subtechniques_of()

    if technique["id"] in subtechniques_of:
        subtechniques = subtechniques_of[technique["id"]]
        for subtechnique in subtechniques:
            revoked = util.buildhelpers.is_revoked(sdo=subtechnique["object"])
            deprecated = util.buildhelpers.is_deprecated(sdo=subtechnique["object"])
            if revoked or deprecated:
                continue

            sub_data = {}
            sub_data["id"] = util.buildhelpers.get_attack_id(subtechnique["object"])
            if sub_data["id"]:
                sub_data["stix_id"] = technique["id"]
                sub_data["name"] = subtechnique["object"]["name"]
                sub_number = sub_data["id"].split(".")[1]
                attack_id = util.buildhelpers.get_attack_id(technique)
                sub_data["path"] = f"/techniques/{attack_id}/{sub_number}/"
                subtechs.append(sub_data)

    return sorted(subtechs, key=lambda k: k["id"])


def get_datasources_and_components_of_technique(technique, reference_list):
    """Given a technique object, find data sources and components
    detecting the technique. Returns list with the following structure

    For each data source:
    Data Source ATT&CK ID
    Data Source name
    Data components
            Data component name
            Data component descr
    """
    datasource_and_components = []

    datacomponents_of_technique = util.relationshipgetters.get_datacomponents_detecting_technique().get(technique["id"])
    datasource_of = util.relationshipgetters.get_datasource_of()

    show_descriptions = False

    if datacomponents_of_technique:
        datasources_data = {}
        for datacomponent in datacomponents_of_technique:
            datasource = datasource_of.get(datacomponent["object"]["id"])
            datasource_attack_id = util.buildhelpers.get_attack_id(datasource)
            if datasource_attack_id:
                if not datasources_data.get(datasource_attack_id):
                    datasources_data[datasource_attack_id] = {}
                    datasources_data[datasource_attack_id]["attack_id"] = datasource_attack_id
                    datasources_data[datasource_attack_id]["name"] = datasource["name"]
                    datasources_data[datasource_attack_id]["datacomponents"] = []

                datacomponent_data = {}
                datacomponent_data["name"] = datacomponent["object"]["name"]

                if datacomponent["relationship"].get("description"):
                    reference_list = util.buildhelpers.update_reference_list(
                        reference_list, datacomponent["relationship"]
                    )
                    datacomponent_data["descr"] = datacomponent["relationship"]["description"]
                    if not show_descriptions:
                        show_descriptions = True

                datasources_data[datasource_attack_id]["datacomponents"].append(datacomponent_data)

        for datasource_key in datasources_data:
            # Sort data components
            datasources_data[datasource_key]["datacomponents"] = sorted(
                datasources_data[datasource_key]["datacomponents"], key=lambda k: k["name"].lower()
            )
            # Add
            datasource_and_components.append(datasources_data[datasource_key])

    if datasource_and_components:
        # Sort by data source name
        datasource_and_components = sorted(datasource_and_components, key=lambda k: k["name"].lower())

    return datasource_and_components, show_descriptions
