import json
import os
import requests
import collections
import urllib3
import re
import markdown
import stix2
from . import config
from . import stixhelpers
from . import util

def generate():
    """Responsible for verifying techniques directory and generating
       techniques index markdown
    """

    # Verify if directory exists
    if not os.path.isdir(config.techniques_markdown_path):
        os.mkdir(config.techniques_markdown_path)

    #Write the technique index.html page
    with open(os.path.join(config.techniques_markdown_path, "overview.md"), "w", encoding='utf8') as md_file:
        md_file.write(config.technique_overview_md)

    techniques = {}
    tactics = {}

    for domain in config.domains:
        #Reads the STIX and creates a list of the ATT&CK Techniques
        techniques[domain] = stixhelpers.get_techniques(config.ms[domain])
        tactics[domain] = stixhelpers.get_tactic_list(config.ms[domain])
    
    side_nav_data = get_technique_side_nav_data(techniques, tactics)

    for domain in config.domains:
        generate_domain_markdown(domain, techniques, tactics, side_nav_data)

def generate_domain_markdown(domain, techniques, tactics, side_nav_data):
    """Generate technique index markdown for each domain and generates 
       shared data for techniques
    """

    data = {}
    data['domain'] = domain.split("-")[0]

    # Get technique table data and number of techniques
    data['technique_table'] = util.get_technique_table_data(None, techniques[domain])
    data['technique_list_len'] = str(len(techniques[domain]))

    # Get tactic-techniques table
    data['menu'] = side_nav_data

    subs = config.technique_domain_md.substitute(data)
    subs = subs + json.dumps(data)

    with open(os.path.join(config.techniques_markdown_path, data['domain'] + "-techniques.md"), "w", encoding='utf8') as md_file:
        md_file.write(subs)

    # Create the markdown for the enterprise groups in the STIX

    for technique in techniques[domain]:
        if 'revoked' not in technique or technique['revoked'] is False:
            generate_technique_md(technique, domain, side_nav_data, tactics[domain])

def generate_technique_md(technique, domain, side_nav_data, tactic_list):
    """Generetes markdown data for given technique"""

    attack_id = util.get_attack_id(technique)

    # Only add technique if the attack id was found
    if attack_id:

        technique_dict = {}

        technique_dict['attack_id'] = attack_id
        technique_dict['domain'] = domain.split("-")[0]
        technique_dict['menu'] = side_nav_data
        technique_dict['name'] = technique.get('name')

        # Get capecs and mtcs
        for ref in technique['external_references']:
            if ref.get('source_name'):
                if ref['source_name'] == "capec":
                    if technique_dict.get('capecs') is None:
                        technique_dict['capecs'] = []
                    capec_dict = {
                        'id': ref['external_id'],
                        'url': ref['url']
                    }
                    technique_dict['capecs'].append(capec_dict)

                if ref['source_name'] == "NIST Mobile Threat Catalogue":
                    if technique_dict.get('mtcs') is None:
                        technique_dict['mtcs'] = []

                    mtcs_dict = {
                        'id': ref['external_id'],
                        'url': ref['url']
                    }
                    technique_dict['mtcs'].append(mtcs_dict)

        # Get initial reference list
        reference_list = []
        # Decleared as an object to be able to pass by reference
        next_reference_number = {}
        next_reference_number['value'] = 1
        reference_list = util.update_reference_list(reference_list, technique)

        dates = util.get_created_and_modified_dates(technique)
        
        if dates.get('created'):
            technique_dict['created'] = dates['created']

        if dates.get('modified'):
            technique_dict['modified'] = dates['modified']

        # Get technique description
        if technique.get("description"):
            citations_from_descr = util.get_citations_from_descr(technique['description'])

            technique_dict['descr'] = util.replace_html_chars(markdown.markdown(technique['description']))
            technique_dict['descr'] = util.filter_urls(technique_dict['descr'])
            technique_dict['descr'] = util.get_descr_reference_sect(citations_from_descr, reference_list, next_reference_number, technique_dict['descr'])
            
            if 'x_mitre_deprecated' in technique:
                technique_dict['deprecated'] = True
        
        # Get mitigation table
        technique_dict['mitigation_table'] = get_mitigations_table_data(technique, reference_list, next_reference_number)
        
        # Get related techniques
        technique_dict['rel_techniques_table'] = get_related_techniques_data(technique, tactic_list)

        # Get examples
        technique_dict['examples_table'] = get_examples_table_data(technique, reference_list, next_reference_number)

        # Get technique version
        if technique.get("x_mitre_version"):
            technique_dict['version'] = technique["x_mitre_version"]

        # Get tactics of technique
        if technique.get('kill_chain_phases'):
            technique_dict['tactics'] = []
            for elem in technique['kill_chain_phases']:
                technique_dict['tactics'].append(elem['phase_name'].title().replace('-', ' '))

        # Get platforms that technique uses
        if technique.get('x_mitre_platforms'):
            technique['x_mitre_platforms'].sort()
            technique_dict['platforms'] = ", ".join(technique['x_mitre_platforms'])

        # Get system requirements
        if technique.get('x_mitre_system_requirements'):
            technique['x_mitre_system_requirements'].sort()
            technique_dict['sysreqs'] = ", ".join(technique['x_mitre_system_requirements'])
            technique_dict['sysreqs'] = re.sub("\.?\\n+", "; ", technique_dict['sysreqs'])

        # Get permissions required
        if technique.get('x_mitre_permissions_required'):
            technique['x_mitre_permissions_required'].sort()
            technique_dict['perms'] = ", ".join(technique['x_mitre_permissions_required'])

        # Get effective permissions
        if technique.get('x_mitre_effective_permissions'):
            technique['x_mitre_effective_permissions'].sort()
            technique_dict['eff_perms'] = ", ".join(technique['x_mitre_effective_permissions'])

        # Get data sources
        if technique.get('x_mitre_data_sources'):
            technique['x_mitre_data_sources'].sort()
            technique_dict['data_sources'] = ", ".join(technique['x_mitre_data_sources'])

        # Get if technique supports remote
        if technique.get('x_mitre_remote_support'):
            if technique['x_mitre_remote_support']:
                technique_dict['supports_remote'] = " Yes"
            else:
                technique_dict['supports_remote'] = " No"

        # Get network requirements
        if technique.get('x_mitre_network_requirements'):
            if technique['x_mitre_network_requirements']:
                technique_dict['network_reqs'] = " Yes"
            else:
                technique_dict['network_reqs'] = " No"

        # Get list of impacts
        if technique.get('x_mitre_impact_type'):
            technique['x_mitre_impact_type'].sort()
            technique_dict['impact_type'] = ", ".join(technique['x_mitre_impact_type'])

        # Get list of defenses bypassed
        if technique.get('x_mitre_defense_bypassed'):
            technique['x_mitre_defense_bypassed'].sort()
            technique_dict['def_bypass'] = ", ".join(technique['x_mitre_defense_bypassed'])

        # Get list of contributors        
        if technique.get('x_mitre_contributors'):
            technique['x_mitre_contributors'].sort()
            technique_dict['contributors'] = "; ".join(technique['x_mitre_contributors'])

        # Get list of tactic types
        if technique.get('x_mitre_tactic_type'):
            technique['x_mitre_tactic_type'].sort()
            technique_dict['tactic_type'] = ", ".join(technique['x_mitre_tactic_type'])

        # Get detection data
        if technique.get('x_mitre_detection'):
            technique_dict['detection'] = get_detection_string(technique['x_mitre_detection'], reference_list, next_reference_number)

        # Get if technique is detectable by common defenses
        if technique.get('x_mitre_detectable_by_common_defenses'):
            technique_dict['detectable'] = technique.get('x_mitre_detectable_by_common_defenses')

        # Get explanation of detecatable by common defenses
        if technique.get('x_mitre_detectable_by_common_defenses_explanation'):
            technique_dict['detectable_exp'] = util.replace_html_chars(technique['x_mitre_detectable_by_common_defenses_explanation'])

        # Get diffulty for adversaries
        if technique.get('x_mitre_difficulty_for_adversary'):
            technique_dict['diff_for_adv'] = technique['x_mitre_difficulty_for_adversary']

        # Get explanation of difficulty for adversaries
        if technique.get('x_mitre_difficulty_for_adversary_explanation'):
            technique_dict['diff_for_adv_exp'] = util.replace_html_chars(technique['x_mitre_difficulty_for_adversary_explanation'])            
        
        # Add reference for bottom part of technique page
        if reference_list:
            technique_dict['bottom_ref'] = util.sort_reference_list(reference_list)

        subs = config.technique_md.substitute(technique_dict)
        subs = subs + json.dumps(technique_dict)

        #Write out the markdown file
        with open(os.path.join(config.techniques_markdown_path, technique_dict['attack_id'] +".md"), "w", encoding='utf8') as md_file:
            md_file.write(subs)

def get_related_techniques_data(technique, tactic_list):
    """Given a technique and a tactic list, return data of related techniques.
       Data includes technique id/name and tactic name/id for each related
       technique
    """
    
    technique_data = []

    if config.related_techniques.get(technique['id']):
        for rel_tech in config.related_techniques[technique['id']]:

            attack_id = util.get_attack_id(rel_tech['object'])

            if attack_id:
                row = {}
                row['technique_id'] = attack_id

                tactic = [x for x in tactic_list if x['x_mitre_shortname'] == rel_tech['object']['kill_chain_phases'][0]['phase_name']][0]
                if tactic:
                    row['tactic_id'] = util.get_attack_id(tactic)
                row['tactic_name'] = rel_tech['object']['kill_chain_phases'][0]['phase_name'].title().replace('-', ' ')
                
                row['technique_name'] = rel_tech['object']['name']
                technique_data.append(row)

    if technique_data:
        technique_data = sorted(technique_data, key=lambda k: k['tactic_name'].lower())
    return technique_data

def get_mitigations_table_data(technique, reference_list, next_reference_number):
    """Given a technique a reference list, find mitigations that mitigate
       technique and return list with mitigation data. Also modifies the 
       reference list if it finds a reference that is not on the list
    """

    mitigation_data = []

    # Check if technique has mitigations
    if config.technique_mitigated.get(technique['id']):
        # Iterate through technique mitigations
        for mitigation in config.technique_mitigated[technique['id']]:

            # Do not add deprecated mitigation to table
            if 'x_mitre_deprecated' not in mitigation['object']:

                attack_id = util.get_attack_id(mitigation['object'])

                # Only add if mitigation attack id is found 
                if attack_id:

                    row = {}
                    row['mid'] = attack_id
                    row['name'] = mitigation['object']['name']
                    if mitigation['relationship'].get('description'):
                        # Get filtered description
                        row['descr'] = util.get_filtered_description(reference_list, next_reference_number, mitigation)
             
                    mitigation_data.append(row)
    
    if mitigation_data:
        mitigation_data = sorted(mitigation_data, key=lambda k: k['name'].lower())
    return mitigation_data
    
def get_examples_table_data(technique, reference_list, next_reference_number):
    """Given a technique object, find examples in malware using technique,
       tools using technique and groups using technique. Return list with
       example data
    """

    # Creating map to avoid repeating the code 3 times
    examples_map = [
        { 'example_type': config.tools_using_technique }, 
        { 'example_type': config.malware_using_technique },
        { 'example_type': config.groups_using_technique }
    ]

    example_data = []

    # Get malware or tools used by group
    for examples in examples_map:
        if examples['example_type'].get(technique.get('id')):
            for example in examples['example_type'][technique['id']]:

                attack_id = util.get_attack_id(example['object'])

                # Only add example data if the attack id is found    
                if attack_id:
                    row = {}

                    row['id'] = attack_id

                    if attack_id.startswith('S'):
                        row['path'] = "software"
                    else:
                        row['path'] = "groups"

                    row['name'] = example['object']['name']

                    if example['relationship'].get('description'):
                        # Get filtered description
                        row['descr'] = util.get_filtered_description(reference_list, next_reference_number, example)

                    example_data.append(row)
        
    if example_data:
        example_data = sorted(example_data, key=lambda k: k['name'].lower())
    return example_data

def get_technique_side_nav_data(techniques, tactics):
    """Responsible for generating the links that are located on the
       left side of individual technique domain pages
    """
    
    side_nav_data = []

    for domain in config.domains:

        # Get alias for domain
        domain_alias = util.get_domain_alias(domain.split("-")[0])

        domain_data = {
            "name": domain_alias,
            "id": domain.split("-")[0],
            "path": "/techniques/{}/".format(domain.split("-")[0]), # root level doesn't get a path
            "children": []
        }

        technique_list = get_techniques_list(techniques[domain])

        # Get tactics > techniques data
        for tactic in tactics[domain]:
            tactic_row = {}
            
            tactic_row['name'] = tactic['name']
            tactic_row['id'] = util.get_attack_id(tactic)
            tactic_row['path'] = "/tactics/{}".format(util.get_attack_id(tactic))
            
            tactic_row['children'] = []
            for technique in technique_list[tactic['x_mitre_shortname']]:
                technique_row = {}
                # Get technique id and name for each technique
                technique_row['name'] = technique['name']
                technique_row['id'] = technique['id']
                technique_row['path'] = "/techniques/{}/".format(technique['id'])
                technique_row['children'] = []
                # Add technique data to tactic
                tactic_row['children'].append(technique_row)
            
            domain_data['children'].append(tactic_row)
        
        side_nav_data.append(domain_data)
     
    return {
        "name": "techniques",
        "id": "techniques",
        "path": None, # root level doesn't get a path
        "children": side_nav_data
    }

def get_techniques_list(techniques):
    """This method is used to generate a list of techniques"""

    technique_list = {}
    
    for technique in techniques:
        if 'revoked' not in technique or technique['revoked'] == False:

            attack_id = util.get_attack_id(technique)

            if attack_id:

                technique_dict = {}
                technique_dict['id'] = attack_id
            
                technique_dict['name'] = technique['name']
                technique_dict['description'] = technique['description']

                if technique.get('kill_chain_phases'):
                    for elem in technique['kill_chain_phases']:
                        # Fill dict

                        if elem['phase_name'] not in technique_list:
                            technique_list[elem['phase_name']] = []
                            
                        technique_list[elem['phase_name']].append(technique_dict)

    for key, value in technique_list.items():
        technique_list[key] = sorted(technique_list[key], key=lambda k: k['name'].lower())
    
    return technique_list


def get_detection_string(detection, reference_list, next_reference_number):
    """Given the technique's detection string, replace the citations and
       add them to the reference_list is they are not found. Return
       modified detection string
    """

    citations_from_descr = util.get_citations_from_descr(detection)

    filtered_detection = util.replace_html_chars(markdown.markdown(detection))
    filtered_detection = util.filter_urls(filtered_detection)
    filtered_detection = util.get_descr_reference_sect(citations_from_descr, reference_list, next_reference_number, filtered_detection)
    
    return filtered_detection