import argparse
import datetime
import markdown
import json
import re
import collections
import stix2
import string
import math
import uuid
import sys
import bleach
from modules import site_config
from . import stixhelpers
from . import relationshiphelpers as rsh
from . import util_config

malware_used_by_groups = {}
tools_used_by_groups = {}
techniques_used_by_malware = {}
techniques_used_by_tools = {}
techniques_used_by_groups = {}
groups_using_tool = {}
groups_using_malware = {}
mitigation_mitigates_techniques = {}
technique_mitigated_by_mitigation = {}
technique_related_to_technique = {}
tools_using_technique = {}
malware_using_technique = {}
groups_using_technique = {}
ms = {}
resources = {}
relationships = []
group_list = []
software_list = []
technique_list = []
mitigation_list = []
technique_to_domain = {}

# Relationship getters

def get_malware_used_by_groups():
    """ malware used by groups getter """

    if malware_used_by_groups:
        return malware_used_by_groups
    else:
        return rsh.malware_used_by_groups(site_config.srcs)

def get_tools_used_by_groups():
    """ tools used by groups getter """

    if tools_used_by_groups:
        return tools_used_by_groups
    else:
        return rsh.tools_used_by_groups(site_config.srcs)

def get_techniques_used_by_malware():
    """ techniques used by malware getter """

    if techniques_used_by_malware:
        return techniques_used_by_malware
    else:
        return rsh.techniques_used_by_malware(site_config.srcs)

def get_techniques_used_by_tools():
    """ techniques used by tools getter """

    if techniques_used_by_tools:
        return techniques_used_by_tools
    else:
        return rsh.techniques_used_by_tools(site_config.srcs)

def get_techniques_used_by_groups():
    """ techniques used by groups getter """

    if techniques_used_by_groups:
        return techniques_used_by_groups
    else:
        return rsh.techniques_used_by_groups(site_config.srcs)

def get_groups_using_tool():
    """ groups using tool getter """

    if groups_using_tool:
        return groups_using_tool
    else:
        return rsh.groups_using_tool(site_config.srcs)

def get_groups_using_malware():
    """ groups using malware getter """

    if groups_using_malware:
        return groups_using_malware
    else:
        return rsh.groups_using_malware(site_config.srcs)
        
def get_mitigation_mitigates_techniques():
    """ mitigation migates techniques getter """

    if mitigation_mitigates_techniques:
        return mitigation_mitigates_techniques
    else:
        return rsh.mitigation_mitigates_techniques(site_config.srcs)

def get_technique_mitigated_by_mitigation():
    """ technique mitigated by mitigation getter """

    if technique_mitigated_by_mitigation:
        return technique_mitigated_by_mitigation
    else:
        return rsh.technique_mitigated_by_mitigation(site_config.srcs)

def get_technique_related_to_technique():
    """ technique related to technique """

    if technique_related_to_technique:
        return technique_related_to_technique
    else:
        return rsh.technique_related_to_technique(site_config.srcs)

def get_tools_using_technique():
    """ tools using technique getter """

    if tools_using_technique:
        return tools_using_technique
    else:
        return rsh.tools_using_technique(site_config.srcs)

def get_malware_using_technique():
    """ malware using technique getter """

    if malware_using_technique:
        return malware_using_technique
    else:
        return rsh.malware_using_technique(site_config.srcs)

def get_groups_using_technique():
    """ groups using technique getter """

    if groups_using_technique:
        return groups_using_technique
    else:
        return rsh.groups_using_technique(site_config.srcs)

def get_ms():
    """ memory share getter """

    if ms:
        return ms
    else:
        return stixhelpers.get_stix_memory_stores()

def get_resources():
    """ resources getter """

    if resources:
        return resources
    else:
        return stixhelpers.grab_resources(get_ms())

def get_relationships():
    """ relationship getter """

    if relationships:
        return relationships
    else:
        return get_resources()['relationships']

def get_group_list():
    """ group list getter """

    if group_list:
        return group_list
    else:
        return get_resources()['groups']

def get_software_list():
    """ software list getter """

    if software_list:
        return software_list
    else:
        return get_resources()['software']

def get_technique_list():
    """ technique list getter """

    if technique_list:
        return technique_list
    else:
        return get_resources()['techniques']

def get_mitigation_list():
    """ mitigation list getter """

    if mitigation_list:
        return mitigation_list
    else:
        return get_resources()['mitigations']

def get_technique_to_domain():
    """ technique to domain getter """
    
    if technique_to_domain:
        return technique_to_domain
    else:
        return stixhelpers.get_technique_id_domain_map(get_ms())

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

def filter_urls(descr):
    """Filters out URLs to return path and not domain"""

    if not config.args.no_stix_link_replacement:
        if "https://attack.mitre.org/groups/" in descr:
            descr = descr.replace(
                "https://attack.mitre.org/groups/", "/groups/")
        if "https://attack.mitre.org/software/" in descr:
            descr = descr.replace(
                "https://attack.mitre.org/software/", "/software/")
        if "https://attack.mitre.org/techniques/" in descr:
            descr = descr.replace(
                "https://attack.mitre.org/techniques/", "/techniques/")
        if "https://attack.mitre.org/technique/" in descr:
            descr = descr.replace(
                "https://attack.mitre.org/technique/", "/techniques/")

    return descr

def format_description_markdown_link(descr):
    """This method is used to convert a markdown link to an html link"""

    p = re.compile('\[(.*?)\]\((.*?)\)')
    md_list = p.findall(descr)
    desc_link_temp = "<a href=\"{}\">{}</a>"
    md_link_temp ="[{}]({})"
    #Interate through each regex match set, and replace the markdown
    # link with the html link
    for md in md_list:
        url = md[1]
        sname = md[0]
        descr_markdown_link = md_link_temp.format(sname, url)
        descr = descr.replace(descr_markdown_link, desc_link_temp.format(url,sname))

    descr = filter_urls(descr)

    return descr

def get_descr_reference_sect(citations, reference_list, next_reference_number, description):
    """This method is responsible for properly formatting the 
       description citation area on Software, Groups pages
    """

    citation_temp = "(Citation: {})"

    # Find citations in description
    for citation in citations:     
        reference_str = find_reference_html(reference_list, next_reference_number, citation)
        if reference_str:
            description = description.replace(citation_temp.format(citation), reference_str)

    return description

def find_reference_number(reference_list, next_reference_number, source_name):
    """ Given a reference list and a source name, find the number of the source name
    """

    for reference in reference_list:
        if reference['sname'] == source_name:
            if not reference['number']:
                reference['number'] = next_reference_number['value']
                next_reference_number['value'] += 1
            return reference['number']
    return util_config.NOT_FOUND

def find_reference_html(reference_list, next_reference_number, source_name):
    """ Given a reference list and a source name, find source name and 
        create html string
    """

    for reference in reference_list:
        if reference['sname'] == source_name:
            if not reference['number']:
                reference['number'] = next_reference_number['value']
                next_reference_number['value'] += 1

            if not reference.get("url"):
                reference_html = util_config.reference_marker_template_no_url.format(reference['number'],reference['number'],reference['sname'],reference['number'])
            else:
                reference_html = util_config.reference_marker_template.format(reference['number'],reference['number'],reference['sname'],reference['url'],reference['number'] - 1, reference['number'] - 1, reference['number'])
            
            return reference_html
    return ""

def add_external_references_not_in_descr(description, reference_list, next_reference_number, obj, citations_from_descr):
    """Given an object, find external references that are not referenced on the description.
       If it not referenced, append reference to description
    """

    if obj.get('external_references'):
        for ext_ref in obj['external_references']:
            if not ext_ref.get('source_name') in citations_from_descr:
                reference_str = find_reference_html(reference_list, next_reference_number, ext_ref.get('source_name'))
                description += reference_str

    return description                  


def get_citations_from_descr(description):
    """Given a description, find all of the citations"""

    p = re.compile('\(Citation: (.*?)\)')
    return p.findall(description)

def citations_versus_references(obj, citations_from_descr):
    """Given an object an a list of citations found in the description,
       return the difference between the amount of citations and external references
    """

    citations_len = len(citations_from_descr)
    ext_references_len = 0
    if obj.get('external_references'):
        ext_references_len = len(obj.get('external_references'))
    return ext_references_len - citations_len

def get_filtered_description(reference_list, next_reference_number, obj):
    """Given an object, filter the description by changing citations, 
       eliminating unwanted HTML and add external references not in description
    """

    # Update reference list
    reference_list = update_reference_list(reference_list, obj['relationship'])

    # Get citations from description
    citations_from_descr = get_citations_from_descr(obj['relationship']['description'])
    
    # Add in-place citations to relationship description
    description = filter_urls(obj['relationship']['description'])
    description = get_descr_reference_sect(citations_from_descr, reference_list, next_reference_number,description) 

    # Check if description had all references
    # Returns 0 if description has the same amount of 
    # citations as the object's external references
    citations_references_diff = citations_versus_references(obj['relationship'], citations_from_descr)

    if citations_references_diff > 0:
        # Add external references not in description
        description = add_external_references_not_in_descr(description, reference_list, next_reference_number, obj['relationship'], citations_from_descr)

    description = replace_html_chars(markdown.markdown(description))

    return description

def update_reference_list(reference_list, obj):
    """Given a reference list and an object, update the reference list
       with the external references found in the object
    """

    if obj.get('external_references'):

        # Add external reference to reference list if not found
        for ext_ref in obj['external_references']:

            # Only add if reference has source name and a description
            if ext_ref.get('source_name') and ext_ref.get("description"):

                # Do not add if to reference list if citation is in description 
                if "(Citation:" in ext_ref['description']:
                    continue

                in_list = find_in_reference_list(reference_list, ext_ref['source_name'])

                if not in_list:
                    new_ref = {}

                    new_ref['description'] = ext_ref["description"]
                    if ext_ref.get('url'):
                        new_ref['url'] = ext_ref['url']
                    new_ref['sname'] = ext_ref['source_name']
                    new_ref['number'] = None

                    reference_list.append(new_ref)
    
    return reference_list

def sort_reference_list(reference_list):
    """Given a reference_list, sort it by number"""

    used_reference_list = []
    # Remove unused references from list
    for reference in reference_list:
        if reference.get('number'):
            used_reference_list.append(reference)
        
    return sorted(used_reference_list, key=lambda k: k['number'])

def remove_html_paragraph(description):
    """Given a description, remove <p> tags from the beginning and end"""

    if description.startswith("<p>") and description.endswith("</p>"):
        return description[3:-4]
    return description

def get_alias_data(alias_list, ext_refs, reference_list, next_reference_number):
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
                citations_from_descr = get_citations_from_descr(ext['description'])
                row = {}
                row['name'] = alias
                row['descr'] = markdown.markdown(ext['description'])
                row['descr'] = filter_urls(row['descr'])
                row['descr'] = get_descr_reference_sect(citations_from_descr, reference_list, next_reference_number, row['descr'])
                row['descr'] = remove_html_paragraph(row['descr'])
                
                alias_data.append(row)
        
    return alias_data

def get_technique_table_data(tactic, techniques_list):
    """Generate techniques table for tactics pages and techniques
       domain pages
    """

    technique_table = []

    for tech in techniques_list:

        attack_id = get_attack_id(tech)

        if attack_id:

            row = {}
            row['tid'] = attack_id

            row['descr'] = remove_citations(tech['description'], tech['external_references'])

            if row['descr'].split("\n")[0] == '### Windows':
                row['descr'] = markdown.markdown(row['descr'].split("\n")[2])
            else:
                row['descr'] = markdown.markdown(row['descr'].split("\n")[0])

            row['descr'] = filter_urls(row['descr'])

            if tactic is None and tech.get('x_mitre_deprecated'):
                row['deprecated'] = True

            row['technique_name'] = tech['name']
            technique_table.append(row)

    return technique_table

def remove_citations(descr, citations):
    """This method is used to replace and citation in markdown format
       with a link leading to the resource
    """

    for citation in citations:
        descr = descr.replace("(Citation: " + citation['source_name'] + ")","")

    return descr

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

def find_num_of_ref_in_list(reference_list, ref_sname):
    """Given a reference list and a reference, search for reference
       in list. Return number if found, else return NOT_FOUND
    """

    for reference in reference_list:
        if reference['sname'] == ref_sname:
            return reference['number']
    return util_config.NOT_FOUND

def find_in_reference_list(reference_list, source_name):
    """Check if it is already in reference list"""

    for reference in reference_list:
        if reference['sname'] == source_name:
            return True
    return False

def replace_html_chars(to_be_replaced):
    return to_be_replaced.replace("\n", "")\
                         .replace("{", "{{")\
                         .replace("}", "}}")\
                         .replace("”","\"")\
                         .replace("“","\"")

def get_index_of_ref(reference_list, ref_sname):
    """Given a reference source name, return reference list index if found"""

    index = 0
    for reference in reference_list:
        if reference['sname'] == ref_sname:
            return index
        index += 1
    return util_config.NOT_FOUND

def get_navigator_layers(name, attack_id, obj_type, version, techniques_used):
    """Given a list of techniques used, return the navigator json objects
       for enterprise and mobile"""

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
    enterprise_layer['domain'] = "mitre-enterprise"
    enterprise_layer['version'] = "2.2"
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
    mobile_layer['domain'] = "mitre-mobile"
    mobile_layer['version'] = "2.2"
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
        navigator_technique = get_navigator_technique(technique['id'], technique["descr"])

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

def get_navigator_technique(attack_id, description):
    """Given an attack id, return it as a dict for the navigator layer"""

    navigator_technique = {}
    navigator_technique['score'] = 1
    navigator_technique['techniqueID'] = attack_id
    if description: navigator_technique['comment'] = bleach.clean(description, tags=[], strip=True) #remove html tags
    return navigator_technique

def print_test_output(status, test, message):
    """Standard printing for all tests"""

    if status.startswith("RUNNING"):
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

def progress_bar(name, time = None):
    """Given a name and a time, display current progress"""

    number_of_hyphens = 40
    name_space = 22

    hyphens = '-' * number_of_hyphens

    if time:
        # spaces here because we need to overwrite the word "running"
        sys.stdout.write(f"\r{name: <{name_space}} : {hyphens} {time:.2f}s      \n")
    else:
        sys.stdout.write(f"\r{name: <{name_space}} : {hyphens} Running...")

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
