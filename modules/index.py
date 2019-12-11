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
    # labels
    data['matrix_name'] = matrix['name']
    data['matrix_descr'] = matrix['descr']
    # layout
    data["matrices"], data["has_subtechniques"] = matrixhelpers.get_sub_matrices(matrix)

    # substitute into template
    subs = config.attack_index_md + json.dumps(data)

    with open(config.attack_index_path, "w", encoding='utf8') as md_file:
        md_file.write(subs)
