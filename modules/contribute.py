import math
import json
import os
from . import config
from . import stixhelpers

def generate():
    """Generate contribute page markdown"""
    
    contributors = stixhelpers.get_contributors(config.ms)

    data = {}

    data['contributors'] = []

    contributors_first_col = []
    contributors_second_col = []

    half = math.ceil((len(contributors))/2)
    list_size = len(contributors)

    for index in range(0, half):
        contributors_first_col.append(contributors[index])
    
    for index in range(half, list_size):
        contributors_second_col.append(contributors[index])

    data['contributors'].append(contributors_first_col)
    data['contributors'].append(contributors_second_col)

    subs = config.contribute_index_md + json.dumps(data)

    #Open markdown file for the contribute page
    with open(os.path.join(config.contribute_markdown_path, "contribute.md"), "w", encoding='utf8') as md_file:
        md_file.write(subs)