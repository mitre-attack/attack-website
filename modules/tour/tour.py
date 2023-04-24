import os

import modules
from modules import matrices, site_config, util

from . import tour_config


def generate_tour():
    """Responsible for dynamically generating tour steps"""

    # Algorithm
    # For each domain:
    # 1. index (start page, doesn't need to be dynamic)
    # 2. A matrix with sub-techniques
    # 3. A technique with sub-techniques
    # 4. One of the sub-techniques of that technique
    # 5. A group/software that meets the following criteria:
    # 5.1. Group has a relationship with a technique but not that technique's sub-techniques
    # 5.2. Group has a relationship with a technique and (preferably) 2+ of that technique's sub-techniques
    # 5.3. Group has a relationship with (preferably) 2+ sub-techniques but not the parent technique.

    tours = []

    # Step 1 find matrix
    # Check if matrices module is enabled
    matrices_found = False
    for module in modules.run_ptr:
        if module["module_name"] == "matrices":
            matrices_found = True
    if not matrices_found:
        return

    for matrix in matrices.matrices_config.matrices:
        if matrix["type"] == "external":
            continue  # link to externally hosted matrix, ignore it
        tours.append(get_tour_steps(matrix))

    # Choose longest tour
    def get_longest_tour():
        if tours:
            longest = {}
            for tour in tours:
                if len(tour.keys()) > len(longest.keys()):
                    longest = tour

            return longest

        return {}

    tour_steps = get_longest_tour()

    # Write tour steps to settings.js file
    javascript_settings_file = os.path.join(site_config.javascript_path, "settings.js")

    with open(javascript_settings_file, "w", encoding="utf8") as js_f:
        js_data = tour_config.js_tour_settings.substitute({"tour_steps": tour_steps})
        js_f.write(js_data)


def get_tour_steps(matrix):
    """Get all the tour steps"""

    ms = util.relationshipgetters.get_ms()

    ms = ms[matrix["matrix"]]

    # Check if techniques module is enabled
    techniques_found = False
    for module in modules.run_ptr:
        if module["module_name"] == "techniques":
            techniques_found = True
    if not techniques_found:
        return {}

    # Reads the STIX and creates a list of the techniques
    techniques = util.stixhelpers.get_techniques(ms, matrix["matrix"])

    techs_no_subtechs = util.buildhelpers.filter_out_subtechniques(techniques)
    techs_with_subtechs = util.buildhelpers.filter_out_techniques_without_subtechniques(techniques)

    # steps as array
    steps = {}

    # If matrix has techniques with subtechniques
    if techs_with_subtechs:
        steps["matrix"] = "matrices/" + matrix["path"]
    else:
        return steps

    # Find technique with sub-techniques
    technique = get_technique_with_subtechniques(techs_no_subtechs)

    if not technique:
        # Did not find technique with sub-technique
        return steps

    # Get technique ID and store that as the step
    steps["technique"] = "techniques/{}".format(util.buildhelpers.get_attack_id(technique))
    subtechnique_attack_id = get_subtech_n_of_technique(technique)
    if subtechnique_attack_id:
        steps["subtechnique"] = steps["technique"] + "/{}".format(subtechnique_attack_id)

    # Get group steps
    group_tour = []
    # Check if groups module is enabled
    groups_found = False
    for module in modules.run_ptr:
        if module["module_name"] == "groups":
            groups_found = True
    if groups_found:
        group_tour = get_group_or_software_with_subtechniques("groups")

    # Get software steps
    software_tour = []
    # Check if software module is enabled
    software_found = False
    for module in modules.run_ptr:
        if module["module_name"] == "software":
            software_found = True
    if software_found:
        software_tour = get_group_or_software_with_subtechniques("software")

    def choose_software_or_group_tour():
        """Choose between software or group tour"""

        # Return if one or neither of the tours does not exist
        if not group_tour and not software_tour:
            return []
        elif group_tour and not software_tour:
            return group_tour
        elif not group_tour and software_tour:
            return software_tour

        # First case, both tours have step 2 and 3
        if (
            group_tour.get("step2")
            and software_tour.get("step2")
            and group_tour.get("step3")
            and software_tour.get("step3")
        ):
            # If group tour has longer or equal steps length, return
            if (group_tour["step2"][1] >= software_tour["step2"][1]) and (
                group_tour["step3"][1] >= software_tour["step3"][1]
            ):
                return group_tour
            else:
                return software_tour
        # Case when both tours have step 2
        elif group_tour.get("step2") and software_tour.get("step2"):
            # If group tour has longer or equal step 2 length, return
            if group_tour["step2"][1] >= software_tour["step2"][1]:
                return group_tour
            else:
                return software_tour
        # Case when both tours have step 3
        elif group_tour.get("step3") and software_tour.get("step3"):
            # If group tour has longer or equal step 2 length, return
            if group_tour["step3"][1] >= software_tour["step3"][1]:
                return group_tour
            else:
                return software_tour
        # Case when group tour has step 2 but software tour only has step 3
        elif group_tour.get("step2") and software_tour.get("step3"):
            # If group tour has longer or equal step 2 length, return
            if group_tour["step2"][1] >= software_tour["step3"][1]:
                return group_tour
            else:
                return software_tour
        # Case when group tour has step 2 but software tour only has step 3
        elif group_tour.get("step3") and software_tour.get("step2"):
            # If group tour has longer or equal step 2 length, return
            if group_tour["step3"][1] >= software_tour["step1"][1]:
                return group_tour
            else:
                return software_tour

        # If for some reason none of the cases fit
        return []

    # Add group or software tour
    obj = choose_software_or_group_tour()

    if obj:
        steps["relationships"] = obj

    return steps


def get_technique_with_subtechniques(techs_no_subtechs):
    """Find first technique with at least 4 sub-techniques and return technique
    Return technique with the most sub-techniques if not the case
    """

    subtech_count_min = 4
    counter = 0
    chosen_tech = {}

    subtechniques_of = util.relationshipgetters.get_subtechniques_of()

    for tech in techs_no_subtechs:
        if tech["id"] in subtechniques_of:
            # Grab sub-technique count from technique
            subtech_count = len(subtechniques_of[tech["id"]])
            # Check if sub-technique count is bigger than counter
            if counter < subtech_count:
                # Quick return if found
                if subtech_count >= subtech_count_min:
                    return tech
                # Set counter and new techique
                counter = subtech_count
                chosen_tech = tech

    return chosen_tech


def get_subtech_n_of_technique(technique):
    """Return ID number of first sub-technique of given technique"""

    subtechniques_of = util.relationshipgetters.get_subtechniques_of()

    for subtech in subtechniques_of[technique["id"]]:
        attack_id = util.buildhelpers.get_attack_id(subtech["object"])
        if attack_id:
            return attack_id.split(".")[1]

    return None


def get_group_or_software_with_subtechniques(object_type):
    """Get group or software with subtechniques"""

    if object_type == "groups":
        obj_list = util.relationshipgetters.get_group_list()
        techniques_used_by_type = util.relationshipgetters.get_techniques_used_by_groups()
    else:
        obj_list = util.relationshipgetters.get_software_list()
        # Combine tools and malware dictionaries in a copy
        techniques_used_by_type = dict(util.relationshipgetters.get_techniques_used_by_tools())
        techniques_used_by_type.update(util.relationshipgetters.get_techniques_used_by_malware())

    obj_tour_list = []

    for obj in obj_list:
        technique_list = {}

        if techniques_used_by_type.get(obj.get("id")):
            obj_has_subtechniques = False
            for technique in techniques_used_by_type[obj["id"]]:
                if not technique["object"].get("x_mitre_deprecated"):
                    # Get techniques used list and only update if it has subtechniques
                    if techniques_used(technique_list, technique):
                        obj_has_subtechniques = True

            # Get list of potential tours if group has subtechniques
            if obj_has_subtechniques:
                obj_tour = get_groups_tour(technique_list)
                attack_id = util.buildhelpers.get_attack_id(obj)
                if obj_tour and attack_id:
                    obj_tour["obj_id"] = object_type + "/" + attack_id
                    obj_tour_list.append(obj_tour)

    return find_best_group_or_software(obj_tour_list)


def find_best_group_or_software(obj_tour_list):
    """Find group with step 2 and 3 with 2 or more subtechniques"""

    # Ideal: find Step 2 and Step 3 with most subtechniques
    obj_w_best_step_2_3 = {}
    for obj_tour in obj_tour_list:
        # First group
        if not obj_w_best_step_2_3:
            obj_w_best_step_2_3 = obj_tour

        # Verify if group tour has step 2 and step 3
        elif obj_tour.get("step2") and obj_tour.get("step3"):
            # Only update if step 2 and 3 where found
            if obj_w_best_step_2_3.get("step2") and obj_w_best_step_2_3.get("step3"):
                # When new group has same or more subtechniques
                if (obj_w_best_step_2_3["step2"][1] <= obj_tour["step2"][1]) and (
                    obj_w_best_step_2_3["step3"][1] <= obj_tour["step3"][1]
                ):
                    obj_w_best_step_2_3 = obj_tour
            else:
                obj_w_best_step_2_3 = obj_tour
        # Case when step 2 is available but not step 3
        # Only update if current group does not have a step 3
        elif obj_tour.get("step2") and not obj_w_best_step_2_3.get("step3"):
            if not obj_w_best_step_2_3.get("step2"):
                obj_w_best_step_2_3 = obj_tour
            elif obj_w_best_step_2_3["step2"][1] < obj_tour["step2"][1]:
                obj_w_best_step_2_3 = obj_tour
        # Case when step 3 is available but not step 1
        # Only update if current group does not have a step 2
        elif obj_tour.get("step3") and not obj_w_best_step_2_3.get("step2"):
            if not obj_w_best_step_2_3.get("step3"):
                obj_w_best_step_2_3 = obj_tour
            elif obj_w_best_step_2_3["step3"][1] < obj_tour["step3"][1]:
                obj_w_best_step_2_3 = obj_tour

    return obj_w_best_step_2_3


def techniques_used(technique_list, technique):
    """Add technique to technique list and make distinction between techniques
    subtechniques
    """

    attack_id = util.buildhelpers.get_attack_id(technique["object"])
    has_subtechniques = False

    if attack_id:
        # Check if technique not already in technique_list dict
        if attack_id not in technique_list:
            # Check if attack id is a sub-technique
            if util.buildhelpers.is_sub_tid(attack_id):
                has_subtechniques = True

                parent_id = util.buildhelpers.get_parent_technique_id(attack_id)

                # If parent technique not already in list, add to list and add current sub-technique
                if parent_id not in technique_list:
                    technique_list[parent_id] = {}
                    technique_list[parent_id]["subtechniques"] = []

                technique_list[parent_id]["subtechniques"].append(attack_id)

            # Attack id is regular technique
            else:
                # Add technique to list
                technique_list[attack_id] = {}
                technique_list[attack_id]["subtechniques"] = []

        # Check if parent ID was added by sub-technique
        # parent ID will not have description
        elif "descr" not in technique_list[attack_id]:
            # Check if it has external references
            if technique["relationship"].get("description"):
                # Get filtered description
                technique_list[attack_id]["descr"] = True

    return has_subtechniques


def get_groups_tour(technique_list):
    """Get steps 1 through 3 if they are available"""

    groups = {}

    for technique in technique_list:
        # Step 1
        if not technique_list[technique]["subtechniques"]:
            if not groups.get("step1"):
                groups["step1"] = technique
        # Step 2 and 3
        else:
            # If Technique has relationship with group and subtechniques as well (Step 2)
            if technique_list[technique].get("descr"):
                # Check if it has two or more sub-techniques if not it is fine if its the first one found
                if groups.get("step2") and len(technique_list[technique]["subtechniques"]) > 1:
                    groups["step2"] = [technique, len(technique_list[technique]["subtechniques"])]
                elif not groups.get("step2"):
                    groups["step2"] = [technique, len(technique_list[technique]["subtechniques"])]
            # Parent technique does not have relationship with group (Step 3)
            else:
                # Check if it has two or more sub-techniques if not it is fine if its the first one found
                if groups.get("step3") and len(technique_list[technique]["subtechniques"]) > 1:
                    groups["step3"] = [
                        technique_list[technique]["subtechniques"][0].replace(".", "-"),
                        len(technique_list[technique]["subtechniques"]),
                    ]
                elif not groups.get("step3"):
                    groups["step3"] = [
                        technique_list[technique]["subtechniques"][0].replace(".", "-"),
                        len(technique_list[technique]["subtechniques"]),
                    ]

    return groups
