import os
import json
import collections
import re
import markdown
# from . import config
from .. import site_config
from . import groups_config
from modules import util
from modules.util import stixhelpers
from modules.util import relationshiphelpers


def generate_groups():
    """Responsible for verifying group directory and starting off 
       group markdown generation
    """

    # Create content pages directory if does not already exist
    util.buildhelpers.create_content_pages_dir()
    
    # Move templates to templates directory
    util.buildhelpers.move_templates(groups_config.module_name, groups_config.groups_templates_path)

    # Create content pages directory if does not already exist
    util.buildhelpers.create_content_pages_dir()

    # Verify if directory exists
    if not os.path.isdir(groups_config.group_markdown_path):
        os.mkdir(groups_config.group_markdown_path)

    #Generates the markdown files to be used for page generation
    group_generated = generate_markdown_files()

    if not group_generated:
        util.buildhelpers.remove_module_from_menu(groups_config.module_name)

def generate_markdown_files():
    """Responsible for generating group index page and getting shared data for
       all groups
    """

    has_group = False

    group_list = util.relationshipgetters.get_group_list()

    if group_list:
        has_group = True

    if has_group:
        data = {}

        # Amount of characters per category
        group_by = 2

        side_menu_data = util.buildhelpers.get_side_menu_data("Groups", "/groups/", group_list)
        data['side_menu_data'] = side_menu_data

        side_menu_mobile_view_data = util.buildhelpers.get_side_menu_mobile_view_data("groups", "/groups/", group_list, group_by)
        data['side_menu_mobile_view_data'] = side_menu_mobile_view_data

        data['groups_table'] = get_groups_table_data(group_list)
        data['groups_list_len'] = str(len(group_list))
        
        subs = groups_config.group_index_md + json.dumps(data)

        with open(os.path.join(groups_config.group_markdown_path, "overview.md"), "w", encoding='utf8') as md_file:
            md_file.write(subs)

        #Create the markdown for the enterprise groups in the STIX
        for group in group_list:
            generate_group_md(group, side_menu_data, side_menu_mobile_view_data)
    
    return has_group

def generate_group_md(group, side_menu_data, side_menu_mobile_view_data):
    """Responsible for generating markdown of all groups"""

    attack_id = util.buildhelpers.get_attack_id(group)

    if attack_id:
        data = {}

        data['attack_id'] = attack_id

        data['side_menu_data'] = side_menu_data
        data['side_menu_mobile_view_data'] = side_menu_mobile_view_data

        # External references
        ext_ref = group["external_references"]

        dates = util.buildhelpers.get_created_and_modified_dates(group)
        
        if dates.get('created'):
            data['created'] = dates['created']

        if dates.get('modified'):
            data['modified'] = dates['modified']

        if group.get("name"):
            data['name'] = group['name']
        
        if group.get("x_mitre_version"):
            data['version'] = group["x_mitre_version"]

        if isinstance(group.get("x_mitre_contributors"),collections.Iterable):
            data['contributors_list'] = group["x_mitre_contributors"]

        # Get initial reference list
        reference_list = {'current_number': 0}

        # Get initial reference list from group object
        reference_list = util.buildhelpers.update_reference_list(reference_list, group)

        if group.get("description"):
            data['descr'] = group['description']
        
        if group.get('x_mitre_deprecated'):
            data['deprecated'] = True

        # Get technique data for techniques used table
        data['technique_table_data'] = get_techniques_used_by_group_data(group, reference_list)

        # Get navigator layers for this group
        layers = util.buildhelpers.get_navigator_layers(
            data['name'], 
            data["attack_id"],
            "group",
            data["version"] if "version" in data else None,
            data['technique_table_data'], 
        )

        data["layers"] = []
        for layer in layers:
            with open(os.path.join(groups_config.group_markdown_path, "-".join([data['attack_id'], "techniques", layer["domain"]]) + ".md"), "w", encoding='utf8') as layer_json:
                subs = site_config.layer_md.substitute({
                    "attack_id": data["attack_id"],
                    "path": "groups/" + data["attack_id"],
                    "domain": layer["domain"]
                })
                subs = subs + layer["layer"]
                layer_json.write(subs)
            data["layers"].append({
                "domain": layer["domain"],
                "filename": "-".join([data["attack_id"], layer["domain"], "layer"]) + ".json",
                "navigator_link" : site_config.navigator_link
            })

        # Grab software data for Software table
        data['software_data'], data['add_software_ref'] = get_software_table_data(group, reference_list)

        data['alias_descriptions'] = util.buildhelpers.get_alias_data(group.get("aliases")[1:], ext_ref)

        data['citations'] = reference_list
                
        if isinstance(group.get("aliases"), collections.Iterable):
            data['aliases_list'] = group["aliases"][1:]
        
        data['versioning_feature'] = site_config.check_versions_module()

        subs = groups_config.group_md.substitute(data)
        subs = subs + json.dumps(data)

        # Write out the markdown file
        with open(os.path.join(groups_config.group_markdown_path, data['attack_id'] + ".md"), "w", encoding='utf8') as md_file:
            md_file.write(subs)

def get_groups_table_data(group_list):
    """Responsible for generating group table data for the group index page"""

    groups_table_data = []

    #Now the table on the right, which is made up of group data
    for group in group_list:

        attack_id = util.buildhelpers.get_attack_id(group)

        if attack_id:
            row = {}

            row['id'] = attack_id

            if group.get("name"):
                row['name'] = group['name']

            if group.get("description"):
                row['descr'] = group["description"]

                if group.get('x_mitre_deprecated'):
                    row['deprecated'] = True

            if isinstance(group.get("aliases"), collections.Iterable):
                row['aliases_list'] = group["aliases"][1:]
            
            groups_table_data.append(row)
    
    return groups_table_data

def get_techniques_used_by_group_data(group, reference_list):
    """Given a group and its reference list, get the techniques used by the
       group. Check the reference list for citations, if not found
       in list, add it.
    """
    
    technique_list = {}

    techniques_used_by_groups = util.relationshipgetters.get_techniques_used_by_groups()

    if techniques_used_by_groups.get(group.get('id')):
        for technique in techniques_used_by_groups[group['id']]:
            # Do not add if technique is deprecated
            if not technique['object'].get('x_mitre_deprecated'):
                technique_list = util.buildhelpers.technique_used_helper(technique_list, technique, reference_list)

    technique_data = []
    for item in technique_list:
        technique_data.append(technique_list[item])
    # Sort by technique name
    technique_data = sorted(technique_data, key=lambda k: k['name'].lower())

    # Sort by domain name
    technique_data = sorted(technique_data, key=lambda k: [site_config.custom_alphabet.index(c) for c in k['domain'].lower()])
    return technique_data

def get_software_table_data(group, reference_list):
    """Given a group, get software table data"""

    software_list = {}

    reference = False

    # Creating map for tools/malware used by groups 
    # and techniques used by malware/tools
    tools_and_malware = [{
        'software': util.relationshipgetters.get_tools_used_by_groups(), 
        'techniques': util.relationshipgetters.get_techniques_used_by_tools()
    }, 
    {
        'software': util.relationshipgetters.get_malware_used_by_groups(),
        'techniques': util.relationshipgetters.get_techniques_used_by_malware()
    }]

    # Get malware or tools used by group
    for pairing in tools_and_malware:
        if pairing['software'].get(group.get('id')):
            for software in pairing['software'][group['id']]:

                software_id = software['object']['id']

                # Check if software not already in software_list dict
                if software_id not in software_list:

                    attack_id = util.buildhelpers.get_attack_id(software['object'])
                    
                    if attack_id:
                        software_list[software_id] = {}

                        software_list[software_id]['id'] = attack_id
                        software_list[software_id]['name'] = software['object']['name']

                        if software['relationship'].get('description'):
                            if reference == False:
                                reference = True

                            # Get filtered description
                            software_list[software_id]['descr'] = software['relationship']['description']
                            # Update reference list
                            reference_list = util.buildhelpers.update_reference_list(reference_list, software['relationship'])

                        # Check if techniques exists, add techniques used by software
                        if pairing['techniques'].get(software_id):
                                
                            if 'techniques' not in software_list[software_id]:
                                software_list[software_id]['techniques'] = []

                            for technique in pairing['techniques'][software_id]:

                                tech_data = {}

                                t_id = util.buildhelpers.get_attack_id(technique['object'])

                                if t_id:
                                    if util.buildhelpers.is_sub_tid(t_id):
                                        tech_data['parent_id'] = util.buildhelpers.get_parent_technique_id(t_id)
                                        tech_data['id'] = util.buildhelpers.get_sub_technique_id(t_id)
                                        tech_data['name'] = util.buildhelpers.get_technique_name(tech_data['parent_id'])
                                        tech_data['sub_name'] = technique['object']['name']
                                    else:
                                        tech_data['id'] = t_id
                                        tech_data['name'] =  technique['object']['name']

                                    software_list[software_id]['techniques'].append(tech_data)

    # Moving it to an array because jinja does not like to loop
    # through dictionaries
    data = []
    for item in software_list:
        if "techniques" in software_list[item]:
            software_list[item]['techniques'] = sorted(software_list[item]['techniques'], key=lambda k: k['name'].lower())
        data.append(software_list[item])
    data = sorted(data, key=lambda k: k['name'].lower())

    return data, reference