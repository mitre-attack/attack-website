import datetime
import json
import math
import os
import re
import shutil
import string
import sys
import uuid

import bleach
from loguru import logger

import modules
from modules import site_config

from . import relationshipgetters, util_config


def timestamp():
    """This method is here to return a timestamp."""
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    return timestamp


def get_created_and_modified_dates(obj):
    """Given an object, return the modified and created dates."""
    dates = {}

    if obj.get("created"):
        dates["created"] = format_date(obj["created"])
    if obj.get("modified"):
        dates["modified"] = format_date(obj["modified"])

    return dates


def format_date(date):
    """Given a date string, format to %d %B %Y."""
    if isinstance(date, str):
        date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")

    return ("{} {} {}").format(date.strftime("%d"), date.strftime("%B"), date.strftime("%Y"))


def get_first_last_seen_dates(obj):
    """Given an object, return the first_seen and last_seen dates."""
    dates = {}

    if obj.get("first_seen"):
        dates["first_seen"] = format_date_as_month_year(obj["first_seen"])
    if obj.get("last_seen"):
        dates["last_seen"] = format_date_as_month_year(obj["last_seen"])

    return dates


def get_first_last_seen_citations(obj):
    """Given an object, return the first seen and last seen citations. This function generates
    the descriptions/citations for the first/last seen fields."""
    data = {}
    if obj.get("x_mitre_first_seen_citation"):
        data["first_seen_citation"] = obj.get("x_mitre_first_seen_citation")
    if obj.get("x_mitre_last_seen_citation"):
        data["last_seen_citation"] = obj.get("x_mitre_last_seen_citation")
    return data


def format_date_as_month_year(date):
    """Given a date string, format to %B %Y."""
    if isinstance(date, str):
        date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")

    return ("{} {}").format(date.strftime("%B"), date.strftime("%Y"))


def find_index_id(ext_ref):
    """This method will search for the index of the external_id in the external reference list."""
    count = 0
    flag = True
    while count < len(ext_ref) and flag:
        if ext_ref[count].get("external_id") and ext_ref[count]["source_name"] in site_config.source_names:
            flag = False
        else:
            count = count + 1
    if flag:
        return -1
    return count


def get_attack_id(object):
    """Given an object, return attack_id."""
    external_references = object.get("external_references")
    if external_references:
        index = find_index_id(external_references)

        if index != util_config.NOT_FOUND:
            return external_references[index]["external_id"]

    return None


def update_reference_list(reference_list, obj):
    """Given a reference list and an object, update the reference list with the external references found in the object."""
    if obj.get("external_references"):
        # Add external reference to reference list if not found
        for ext_ref in obj["external_references"]:
            # Only add if reference has source name and a description
            if ext_ref.get("source_name") and ext_ref.get("description"):
                # Do not add to reference list if citation is in description
                if "(Citation:" in ext_ref["description"]:
                    continue

                in_list = find_in_reference_list(reference_list, ext_ref["source_name"])

                if not in_list:
                    new_ref = {}

                    new_ref["description"] = ext_ref["description"]
                    if ext_ref.get("url"):
                        new_ref["url"] = ext_ref["url"]
                    new_ref["number"] = None

                    reference_list[ext_ref["source_name"]] = new_ref

    return reference_list


def get_reference_set(reflist):
    """This function retrieves the unique set of references in the given list of descriptions and
    returns them in string format to be displayed as citations."""
    p = re.compile("\(Citation: (.*?)\)")
    citations = {}
    for c in reflist:
        citations_in_ref = p.findall(c)
        for citation in citations_in_ref:
            if citation not in citations:
                citations[citation] = True
    refs = [f"(Citation: {c})" for c in citations]
    return "".join(refs)


def get_alias_data(alias_list, ext_refs):
    """This function generates the Alias Description section for the pages."""
    if not alias_list:
        return []

    alias_data = []

    # Look through the list of aliases to find a match to the external
    # references. Then, create a list of all the mapped aliases
    for alias in alias_list:
        # Returns a list of external references that match the sourcename,
        # we only need one though
        found_ext_refs = [x for x in ext_refs if x["source_name"] == alias]
        if found_ext_refs:
            ext = found_ext_refs[0]

            if ext.get("description"):
                row = {}
                row["name"] = alias
                row["descr"] = ext["description"]
                alias_data.append(row)

    return alias_data


def is_deprecated(sdo):
    """Given a STIX Domain Object, return if it is deprecated."""
    deprecated = sdo.get("x_mitre_deprecated")
    return deprecated


def is_revoked(sdo):
    """Given a STIX Domain Object, return if it is revoked."""
    revoked = sdo.get("revoked")
    return revoked


def get_subtechnique_count(technique_list_no_sub):
    """Given a technique list, return the number of subtechniques."""
    subtech_count = 0
    subtechniques_of = relationshipgetters.get_subtechniques_of()

    for technique in technique_list_no_sub:
        if technique["id"] in subtechniques_of:
            subtechniques = subtechniques_of[technique["id"]]

            for sub in subtechniques:
                revoked = is_revoked(sdo=sub["object"])
                deprecated = is_deprecated(sdo=sub["object"])
                if revoked or deprecated:
                    continue
                subtech_count += 1

    return subtech_count


def get_technique_table_data(tactic, techniques_list):
    """Generate techniques table for tactics pages and techniques domain pages."""
    technique_table = []
    subtechniques_of = relationshipgetters.get_subtechniques_of()

    for tech in techniques_list:
        attack_id = get_attack_id(tech)

        if attack_id:
            row = {}
            row["tid"] = attack_id
            row["descr"] = tech["description"]

            if tactic is None and tech.get("x_mitre_deprecated"):
                row["deprecated"] = True

            row["technique_name"] = tech["name"]

            # Get sub-techniques if available
            row["subtechniques"] = []
            if tech["id"] in subtechniques_of:
                subtechniques = subtechniques_of[tech["id"]]
                for subtechnique in subtechniques:
                    sub_data = {}
                    sub_data["name"] = subtechnique["object"]["name"]
                    sub_attack_id = get_attack_id(subtechnique["object"])
                    if sub_attack_id:
                        if not "." in sub_attack_id:
                            raise Exception(f"{attack_id} subtechnique's attackID '{sub_attack_id}' is malformed")
                        sub_data["id"] = sub_attack_id.split(".")[1]
                        sub_data["descr"] = subtechnique["object"]["description"]

                        revoked = is_revoked(sdo=subtechnique["object"])
                        deprecated = is_deprecated(sdo=subtechnique["object"])
                        if revoked or deprecated:
                            continue

                        row["subtechniques"].append(sub_data)

            technique_table.append(row)

    # Sort by technique name
    technique_table = sorted(technique_table, key=lambda k: k["technique_name"].lower())

    # Sort sub-techniques by name
    for technique in technique_table:
        if technique["subtechniques"]:
            # Sort by technique name
            technique["subtechniques"] = sorted(technique["subtechniques"], key=lambda k: k["id"].lower())

    return technique_table


def get_side_nav_domains_data(side_nav_title, elements_list):
    """Responsible for generating the links that are located on the left side of pages for desktop clients."""

    def get_element_data(element):
        return {
            "name": element["name"],
            "id": element["name"],
            "path": "/{}/{}/".format(side_nav_title, attack_id),
            "children": [],
        }

    elements_data = []

    for domain in site_config.domains:
        if domain["deprecated"]:
            continue
        if elements_list[domain["name"]]:
            domain_data = {
                "name": domain["alias"],
                "id": domain["name"].split("-")[0],
                "path": "/{}/{}/".format(side_nav_title, domain["name"].split("-")[0]),
                "children": [],
            }

            for element in elements_list[domain["name"]]:
                attack_id = get_attack_id(element)
                if attack_id:
                    domain_data["children"].append(get_element_data(element))

            elements_data.append(domain_data)

    # return side menu
    return {
        "name": side_nav_title,
        "id": side_nav_title,
        "path": None,  # root level doesn't get a path
        "children": elements_data,
    }


def get_side_nav_domains_mobile_view_data(side_nav_title, elements_list, amount_per_row):
    """Given a title, an elements list and the amount of elements per row, get the data for the side navigation on a mobile view."""

    def get_element_data(element):
        """Given an element, return the formatted JSON."""
        return {
            "name": element["name"],
            "id": uuid.uuid4().hex,
            "path": "/{}/{}/".format(side_nav_title, attack_id),
            "children": [],
        }

    def check_children(category_list, domain_list):
        """Given a category list, check if there is no children and update list. Ignore if is digits or other."""
        for cat in category_list:
            if not cat["children"]:
                if cat["name"].startswith("1"):
                    continue
                elif cat["name"].startswith("Other"):
                    continue
                else:
                    # Add empty child
                    child = {"name": "No {}".format(side_nav_title), "id": "empty", "path": None, "children": []}
                    cat["children"].append(child)
            domain_data["children"].append(cat)

        return domain_data

    def get_category_list():
        """Get an empty category list."""
        caterogories_content = []
        for cat in categories:
            pane = {"name": cat, "id": uuid.uuid4().hex, "path": None, "children": []}
            caterogories_content.append(pane)

        return caterogories_content

    categories_map = {char: math.ceil((i + 1) / amount_per_row) for i, char in enumerate(string.ascii_uppercase)}
    categories = list(
        map(
            lambda cat: cat[0] + "-" + cat[-1],
            [
                string.ascii_uppercase[i : i + amount_per_row]
                for i in range(0, len(string.ascii_uppercase), amount_per_row)
            ],
        )
    )
    categories = ["1-9"] + categories + ["Other"]

    elements_data = []

    for domain in site_config.domains:
        if domain["deprecated"]:
            continue
        if elements_list[domain["name"]]:
            caterogy_list = get_category_list()

            domain_data = {
                "name": domain["alias"],
                "id": domain["alias"],
                "path": "/{}/{}/".format(side_nav_title, domain["name"].split("-")[0]),
                "children": [],
            }

            for element in elements_list[domain["name"]]:
                attack_id = get_attack_id(element)
                if attack_id:
                    child = get_element_data(element)

                    # Get first character and find in map
                    element_char = element["name"][0]

                    if element_char.isdigit():
                        element_cat_index = 0
                    elif element_char.isalpha():
                        element_cat_index = categories_map[element_char.upper()]
                    else:
                        element_cat_index = len(categories) - 1

                    # Add child to pane
                    caterogy_list[element_cat_index]["children"].append(child)

            domain_data = check_children(caterogy_list, domain_data)

            elements_data.append(domain_data)

    # return side menu
    return {
        "name": side_nav_title,
        "id": side_nav_title,
        "path": None,  # root level doesn't get a path
        "children": elements_data,
    }


def get_side_menu_data(side_nav_title, path_prefix, elements_list, domain=None):
    """Responsible for generating the links that are located on the left side of pages for desktop clients."""

    elements_data = []

    for element in elements_list:
        attack_id = get_attack_id(element)

        if attack_id:
            row = {
                "name": element["name"],
                "id": element["name"],
                "path": path_prefix + attack_id + "/",
                "children": [],
            }
            elements_data.append(row)

    if domain:
        path_prefix += domain + "/"
    # return side menu
    return {
        "name": side_nav_title,
        "id": side_nav_title,
        "path": path_prefix,  # root level doesn't get a path
        "children": elements_data,
    }


def get_side_menu_mobile_view_data(side_nav_title, path_prefix, elements_list, amount_per_row, domain=None):
    """Responsible for generating the links that are located on the left side of pages for mobile devices."""
    categories_map = {char: math.ceil((i + 1) / amount_per_row) for i, char in enumerate(string.ascii_uppercase)}
    categories = list(
        map(
            lambda cat: cat[0] + "-" + cat[-1],
            [
                string.ascii_uppercase[i : i + amount_per_row]
                for i in range(0, len(string.ascii_uppercase), amount_per_row)
            ],
        )
    )
    categories = ["1-9"] + categories + ["Other"]

    mobile_side_table_data = []

    caterogories_content = []
    for cat in categories:
        pane = {"name": cat, "id": uuid.uuid4().hex, "path": None, "children": []}
        caterogories_content.append(pane)

    for element in elements_list:
        # Fill rows for each category
        attack_id = get_attack_id(element)

        if attack_id:
            child = {
                "name": element["name"],
                "id": uuid.uuid4().hex,
                "path": path_prefix + attack_id + "/",
                "children": [],
            }

            # Get first character and find in map
            element_char = element["name"][0]

            if element_char.isdigit():
                element_cat_index = 0
            elif element_char.isalpha():
                element_cat_index = categories_map[element_char.upper()]
            else:
                element_cat_index = len(categories) - 1

            # Add child to pane
            caterogories_content[element_cat_index]["children"].append(child)

    # Add categories to mobile side navigation
    # Remove "1-9" and "Other" categories if empty
    # Add "No [Type]" to empty object, side_nav_title will hold the type of the page

    for cat in caterogories_content:
        if not cat["children"]:
            if cat["name"].startswith("1"):
                continue
            elif cat["name"].startswith("Other"):
                continue
            else:
                # Add empty child
                child = {"name": "No {}".format(side_nav_title), "id": "empty", "path": None, "children": []}
                cat["children"].append(child)
        mobile_side_table_data.append(cat)

    if domain:
        path_prefix += domain + "/"
    # return side menu
    return {
        "name": side_nav_title,
        "id": side_nav_title,
        "path": path_prefix,  # root level doesn't get a path
        "children": mobile_side_table_data,
    }


def is_tid(tid):
    """Check if input has a tid pattern."""
    pattern = re.compile("^T[0-9][0-9][0-9][0-9]$")
    return pattern.match(tid)


def is_sub_tid(sub_tid):
    """Check if input has a sub-technique id pattern."""
    pattern = re.compile("^T[0-9][0-9][0-9][0-9].[0-9][0-9][0-9]$")
    return pattern.match(sub_tid)


def redirection_subtechnique(sub_tid):
    """Convert subtechnique id to redirection format."""
    return get_parent_technique_id(sub_tid) + "/" + get_sub_technique_id(sub_tid)


def get_parent_technique_id(sub_tid):
    """Given a sub-technique id, return parent."""
    return sub_tid.split(".")[0]


def get_sub_technique_id(sub_tid):
    """Given a sub-technique id, remove parent ID and return."""
    return sub_tid.split(".")[1]


def get_technique_name(tid):
    """Given a technique id, return the technique name."""
    technique_list = relationshipgetters.get_technique_list()

    for technique in technique_list:
        attack_id = get_attack_id(technique)
        if attack_id == tid:
            return technique["name"]

    return util_config.NOT_FOUND


def technique_used_helper(technique_list, technique, reference_list, inherited=False):
    """Add technique to technique list and make distinction between techniques subtechniques."""
    attack_id = get_attack_id(technique["object"])

    if attack_id:
        # Check if technique not already in technique_list dict
        # or if the technique was inherited from a relationship (i.e. Group => Campaign => Technique)
        if attack_id not in technique_list or inherited:
            technique_data = get_technique_data_helper(attack_id, technique, reference_list)
            if not technique_data:
                logger.error(f"{attack_id} technique data unavailable, possibly due to domain mismatch")
                return technique_list
            # Check if attack id is a sub-technique
            if is_sub_tid(attack_id):
                parent_id = get_parent_technique_id(attack_id)

                # If parent technique not already in list, add to list
                # Parent technique will be marked as not used until it is seen
                if parent_id not in technique_list:
                    technique_list[parent_id] = {}
                    technique_list[parent_id] = parent_technique_used_helper(parent_id)

                # Check if sub-technique is already in list
                for subtechnique in technique_list[parent_id]["subtechniques"]:
                    # Concatenate the inherited object's description to the existing ID
                    if subtechnique["id"] == technique_data["id"] and inherited:
                        subtechnique["color"] = 3  # belongs both to object and inherited from another
                        if "descr" in technique_data and "descr" in subtechnique:
                            # add markdown newline between descriptions
                            subtechnique["descr"] += "<p>" + technique_data["descr"] + "</p>"
                        elif "descr" in technique_data:
                            subtechnique["descr"] = technique_data["descr"]
                        break
                else:  # sub-technique is not in list
                    # Add subtechnique to list
                    if inherited:
                        technique_data["color"] = 2  # inherited from another object only
                    else:
                        technique_data["color"] = 1  # belongs to object only (not inherited)
                    technique_list[parent_id]["subtechniques"].append(technique_data)

                # Sort subtechniques by name
                technique_list[parent_id]["subtechniques"] = sorted(
                    technique_list[parent_id]["subtechniques"], key=lambda k: k["id"]
                )

            # Attack id is regular technique
            else:
                # Check if technique is already in list (inherited)
                if attack_id in technique_list:
                    technique_list[attack_id]["color"] = 3  # belongs both to object and inherited from another
                    if "descr" in technique_data and "descr" in technique_list[attack_id]:
                        # add markdown newline between descriptions
                        technique_list[attack_id]["descr"] += "<p>" + technique_data["descr"] + "</p>"
                    elif "descr" in technique_data:
                        technique_list[attack_id]["descr"] = technique_data["descr"]
                else:
                    # Add technique to list
                    if inherited:
                        technique_data["color"] = 2  # inherited from another object only
                    else:
                        technique_data["color"] = 1  # belongs to object only (not inherited)
                    technique_list[attack_id] = technique_data

        # Check if parent ID was added by sub-technique
        # parent technique will be marked as not used
        elif technique_list[attack_id]["technique_used"] == False:
            # Include as a technique used
            technique_list[attack_id]["technique_used"] = True

            # Check if it has a description and add references
            if technique["relationship"].get("description"):
                # Get filtered description
                technique_list[attack_id]["descr"] = technique["relationship"]["description"]
                reference_list = update_reference_list(reference_list, technique["relationship"])

    return technique_list


def get_technique_data_helper(attack_id, technique, reference_list):
    """Given an attack id, technique object and reference information, return dictionary with technique data, include as part of technique used."""
    technique_data = {}
    technique_to_domain = relationshipgetters.get_technique_to_domain()
    if attack_id not in technique_to_domain:
        logger.error(f"{attack_id} not in a known domain. check your site_config")
        return {}
    technique_data["technique_used"] = True
    technique_data["domain"] = technique_to_domain[attack_id].split("-")[0]

    if is_sub_tid(attack_id):
        technique_data["id"] = get_sub_technique_id(attack_id)
    else:
        technique_data["id"] = attack_id

    technique_data["name"] = technique["object"]["name"]

    # Check if it has external references
    if technique["relationship"].get("description"):
        # Get filtered description
        technique_data["descr"] = technique["relationship"]["description"]
        reference_list = update_reference_list(reference_list, technique["relationship"])

    technique_data["subtechniques"] = []

    return technique_data


def parent_technique_used_helper(parent_id):
    """Given a parent technique id, add available information for parent."""
    parent_data = {}

    technique_to_domain = relationshipgetters.get_technique_to_domain()

    parent_data["domain"] = technique_to_domain[parent_id].split("-")[0]
    parent_data["id"] = parent_id
    parent_data["name"] = get_technique_name(parent_id)
    parent_data["technique_used"] = False
    parent_data["subtechniques"] = []

    return parent_data


def find_in_reference_list(reference_list, source_name):
    """Check if it is already in reference list."""
    if reference_list.get(source_name):
        return True

    return False


def replace_html_chars(to_be_replaced):
    return to_be_replaced.replace("\n", "").replace("{", "{{").replace("}", "}}").replace("”", '"').replace("“", '"')


colorMap = {
    0: "#ffffff", # techniques not used by the object
    1: "#66b1ff", # techniques used by the object
    2: "#ff6666", # techniques used by inherited campaign relationships
    3: "#ff66f4"  # techniques used by the object AND used by inherited campaign relationships (1 & 2)
}
domain_name_map = {
    "enterprise-attack": "Enterprise",
    "mobile-attack": "Mobile",
    "ics-attack": "ICS"
}


def get_navigator_layers(name, attack_id, obj_type, version, techniques_used, inheritance=False):
    """Generate the Enterprise, Mobile, and ICS Navigator JSON layers for the given object."""

    # Generate Enterprise base layer
    enterprise_layer = build_base_layer("enterprise-attack", name, obj_type, attack_id, version, inheritance)

    # Generate Mobile base layer
    mobile_layer = build_base_layer("mobile-attack", name, obj_type, attack_id, version, inheritance)

    # Generate ICS base layer
    ics_layer = build_base_layer("ics-attack", name, obj_type, attack_id, version, inheritance)

    # Add technique data to layer
    for technique in techniques_used:
        # Generate the navigator technique layer object
        description = technique["descr"] if technique.get("descr") else None
        color = technique["color"] if technique.get("color") else 0
        has_subtechniques = True if technique.get("subtechniques") else False
        score = 1 if technique.get("descr") else 0
        technique_layer_object = get_technique_layer_object(technique["id"], description, score, color, has_subtechniques)

        # Skip this technique if no layer object
        if not technique_layer_object: continue

        # Add technique layer object to domain layer
        if "enterprise" in technique["domain"]:
            enterprise_layer["techniques"].append(technique_layer_object)
        if "mobile" in technique["domain"]:
            mobile_layer["techniques"].append(technique_layer_object)
        if "ics" in technique["domain"]:
            ics_layer["techniques"].append(technique_layer_object)

        # Add subtechnique data to layer
        if has_subtechniques:
            score = 1
            for subtechnique in technique["subtechniques"]:
                # Generate the navigator (sub)technique layer object
                sub_id = f"{technique['id']}.{subtechnique['id']}"
                sub_descr = subtechnique["descr"] if subtechnique.get("descr") else None
                sub_color = subtechnique["color"] if subtechnique.get("color") else 0
                subtechnique_layer_object = get_technique_layer_object(sub_id, sub_descr, score, sub_color, True)

                # Add (sub)technique layer object to domain layer
                if "enterprise" in technique["domain"]:
                    enterprise_layer["techniques"].append(subtechnique_layer_object)
                if "mobile" in technique["domain"]:
                    mobile_layer["techniques"].append(subtechnique_layer_object)
                if "ics" in technique["domain"]:
                    ics_layer["techniques"].append(subtechnique_layer_object)

    # Build list of domains with navigator layers
    layers = []
    if enterprise_layer["techniques"]:
        layers.append({
            "domain": "enterprise",
            "name": domain_name_map["enterprise-attack"],
            "filename": f"{attack_id}-enterprise-layer.json",
            "layer": json.dumps(enterprise_layer)
        })
    if mobile_layer["techniques"]:
        layers.append({
            "domain": "mobile",
            "name": domain_name_map["mobile-attack"],
            "filename": f"{attack_id}-mobile-layer.json",
            "layer": json.dumps(mobile_layer)
        })
    if ics_layer["techniques"]:
        layers.append({
            "domain": "ics",
            "name": domain_name_map["ics-attack"],
            "filename": f"{attack_id}-ics-layer.json",
            "layer": json.dumps(ics_layer)
        })

    return layers


def build_base_layer(domain, object_name, object_type, attack_id, version, inheritance=False):
    """Build the base Navigator layer for the given object."""
    layer = {}

    # Layer description
    layer["description"] = f"{domain_name_map[domain]} techniques used by {object_name}, ATT&CK {object_type} {attack_id}"
    if version:
        # Add object version number if it exists
        layer["description"] += f" (v{version})"

    # Layer name and domain
    layer["name"] = f"{object_name} ({attack_id})"
    layer["domain"] = domain

    # Layer versions (layer/attack/navigator)
    major_attack_version = site_config.attack_version.split(".")[0]
    layer_version = site_config.layer_version
    navigator_version = site_config.navigator_version
    layer["versions"] = {"layer": layer_version, "attack": major_attack_version, "navigator": navigator_version}

    # Layer techniques list
    layer["techniques"] = []

    # Layer gradient (white for un-used, blue for used)
    layer["gradient"] = {
        "colors": [colorMap[0], colorMap[1]],
        "minValue": 0,
        "maxValue": 1,
    }

    # Layer legend
    layer["legendItems"] = [
        {"label": f"used by {object_name}", "color": colorMap[1]}
    ]

    # Add campaign inheritance to legend, if applicable
    if inheritance:
        layer["legendItems"].extend([
            {"label": f"used by a campaign attributed to {object_name}", "color": colorMap[2]},
            {"label": f"used by {object_name} and used by a campaign attributed to {object_name}", "color": colorMap[3]}
        ])

    return layer


def get_technique_layer_object(attack_id, description, score, color, showSub=False):
    """Generate the Navigator technique layer object for the given technique."""
    navigator_technique = {}

    # technique ID
    navigator_technique["techniqueID"] = attack_id

    # technique description
    if description:
        navigator_technique["comment"] = bleach.clean(description, tags=[], strip=True)  # remove html tags

    # optional technique score/color
    if score:
        navigator_technique["score"] = score
    if color and color in colorMap.keys():
        navigator_technique["color"] = colorMap[color]
    
    # show subtechniques?
    navigator_technique["showSubtechniques"] = showSub

    return navigator_technique


def get_platform_path(platform):
    """Given a platform plath, remove spaces and return lower case string."""
    platform_split = platform.split(" ")
    platform_str = ""
    for part in platform_split:
        platform_str += part
    return platform_str.lower()


def add_platform_path(platforms):
    """Given a list of platforms, add the platform path."""
    for platform in platforms:
        platform["path"] = get_platform_path(platform["name"])

    return platforms


def print_start(name):
    """Given a name and a time, display current progress."""
    number_of_hyphens = 40
    name_space = 22

    hyphens = "-" * number_of_hyphens

    sys.stdout.write(f"\r{name: <{name_space}} : {hyphens} Running...")

    sys.stdout.flush()


def print_end(name, start_time, end_time):
    """Given a name and a time, display current progress."""
    number_of_hyphens = 40
    name_space = 22

    hyphens = "-" * number_of_hyphens

    # spaces here because we need to overwrite the word "running"
    sys.stdout.write(f"\r{name: <{name_space}} : {hyphens} {end_time-start_time:.2f}s      \n")

    sys.stdout.flush()


def filter_techniques_by_platform(tech_list, platforms):
    """Given a technique list and a platforms list, filter out techniques that are not part of the platforms."""
    if not platforms:
        return tech_list

    filtered_list = []
    # Map to easily find objs and avoid duplicates
    ids_for_duplicates = {}
    for obj in tech_list:
        # Do not try to find if it's already on the filtered list
        if not ids_for_duplicates.get(obj["id"]):
            for platform in platforms:
                if obj.get("x_mitre_platforms"):
                    if platform in obj["x_mitre_platforms"]:
                        ids_for_duplicates[obj["id"]] = True
                        filtered_list.append(obj)
                        break

    return filtered_list


def filter_deprecated_revoked(sdos):
    filtered_sdos = []
    for sdo in sdos:
        deprecated = is_deprecated(sdo=sdo)
        revoked = is_revoked(sdo=sdo)
        if not deprecated or revoked:
            filtered_sdos.append(sdo)

    return filtered_sdos


def filter_out_subtechniques(techniques):
    return list(filter(lambda t: not ("x_mitre_is_subtechnique" in t and t["x_mitre_is_subtechnique"]), techniques))


def filter_out_techniques_without_subtechniques(techniques):
    return list(filter(lambda t: ("x_mitre_is_subtechnique" in t and t["x_mitre_is_subtechnique"]), techniques))


def get_side_menu_matrices(children):
    """Given a matrix structure, return stripped structure with only names."""

    def children_helper(matrix, path_prefix):
        children = matrix["subtypes"]
        if matrix["type"] == "local":
            return {
                "name": matrix["name"],
                "id": matrix["name"].split("-")[0].split(" ")[0].lower(),
                "path": path_prefix + matrix["path"] + "/",  # parents don't have links
                "children": list(map(lambda child: children_helper(child, path_prefix), children)),
            }
        elif matrix["type"] == "external":
            return {
                "name": matrix["name"],
                "external": True,
                "id": matrix["name"].split("-")[0].split(" ")[0].lower(),
                "path": matrix["path"],  # external links don't get prefixes
                "children": list(map(lambda child: children_helper(child, path_prefix), children)),
            }

    return {
        "name": "matrices",
        "path": None,  # root level doesn't get a path
        "children": list(map(lambda child: children_helper(child, "/matrices/"), children)),
    }


def get_subtype_data(matrix, inside, name):
    """Recursively get subtype data."""
    if not inside.get("subtypes"):
        inside["subtypes"] = []

    subinside = {}
    subinside["name"] = matrix["name"]
    subinside["path"] = matrix["path"]

    for subtype in matrix["subtypes"]:
        get_subtype_data(subtype, subinside, matrix["name"])

    inside["subtypes"].append(subinside)


def remove_module_from_menu(module_to_be_removed):
    """Given a list of results, remove elements from menu if their result was False."""
    for module in modules.menu_ptr:
        if module["module_name"] == module_to_be_removed:
            modules.menu_ptr.remove(module)
            return


def remove_element_from_sub_menu(selected_module, element):
    """Given a sub menu item and a module, removes element from sub menu."""

    def remove_from_sub_menu_list(module):
        if module.get("children"):
            for child in module["children"]:
                if child.get("display_name") == element:
                    module["children"].remove(child)
                    return

    for module in modules.menu_ptr:
        if module["module_name"] == selected_module:
            remove_from_sub_menu_list(module)


def get_matrix_data(techniques):
    """Given a technique list, returns the a dictionary of techniques data under different 'phase_name', also known as tactics."""
    matrix = {}
    for technique in techniques:
        if ("revoked" not in technique or technique["revoked"] is False) and (
            "x_mitre_deprecated" not in technique or technique["x_mitre_deprecated"] is False
        ):
            # Get attack id
            attack_id = get_attack_id(technique)

            if attack_id:
                row = {}
                row["attack_id"] = attack_id
                row["name"] = technique["name"]

                if technique.get("kill_chain_phases"):
                    for elem in technique["kill_chain_phases"]:
                        if elem["phase_name"] not in matrix:
                            matrix[elem["phase_name"]] = []
                        matrix[elem["phase_name"]].append(row)
    return matrix


def get_max_length(matrix, tactics):
    """Given a matrix and a tactics list, returns the maximum column size."""
    max_len = 0
    for tactic in tactics:
        if matrix.get(tactic["x_mitre_shortname"]):
            if len(matrix[tactic["x_mitre_shortname"]]) > max_len:
                max_len = len(matrix[tactic["x_mitre_shortname"]])
    return max_len


def get_tactics_data(tactics):
    """Given a tactics list, returns a tactics dictionary with the name and id of each tactic."""
    tactics_data = {}
    for tactic in tactics:
        attack_id = get_attack_id(tactic)

        if attack_id:
            tactic_dict = {}
            tactic_dict["name"] = tactic["name"]
            tactic_dict["id"] = attack_id
            tactics_data[tactic["x_mitre_shortname"]] = tactic_dict

    return tactics_data


def generate_redirections(redirections_filename, redirect_md=None):
    """Given redirections filename, open and create markdown file for redirections."""
    with open(redirections_filename, "r", encoding="utf8") as json_redirections:
        redirects = json.load(json_redirections)

    if redirects:
        # Verify if redirection directory exists
        if not os.path.isdir(site_config.redirects_markdown_path):
            os.mkdir(site_config.redirects_markdown_path)

        for obj in redirects:
            subs = redirect_md.substitute(obj)

            redirect_md_file = os.path.join(site_config.redirects_markdown_path, f"{obj['title']}.md")
            with open(redirect_md_file, "w", encoding="utf8") as md_file:
                md_file.write(subs)


def create_content_pages_dir():
    """Create content pages directory if it does not exist."""
    if not os.path.exists(site_config.content_dir):
        os.mkdir(site_config.content_dir)
    # Check that docs directory exist
    if not os.path.exists(site_config.pages_dir):
        os.mkdir(site_config.pages_dir)


def move_templates(module_name, module_template_path):
    """Move module specific templates into the website's main template directory holder."""
    if os.path.isdir(module_template_path):
        # New template directory for module
        new_template_dir = os.path.join(site_config.templates_directory, module_name.lower())

        # Create directory in main template directory if does not exist for module
        if not os.path.exists(new_template_dir):
            os.mkdir(new_template_dir)

        for template in os.listdir(module_template_path):
            # Copy template to new directory
            shutil.copyfile(os.path.join(module_template_path, template), os.path.join(new_template_dir, template))
