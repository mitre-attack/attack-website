import json
import os
import urllib3
import re
import markdown
from . import config
from . import stixhelpers
from . import util

def generate():
    """Responsible for verifying mitigation directory and generating index
       mitigation markdown
    """

    # Verify if directory exists
    if not os.path.isdir(config.mitigation_markdown_path):
        os.mkdir(config.mitigation_markdown_path)

    # Create the mitigation index markdown
    with open(os.path.join(config.mitigation_markdown_path, "overview.md"), "w", encoding='utf8') as md_file:
        md_file.write(config.mitigation_overview_md)

    mitigations = {}

    for domain in config.domains:
        #Reads the STIX and creates a list of the ATT&CK mitigations
        mitigations[domain] = stixhelpers.get_mitigation_list(config.ms[domain])

    # Amount of characters per category
    group_by = 3

    side_nav_data = util.get_side_nav_domains_data("mitigations", mitigations)
    side_nav_mobile_data = util.get_side_nav_domains_mobile_view_data("mitigations", mitigations, group_by)
    
    for domain in config.domains:
        generate_markdown_files(domain, mitigations[domain], side_nav_data, side_nav_mobile_data)

def generate_markdown_files(domain, mitigations, side_nav_data, side_nav_mobile_data):
    """Responsible for generating shared data between all mitigation pages
       and begins mitigation markdown generation
    """

    data = {}

    if mitigations:

        data['domain'] = domain.split("-")[0]
        data['mitigation_list_len'] = str(len(mitigations))
        data['side_menu_data'] = side_nav_data
        data['side_menu_mobile_view_data'] = side_nav_mobile_data
                        
        data['mitigation_table'] = get_mitigation_table_data(mitigations)

        subs = config.mitigation_domain_md.substitute(data)
        subs = subs + json.dumps(data)

        with open(os.path.join(config.mitigation_markdown_path, data['domain'] + "-mitigations.md"), "w", encoding='utf8') as md_file:
            md_file.write(subs)

        # Generates the markdown files to be used for page generation
        for mitigation in mitigations:
            generate_mitigation_md(mitigation, domain, side_nav_data, side_nav_mobile_data)

def generate_mitigation_md(mitigation, domain, side_menu_data, \
                                                       side_menu_mobile_data):
    """Generates the markdown for the given mitigation"""

    attack_id = util.get_attack_id(mitigation)

    if attack_id:
        data = {}

        data['attack_id'] = attack_id

        data['domain'] = domain.split("-")[0]
        data['side_menu_data'] = side_menu_data
        data['side_menu_mobile_view_data'] = side_menu_mobile_data
        data['name'] = mitigation['name']

        dates = util.get_created_and_modified_dates(mitigation)
        
        if dates.get('created'):
            data['created'] = dates['created']

        if dates.get('modified'):
            data['modified'] = dates['modified']

        # Get initial reference list
        reference_list = []
        # Decleared as an object to be able to pass by reference
        next_reference_number = {}
        next_reference_number['value'] = 1
        reference_list = util.update_reference_list(reference_list, mitigation)

        if mitigation.get('description'):
            citations_from_descr = util.get_citations_from_descr(mitigation['description'])

            data['descr'] = markdown.markdown(mitigation['description'])\
                                        .replace("\n", "<br>")\
                                        .replace("{", "{{")\
                                        .replace("}", "}}")\
                                        .replace("”","\"")\
                                        .replace("“","\"")

            data['descr'] = util.filter_urls(data['descr'])
            data['descr'] = util.get_descr_reference_sect(citations_from_descr, reference_list, next_reference_number, data['descr'])

        if mitigation.get('x_mitre_deprecated'):
            data['deprecated'] = True
        if mitigation.get('x_mitre_version'):
            data['version'] = mitigation["x_mitre_version"]

        data['techniques_addressed_data'] = get_techniques_addressed_data(mitigation, reference_list, next_reference_number)
    
        if reference_list:
            data['bottom_ref'] = util.sort_reference_list(reference_list)

        subs = config.mitigation_md.substitute(data)
        subs = subs + json.dumps(data)

        with open(os.path.join(config.mitigation_markdown_path, data['attack_id'] + ".md"), "w", encoding='utf8') as md_file:
            md_file.write(subs)

def get_mitigation_table_data(mitigation_list):
    """Given a list of mitigations, returns the data to build
       table on HTML
    """

    mitigation_data = []
    
    # Fill mitigation data
    for mitigation in mitigation_list:
        attack_id = util.get_attack_id(mitigation)

        if attack_id:
            row = {}

            row['id'] = attack_id

            row['name'] = mitigation['name']

            descr = re.sub(' \((Citation:.*?)\)', '', mitigation['description'], flags=re.MULTILINE)
            descr = re.sub('\((Citation:.*?)\)', '', descr, flags=re.MULTILINE)
            if descr.split("\n")[0] == '### Windows':
                descr = markdown.markdown(descr.split("\n")[2])
            else:
                descr = markdown.markdown(descr.split("\n")[0])
            row['descr'] = util.filter_urls(descr)

            if mitigation.get('x_mitre_deprecated'):
                row['deprecated'] = True

            mitigation_data.append(row)
                
    return mitigation_data
    
def get_techniques_addressed_data(mitigation, reference_list, next_reference_number):
    """Given a mitigation, returns a list of techniques addressed by 
       the mitigation
    """
    
    technique_list = {}
    for technique in config.mitigates_techniques.get(mitigation['id']):
        technique_list = util.technique_used_helper(technique_list, technique, reference_list, next_reference_number)            
    
    technique_data = []
    for item in technique_list:
        technique_data.append(technique_list[item])
    # Sort by technique name
    technique_data = sorted(technique_data, key=lambda k: k['name'].lower())

    # Sort by domain name
    technique_data = sorted(technique_data, key=lambda k: [config.custom_alphabet.index(c) for c in k['domain'].lower()])
    return technique_data