import json
import os

from loguru import logger

from modules import site_config, util

from . import tactics_config


def generate_tactics():
    """Responsible for verifying tactic directory and generating tactic
    index markdown
    """
    # Create content pages directory if does not already exist
    util.buildhelpers.create_content_pages_dir()

    # Move templates to templates directory
    util.buildhelpers.move_templates(tactics_config.module_name, tactics_config.tactics_templates_path)

    # Verify if directory exists
    if not os.path.isdir(tactics_config.tactics_markdown_path):
        os.mkdir(tactics_config.tactics_markdown_path)

    # TODO resolve infinite redirect loop when run locally. Needs further testing before code removal.
    # Generate redirections
    util.buildhelpers.generate_redirections(
        redirections_filename=tactics_config.tactics_redirection_location, redirect_md=site_config.redirect_md
    )

    # To verify if a technique was generated
    tactic_generated = False

    techniques_no_sub = {}
    tactics = {}

    ms = util.relationshipgetters.get_ms()

    notes = util.relationshipgetters.get_objects_using_notes()

    for domain in site_config.domains:
        # Reads the STIX and creates a list of the ATT&CK Techniques
        techniques_no_sub[domain["name"]] = util.buildhelpers.filter_out_subtechniques(
            util.stixhelpers.get_techniques(ms[domain["name"]], domain["name"])
        )
        tactics[domain["name"]] = util.stixhelpers.get_tactic_list(ms[domain["name"]], domain["name"])

    side_nav_data = util.buildhelpers.get_side_nav_domains_data("tactics", tactics)

    for domain in site_config.domains:
        deprecated = True if domain["deprecated"] else False
        check_if_generated = generate_domain_markdown(
            domain["name"], techniques_no_sub, tactics, side_nav_data, notes, deprecated
        )
        if not tactic_generated:
            if check_if_generated:
                tactic_generated = True

    if not tactic_generated:
        util.buildhelpers.remove_module_from_menu(tactics_config.module_name)


def generate_domain_markdown(domain, techniques, tactics, side_nav_data, notes, deprecated=None):
    """Generate tactic index markdown for each domain and generates
    shared data for tactics
    """
    if tactics[domain]:
        # Write out the markdown file for overview of domain
        data = {"domain": domain.split("-")[0], "tactics_list_len": str(len(tactics[domain]))}

        data["side_menu_data"] = side_nav_data
        data["tactics_table"] = get_domain_table_data(tactics[domain])

        if deprecated:
            data["deprecated"] = deprecated

        subs = tactics_config.tactic_domain_md.substitute(data)
        subs = subs + json.dumps(data)

        with open(
            os.path.join(tactics_config.tactics_markdown_path, data["domain"] + "-tactics.md"), "w", encoding="utf8"
        ) as md_file:
            md_file.write(subs)

        # Write the tactic index.html page
        with open(os.path.join(tactics_config.tactics_markdown_path, "overview.md"), "w", encoding="utf8") as i_md_file:
            i_md_file.write(tactics_config.tactic_overview_md)

        # Create the markdown for the enterprise groups in the STIX
        for tactic in tactics[domain]:
            generate_tactic_md(tactic, domain, tactics, techniques, side_nav_data, notes)

        return True

    return False


def generate_tactic_md(tactic, domain, tactic_list, techniques, side_nav_data, notes):
    """Generate markdown for given tactic"""
    attack_id = util.buildhelpers.get_attack_id(tactic)

    # Add if attack id is found
    if attack_id:
        data = {}

        # Fill out data

        data["attack_id"] = attack_id
        data["name"] = tactic["name"]
        data["name_lower"] = tactic["name"].lower()
        data["side_menu_data"] = side_nav_data
        data["domain"] = domain.split("-")[0]
        data["notes"] = notes.get(tactic["id"])

        if tactic.get("x_mitre_deprecated"):
            data["deprecated"] = True
        else:
            data["deprecated"] = False

        # Add more detail if descriptione exists and it is not deprecated
        if tactic.get("description") and not data["deprecated"]:
            data["descr"] = tactic["description"]

            dates = util.buildhelpers.get_created_and_modified_dates(tactic)

            if dates.get("created"):
                data["created"] = dates["created"]

            if dates.get("modified"):
                data["modified"] = dates["modified"]

            # Get techniques that are in the given tactic
            techniques_list = get_techniques_of_tactic(tactic, techniques[domain])

            data["techniques_table"] = util.buildhelpers.get_technique_table_data(tactic, techniques_list)
            data["techniques_table_len"] = str(len(techniques_list))

            data["versioning_feature"] = site_config.check_versions_module()

        else:
            if data["deprecated"]:
                data["descr"] = tactic.get("description")

        subs = tactics_config.tactic_md.substitute(data)
        subs = subs + json.dumps(data)

        with open(
            os.path.join(tactics_config.tactics_markdown_path, data["attack_id"] + ".md"), "w", encoding="utf8"
        ) as md_file:
            md_file.write(subs)


def get_domain_table_data(tactic_list):
    """Given a tactic list, returns an array of jsons with tactic name, id
    and their description
    """
    tactic_table = []

    # Set up the tactics table for a domain
    for tactic in tactic_list:
        attack_id = util.buildhelpers.get_attack_id(tactic)

        if attack_id:
            # Create json and fill out with tactic data
            tactic_dict = {}
            tactic_dict["name"] = tactic["name"]
            tactic_dict["tid"] = attack_id
            tactic_dict["description"] = tactic["description"]
            tactic_table.append(tactic_dict)

    return tactic_table


def get_techniques_of_tactic(tactic, techniques):
    """Given a tactic and a full list of techniques, return techniques that
    appear inside of tactic
    """
    techniques_list = []

    for technique in techniques:
        if not technique.get("x_mitre_deprecated"):
            if not technique.get("kill_chain_phases"):
                logger.warning(f"Technique not assigned to any Tactics: {technique['id']} - {technique['name']}")
                continue
            for phase in technique["kill_chain_phases"]:
                if phase["phase_name"] == tactic["x_mitre_shortname"]:
                    techniques_list.append(technique)

    techniques_list = sorted(techniques_list, key=lambda k: k["name"].lower())
    return techniques_list
