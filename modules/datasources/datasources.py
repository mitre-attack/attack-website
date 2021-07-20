import os
import json
import collections
import re
import markdown
from .. import site_config
from . import datasources_config
from modules import util
from modules.util import stixhelpers
from modules.util import relationshiphelpers

def generate_datasources():
    """Responsible for verifying data source directory and starting off 
       data source markdown generation
    """

    # Create content pages directory if does not already exist
    util.buildhelpers.create_content_pages_dir()
    
    # Move templates to templates directory
    util.buildhelpers.move_templates(datasources_config.module_name, datasources_config.datasources_templates_path)

    # Create content pages directory if does not already exist
    util.buildhelpers.create_content_pages_dir()

    # Verify if directory exists
    if not os.path.isdir(datasources_config.datasource_markdown_path):
        os.mkdir(datasources_config.datasource_markdown_path)

    # Generates the markdown files to be used for page generation
    datasource_generated = generate_markdown_files()

    if not datasource_generated:
        util.buildhelpers.remove_module_from_menu(datasources_config.module_name)

def generate_markdown_files():
    """Responsible for generating datasource index page and getting shared data for
       all datasources
    """

    has_datasource = False

    datasource_list = util.relationshipgetters.get_datasource_list()
    datasource_list_no_deprecated_revoked = util.buildhelpers.filter_deprecated_revoked(datasource_list)

    if datasource_list_no_deprecated_revoked:
        has_datasource = True

    if has_datasource:
        data = {}

        # Amount of characters per category
        group_by = 2

        notes = util.relationshipgetters.get_objects_using_notes()
        side_menu_data = util.buildhelpers.get_side_menu_data("datasources", "/datasources/", datasource_list_no_deprecated_revoked)
        data['side_menu_data'] = side_menu_data

        side_menu_mobile_view_data = util.buildhelpers.get_side_menu_mobile_view_data("datasources", "/datasources/", datasource_list_no_deprecated_revoked, group_by)
        data['side_menu_mobile_view_data'] = side_menu_mobile_view_data

        data['datasources_table'] = get_datasources_table_data(datasource_list_no_deprecated_revoked)
        data['datasources_list_len'] = str(len(datasource_list_no_deprecated_revoked))
        
        subs = datasources_config.datasource_index_md + json.dumps(data)

        with open(os.path.join(datasources_config.datasource_markdown_path, "overview.md"), "w", encoding='utf8') as md_file:
            md_file.write(subs)

        #Create the markdown for the enterprise datasources in the STIX
        for datasource in datasource_list:
            generate_datasource_md(datasource, side_menu_data, side_menu_mobile_view_data, notes)
    
    return has_datasource

def generate_datasource_md(datasource, side_menu_data, side_menu_mobile_view_data, notes):
    """Responsible for generating markdown of all datasources"""

    attack_id = util.buildhelpers.get_attack_id(datasource)
    print(attack_id)
    if attack_id:
        data = {}

        data['attack_id'] = attack_id

        data['side_menu_data'] = side_menu_data
        data['side_menu_mobile_view_data'] = side_menu_mobile_view_data
        data['notes'] = notes.get(datasource['id'])

        # Get data components of data source
        datacomponents_of = util.relationshipgetters.get_datacomponent_of()
        print(datacomponent_of[datasource['id']])


        # get data components to techniques mapping 

        # External references
        # ext_ref = datasource["external_references"]

        # dates = util.buildhelpers.get_created_and_modified_dates(datasource)
        
        # if dates.get('created'):
        #     data['created'] = dates['created']

        # if dates.get('modified'):
        #     data['modified'] = dates['modified']

        # if datasource.get("name"):
        #     data['name'] = datasource['name']
        
        # if datasource.get("x_mitre_version"):
        #     data['version'] = datasource["x_mitre_version"]

        # if isinstance(datasource.get("x_mitre_contributors"),collections.Iterable):
        #     data['contributors_list'] = datasource["x_mitre_contributors"]

        # # Get initial reference list
        # reference_list = {'current_number': 0}

        # # Get initial reference list from datasource object
        # reference_list = util.buildhelpers.update_reference_list(reference_list, datasource)

        # if datasource.get("description"):
        #     data['descr'] = datasource['description']
        
        # if datasource.get('x_mitre_deprecated'):
        #     data['deprecated'] = True

        # # Get technique data for techniques used table
        # data['technique_table_data'] = get_techniques_used_by_datasource_data(datasource, reference_list)

        # # Get navigator layers for this datasource
        # layers = util.buildhelpers.get_navigator_layers(
        #     data['name'], 
        #     data["attack_id"],
        #     "datasource",
        #     data["version"] if "version" in data else None,
        #     data['technique_table_data'], 
        # )

        # data["layers"] = []
        # for layer in layers:
        #     with open(os.path.join(datasources_config.datasource_markdown_path, "-".join([data['attack_id'], "techniques", layer["domain"]]) + ".md"), "w", encoding='utf8') as layer_json:
        #         subs = site_config.layer_md.substitute({
        #             "attack_id": data["attack_id"],
        #             "path": "datasources/" + data["attack_id"],
        #             "domain": layer["domain"]
        #         })
        #         subs = subs + layer["layer"]
        #         layer_json.write(subs)
        #     data["layers"].append({
        #         "domain": layer["domain"],
        #         "filename": "-".join([data["attack_id"], layer["domain"], "layer"]) + ".json",
        #         "navigator_link" : site_config.navigator_link
        #     })

        # # Grab software data for Software table
        # data['software_data'], data['add_software_ref'] = get_software_table_data(datasource, reference_list)

        # if datasource.get('aliases'):
        #     data['alias_descriptions'] = util.buildhelpers.get_alias_data(datasource['aliases'][1:], ext_ref)

        # data['citations'] = reference_list
                
        # if isinstance(datasource.get("aliases"), collections.Iterable):
        #     data['aliases_list'] = datasource["aliases"][1:]
        
        # data['versioning_feature'] = site_config.check_versions_module()

        # subs = datasources_config.datasource_md.substitute(data)
        # subs = subs + json.dumps(data)

        # Write out the markdown file
        # with open(os.path.join(datasources_config.datasource_markdown_path, data['attack_id'] + ".md"), "w", encoding='utf8') as md_file:
        #     md_file.write(subs)

def get_datasources_side_nav_data(datasources, tactics):
    """Responsible for generating the links that are located on the
       left side of individual data sources domain pages
    """
    
    side_nav_data = []

    subtechniques_of = util.relationshipgetters.get_subtechniques_of()

    for domain in site_config.domains:
        if domain['deprecated']: continue

        domain_data = {
            "name": domain['alias'],
            "id": domain['name'].split("-")[0],
            "path": "/techniques/{}/".format(domain['name'].split("-")[0]), # root level doesn't get a path
            "children": []
        }

        technique_list = get_techniques_list(techniques[domain['name']])

        for tactic in tactics[domain['name']]:
            tactic_row = {}
            
            tactic_row['name'] = tactic['name']
            tactic_row['id'] = util.buildhelpers.get_attack_id(tactic)
            tactic_row['path'] = "/tactics/{}".format(util.buildhelpers.get_attack_id(tactic))
            
            tactic_row['children'] = []
            
            for technique in technique_list[tactic['x_mitre_shortname']]:
                technique_row = {}
                # Get technique id and name for each technique
                technique_row['name'] = technique['name']
                technique_row['id'] = technique['id']
                technique_row['path'] = "/techniques/{}/".format(technique['id'])
                technique_row['children'] = []

                # Add subtechniques as children if they are found:
                if technique["stix_id"] in subtechniques_of:
                    subtechniques = subtechniques_of[technique["stix_id"]]
                    for subtechnique in subtechniques:
                        child = {}
                        child['id'] = util.buildhelpers.get_attack_id(subtechnique['object'])
                        if child['id']:
                            child['name'] = subtechnique['object']['name']
                            sub_number = child["id"].split(".")[1]
                            child['path'] = "/techniques/{}/{}/".format(technique['id'], sub_number)
                            child['children'] = []
                            technique_row['children'].append(child)

                    # Sort subtechniques by ATT&CK ID
                    if technique_row['children']:
                        technique_row['children'] = sorted(technique_row['children'], key=lambda k: k['id'])

                # Add technique data to tactic
                tactic_row['children'].append(technique_row)
            # Add tactic to domain
            domain_data['children'].append(tactic_row)
        # add domain to the table
        side_nav_data.append(domain_data)

    return {
        "name": "techniques",
        "id": "techniques",
        "path": None, # root level doesn't get a path
        "children": side_nav_data
    }

def get_datasources_table_data(datasource_list):
    """Responsible for generating datasource table data for the datasource index page"""

    datasources_table_data = []

    #Now the table on the right, which is made up of datasource data
    for datasource in datasource_list:

        attack_id = util.buildhelpers.get_attack_id(datasource)

        if attack_id:
            row = {}

            row['id'] = attack_id

            if datasource.get("name"):
                row['name'] = datasource['name']

            if datasource.get("description"):
                row['descr'] = datasource["description"]

                if datasource.get('x_mitre_deprecated'):
                    row['deprecated'] = True

            if isinstance(datasource.get("aliases"), collections.Iterable):
                row['aliases_list'] = datasource["aliases"][1:]
            
            datasources_table_data.append(row)
    
    return datasources_table_data

def get_techniques_used_by_datasource_data(datasource, reference_list):
    """Given a datasource and its reference list, get the techniques used by the
       datasource. Check the reference list for citations, if not found
       in list, add it.
    """
    
    technique_list = {}

    techniques_used_by_datasources = util.relationshipgetters.get_techniques_used_by_datasources()

    if techniques_used_by_datasources.get(datasource.get('id')):
        for technique in techniques_used_by_datasources[datasource['id']]:
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

def get_software_table_data(datasource, reference_list):
    """Given a datasource, get software table data"""

    software_list = {}

    reference = False

    # Creating map for tools/malware used by datasources 
    # and techniques used by malware/tools
    tools_and_malware = [{
        'software': util.relationshipgetters.get_tools_used_by_datasources(), 
        'techniques': util.relationshipgetters.get_techniques_used_by_tools()
    }, 
    {
        'software': util.relationshipgetters.get_malware_used_by_datasources(),
        'techniques': util.relationshipgetters.get_techniques_used_by_malware()
    }]

    # Get malware or tools used by datasource
    for pairing in tools_and_malware:
        if pairing['software'].get(datasource.get('id')):
            for software in pairing['software'][datasource['id']]:

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