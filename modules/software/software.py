import os
import json
import collections
import re
import time
import markdown
from .. import site_config
from . import software_config
from modules import util

def generate_software():
    """Responsible for verifying software directory and generating software 
       index markdown
    """

    # Move templates to templates directory
    util.buildhelpers.move_templates(software_config.module_name, software_config.software_templates_path)

    # Verify if directory exists
    if not os.path.isdir(software_config.software_markdown_path):
        os.mkdir(software_config.software_markdown_path)
    
    # Generate redirections
    util.buildhelpers.generate_redirections(software_config.software_redirection_location)
        
    # Generates the markdown files to be used for page generation and verifies if a software was generated
    software_generated = generate_markdown_files()

    if not software_generated:
        util.buildhelpers.remove_module_from_menu(software_config.module_name)

def generate_markdown_files():
    """Responsible for generating the shared data for all software and 
       kicking off markdown generation
    """
    
    data = {}

    has_software = False

    # Amount of characters per category
    group_by = 2

    software_list = util.relationshipgetters.get_software_list()        

    if software_list:
        has_software = True
    
    if has_software:
        data['software_list_len'] = str(len(software_list))

        side_menu_data = util.buildhelpers.get_side_menu_data("software", "/software/", software_list)
        data['side_menu_data'] = side_menu_data

        side_menu_mobile_view_data = util.buildhelpers.get_side_menu_mobile_view_data("software", "/software/", software_list, group_by)
        data['side_menu_mobile_view_data'] = side_menu_mobile_view_data

        data['software_table'] = get_software_table_data(software_list)
        
        subs = software_config.software_index_md + json.dumps(data)

        with open(os.path.join(software_config.software_markdown_path, "overview.md"), "w", encoding='utf8') as md_file:
            md_file.write(subs)

        # Create the markdown for the enterprise groups in the stix
        for software in software_list:
            generate_software_md(software, side_menu_data, side_menu_mobile_view_data)
    
    return has_software
    
def generate_software_md(software,side_menu_data,side_menu_mobile_view_data):
    """Responsible for generating given software markdown"""

    attack_id = util.buildhelpers.get_attack_id(software)

    # If software has id generate software data
    if attack_id:
        
        data = {}

        data['attack_id'] = attack_id

        data['side_menu_data'] = side_menu_data
        data['side_menu_mobile_view_data'] = side_menu_mobile_view_data

        dates = util.buildhelpers.get_created_and_modified_dates(software)
        
        if dates.get('created'):
            data['created'] = dates['created']

        if dates.get('modified'):
            data['modified'] = dates['modified']

        # Get name
        if software.get("name"): 
            data['name'] = software["name"]

        # Get type
        if software.get("type"):
            data['type'] = software["type"].upper()   

        # Get version
        if software.get("x_mitre_version"):
            data['version'] = software["x_mitre_version"]
        
        ext_ref = software["external_references"]
        
        # Get initial reference list
        reference_list = []
        # Decleared as an object to be able to pass by reference
        next_reference_number = {}
        next_reference_number['value'] = 1
        reference_list = util.buildhelpers.update_reference_list(reference_list, software)
                         
        # Get description
        if software.get("description"):
            citations_from_descr = util.buildhelpers.get_citations_from_descr(software['description'])
            data['descr'] = markdown.markdown(software["description"])
            data['descr'] = util.buildhelpers.filter_urls(data['descr'])
            data['descr'] = util.buildhelpers.get_descr_reference_sect(citations_from_descr, reference_list, next_reference_number, data['descr'])

            if 'x_mitre_deprecated' in software:
                data['deprecated'] = True

        # Get techniques used by software
        data['technique_table_data'] = get_techniques_used_by_software_data(software, reference_list, next_reference_number)

        # # Get enterprise and mobile layers for navigator
        # enterprise_layer, mobile_layer = util.get_navigator_layers(data['name'], data['technique_table_data'])

        # Get navigator layers for this group
        layers = util.buildhelpers.get_navigator_layers(
            data['name'], 
            data["attack_id"],
            "software",
            data["version"] if "version" in data else None,
            data['technique_table_data'], 
        )

        data["layers"] = []
        for layer in layers:
            with open(os.path.join(software_config.software_markdown_path, "-".join([data['attack_id'], "techniques", layer["domain"]]) + ".md"), "w", encoding='utf8') as layer_json:
                subs = site_config.layer_md.substitute({
                    "attack_id": data["attack_id"],
                    "path": "software/" + data["attack_id"],
                    "domain": layer["domain"]
                })
                subs = subs + layer["layer"]
                layer_json.write(subs)
            data["layers"].append({
                "domain": layer["domain"],
                "filename": "-".join([data["attack_id"], layer["domain"], "layer"]) + ".json",
                "navigator_link_enterprise" : site_config.navigator_link_enterprise,
                "navigator_link_mobile" : site_config.navigator_link_mobile
            })
        
        # Get aliases descriptions
        data['alias_descriptions'] = util.buildhelpers.get_alias_data(software.get("x_mitre_aliases")[1:], ext_ref, reference_list, next_reference_number)

        # Get group data of groups that use software
        data['groups'] = get_groups_using_software(software, reference_list, next_reference_number)

        data['bottom_ref'] = util.buildhelpers.sort_reference_list(reference_list)

        # Get aliases list
        if isinstance(software.get("x_mitre_aliases"), collections.Iterable):
            data['aliases_list'] = software["x_mitre_aliases"][1:]

        # Get contributors
        if isinstance(software.get("x_mitre_contributors"), collections.Iterable):
            data['contributors_list'] = software["x_mitre_contributors"]
        
        # Get platform list
        if isinstance(software.get("x_mitre_platforms"), collections.Iterable):
            data['platform_list'] = software["x_mitre_platforms"]

        subs = software_config.software_md.substitute(data)
        subs = subs + json.dumps(data)

        # Write out the markdown file
        with open(os.path.join(software_config.software_markdown_path, data['attack_id'] + ".md"), "w", encoding='utf8') as md_file:
            md_file.write(subs)

def get_software_table_data(software_list):
    """Responsible for generating software table data for the software 
       index page
    """

    software_table_data = []

    for software in software_list:

        if software.get("name"):
            row = {}

            row['name'] = software["name"]

            if software.get("description"):
                row['descr'] = software["description"]
                citation_temp = "(Citation: {})"
                p = re.compile('\(Citation: (.*?)\)')
                found_citations = p.findall(row['descr'])

                for citation in found_citations:
                    row['descr'] = row['descr'].replace(citation_temp.format(citation), "")

                row['descr'] = markdown.markdown(row['descr'])
                row['descr'] = util.buildhelpers.filter_urls(row['descr'])
                if software.get('x_mitre_deprecated'):
                    row['deprecated'] = True
            
            attack_id = util.buildhelpers.get_attack_id(software)

            if attack_id:
                row['id'] = attack_id

            if isinstance(software.get("x_mitre_aliases"), collections.Iterable):
                row['aliases_list'] = software["x_mitre_aliases"][1:]
        
            software_table_data.append(row)
    
    return software_table_data

def get_groups_using_software(software, reference_list, next_reference_number):
    """Given a software object, return group list with id and name of
       groups
    """

    if software.get('type').lower() == "malware":
        groups_using_software = util.relationshipgetters.get_groups_using_malware().get(software['id'])
    else:
        groups_using_software = util.relationshipgetters.get_groups_using_tool().get(software['id'])    
    
    groups = []

    if groups_using_software:
        # Get name, id of group
        for group in groups_using_software:
            attack_id = util.buildhelpers.get_attack_id(group['object'])

            if attack_id:
                row = {}
                row['id'] = attack_id
                row['name'] = group['object']['name']

                if group['relationship'].get('description'):
                    # Get filtered description
                    row['descr'] = util.buildhelpers.get_filtered_description(reference_list, next_reference_number, group)
                elif group['relationship'].get('external_references'):

                    # Update reference list
                    reference_list = util.buildhelpers.update_reference_list(reference_list, group['relationship'])

                    row['refs'] = []

                    for ext_ref in group['relationship']['external_references']:
                        if ext_ref.get('source_name'):
                            ref = {}
                            ref['url'] = ext_ref.get('url')
                            ref['number'] = util.buildhelpers.find_reference_number(reference_list, next_reference_number, ext_ref['source_name'])                          

                        row['refs'].append(ref) 
    
                groups.append(row)
            
    return groups

def get_techniques_used_by_software_data(software, reference_list, next_reference_number):
    """Given a software and its reference list, get the techniques used by the
       software. Check the reference list for citations, if not found
       in list, add it.
    """

    if software.get('type').lower() == "malware":
        techniques_used_by_software = util.relationshipgetters.get_techniques_used_by_malware().get(software['id'])
    else:
        techniques_used_by_software = util.relationshipgetters.get_techniques_used_by_tools().get(software['id'])

    technique_list = {}
    if techniques_used_by_software:

        for technique in techniques_used_by_software:
            # Do not add if technique is deprecated
            if not technique['object'].get('x_mitre_deprecated'):
                technique_list = util.buildhelpers.technique_used_helper(technique_list, technique, reference_list, next_reference_number)
            
    technique_data = []
    for item in technique_list:
        technique_data.append(technique_list[item])
    # Sort by technique name
    technique_data = sorted(technique_data, key=lambda k: k['name'].lower())

    # Sort by domain name
    technique_data = sorted(technique_data, key=lambda k: [site_config.custom_alphabet.index(c) for c in k['domain'].lower()])
    return technique_data