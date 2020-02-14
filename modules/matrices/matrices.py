import json
import os
import requests
import collections
import sys
import urllib3
# import stix2
import datetime
# from . import config
from modules import util
from modules.util import stixhelpers
from modules import site_config
from . import matrices_config

# def generate_matrices():
#     """ Generate matrices, return True if matrices was generated,
#         False if nothing was generated
#     """

    # First call to lazy loading
    # util.relationshipgetters.get_malware_used_by_matrices()

    # Call function to generate matrices
    # Return True if a group was generated, False if not

    # group_generated = True

    # if not group_generated:
        # util.buildhelpers.remove_module_from_menu(matrices_config.module_name)   
    

# suppress InsecureRequestWarning: Unverified HTTPS request is being made
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def generate_matrices():
    """Responsible for verifying matrix directory and generating index
       matrix markdown. 
    """

    # Verify if directory exists
    if not os.path.isdir(matrices_config.matrix_markdown_path):
        os.mkdir(matrices_config.matrix_markdown_path)
    
    # Write the matrix index.html page
    with open(os.path.join(matrices_config.matrix_markdown_path, "overview.md"), "w", encoding='utf8') as md_file:
        md_file.write(matrices_config.matrix_overview_md)
    
    old_ms = stixhelpers.get_old_stix_memory_stores()    

    side_menu_data = util.buildhelpers.get_side_menu_matrices(matrices_config.matrices)

    for matrix in matrices_config.matrices:
        if matrix["type"] == "external": continue # link to externally hosted matrix, don't create a page for it
        generate_matrix_md(matrix, old_ms, None, None, side_menu_data)


def generate_matrix_md(matrix, old_ms, techniques=None, old_techniques=None, side_menu_data=None):
    """Given a matrix, generates the matrix markdown"""
    
    data = {}
    data['menu'] = side_menu_data
    data['domain'] = matrix['matrix'].split("-")[0]

    ms = util.relationshipgetters.get_ms()

    # Optimization to only load on first matrix level
    # Path needs to be equal to the domain
    if matrix['path'] ==  data['domain']:
        techniques = stixhelpers.get_techniques(ms[matrix['matrix']])
        old_techniques = stixhelpers.get_techniques(old_ms[matrix['matrix']])

    # Filter techniques
    filtered_techniques = util.buildhelpers.filter_techniques_by_platform(techniques, matrix['platforms'])
    filtered_old_techniques = util.buildhelpers.filter_techniques_by_platform(old_techniques, matrix['platforms'])
    
    data['name'] = matrix['name']
    data['timestamp'] = get_timestamp(matrix['matrix'], filtered_techniques, filtered_old_techniques)
    data['matrix'] = get_matrix_data(filtered_techniques) 
    data['platforms'] = [ {"name": platform, "path": site_config.platform_to_path[platform] } for platform in matrix['platforms'] ]
    
    data['domain'] = matrix['matrix'].split("-")[0]
    data['descr'] = matrix['descr']
    data['path'] = matrix['path']
 
    data['tactics'] = []
    data['max_len'] = []

    matrices = stixhelpers.get_matrices(ms[matrix['matrix']])
    for curr_matrix in matrices:
        tactics = stixhelpers.get_tactic_list(ms[matrix['matrix']], matrix_id=curr_matrix['id'])
        data['tactics'].append(get_tactics_data(tactics))
        data['max_len'].append(get_max_length(data['matrix'], tactics))
    
    subs = matrices_config.matrix_md.substitute(data)
    subs = subs + json.dumps(data)

    with open(os.path.join(matrices_config.matrix_markdown_path, data['domain'] + "-" + matrix['name'] + ".md"), "w", encoding='utf8') as md_file:
        md_file.write(subs)

    for subtype in matrix['subtypes']:
        generate_matrix_md(subtype, old_ms, techniques, old_techniques, side_menu_data)

def get_tactics_data(tactics):
    """Given a tactics list, returns a tactics dictionary with the name and
       id of each tactic
    """

    tactics_data = {}
    for tactic in tactics:
        attack_id = util.buildhelpers.get_attack_id(tactic)

        if attack_id:
            tactic_dict = {}
            tactic_dict['name'] = tactic['name']
            tactic_dict['id'] = attack_id
            tactics_data[tactic['x_mitre_shortname']] = tactic_dict
    
    return tactics_data

def get_max_length(matrix, tactics):
    """Given a matrix and a tactics list, returns the maximum column size"""

    max_len = 0
    for tactic in tactics:
        if matrix.get(tactic['x_mitre_shortname']):
            if len(matrix[tactic['x_mitre_shortname']]) > max_len:
                max_len = len(matrix[tactic['x_mitre_shortname']])
    return max_len

def get_recent_date(date_string1, date_string2):
    """Given two dates, returns the newest date"""

    date1 = datetime.datetime.strptime(date_string1, "%Y-%m-%d %H:%M:%S.%f")
    try:
        date2 = datetime.datetime.strptime(date_string2, "%Y-%m-%d %H:%M:%S.%f")
    except:
        print(date_string2)
        quit()
    if date1 > date2:
        return date1.strftime('%Y-%m-%d %H:%M:%S.%f')
    return date2.strftime('%Y-%m-%d %H:%M:%S.%f')

def get_default_date(proposed_default_date, domain, platform=None):
    """Given a proposed date, returns the target date"""

    with open(os.path.join(site_config.stix_directory, 'old_dates.json'), 'r') as file:
        core = file.read()
    addressible = json.loads(core)
    if domain == 'enterprise-attack':
        if platform == None:
            platform = 'all'
        date = addressible[domain][platform]
        target_date = get_recent_date(proposed_default_date, date)
        addressible[domain][platform] = target_date
    else:
        date = addressible[domain]
        target_date = get_recent_date(proposed_default_date, date)
        addressible[domain] = target_date
    with open(os.path.join(site_config.stix_directory, 'old_dates.json'),'w') as file:
        file.write(json.dumps(addressible))

    return target_date

def get_timestamp(domain, techniques, old_techniques, platform=None):
    """Given current and old techniques, returns the timestamp of the most
       recent modified object
    """

    ql_current = {}
    for k in techniques:
        ql_current[k['id']] = k
    ql_old = {}
    for k in old_techniques:
        ql_old[k['id']] = k

    time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "+00:00"
    raw_changes = [{k:time_now} if k in ql_old.keys() else {k:str(ql_current[k]['created'])} for k in set(ql_old.keys())^set(ql_current.keys())]
    newest_date = datetime.datetime.min.strftime('%Y-%m-%d %H:%M:%S.%f')
    if len(newest_date) != 26:
        newest_date = '000' + newest_date

    for entry in raw_changes:
        newest_date = get_recent_date(newest_date, str(next(iter(entry.values()))[:-6]))

    newest_date = get_default_date(newest_date, domain, platform)

    return newest_date

def get_matrix_data(techniques):
    """Given a technique list, returns the a dictionary of techniques data
       under different 'phase_name', also known as tactics.
    """
    matrix = {}
    for technique in techniques:
        if ('revoked' not in technique or technique['revoked'] is False) and ('x_mitre_deprecated' not in technique or technique['x_mitre_deprecated'] is False):
            # Get attack id
            attack_id = util.buildhelpers.get_attack_id(technique)
            
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