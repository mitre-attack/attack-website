import modules
from . import website_build_config
from modules import util
from string import Template
import json
import os
import shutil
import subprocess

def generate_website():
    """ Function that generates base template for HTML pages, 
        generates the index page of the website and
        runs pelican content to convert markdown pages into html
    """

    generate_base_html()
    generate_index_page()
    generate_static_pages()
    pelican_content()
    remove_unwanted_output()

def generate_base_html():
    """ Responsible for generating the header and footer of website pages """

    # Update navigation menu in the case that some module did not generate markdowns
    website_build_config.base_page_data['NAVIGATION_MENU'] = modules.menu_ptr

    with open(os.path.join(website_build_config.template_dir, "base.bak"), "r", encoding='utf8') as base_template_f:
        base_template = base_template_f.read()
        base_template = Template(base_template)
        subs = base_template.substitute(website_build_config.base_page_data)

    with open(os.path.join(website_build_config.template_dir, "base.html"), "w", encoding='utf8') as base_template_f:
        base_template_f.write(subs)

def generate_index_page():
    """Responsible for creating the landing page"""
    data = {}

    ms = util.relationshipgetters.get_ms()

    # get enterprise matrix data
    matrix = website_build_config.index_matrix
    techniques = util.stixhelpers.get_techniques(ms[matrix['matrix']])
    filtered_techniques = util.buildhelpers.filter_techniques_by_platform(techniques, matrix['platforms'])

    data['matrix_name'] = matrix['name']
    data['matrix_descr'] = matrix['descr']

    data['matrix'] = util.buildhelpers.get_matrix_data(filtered_techniques) 
    data['platforms'] = matrix['platforms']
    data['domain'] = matrix['matrix'].split("-")[0]

    data['tactics'] = []
    data['max_len'] = []

    matrices = util.stixhelpers.get_matrices(ms[matrix['matrix']])
    for curr_matrix in matrices:
        tactics = util.stixhelpers.get_tactic_list(ms[matrix['matrix']], matrix_id=curr_matrix['id'])
        data['tactics'].append(util.buildhelpers.get_tactics_data(tactics))
        data['max_len'].append(util.buildhelpers.get_max_length(data['matrix'], tactics))

    # Fill ATT&CK enterprise matrix of index pages
    subs = website_build_config.attack_index_md + json.dumps(data)

    with open(website_build_config.attack_index_path, "w", encoding='utf8') as md_file:
        md_file.write(subs)

def pelican_content():
    # Run pelican with limited output, -q is for quiet
    subprocess.check_output("pelican content -q", shell=True)

def remove_unwanted_output():
    """Remove unwanted files from the output directory"""

    # Files to be deleted:
    # archives.html, authors.html, categories.html, tags.html, 
    # author\blake-strom.html, category\cyber-threat-intelligence.html
    output_path = "output"

    archives_path = os.path.join(output_path, "archives.html")
    if os.path.exists(archives_path):
        os.remove(archives_path)
    
    authors_path = os.path.join(output_path, "authors.html")
    if os.path.exists(authors_path):
        os.remove(authors_path)

    categories_path = os.path.join(output_path, "categories.html")
    if os.path.exists(categories_path):
        os.remove(categories_path)
    
    tags_path = os.path.join(output_path, "tags.html")
    if os.path.exists(tags_path):
        os.remove(tags_path)
    
    author_path = os.path.join(output_path, "author")
    if os.path.exists(author_path):
        shutil.rmtree(author_path)
    
    category_path = os.path.join(output_path, "category")
    if os.path.exists(category_path):
        shutil.rmtree(category_path)

def generate_static_pages():
    """ Reads markdown files from the static pages directory and copies them into 
        the markdown directory
    """

    # Verify if content/pages directory exists
    if not os.path.isdir(website_build_config.website_build_markdown_path):
        os.mkdir(website_build_config.website_build_markdown_path)

    static_pages_dir = os.path.join('modules', website_build_config.module_name, 'static_pages')

    for static_page in os.listdir(static_pages_dir):

        with open(os.path.join(static_pages_dir, static_page), "r", encoding='utf8') as md:
            content = md.read()
            
            with open(os.path.join(website_build_config.website_build_markdown_path, static_page), "w", encoding='utf8') as md_file:
                md_file.write(content)