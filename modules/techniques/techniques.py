import json
import os
import requests
import collections
import urllib3
import re
import markdown
from . import techniques_config
from modules import site_config
from modules import util

def generate_techniques():
    """ Generate techniques, return True if technique was generated,
        False if nothing was generated
    """

    # Create content pages directory if does not already exist
    util.buildhelpers.create_content_pages_dir()
    
    # Move templates to templates directory
    util.buildhelpers.move_templates(techniques_config.module_name, techniques_config.techniques_templates_path)

    # Verify if directory exists
    if not os.path.isdir(techniques_config.techniques_markdown_path):
        os.mkdir(techniques_config.techniques_markdown_path)
    
    # Generate redirections
    util.buildhelpers.generate_redirections(techniques_config.techniques_redirection_location)

    #Write the technique index.html page
    with open(os.path.join(techniques_config.techniques_markdown_path, "overview.md"), "w", encoding='utf8') as md_file:
        md_file.write(techniques_config.technique_overview_md)
    
    # To verify if a technique was generated
    technique_generated = False

    techniques_no_sub = {}
    tactics = {}

    ms = util.relationshipgetters.get_ms()

    for domain in site_config.domains:
        #Reads the STIX and creates a list of the ATT&CK Techniques
        techniques_no_sub[domain] = util.buildhelpers.filter_out_subtechniques(util.stixhelpers.get_techniques(ms[domain]))
        tactics[domain] = util.stixhelpers.get_tactic_list(ms[domain])

    for deprecated_domain in site_config.deprecated_domains:
        techniques_no_sub[deprecated_domain] = util.buildhelpers.filter_out_subtechniques(util.stixhelpers.get_techniques(ms[deprecated_domain]))
        tactics[deprecated_domain] = util.stixhelpers.get_tactic_list(ms[deprecated_domain])

    side_nav_data = get_technique_side_nav_data(techniques_no_sub, tactics)

    for domain in site_config.domains:
        check_if_generated = generate_domain_markdown(domain, techniques_no_sub, tactics, side_nav_data)
        if not technique_generated:
            if check_if_generated:
                technique_generated = True
    
    for deprecated_domain in site_config.deprecated_domains:
        generate_domain_markdown(deprecated_domain, techniques_no_sub, tactics, side_nav_data, deprecated=True)

    if not technique_generated:
        util.buildhelpers.remove_module_from_menu(techniques_config.module_name)   

def generate_domain_markdown(domain, techniques_no_sub, tactics, side_nav_data, deprecated=None):
    """Generate technique index markdown for each domain and generates 
       shared data for techniques
    """

    # Check if there is at least one technique
    if techniques_no_sub[domain]:

        techhnique_list_no_sub_no_deprecated = util.buildhelpers.filter_deprecated_revoked(techniques_no_sub[domain])

        data = {}

        data['domain'] = domain.split("-")[0]

        # Get technique table data and number of techniques
        data['technique_table'] = util.buildhelpers.get_technique_table_data(None, techhnique_list_no_sub_no_deprecated)
        data['technique_list_len'] = str(len(techhnique_list_no_sub_no_deprecated))
        data['subtechniques_len'] = util.buildhelpers.get_subtechnique_count(techhnique_list_no_sub_no_deprecated)

        # Get tactic-techniques table
        data['menu'] = side_nav_data

        if deprecated:
            data['deprecated'] = deprecated

        subs = techniques_config.technique_domain_md.substitute(data)
        subs = subs + json.dumps(data)

        with open(os.path.join(techniques_config.techniques_markdown_path, data['domain'] + "-techniques.md"), "w", encoding='utf8') as md_file:
            md_file.write(subs)

        # Create the markdown for techniques in the STIX
        for technique in techniques_no_sub[domain]:
            if 'revoked' not in technique or technique['revoked'] is False:
                generate_technique_md(technique, domain, side_nav_data, tactics[domain])
        
        return True
    
    return False

def generate_technique_md(technique, domain, side_nav_data, tactic_list):
    """Generetes markdown data for given technique"""

    attack_id = util.buildhelpers.get_attack_id(technique)

    # Only add technique if the attack id was found
    if attack_id:

        subtechniques_of = util.relationshipgetters.get_subtechniques_of()

        technique_dict = {}

        technique_dict['attack_id'] = attack_id
        technique_dict['domain'] = domain.split("-")[0]
        technique_dict['menu'] = side_nav_data
        technique_dict['name'] = technique.get('name')

        # Get subtechniques
        technique_dict['subtechniques'] = get_subtechniques(technique)

        # Generate data for technique
        technique_dict = generate_data_for_md(technique_dict, technique, tactic_list)

        subs = techniques_config.technique_md.substitute(technique_dict)
        path = technique_dict['attack_id']

        subs = subs + json.dumps(technique_dict)

        #Write out the technique markdown file
        with open(os.path.join(techniques_config.techniques_markdown_path, path + ".md"), "w", encoding='utf8') as md_file:
            md_file.write(subs)

        # Generate data for sub-techniques
        if technique_dict['subtechniques']:

            # Generate sub-technique markdown file for each sub technique
            subtechniques = subtechniques_of[technique["id"]]
            for subtechnique in subtechniques:
                sub_tech_dict = {}

                sub_tech_dict['domain'] = domain.split("-")[0]
                sub_tech_dict['menu'] = side_nav_data
                sub_tech_dict['parent_id'] = technique_dict['attack_id']
                sub_tech_dict['parent_name'] = technique.get('name')
                sub_tech_dict['subtechniques'] = technique_dict['subtechniques']

                sub_tech_dict = generate_data_for_md(sub_tech_dict, subtechnique['object'], tactic_list, True)

                subs = techniques_config.sub_technique_md.substitute(sub_tech_dict)
                path = sub_tech_dict['parent_id'] + "-" + sub_tech_dict['sub_number']

                subs = subs + json.dumps(sub_tech_dict)

                #Write out the technique markdown file
                with open(os.path.join(techniques_config.techniques_markdown_path, path + ".md"), "w", encoding='utf8') as md_file:
                    md_file.write(subs)
        

def generate_data_for_md(technique_dict, technique, tactic_list, is_sub_technique = False):
    """Given a technique or subtechnique, fill technique dictionary to create
       markdown file
    """

    technique_dict['name'] = technique.get('name')

    if is_sub_technique:
        technique_dict['attack_id'] = util.buildhelpers.get_attack_id(technique)
        technique_dict['sub_number'] = technique_dict['attack_id'].split(".")[1]
        technique_dict['is_subtechnique'] = True

    if technique_dict['attack_id']:
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
        reference_list = {'current_number': 0}
        
        # Get initial reference list from technique object
        reference_list = util.buildhelpers.update_reference_list(reference_list, technique)

        dates = util.buildhelpers.get_created_and_modified_dates(technique)
        
        if dates.get('created'):
            technique_dict['created'] = dates['created']

        if dates.get('modified'):
            technique_dict['modified'] = dates['modified']
        
        if technique.get('x_mitre_deprecated'):
            technique_dict['deprecated'] = True
        else:
            technique_dict['deprecated'] = False

        # Get technique description with citations
        if technique.get("description") and not technique_dict['deprecated']:

            technique_dict['descr'] = technique['description']
        
            # Get mitigation table
            technique_dict['mitigation_table'] = get_mitigations_table_data(technique, reference_list)
            
            # Get related techniques
            technique_dict['rel_techniques_table'] = get_related_techniques_data(technique, tactic_list)

            # Get examples
            technique_dict['examples_table'] = get_examples_table_data(technique, reference_list)

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
                technique_dict['detection'] = technique['x_mitre_detection']

            # Get if technique is detectable by common defenses
            if technique.get('x_mitre_detectable_by_common_defenses'):
                technique_dict['detectable'] = technique.get('x_mitre_detectable_by_common_defenses')

            # Get explanation of detecatable by common defenses
            if technique.get('x_mitre_detectable_by_common_defenses_explanation'):
                technique_dict['detectable_exp'] = util.buildhelpers.replace_html_chars(technique['x_mitre_detectable_by_common_defenses_explanation'])

            # Get diffulty for adversaries
            if technique.get('x_mitre_difficulty_for_adversary'):
                technique_dict['diff_for_adv'] = technique['x_mitre_difficulty_for_adversary']

            # Get explanation of difficulty for adversaries
            if technique.get('x_mitre_difficulty_for_adversary_explanation'):
                technique_dict['diff_for_adv_exp'] = util.buildhelpers.replace_html_chars(technique['x_mitre_difficulty_for_adversary_explanation'])            
            
            technique_dict['citations'] = reference_list

            technique_dict['versioning_feature'] = site_config.check_versions_module()
        
        else:
            if technique_dict['deprecated']:
                technique_dict['descr'] = technique.get('description')

        return technique_dict

def get_related_techniques_data(technique, tactic_list):
    """Given a technique and a tactic list, return data of related techniques.
       Data includes technique id/name and tactic name/id for each related
       technique
    """
    
    technique_data = []

    if util.relationshipgetters.get_technique_related_to_technique().get(technique['id']):
        for rel_tech in util.relationshipgetters.get_technique_related_to_technique()[technique['id']]:

            attack_id = util.buildhelpers.get_attack_id(rel_tech['object'])

            if attack_id:
                row = {}
                row['technique_id'] = attack_id

                tactic = [x for x in tactic_list if x['x_mitre_shortname'] == rel_tech['object']['kill_chain_phases'][0]['phase_name']][0]
                if tactic:
                    row['tactic_id'] = util.buildhelpers.get_attack_id(tactic)
                row['tactic_name'] = rel_tech['object']['kill_chain_phases'][0]['phase_name'].title().replace('-', ' ')
                
                row['technique_name'] = rel_tech['object']['name']
                technique_data.append(row)

    if technique_data:
        technique_data = sorted(technique_data, key=lambda k: k['tactic_name'].lower())
    return technique_data

def get_mitigations_table_data(technique, reference_list):
    """Given a technique a reference list, find mitigations that mitigate
       technique and return list with mitigation data. Also modifies the 
       reference list if it finds a reference that is not on the list
    """

    mitigation_data = []

    # Check if technique has mitigations
    if util.relationshipgetters.get_technique_mitigated_by_mitigation().get(technique['id']):
        # Iterate through technique mitigations
        for mitigation in util.relationshipgetters.get_technique_mitigated_by_mitigation()[technique['id']]:

            # Do not add deprecated mitigation to table
            if 'x_mitre_deprecated' not in mitigation['object']:

                attack_id = util.buildhelpers.get_attack_id(mitigation['object'])

                # Only add if mitigation attack id is found 
                if attack_id:

                    row = {}
                    row['mid'] = attack_id
                    row['name'] = mitigation['object']['name']
                    if mitigation['relationship'].get('description'):
                        # Get filtered description
                        reference_list = util.buildhelpers.update_reference_list(reference_list, mitigation['relationship'])
                        row['descr'] = mitigation['relationship']['description']
             
                    mitigation_data.append(row)
    
    if mitigation_data:
        mitigation_data = sorted(mitigation_data, key=lambda k: k['name'].lower())
    return mitigation_data
    
def get_examples_table_data(technique, reference_list):
    """Given a technique object, find examples in malware using technique,
       tools using technique and groups using technique. Return list with
       example data
    """

    # Creating map to avoid repeating the code 3 times
    examples_map = [
        { 'example_type': util.relationshipgetters.get_tools_using_technique() }, 
        { 'example_type': util.relationshipgetters.get_malware_using_technique() },
        { 'example_type': util.relationshipgetters.get_groups_using_technique() }
    ]

    example_data = []

    # Get malware or tools used by group
    for examples in examples_map:
        if examples['example_type'].get(technique.get('id')):
            for example in examples['example_type'][technique['id']]:

                attack_id = util.buildhelpers.get_attack_id(example['object'])

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
                        reference_list = util.buildhelpers.update_reference_list(reference_list, example['relationship'])
                        row['descr'] = example['relationship']['description']

                    example_data.append(row)
        
    if example_data:
        example_data = sorted(example_data, key=lambda k: k['name'].lower())
    return example_data

def get_technique_side_nav_data(techniques, tactics):
    """Responsible for generating the links that are located on the
       left side of individual technique domain pages
    """
    
    side_nav_data = []

    subtechniques_of = util.relationshipgetters.get_subtechniques_of()

    for domain in site_config.domains:

        # Get alias for domain
        domain_alias = util.buildhelpers.get_domain_alias(domain.split("-")[0])

        domain_data = {
            "name": domain_alias,
            "id": domain.split("-")[0],
            "path": "/techniques/{}/".format(domain.split("-")[0]), # root level doesn't get a path
            "children": []
        }

        technique_list = get_techniques_list(techniques[domain])

        for tactic in tactics[domain]:
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
                        child['name'] = subtechnique['object']['name']
                        child['id'] = util.buildhelpers.get_attack_id(subtechnique['object'])
                        sub_number = child["id"].split(".")[1]
                        child['path'] = "/techniques/{}/{}/".format(technique['id'], sub_number)
                        child['children'] = []
                        technique_row['children'].append(child)

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

def get_techniques_list(techniques):
    """This method is used to generate a list of techniques"""

    technique_list = {}
    
    for technique in techniques:
        if not technique.get('revoked') and not technique.get('x_mitre_deprecated'):

            attack_id = util.buildhelpers.get_attack_id(technique)

            if attack_id:

                technique_dict = {}
                technique_dict['id'] = attack_id
                technique_dict['stix_id'] = technique['id']
                technique_dict['name'] = technique['name']
                technique_dict['description'] = technique['description']

                if technique.get('kill_chain_phases'):
                    for elem in technique['kill_chain_phases']:
                        # Fill dict
                        if elem['phase_name'] not in technique_list:
                            technique_list[elem['phase_name']] = []
                            
                        technique_list[elem['phase_name']].append(technique_dict)

    for key, __ in technique_list.items():
        technique_list[key] = sorted(technique_list[key], key=lambda k: k['name'].lower())
    
    return technique_list

def get_subtechniques(technique):
    """Given a technique, return the ID and name of the subtechnique"""

    subtechs = []
    attack_id = util.buildhelpers.get_attack_id(technique)

    subtechniques_of = util.relationshipgetters.get_subtechniques_of()

    if technique["id"] in subtechniques_of:
        subtechniques = subtechniques_of[technique["id"]]
        for subtechnique in subtechniques:
            sub_data = {}
            sub_data['stix_id'] = technique['id']
            sub_data['name'] = subtechnique['object']['name']
            sub_data['id'] = util.buildhelpers.get_attack_id(subtechnique['object'])
            sub_number = sub_data["id"].split(".")[1]
            attack_id = util.buildhelpers.get_attack_id(technique)
            sub_data['path'] = "/techniques/{}/{}/".format(attack_id, sub_number)
            subtechs.append(sub_data)
    
    return sorted(subtechs, key=lambda k: k['id'])