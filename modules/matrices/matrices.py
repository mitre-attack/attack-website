import json
import os

from loguru import logger

from modules import site_config, util

from . import matrices_config


def generate_matrices():
    """Responsible for verifying matrix directory and generating index matrix markdown."""
    # Create content pages directory if does not already exist
    util.buildhelpers.create_content_pages_dir()

    # Move templates to templates directory
    util.buildhelpers.move_templates(matrices_config.module_name, matrices_config.matrices_templates_path)

    # Verify if directory exists
    if not os.path.isdir(matrices_config.matrix_markdown_path):
        os.mkdir(matrices_config.matrix_markdown_path)

    # Write the matrix index.html page
    with open(os.path.join(matrices_config.matrix_markdown_path, "overview.md"), "w", encoding="utf8") as md_file:
        md_file.write(matrices_config.matrix_overview_md)

    notes = util.relationshipgetters.get_objects_using_notes()

    side_menu_data = util.buildhelpers.get_side_menu_matrices(matrices_config.matrices)

    matrix_generated = False

    for matrix in matrices_config.matrices:
        if matrix["type"] == "external":
            # link to externally hosted matrix, don't create a page for it
            continue
        matrix_generated = generate_platform_matrices(matrix, notes, side_menu_data)

    for deprecated_matrix in matrices_config.deprecated_matrices:
        generate_deprecated_matrix(deprecated_matrix, side_menu_data)

    if not matrix_generated:
        util.buildhelpers.remove_module_from_menu(matrices_config.module_name)


def generate_platform_matrices(matrix, notes, side_menu_data=None):
    """Given a matrix, generates the matrix markdown"""
    has_data = False
    data = {}
    data["menu"] = side_menu_data
    data["domain"] = matrix["matrix"].split("-")[0]
    data["name"] = matrix["name"]

    data["matrices"], data["has_subtechniques"], data["tour_technique"] = get_sub_matrices(matrix)
    if data["matrices"]:
        has_data = True
        matrix_ids = get_matrix_ids(data["matrices"])
        data["notes"] = []
        for matrix_id in matrix_ids:
            data["notes"].append(notes.get(matrix_id))

    data["platforms"] = [
        {"name": platform, "path": matrices_config.platform_to_path[platform]} for platform in matrix["platforms"]
    ]
    data["navigator_link"] = site_config.navigator_link

    data["descr"] = matrix["descr"]
    data["path"] = matrix["path"]

    data["versioning_feature"] = site_config.check_versions_module()
    data["resources"] = site_config.check_resources_module()

    subs = matrices_config.matrix_md.substitute(data)
    subs = subs + json.dumps(data)

    with open(
        os.path.join(matrices_config.matrix_markdown_path, data["domain"] + "-" + matrix["name"] + ".md"),
        "w",
        encoding="utf8",
    ) as md_file:
        md_file.write(subs)

    for subtype in matrix["subtypes"]:
        generate_platform_matrices(subtype, notes, side_menu_data)

    return has_data


def generate_deprecated_matrix(matrix, side_menu_data=None):
    """Generate deprecated matrix md file"""

    data = {}
    data["menu"] = side_menu_data
    data["name"] = matrix["name"]
    data["domain"] = matrix["matrix"].split("-")[0]
    data["path"] = matrix["path"]
    data["deprecated"] = True

    ms = util.relationshipgetters.get_ms()

    # memorystore for the current domain
    domain_ms = ms[matrix["matrix"]]

    sub_matrices = util.stixhelpers.get_matrices(domain_ms, matrix["matrix"])
    data["descr"] = ""
    for sub in sub_matrices:
        if sub.get("description"):
            data["descr"] += sub["description"]

    subs = matrices_config.matrix_md.substitute(data)
    subs = subs + json.dumps(data)

    with open(
        os.path.join(matrices_config.matrix_markdown_path, data["domain"] + "-" + matrix["name"] + ".md"),
        "w",
        encoding="utf8",
    ) as md_file:
        md_file.write(subs)


def get_matrix_ids(matrices):
    """Get matrix ids from matrix list"""
    matrix_ids = []

    for matrix in matrices:
        if not matrix["id"] in matrix_ids:
            matrix_ids.append(matrix["id"])

    return matrix_ids


def get_sub_matrices(matrix):
    ms = util.relationshipgetters.get_ms()

    # memorystore for the current domain
    domain_ms = ms[matrix["matrix"]]
    # get relevant techniques
    techniques = util.stixhelpers.get_techniques(domain_ms, matrix["matrix"])
    platform_techniques = util.buildhelpers.filter_techniques_by_platform(techniques, matrix["platforms"])
    platform_techniques = util.buildhelpers.filter_out_subtechniques(platform_techniques)
    platform_techniques = util.buildhelpers.filter_deprecated_revoked(platform_techniques)
    # get relevant tactics
    all_tactics = util.stixhelpers.get_all_of_type(domain_ms, ["x-mitre-tactic"])
    tactic_id_to_shortname = {}
    for tactic in all_tactics:
        if "x_mitre_shortname" in tactic:
            tactic_id_to_shortname[tactic["id"]] = tactic["x_mitre_shortname"]
        else:
            logger.error(f"[{tactic['id']}] Tactic does not have 'x_mitre_shortname' set, ignoring: {tactic['name']}")

    has_subtechniques = False  # track whether the current matrix has subtechniques
    tour_technique = {  # technique used as an example in the sub-technique tour / usage explainer
        "technique": None,
        "tactic": None,
        "subtechnique_count": 0,
    }

    # helper functions
    def phase_names(technique):
        """get kill chain phase names from the given technique"""
        if "kill_chain_phases" not in technique:
            logger.warning(f"Technique not assigned to any Tactics: {technique['id']} - {technique['name']}")
            return []
        phases = technique["kill_chain_phases"]
        return [phase["phase_name"] for phase in phases]

    def transform_technique(technique, tactic_id):
        """transform a technique object into the format required by the matrix macro"""
        attack_id = util.buildhelpers.get_attack_id(technique)

        obj = {}

        if attack_id:
            obj["id"] = technique["id"]
            obj["name"] = technique["name"]
            obj["external_id"] = attack_id

            obj["url"] = "/techniques/" + attack_id.replace(".", "/")  # sub-technique URL replacement
            obj["x_mitre_platforms"] = technique.get("x_mitre_platforms")
            obj["x_mitre_deprecated"] = technique.get("x_mitre_deprecated")
            obj["revoked"] = technique.get("revoked")

            subtechniques_of = util.relationshipgetters.get_subtechniques_of()

            if technique["id"] in subtechniques_of:
                subtechniques = subtechniques_of[technique["id"]]
                obj["subtechniques"] = list(map(lambda st: transform_technique(st["object"], tactic_id), subtechniques))
                # Filter out empty subtechniques
                obj["subtechniques"] = list(filter(lambda st: len(st) > 0, obj["subtechniques"]))
                # Filter subtechniques by platform
                obj["subtechniques"] = util.buildhelpers.filter_techniques_by_platform(
                    obj["subtechniques"], matrix["platforms"]
                )
                # remove deprecated and revoked
                obj["subtechniques"] = util.buildhelpers.filter_deprecated_revoked(obj["subtechniques"])
                # sort subtechniques by ATT&CK ID
                obj["subtechniques"] = sorted(obj["subtechniques"], key=lambda x: x["external_id"])

                nonlocal has_subtechniques
                has_subtechniques = True
                nonlocal tour_technique
                if tour_technique["subtechnique_count"] < 4 and tour_technique["subtechnique_count"] < len(
                    obj["subtechniques"]
                ):
                    # use this for the tour
                    tour_technique["technique"] = technique["id"]
                    tour_technique["tactic"] = tactic_id
                    tour_technique["subtechnique_count"] = len(obj["subtechniques"])

        return obj

    def techniques_in_tactic(tactic_id):
        """helper function mapping a tactic_id
        to a structured tactic object including the (filtered) techniques
        in the tactic"""
        # filter platform techniques to those inside of this tactic
        techniques = list(
            filter(lambda technique: tactic_id_to_shortname[tactic_id] in phase_names(technique), platform_techniques)
        )
        # transform into format required by matrix macro
        return list(map(lambda t: transform_technique(t, tactic_id), techniques))

    def transform_tactic(tactic_id):
        """transform a tactic object into the format required by the matrix macro"""
        tactic_obj = list(filter(lambda t: t["id"] == tactic_id, all_tactics))[0]

        attack_id = util.buildhelpers.get_attack_id(tactic_obj)

        obj = {"techniques": []}

        if attack_id:
            obj["id"] = tactic_id
            obj["name"] = tactic_obj["name"]
            obj["external_id"] = attack_id

            obj["url"] = "/tactics/" + attack_id
            obj["techniques"] = techniques_in_tactic(tactic_id)

        return obj

    data = []
    sub_matrices = util.stixhelpers.get_matrices(domain_ms, matrix["matrix"])
    for sub_matrix in sub_matrices:
        # find last modified date
        matrix_dates = util.buildhelpers.get_created_and_modified_dates(sub_matrix)
        matrix_timestamp = matrix_dates["modified"] if "modified" in matrix_dates else matrix_dates["created"]
        # get tactics for the matrix
        tactics = list(map(lambda tid: transform_tactic(tid), sub_matrix["tactic_refs"]))
        # filter out empty tactics
        tactics = list(filter(lambda t: len(t["techniques"]) > 0, tactics))
        data.append(
            {
                "name": sub_matrix["name"],
                "id": sub_matrix["id"],
                "timestamp": matrix_timestamp,
                "description": sub_matrix["description"],
                "tactics": tactics,
            }
        )

    return data, has_subtechniques, tour_technique
