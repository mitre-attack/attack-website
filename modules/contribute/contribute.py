import json
import math
import os

from modules import util

from . import contribute_config
from .. import site_config


def generate_contribute():
    """Generate contribute page markdown"""

    # Create content pages directory if does not already exist
    util.buildhelpers.create_content_pages_dir()

    # Move templates to templates directory
    util.buildhelpers.move_templates(contribute_config.module_name, contribute_config.contribute_templates_path)

    # Generate redirections
    util.buildhelpers.generate_redirections(
        redirections_filename=contribute_config.contribute_redirection_location, redirect_md=site_config.redirect_md
    )

    ms = util.relationshipgetters.get_ms()
    contributors = util.stixhelpers.get_contributors(ms)

    if not contributors:
        util.buildhelpers.remove_module_from_menu(contribute_config.module_name)
        return

    data = {}

    data["contributors"] = []

    contributors_first_col = []
    contributors_second_col = []

    half = math.ceil((len(contributors)) / 2)
    list_size = len(contributors)

    for index in range(0, half):
        contributors_first_col.append(contributors[index])

    for index in range(half, list_size):
        contributors_second_col.append(contributors[index])

    data["contributors"].append(contributors_first_col)
    data["contributors"].append(contributors_second_col)

    subs = contribute_config.contribute_index_md + json.dumps(data)

    # Create directory if it does not exist
    if not os.path.isdir(contribute_config.contribute_markdown_path):
        os.mkdir(contribute_config.contribute_markdown_path)

    # Open markdown file for the contribute page
    with open(
        os.path.join(contribute_config.contribute_markdown_path, "contribute.md"), "w", encoding="utf8"
    ) as md_file:
        md_file.write(subs)
