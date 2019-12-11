import json
import os
import requests
import collections
import sys
import urllib3
import stix2
import datetime
from . import config
from . import stixhelpers
from . import  util

# suppress InsecureRequestWarning: Unverified HTTPS request is being made
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def generate():
    """Responsible for verifying matrix directory and generating index
       matrix markdown
    """

    # Verify if directory exists
    if not os.path.isdir(config.matrix_markdown_path):
        os.mkdir(config.matrix_markdown_path)
    
    # Write the matrix index.html page
    with open(os.path.join(config.matrix_markdown_path, "overview.md"), "w", encoding='utf8') as md_file:
        md_file.write(config.matrix_overview_md)
    
    # Read old json attack STIX 
    old_ms = stixhelpers.get_old_stix_memory_stores()

    side_menu_data = util.get_side_menu_matrices(config.matrices)

    for matrix in config.matrices:
        generate_platform_matrices(matrix, side_menu_data)

def generate_platform_matrices(matrix, side_menu_data=None):
    """Given a matrix, generates the matrix markdown"""
    
    data = {}
    data['menu'] = side_menu_data
    data['domain'] = matrix['matrix'].split("-")[0]
    data['name'] = matrix['name']
    data['platforms'] = [ {"name": platform, "path": config.platform_to_path[platform] } for platform in matrix['platforms'] ] 
    data['matrices'], data["has_subtechniques"] = get_sub_matrices(matrix)
    data['path'] = matrix['path']
    
    subs = config.matrix_md.substitute(data)
    subs = subs + json.dumps(data)

    with open(os.path.join(config.matrix_markdown_path, data['domain'] + "-" + matrix['name'] + ".md"), "w", encoding='utf8') as md_file:
        md_file.write(subs)

    for subtype in matrix['subtypes']:
        generate_platform_matrices(subtype, side_menu_data)

def get_sub_matrices(matrix):
    # memorystore for the current domain
    domain_ms = config.ms[matrix['matrix']]
    # get relevant techniques
    techniques = stixhelpers.get_techniques(domain_ms)
    platform_techniques = util.filter_techniques_by_platform(techniques, matrix['platforms'])
    platform_techniques = util.filter_out_subtechniques(platform_techniques)
    # get relevant tactics
    all_tactics = stixhelpers.get_all_of_type(domain_ms, "x-mitre-tactic")
    tactic_id_to_shortname = { tactic["id"]: tactic["x_mitre_shortname"] for tactic in all_tactics }
    
    has_subtechniques = False #track whether the current matrix has subtechniques

    # helper functions
    def phase_names(technique):
        """get kill chain phase names from the given technique"""
        return [ phase["phase_name"] for phase in technique["kill_chain_phases"] ]
    
    def transform_technique(technique):
        """transform a technique object into the format required by the matrix macro"""
        obj = {
            "id": technique["id"],
            "name": technique["name"],
            "url": technique["external_references"][0]["url"].split("attack.mitre.org")[1]
        }

        if technique["id"] in config.subtechniques_of:
            subtechniques = config.subtechniques_of[technique["id"]]
            obj["subtechniques"] = list(map(lambda st: transform_technique(st["object"]), subtechniques))
            nonlocal has_subtechniques
            has_subtechniques = True
        return obj

    def techniques_in_tactic(tactic_id):
        """helper function mapping a tactic_id
           to a structured tactic object including the (filtered) techniques 
           in the tactic"""
                
        # filter platform techniques to those inside of this tactic
        techniques = list(filter(lambda technique: tactic_id_to_shortname[tactic_id] in phase_names(technique), platform_techniques))
        # transform into format required by matrix macro
        return list(map(lambda t: transform_technique(t), techniques))
    
    def transform_tactic(tactic_id):
        """transform a tactic object into the format required by the matrix macro"""
        tactic_obj = list(filter(lambda t: t["id"] == tactic_id, all_tactics))[0]
        return {
            "id": tactic_id,
            "name": tactic_obj["name"],
            "url": tactic_obj["external_references"][0]["url"].split("attack.mitre.org")[1],
            "techniques": techniques_in_tactic(tactic_id),
        }

    data = []
    sub_matrices = stixhelpers.get_matrices(domain_ms)
    for sub_matrix in sub_matrices:
        # get tactics for the matrix
        tactics = list(map(lambda tid: transform_tactic(tid), sub_matrix["tactic_refs"]))
        # filter out empty tactics
        tactics = list(filter(lambda t: len(t["techniques"]) > 0, tactics))
        data.append({
            "name": sub_matrix["name"],
            "description": sub_matrix["description"],
            "tactics": tactics,
        })
        
    return data, has_subtechniques
