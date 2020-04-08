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
    data["matrices"], data["has_subtechniques"], data["tour_technique"] = matrixhelpers.get_sub_matrices(matrix)

    # substitute into template
    subs = config.attack_index_md + json.dumps(data)

    with open(config.attack_index_path, "w", encoding='utf8') as md_file:
        md_file.write(subs)

def javascript_settings():
    """Creates javascript settings file that will be used to other javascript files"""

    javascript_settings_file = os.path.join(config.javascript_path, "settings.js")

    with open(javascript_settings_file, "w", encoding='utf8') as js_f:

        web_dir = config.web_directory
        if not web_dir.startswith("/"):
            web_dir = "/" + web_dir
        
        web_dir = web_dir.replace("\\", "/")

        if not web_dir.endswith("/"):
            web_dir = "/" + web_dir

        js_data = config.js_settings.substitute({"web_directory": web_dir})
        js_f.write(js_data)