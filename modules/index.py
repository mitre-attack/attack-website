import json
import os
from . import config
from . import stixhelpers
from . import util
from . import matrix as matrixhelpers

def generate():
    """Responsible for creating the landing page"""
    data = {}

    # get enterprise matrix data
    matrix = config.index_matrix
    techniques = stixhelpers.get_techniques(config.ms[matrix['matrix']])
    filtered_techniques = util.filter_techniques_by_platform(techniques, matrix['platforms'])

    data['matrix_name'] = matrix['name']
    data['matrix_descr'] = matrix['descr']

    data['matrix'] = matrixhelpers.get_matrix_data(filtered_techniques) 
    data['platforms'] = matrix['platforms']
    data['domain'] = matrix['matrix'].split("-")[0]

    data['tactics'] = []
    data['max_len'] = []

    data['logo_landingpage'] = config.settings_dict['logo_landingpage']

    matrices = stixhelpers.get_matrices(config.ms[matrix['matrix']])
    for curr_matrix in matrices:
        tactics = stixhelpers.get_tactic_list(config.ms[matrix['matrix']], matrix_id=curr_matrix['id'])
        data['tactics'].append(matrixhelpers.get_tactics_data(tactics))
        data['max_len'].append(matrixhelpers.get_max_length(data['matrix'], tactics))
    

    # Fill ATT&CK enterprise matrix of index pages
    subs = config.attack_index_md + json.dumps(data)

    with open(config.attack_index_path, "w", encoding='utf8') as md_file:
        md_file.write(subs)
