import modules
from . import website_build_config
from . import subdirectory
from modules import util
from modules import matrices
from modules import site_config
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

    generate_javascript_settings()
    generate_base_html()
    generate_index_page()
    generate_static_pages()
    pelican_content()
    remove_unwanted_output()
    generate_subdirectory()

def generate_javascript_settings():
    """Creates javascript settings file that will be used to other javascript files"""

    javascript_settings_file = os.path.join(site_config.javascript_path, "settings.js")

    # Check if file already exists
    # Copy all lines that do not have base_url in it
    data = ""
    if os.path.exists(javascript_settings_file):
        with open(javascript_settings_file, "r", encoding='utf8') as js_f:
            for line in js_f:
                if not "base_url" in line:
                    # Copy line to data buffer
                    data += line

    with open(javascript_settings_file, "w", encoding='utf8') as js_f:
        # Get subdirectory path, will be empty if it was not declared
        web_dir = site_config.subdirectory
        if not web_dir.startswith("/"):
            web_dir = "/" + web_dir
        
        web_dir = web_dir.replace("\\", "/")

        if not web_dir.endswith("/"):
            web_dir = web_dir + "/"

        js_data = website_build_config.js_dir_settings.substitute({"web_directory": web_dir})
        js_f.write(js_data)
        # Add trailing data
        js_f.write(data)

def generate_base_html():
    """ Responsible for generating the header and footer of website pages """

    # Update navigation menu in the case that some module did not generate markdowns
    website_build_config.base_page_data['NAVIGATION_MENU'] = modules.menu_ptr

    with open(os.path.join(website_build_config.template_dir, "base-template.html"), "r", encoding='utf8') as base_template_f:
        base_template = base_template_f.read()
        base_template = Template(base_template)
        subs = base_template.substitute(website_build_config.base_page_data)

    with open(os.path.join(website_build_config.template_dir, "base.html"), "w", encoding='utf8') as base_template_f:
        base_template_f.write(subs)

def generate_index_page():
    """Responsible for creating the landing page"""
    data = {}

    # get index matrix data
    matrix = website_build_config.index_matrix
    data['matrix_name'] = matrix['name']
    data['matrix_descr'] = matrix['descr']
    data["matrices"], data["has_subtechniques"], data["tour_technique"] = matrices.matrices.get_sub_matrices(matrix)
    data['logo_landingpage'] = website_build_config.base_page_data['logo_landingpage']

    # Get list of routes for random page feature
    all_routes = {
        "matrices": "Matrix",
        "tactics": "Tactic",
        "techniques": "Technique",
        "mitigations": "Mitigation", 
        "groups": "Group",
        "software": "Software"
    }
    routes = {}

    if site_config.args.modules:
        for route in all_routes.keys():
            if route in site_config.args.modules:
                routes[route] = all_routes[route]
    else:
        routes = all_routes
    
    data['random_page_options'] = routes

    # Fill ATT&CK enterprise matrix of index pages
    subs = website_build_config.attack_index_md + json.dumps(data)

    with open(website_build_config.attack_index_path, "w", encoding='utf8') as md_file:
        md_file.write(subs)

def pelican_content():
    # Run pelican with limited output, -q is for quiet
    if site_config.subdirectory:
        subprocess.check_output(f"pelican content -q -o {site_config.web_directory}", shell=True)
    else:
        subprocess.check_output("pelican content -q", shell=True)
    
def remove_unwanted_output():
    """Remove unwanted files from the output directory"""

    # Files to be deleted:
    # archives.html, authors.html, categories.html, tags.html, 
    # author\blake-strom.html, category\cyber-threat-intelligence.html

    archives_path = os.path.join(site_config.web_directory, "archives.html")
    if os.path.exists(archives_path):
        os.remove(archives_path)
    
    authors_path = os.path.join(site_config.web_directory, "authors.html")
    if os.path.exists(authors_path):
        os.remove(authors_path)

    categories_path = os.path.join(site_config.web_directory, "categories.html")
    if os.path.exists(categories_path):
        os.remove(categories_path)
    
    tags_path = os.path.join(site_config.web_directory, "tags.html")
    if os.path.exists(tags_path):
        os.remove(tags_path)
    
    author_path = os.path.join(site_config.web_directory, "author")
    if os.path.exists(author_path):
        shutil.rmtree(author_path)
    
    category_path = os.path.join(site_config.web_directory, "category")
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

def generate_subdirectory():
    """ Build website to subdirectory """

    if site_config.args.subdirectory:
        subdirectory.replace()