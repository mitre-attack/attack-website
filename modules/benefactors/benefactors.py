import os

from modules import util

from . import benefactors_config


def generate_benefactors():
    """Generate benefactors page markdown"""
    # Create content pages directory if does not already exist
    util.buildhelpers.create_content_pages_dir()

    # Move templates to templates directory
    util.buildhelpers.move_templates(benefactors_config.module_name, benefactors_config.benefactors_templates_path)

    # Create directory if it does not exist
    if not os.path.isdir(benefactors_config.benefactors_markdown_path):
        os.mkdir(benefactors_config.benefactors_markdown_path)

    benefactors_md = benefactors_config.benefactors_md

    # write markdown to file
    with open(
        os.path.join(benefactors_config.benefactors_markdown_path, "benefactors.md"), "w", encoding="utf8"
    ) as md_file:
        md_file.write(benefactors_md)
