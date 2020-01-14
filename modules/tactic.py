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
    """Responsible for verifying tactic directory and generating tactic 
       index markdown
    """

    # Verify if directory exists
    if not os.path.isdir(config.tactics_markdown_path):
        os.mkdir(config.tactics_markdown_path)

    for domain in config.domains:
        generate_domain_markdown(domain)

def generate_domain_markdown(domain):
    """Generate tactic index markdown for each domain and generates 
       shared data for tactics
    """
 
    # Reads the json attack STIX and creates a list of the ATTACK Techniques
    tactic_list = stixhelpers.get_tactic_list(config.ms[domain])

    # Get technique list of current domain
    technique_list = stixhelpers.get_techniques(config.ms[domain])

    # Filter sub-techniques from technique list
    technique_list_no_sub = util.filter_out_subtechniques(technique_list)

    # Write out the markdown file for overview of domain
    data = {
        'domain': domain.split("-")[0],
        'tactics_list_len': str(len(tactic_list))
    }

    side_menu_data = util.get_side_menu_data("tactics", "/tactics/", tactic_list, domain.split("-")[0])
    data['side_menu_data'] = side_menu_data
    data['tactics_table'] = get_domain_table_data(tactic_list)

    subs = config.tactic_domain_md.substitute(data)
    subs = subs + json.dumps(data)

    with open(os.path.join(config.tactics_markdown_path, data['domain'] + "-tactics.md"), "w", encoding='utf8') as md_file:
        md_file.write(subs)

    # Write the tactic index.html page
    with open(os.path.join(config.tactics_markdown_path, "overview.md"), "w", encoding='utf8') as i_md_file:
        i_md_file.write(config.tactic_overview_md)

    # Create the markdown for the enterprise groups in the STIX
    for tactic in tactic_list:
        generate_tactic_md(tactic, domain, tactic_list, technique_list_no_sub, side_menu_data)

def generate_tactic_md(tactic, domain, tactic_list, techniques, side_menu_data):
    """Generate markdown for given tactic"""

    attack_id = util.get_attack_id(tactic)
    
    # Add if attack id is found
    if attack_id:

        data = {}

        # Fill out data

        data['attack_id'] = attack_id
        data['name'] = tactic['name']
        data['name_lower'] = tactic['name'].lower()
        data['descr'] = markdown.markdown(tactic['description'])
        data['side_menu_data'] = side_menu_data
        data['domain'] = domain.split("-")[0]

        # Get techniques that are in the given tactic
        techniques_list = get_techniques_of_tactic(tactic, techniques)

        data['techniques_table'] = util.get_technique_table_data(tactic, techniques_list)
        data['techniques_table_len'] = str(len(techniques_list))

        subs = config.tactic_md.substitute(data)
        subs = subs + json.dumps(data)

        with open(os.path.join(config.tactics_markdown_path, data['attack_id'] + ".md"), "w", encoding='utf8') as md_file:
            md_file.write(subs)

def get_domain_table_data(tactic_list):
    """Given a tactic list, returns an array of jsons with tactic name, id 
       and their description
    """
    tactic_table = []
    
    # Set up the tactics table for a domain
    for tactic in tactic_list:
        attack_id = util.get_attack_id(tactic)

        if attack_id:
            # Create json and fill out with tactic data
            tactic_dict = {}
            tactic_dict['name'] = tactic['name']
            tactic_dict['tid'] = attack_id          
            tactic_dict['description'] = tactic['description'].split("\n")[0]
            tactic_table.append(tactic_dict)
    
    return tactic_table

def get_techniques_of_tactic(tactic, techniques):
    """Given a tactic and a full list of techniques, return techniques that
       appear inside of tactic
    """

    techniques_list = []

    for technique in techniques:
        for phase in technique['kill_chain_phases']:
            if phase['phase_name'] == tactic['x_mitre_shortname']:
                techniques_list.append(technique)

    techniques_list = sorted(techniques_list, key=lambda k: k['name'].lower())
    return techniques_list
