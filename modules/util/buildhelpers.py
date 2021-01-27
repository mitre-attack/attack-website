import argparse
import datetime
import markdown
import json
import re
import collections
import shutil
import string
import math
import os
import uuid
import sys
import bleach
import modules
from modules import site_config
from . import util_config
from . import relationshipgetters

def timestamp():
    """This method is here to return a timestamp"""

    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    return timestamp

def get_created_and_modified_dates(obj):
    """ Given an object, return the modified and created dates """
    
    dates = {}

    if obj.get('created'):
        dates['created'] = format_date(obj['created'])
    if obj.get('modified'):
        dates['modified'] = format_date(obj['modified'])

    return dates

def format_date(date):
    """ Given a date string, format to %d %B %Y """

    if isinstance(date, str):
        date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")

    return ("{} {} {}").format(date.strftime("%d"), date.strftime("%B"), date.strftime("%Y"))

def find_index_id(ext_ref):
    """This method will search for the index of the external_id in the
       external reference list
    """

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
    """Given an object, return attack_id"""

    if object.get('external_references'):
        index = find_index_id(object['external_references'])

        if index != util_config.NOT_FOUND:
            return object['external_references'][index]['external_id']

    return None

def update_reference_list(reference_list, obj):
    """Given a reference list and an object, update the reference list
       with the external references found in the object
    """

    if obj.get('external_references'):

        # Add external reference to reference list if not found
        for ext_ref in obj['external_references']:

            # Only add if reference has source name and a description
            if ext_ref.get('source_name') and ext_ref.get("description"):

                # Do not add to reference list if citation is in description 
                if "(Citation:" in ext_ref['description']:
                    continue

                in_list = find_in_reference_list(reference_list, ext_ref['source_name'])

                if not in_list:
                    new_ref = {}

                    new_ref['description'] = ext_ref["description"]
                    if ext_ref.get('url'):
                        new_ref['url'] = ext_ref['url']
                    new_ref['number'] = None

                    reference_list[ext_ref['source_name']] = new_ref
    
    return reference_list

def get_alias_data(alias_list, ext_refs):
    """This function generates the Alias Description section for the pages"""

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
                row['name'] = alias
                row['descr'] = ext['description']
                alias_data.append(row)
        
    return alias_data

def get_subtechnique_count(technique_list_no_sub):
    """Given a technique list, return the number of subtechniques"""

    subtech_count = 0

    subtechniques_of = relationshipgetters.get_subtechniques_of()

    for technique in technique_list_no_sub:

        if technique["id"] in subtechniques_of:
            subtechniques = subtechniques_of[technique["id"]]
            subtech_count += len(subtechniques)
    
    return subtech_count

def get_technique_table_data(tactic, techniques_list):
    """Generate techniques table for tactics pages and techniques
       domain pages
    """

    technique_table = []
    subtechniques_of = relationshipgetters.get_subtechniques_of()

    for tech in techniques_list:

        attack_id = get_attack_id(tech)

        if attack_id:

            row = {}
            row['tid'] = attack_id

            row['descr'] = tech['description']

            if tactic is None and tech.get('x_mitre_deprecated'):
                row['deprecated'] = True

            row['technique_name'] = tech['name']

            # Get sub-techniques if available
            row['subtechniques'] = []
            if tech["id"] in subtechniques_of:
                subtechniques = subtechniques_of[tech["id"]]
                for subtechnique in subtechniques:
                    sub_data = {}
                    sub_data['name'] = subtechnique['object']['name']
                    sub_attack_id = get_attack_id(subtechnique['object'])
                    if not "." in sub_attack_id:
                        raise Exception(f"{attack_id} subtechnique's attackID '{sub_attack_id}' is malformed")
                    sub_data['id'] = sub_attack_id.split(".")[1]
                    sub_data['descr'] = subtechnique['object']['description']
                    row['subtechniques'].append(sub_data)

            technique_table.append(row)
    
    # Sort by technique name
    technique_table = sorted(technique_table, key=lambda k: k['technique_name'].lower())

    # Sort sub-techniques by name
    for technique in technique_table:
        if technique['subtechniques']:
            # Sort by technique name
            technique['subtechniques'] = sorted(technique['subtechniques'], key=lambda k: k['id'].lower())

    return technique_table

def get_side_nav_domains_data(side_nav_title, elements_list):
    """Responsible for generating the links that are located on the
       left side of pages for desktop clients
    """

    def get_element_data(element):
        return {
            "name": element['name'],
            "id": element['name'],
            "path": "/{}/{}/".format(side_nav_title, attack_id),
            "children": []
        }

    elements_data = []

    for domain in site_config.domains:
        if elements_list[domain]:
            # Get alias for domain
            domain_alias = get_domain_alias(domain.split("-")[0])

            domain_data = {
                "name": domain_alias,
                "id": domain.split("-")[0],
                "path": "/{}/{}/".format(side_nav_title, domain.split("-")[0]),
                "children": []
            }

            for element in elements_list[domain]:
                attack_id = get_attack_id(element)
                if attack_id:
                    domain_data['children'].append(get_element_data(element))
            
            elements_data.append(domain_data)

    # return side menu
    return {
        "name": side_nav_title,
        "id": side_nav_title,
        "path": None, # root level doesn't get a path
        "children": elements_data
    }  

def get_side_nav_domains_mobile_view_data(side_nav_title, elements_list, amount_per_row):
    """ Given a title, an elements list and the amount of elements per row,
        get the data for the side navigation on a mobile view.
    """

    def get_element_data(element):
        """ Given an element, return the formatted JSON """
        
        return {
            "name": element['name'],
            "id": uuid.uuid4().hex,
            "path": "/{}/{}/".format(side_nav_title, attack_id),
            "children": []
        }
    
    def check_children(category_list, domain_list):
        """ Given a category list, check if there is no children and update list.
            Ignore if is digits or other.
        """

        for cat in category_list:
            if not cat['children']:
                if cat['name'].startswith("1"):
                    continue
                elif cat['name'].startswith("Other"):
                    continue
                else:
                    # Add empty child
                    child = {
                        "name" : "No {}".format(side_nav_title),
                        'id' : "empty",
                        "path" : None,
                        "children" : []
                    }
                    cat['children'].append(child)
            domain_data['children'].append(cat)
        
        return domain_data
    
    def get_category_list():
        """ Get an empty category list """

        caterogories_content = []
        for cat in categories:
            pane = {
                "name" : cat,
                "id" : uuid.uuid4().hex,
                "path" : None,
                "children" : []
            }
            caterogories_content.append(pane)
        
        return caterogories_content

    categories_map = {char: math.ceil((i+1)/amount_per_row) for i,char in enumerate(string.ascii_uppercase)}
    categories = list(map(lambda cat: cat[0] + "-" + cat[-1], \
                      [string.ascii_uppercase[i:i+amount_per_row] \
                          for i in range(0, len(string.ascii_uppercase), \
                              amount_per_row)]))
    categories = ["1-9"] + categories + ["Other"]

    elements_data = []

    for domain in site_config.domains:

        if elements_list[domain]:

            caterogy_list = get_category_list()

            # Get alias for domain
            domain_alias = get_domain_alias(domain.split("-")[0])

            domain_data = {
                "name": domain_alias,
                "id": domain_alias,
                "path": "/{}/{}/".format(side_nav_title, domain.split("-")[0]),
                "children": []
            }

            for element in elements_list[domain]:
                attack_id = get_attack_id(element)
                if attack_id:
                        
                    child = get_element_data(element)

                    # Get first character and find in map
                    element_char = element['name'][0]

                    if element_char.isdigit():
                        element_cat_index = 0
                    elif element_char.isalpha():
                        element_cat_index = categories_map[element_char.upper()]
                    else:
                        element_cat_index = len(categories) - 1

                    # Add child to pane
                    caterogy_list[element_cat_index]['children'].append(child)
            
            domain_data = check_children(caterogy_list, domain_data)
            
            elements_data.append(domain_data)

    # return side menu
    return {
        "name": side_nav_title,
        "id": side_nav_title,
        "path": None, # root level doesn't get a path
        "children": elements_data
    }

def get_side_menu_data(side_nav_title, path_prefix, elements_list, domain=None):
    """Responsible for generating the links that are located on the
       left side of pages for desktop clients
    """

    elements_data = []

    for element in elements_list:
        attack_id = get_attack_id(element)

        if attack_id:
            row = {
                "name": element['name'],
                "id": element['name'],
                "path": path_prefix + attack_id + "/",
                "children": []
            }
            elements_data.append(row)

    if domain:
        path_prefix += domain + "/"
    # return side menu
    return {
        "name": side_nav_title,
        "id": side_nav_title,
        "path": path_prefix, # root level doesn't get a path
        "children": elements_data
    }

def get_side_menu_mobile_view_data(side_nav_title, path_prefix, elements_list, amount_per_row, domain=None):
    """Responsible for generating the links that are located on
       the left side of pages for mobile devices
    """

    categories_map = {char: math.ceil((i+1)/amount_per_row) for i,char in enumerate(string.ascii_uppercase)}
    categories = list(map(lambda cat: cat[0] + "-" + cat[-1], \
                      [string.ascii_uppercase[i:i+amount_per_row] \
                          for i in range(0, len(string.ascii_uppercase), \
                              amount_per_row)]))
    categories = ["1-9"] + categories + ["Other"]

    mobile_side_table_data = []

    caterogories_content = []
    for cat in categories:
        pane = {
            "name" : cat,
            "id" : uuid.uuid4().hex,
            "path" : None,
            "children" : []
        }
        caterogories_content.append(pane)

    for element in elements_list:
        # Fill rows for each category
        attack_id = get_attack_id(element)

        if attack_id:
            child = {
                "name": element['name'],
                "id": uuid.uuid4().hex,
                "path": path_prefix + attack_id + "/",
                "children": []
            }

            # Get first character and find in map
            element_char = element['name'][0]

            if element_char.isdigit():
                element_cat_index = 0
            elif element_char.isalpha():
                element_cat_index = categories_map[element_char.upper()]
            else:
                element_cat_index = len(categories) - 1

            # Add child to pane
            caterogories_content[element_cat_index]['children'].append(child)

    # Add categories to mobile side navigation
    # Remove "1-9" and "Other" categories if empty
    # Add "No [Type]" to empty object, side_nav_title will hold the type of the page

    for cat in caterogories_content:
        if not cat['children']:
            if cat['name'].startswith("1"):
                continue
            elif cat['name'].startswith("Other"):
                continue
            else:
                # Add empty child
                child = {
                    "name" : "No {}".format(side_nav_title),
                    'id' : "empty",
                    "path" : None,
                    "children" : []
                }
                cat['children'].append(child)
        mobile_side_table_data.append(cat)

    if domain:
        path_prefix += domain + "/"
    # return side menu
    return {
        "name": side_nav_title,
        "id": side_nav_title,
        "path": path_prefix, # root level doesn't get a path
        "children": mobile_side_table_data
    }

def is_tid(tid):
    """Check if input has a tid pattern"""

    pattern = re.compile("^T[0-9][0-9][0-9][0-9]$")
    return pattern.match(tid)

def is_sub_tid(sub_tid):
    """Check if input has a sub-technique id pattern"""

    pattern = re.compile("^T[0-9][0-9][0-9][0-9].[0-9][0-9][0-9]$")
    return pattern.match(sub_tid)

def redirection_subtechnique(sub_tid):
    """ Convert subtechnique id to redirection format """

    return get_parent_technique_id(sub_tid) + "/" + get_sub_technique_id(sub_tid)

def get_parent_technique_id(sub_tid):
    """Given a sub-technique id, return parent"""

    return sub_tid.split(".")[0]

def get_sub_technique_id(sub_tid):
    """Given a sub-technique id, remove parent ID and return"""

    return sub_tid.split(".")[1]

def get_technique_name(tid):
    """ Given a technique id, return the technique name """

    technique_list = relationshipgetters.get_technique_list()

    for technique in technique_list:
        attack_id = get_attack_id(technique)
        if attack_id == tid:
            return technique['name']
    
    return util_config.NOT_FOUND

def technique_used_helper(technique_list, technique, reference_list):
    """ Add technique to technique list and make distinction between techniques
        subtechniques
    """

    attack_id = get_attack_id(technique['object'])
    
    if attack_id:
        # Check if technique not already in technique_list dict
        if attack_id not in technique_list:

            # Check if attack id is a sub-technique
            if is_sub_tid(attack_id):
                parent_id = get_parent_technique_id(attack_id)

                # If parent technique not already in list, add to list and add current sub-technique
                if parent_id not in technique_list:
                    technique_list[parent_id] = {}
                    technique_list[parent_id] = parent_technique_used_helper(parent_id)

                technique_list[parent_id]['subtechniques'].append(get_technique_data_helper(attack_id, technique, reference_list))
            
            # Attack id is regular technique
            else:
                # Add technique to list
                technique_list[attack_id] = {}
                technique_list[attack_id] = get_technique_data_helper(attack_id, technique, reference_list)

        # Check if parent ID was added by sub-technique
        # parent ID will not have description
        elif 'descr' not in technique_list[attack_id]:
            # Check if it has external references
            if technique['relationship'].get('description'):
                # Get filtered description
                technique_list[attack_id]['descr'] = technique['relationship']['description']
                reference_list = update_reference_list(reference_list, technique['relationship'])
    
    return technique_list

def get_technique_data_helper(attack_id, technique, reference_list):
    """ Given an attack id, technique object and reference information, 
        return dictionary with technique data
    """

    technique_data = {}

    technique_to_domain = relationshipgetters.get_technique_to_domain()

    technique_data['domain'] = technique_to_domain[attack_id].split('-')[0]

    if is_sub_tid(attack_id):
        technique_data['id'] = get_sub_technique_id(attack_id)
    else:
        technique_data['id'] = attack_id
    
    technique_data['name'] = technique['object']['name']

    # Check if it has external references
    if technique['relationship'].get('description'):
        # Get filtered description
        technique_data['descr'] = technique['relationship']['description']
        reference_list = update_reference_list(reference_list, technique['relationship'])
    
    technique_data['subtechniques'] = []
    
    return technique_data

def parent_technique_used_helper(parent_id):
    """ Given a parent technique id, add available information for 
        parent
    """

    parent_data = {}

    technique_to_domain = relationshipgetters.get_technique_to_domain()

    parent_data['domain'] = technique_to_domain[parent_id].split('-')[0]
    parent_data['id'] = parent_id
    parent_data['name'] = get_technique_name(parent_id)
    parent_data['subtechniques'] = []

    return parent_data

def find_in_reference_list(reference_list, source_name):
    """Check if it is already in reference list"""

    if reference_list.get(source_name):
        return True

    return False

def get_domain_alias(domain):
    """ Given a domain name, return its alias.
        If not found return the same domain
    """

    for domain_pair in site_config.domain_aliases:
        if domain_pair[1] == domain:
            return domain_pair[0]
    
    return domain

def replace_html_chars(to_be_replaced):
    return to_be_replaced.replace("\n", "")\
                         .replace("{", "{{")\
                         .replace("}", "}}")\
                         .replace("”","\"")\
                         .replace("“","\"")

def get_navigator_layers(name, attack_id, obj_type, version, techniques_used):
    """Given a list of techniques used, return the navigator json objects
       for enterprise and mobile"""

    # Remove minor version from ATT&CK version if any
    major_attack_version = site_config.attack_version.split(".")[0]

    layer_name = f"{name} ({attack_id})"

    enterprise_layer_description = f"Enterprise techniques used by {name}, ATT&CK {obj_type} {attack_id}"
    mobile_layer_description = f"Mobile techniques used by {name}, ATT&CK {obj_type} {attack_id}"

    if (version): # add version number if it exists
        enterprise_layer_description += f" v{version}"
        mobile_layer_description += f" v{version}"

    # Enterprise navigator layer
    enterprise_layer = {}
    enterprise_layer['description'] = enterprise_layer_description
    enterprise_layer['name'] = layer_name
    enterprise_layer['domain'] = "enterprise-attack"
    enterprise_layer['versions'] = {
        "layer": "4.1",
        "attack": major_attack_version,
        "navigator": "4.1"
    }
    enterprise_layer['techniques'] = []
    enterprise_layer["gradient"] = { # white for nonused, blue for used
		"colors": [
			"#ffffff",
			"#66b1ff"
		],
		"minValue": 0,
		"maxValue": 1
	}
    enterprise_layer['legendItems'] = [{
        'label': f'used by {name}',
        'color': "#66b1ff"
    }]

    # Mobile navigator layer
    mobile_layer = {}
    mobile_layer['description'] = mobile_layer_description
    mobile_layer['name'] = layer_name
    mobile_layer['domain'] = "mobile-attack"
    mobile_layer['versions'] = {
        "layer": "4.1",
        "attack": major_attack_version,
        "navigator": "4.1"
    }
    mobile_layer['techniques'] = []
    mobile_layer["gradient"] = { # white for nonused, blue for used
		"colors": [
			"#ffffff",
			"#66b1ff"
		],
		"minValue": 0,
		"maxValue": 1
	}
    mobile_layer['legendItems'] = [{
        'label': f'used by {name}',
        'color': "#66b1ff"
    }]

    # Append techniques to enterprise and mobile layers
    for technique in techniques_used:
        navigator_technique = {}

        # Add parent technique
        if technique.get('descr'):
            score = 1
            if technique.get('subtechniques'):
                navigator_technique = get_navigator_technique(technique['id'], technique["descr"], score, True)
            else:
                navigator_technique = get_navigator_technique(technique['id'], technique["descr"], score, False)
        else:
            if technique.get('subtechniques'):
                navigator_technique = get_navigator_technique(technique['id'], None, None, True)
        
        if navigator_technique:
            if technique['domain'].startswith("enterprise"):
                enterprise_layer['techniques'].append(navigator_technique)
            elif technique['domain'].startswith("mobile"):
                mobile_layer['techniques'].append(navigator_technique) 
        
        # Add subtechniques
        if technique.get('subtechniques'):
            for subtechnique in technique['subtechniques']:
                score = 1
                navigator_technique = get_navigator_technique(technique['id']+"."+subtechnique['id'], subtechnique["descr"], score, True)

                if technique['domain'].startswith("enterprise"):
                    enterprise_layer['techniques'].append(navigator_technique)
                elif technique['domain'].startswith("mobile"):
                    mobile_layer['techniques'].append(navigator_technique)        

    layers = []
    if enterprise_layer["techniques"]:
        layers.append({
            "domain": "enterprise",
            "layer": json.dumps(enterprise_layer)
        })
    if mobile_layer["techniques"]:
        layers.append({
            "domain": "mobile",
            "layer": json.dumps(mobile_layer)
        })
    return layers

def get_navigator_technique(attack_id, description, score, showSub = False):
    """Given an attack id, return it as a dict for the navigator layer"""

    navigator_technique = {}
    if score:
        navigator_technique['score'] = score
    navigator_technique['techniqueID'] = attack_id
    navigator_technique['showSubtechniques'] = showSub
    if description: navigator_technique['comment'] = bleach.clean(description, tags=[], strip=True) #remove html tags
    return navigator_technique

def print_test_output(status, test, message):
    """Standard printing for all tests"""
    if status.startswith("-"):
        sys.stdout.write(f"\r{(status*(util_config.status_space-1)): <{util_config.status_space}} "
                         f"{(test*(util_config.other_column_space-1)): <{util_config.other_column_space}} "
                         f"{(message*(util_config.other_column_space-1)): <{util_config.other_column_space}}\n")
    elif status.startswith("RUNNING"):
        sys.stdout.write(f"\r{status: <{util_config.status_space}} "
                         f"{test: <{util_config.other_column_space}} "
                         f"{message: <{util_config.other_column_space}}")
    else:
        sys.stdout.write(f"\r{status: <{util_config.status_space}} "
                         f"{test: <{util_config.other_column_space}} "
                         f"{message: <{util_config.other_column_space}}\n")

    sys.stdout.flush()

def get_platform_path(platform):
    """Given a platform plath, remove spaces and return
       lower case string"""

    platform_split = platform.split(" ")
    platform_str = ""
    for part in platform_split:
        platform_str += part
    return platform_str.lower()

def add_platform_path(platforms):
    """Given a list of platforms, add the platform path"""

    for platform in platforms:
        platform['path'] = get_platform_path(platform['name'])

    return platforms

def print_start(name):
    """Given a name and a time, display current progress"""

    number_of_hyphens = 40
    name_space = 22

    hyphens = '-' * number_of_hyphens

    sys.stdout.write(f"\r{name: <{name_space}} : {hyphens} Running...")

    sys.stdout.flush()

def print_end(name, start_time, end_time):
    """Given a name and a time, display current progress"""

    number_of_hyphens = 40
    name_space = 22

    hyphens = '-' * number_of_hyphens

    # spaces here because we need to overwrite the word "running"
    sys.stdout.write(f"\r{name: <{name_space}} : {hyphens} {end_time-start_time:.2f}s      \n")

    sys.stdout.flush()

def filter_techniques_by_platform(tech_list, platforms):
    """Given a technique lsit and a platforms list, filter out techniques
       that are not part of the platforms
    """

    if not platforms:
        return tech_list

    filtered_list = []
    # Map to easily find objs and avoid duplicates
    ids_for_duplicates = {}
    for obj in tech_list:
        # Do not try to find if it's already on the filtered list
        if not ids_for_duplicates.get(obj['id']):
            for platform in platforms:
                if platform in obj["x_mitre_platforms"]:
                    ids_for_duplicates[obj['id']] = True
                    filtered_list.append(obj)
                    break

    return filtered_list

def filter_deprecated_revoked(sdos):
    return list(filter(lambda t: not ( ("x_mitre_deprecated" in t and t["x_mitre_deprecated"]) or ("revoked" in t and t["revoked"]) ) ,sdos))

def filter_out_subtechniques(techniques):
    return list(filter(lambda t: not ("x_mitre_is_subtechnique" in t and t["x_mitre_is_subtechnique"]), techniques))

def filter_out_techniques_without_subtechniques(techniques):
    return list(filter(lambda t: ("x_mitre_is_subtechnique" in t and t["x_mitre_is_subtechnique"]), techniques))

def get_side_menu_matrices(children):
    """Given a matrix structure, return stripped structure
       with only names
    """

    def children_helper(matrix, path_prefix):
        children = matrix["subtypes"]
        if matrix["type"] == "local":
            return {
                "name": matrix["name"],
                "id": matrix["name"].split("-")[0].split(" ")[0].lower(),
                "path": path_prefix + matrix["path"] + "/", # parents don't have links
                "children": list(map(lambda child: children_helper(child, path_prefix), children))
            }
        elif matrix["type"] == "external":
            return {
                "name": matrix["name"],
                "external": True,
                "id": matrix["name"].split("-")[0].split(" ")[0].lower(),
                "path": matrix["path"],  # external links don't get prefixes
                "children": list(map(lambda child: children_helper(child, path_prefix), children))
            }

    return {
        "name": "matrices",
        "path": None, # root level doesn't get a path
        "children": list(map(lambda child: children_helper(child, "/matrices/"), children))
    }

def get_subtype_data(matrix, inside, name):
    """Recursively get subtype data"""

    if not inside.get('subtypes'):
        inside['subtypes'] = []

    subinside = {}
    subinside['name'] = matrix['name']
    subinside['path'] = matrix['path']

    for subtype in matrix['subtypes']:
        get_subtype_data(subtype, subinside, matrix['name'])

    inside['subtypes'].append(subinside)

def remove_module_from_menu(module_to_be_removed):
    """ Given a list of results, remove elements from menu if their result was False """

    for module in modules.menu_ptr:
        if module['name'] == module_to_be_removed:
            modules.menu_ptr.remove(module)
            return

def remove_element_from_sub_menu(selected_module, element):
    """ Given a sub menu item and a module, removes element from sub menu """

    def remove_from_sub_menu_list(module):
        if module.get('children'):
            for child in module['children']:
                if child['name'] == element:
                    module['children'].remove(child)
                    return

    for module in modules.menu_ptr:
        if module['name'] == selected_module:
            remove_from_sub_menu_list(module)

def get_matrix_data(techniques):
    """Given a technique list, returns the a dictionary of techniques data
       under different 'phase_name', also known as tactics.
    """
    matrix = {}
    for technique in techniques:
        if ('revoked' not in technique or technique['revoked'] is False) and ('x_mitre_deprecated' not in technique or technique['x_mitre_deprecated'] is False):
            # Get attack id
            attack_id = get_attack_id(technique)
            
            if attack_id:
                row = {}
                row['attack_id'] = attack_id
                row['name'] = technique['name']
                        
                if technique.get('kill_chain_phases'):
                    for elem in technique['kill_chain_phases']:
                        if elem['phase_name'] not in matrix:
                            matrix[elem['phase_name']] = []
                        matrix[elem['phase_name']].append(row)
    return matrix

def get_max_length(matrix, tactics):
    """Given a matrix and a tactics list, returns the maximum column size"""

    max_len = 0
    for tactic in tactics:
        if matrix.get(tactic['x_mitre_shortname']):
            if len(matrix[tactic['x_mitre_shortname']]) > max_len:
                max_len = len(matrix[tactic['x_mitre_shortname']])
    return max_len

def get_tactics_data(tactics):
    """Given a tactics list, returns a tactics dictionary with the name and
       id of each tactic
    """

    tactics_data = {}
    for tactic in tactics:
        attack_id = get_attack_id(tactic)

        if attack_id:
            tactic_dict = {}
            tactic_dict['name'] = tactic['name']
            tactic_dict['id'] = attack_id
            tactics_data[tactic['x_mitre_shortname']] = tactic_dict
    
    return tactics_data

def generate_redirections(redirections_filename):
    """ Given redirections filename, open and create markdown file
        for redirections
    """

    with open(redirections_filename, "r", encoding="utf8") as json_redirections:
        redirects = json.load(json_redirections)
    
    if redirects:

        # Verify if redirection directory exists
        if not os.path.isdir(site_config.redirects_markdown_path):
            os.mkdir(site_config.redirects_markdown_path)

        for obj in redirects:

            if not obj["from"].endswith("/index.html"):
                obj["from"] += "/index.html"

            subs = site_config.redirect_md.substitute(obj)

            with open(os.path.join(site_config.redirects_markdown_path, obj['title'] + ".md"), "w", encoding='utf8') as md_file:
                md_file.write(subs)

def create_content_pages_dir():
    """ Create content pages directory if it does not exist """

    if not os.path.exists(site_config.content_dir):
        os.mkdir(site_config.content_dir)
    # Check that docs directory exist
    if not os.path.exists(site_config.pages_dir):
        os.mkdir(site_config.pages_dir)

def move_templates(module_name, module_template_path):
    """ Move module specific templates into the website's main template directory holder """

    if os.path.isdir(module_template_path):

        # New template directory for module 
        new_template_dir = os.path.join(site_config.templates_directory, module_name.lower()) 

        # Create directory in main template directory if does not exist for module
        if not os.path.exists(new_template_dir):
            os.mkdir(new_template_dir)

        for template in os.listdir(module_template_path):
            # Copy template to new directory
            shutil.copyfile(os.path.join(module_template_path,template), os.path.join(new_template_dir, template))

def move_docs(module_docs_path):
    """ Move module specific docs into the website's content directory for pelican """

    if os.path.isdir(module_docs_path):
        # Check that content directory exist
        if not os.path.exists(site_config.content_dir):
            os.mkdir(site_config.content_dir)
        # Check that docs directory exist
        if not os.path.exists(site_config.docs_dir):
            os.mkdir(site_config.docs_dir)
        
        for doc in os.listdir(module_docs_path):
            if os.path.isdir(os.path.join(module_docs_path, doc)):
                shutil.copytree(os.path.join(module_docs_path,doc), os.path.join(site_config.docs_dir, doc))
            else:
                shutil.copyfile(os.path.join(module_docs_path,doc), os.path.join(site_config.docs_dir, doc))