import json
import os
import shutil
import subprocess
import uuid
from string import Template

from loguru import logger

import modules
from modules import matrices, site_config, util

from . import website_build_config


def generate_website():
    """Function that generates base template for HTML pages,
    generates the index page of the website and
    runs pelican content to convert markdown pages into html
    """
    logger.info("Generating the website")
    # Create content pages directory if does not already exist
    util.buildhelpers.create_content_pages_dir()

    # Verify if resources directory exists
    if not os.path.isdir(site_config.resources_markdown_path):
        os.mkdir(site_config.resources_markdown_path)

    util.buildhelpers.move_templates(
        website_build_config.module_name, website_build_config.website_build_templates_path
    )
    generate_javascript_settings()
    generate_base_html()
    generate_index_page()
    generate_static_pages()
    generate_faq_page()
    generate_changelog_page()
    store_pelican_settings()
    override_colors()
    pelican_content()
    reset_override_colors()
    # this is nice to have if you want to run pelican manually later
    # remove_pelican_settings()
    remove_unwanted_output()


def generate_javascript_settings():
    """Creates javascript settings file that will be used to other javascript files"""
    logger.info("Generating JavaScript settings.js")
    javascript_settings_file = os.path.join(site_config.javascript_path, "settings.js")

    # Check if file already exists
    # Copy all lines that do not have base_url in it
    data = ""
    if os.path.exists(javascript_settings_file):
        with open(javascript_settings_file, "r", encoding="utf8") as js_f:
            for line in js_f:
                if not "base_url" in line and not "build_uuid" in line:
                    # Copy line to data buffer
                    data += line

    with open(javascript_settings_file, "w", encoding="utf8") as js_f:
        # Get subdirectory path, will be empty if it was not declared
        web_dir = site_config.subdirectory
        if not web_dir.startswith("/"):
            web_dir = "/" + web_dir

        web_dir = web_dir.replace("\\", "/")

        if not web_dir.endswith("/"):
            web_dir = web_dir + "/"

        js_data = website_build_config.js_dir_settings.substitute({"web_directory": web_dir})

        build_uuid = str(uuid.uuid4())
        js_build_uuid = website_build_config.js_build_uuid.substitute({"build_uuid": build_uuid})

        js_data += js_build_uuid

        js_f.write(js_data)

        # Add trailing data
        js_f.write(data)


def generate_base_html():
    """Responsible for generating the header and footer of website pages"""
    logger.info("Generating base.html from template")
    # Update navigation menu in the case that some module did not generate markdowns
    website_build_config.base_page_data["NAVIGATION_MENU"] = modules.menu_ptr
    website_build_config.base_page_data["ATTACK_BRANDING"] = site_config.args.attack_brand
    website_build_config.base_page_data["RESOURCES"] = [
        key["module_name"] for key in modules.run_ptr if key["module_name"] == "resources"
    ]

    banner_enabled = site_config.BANNER_ENABLED
    # if banner was disabled as a command line argument
    if site_config.args.banner_disable:
        banner_enabled = False
    website_build_config.base_page_data["BANNER_ENABLED"] = banner_enabled

    banner_message = site_config.BANNER_MESSAGE
    # if banner message has been passed in via command line argument
    if site_config.args.banner:
        banner_message = site_config.args.banner
    website_build_config.base_page_data["BANNER_MESSAGE"] = banner_message

    logger.debug(f"{banner_enabled=}")
    logger.debug(f"{banner_message=}")

    if site_config.args.attack_brand:
        if website_build_config.base_page_data["BANNER_MESSAGE"].startswith("This is a custom instance"):
            website_build_config.base_page_data["BANNER_ENABLED"] = False

    with open(
        os.path.join(website_build_config.template_dir, "base-template.html"), "r", encoding="utf8"
    ) as base_template_f:
        base_template = base_template_f.read()
        base_template = Template(base_template)
        subs = base_template.substitute(website_build_config.base_page_data)

    with open(os.path.join(website_build_config.template_dir, "base.html"), "w", encoding="utf8") as base_template_f:
        base_template_f.write(subs)


def generate_index_page():
    """Responsible for creating the landing page"""
    logger.info("Generating index page")
    data = {}

    # get index matrix data
    matrix = website_build_config.index_matrix
    data["matrix_name"] = matrix["name"]
    data["matrix_descr"] = matrix["descr"]
    data["matrices"], data["has_subtechniques"], data["tour_technique"] = matrices.matrices.get_sub_matrices(matrix)
    data["logo_landingpage"] = website_build_config.base_page_data["logo_landingpage"]
    data["attack_branding"] = site_config.args.attack_brand
    data["resources"] = [key["module_name"] for key in modules.run_ptr if key["module_name"] == "resources"]

    # Get list of routes for random page feature
    all_routes = {
        "matrices": "Matrix",
        "tactics": "Tactic",
        "techniques": "Technique",
        "datasources": "Data Source",
        "mitigations": "Mitigation",
        "groups": "Group",
        "software": "Software",
        "campaigns": "Campaign",
    }
    routes = {}

    if site_config.args.modules:
        for route in all_routes.keys():
            if route in site_config.args.modules:
                routes[route] = all_routes[route]
    else:
        routes = all_routes

    data["random_page_options"] = routes

    # Fill ATT&CK enterprise matrix of index pages
    subs = website_build_config.attack_index_md + json.dumps(data)

    with open(website_build_config.attack_index_path, "w", encoding="utf8") as md_file:
        md_file.write(subs)


def store_pelican_settings():
    """Store pelican settings"""
    logger.info("Storing additional Pelican settings")
    pelican_settings_f = os.path.join(site_config.data_directory, "pelican_settings.json")
    with open(pelican_settings_f, "w", encoding="utf8") as json_f:
        json_f.write(json.dumps(site_config.staged_pelican))


def override_colors():
    """Override colors scss file if attack brand flag is enabled"""
    if site_config.args.attack_brand:
        logger.info("Overriding colors for attack-brand")
        colors_scss_f = os.path.join(site_config.static_style_dir, "_colors.scss")

        temp_file = ""
        with open(colors_scss_f, "r", encoding="utf8") as colors_f:
            lines = colors_f.readlines()

            end_search = True
            for line in lines:
                if end_search and line.startswith("//$use_attack_them"):
                    temp_file += line[2:]
                elif end_search and line.startswith("// end search"):
                    end_search = False
                    temp_file += line
                else:
                    temp_file += line

        with open(colors_scss_f, "w", encoding="utf8") as colors_f:
            colors_f.write(temp_file)


def reset_override_colors():
    """Reset override colors scss file if attack brand flag is enabled"""
    if site_config.args.attack_brand:
        logger.info("Resetting override colors for using attack-brand")
        colors_scss_f = os.path.join(site_config.static_style_dir, "_colors.scss")

        temp_file = ""
        with open(colors_scss_f, "r", encoding="utf8") as colors_f:
            lines = colors_f.readlines()

            end_search = True
            for line in lines:
                if end_search and line.startswith("$use_attack_them"):
                    temp_file += "//" + line
                elif end_search and line.startswith("// end search"):
                    end_search = False
                    temp_file += line
                else:
                    temp_file += line

        with open(colors_scss_f, "w", encoding="utf8") as colors_f:
            colors_f.write(temp_file)


def generate_faq_page():
    """Responsible for compiling faq json into faq markdown file for rendering on the HMTL."""
    logger.info("Generating FAQ page")
    # load faq data from json
    with open(os.path.join(site_config.data_directory, "faq.json"), "r", encoding="utf8") as f:
        faqdata = json.load(f)
    # add unique IDs
    for i, section in enumerate(faqdata["sections"]):
        for j, item in enumerate(section["questions"]):
            item["id"] = f"faq-{i}-{j}"

    # get markdown
    faq_content = website_build_config.faq_md + json.dumps(faqdata)
    # write markdown to file
    with open(os.path.join(site_config.resources_markdown_path, "faq.md"), "w", encoding="utf8") as md_file:
        md_file.write(faq_content)


def generate_changelog_page():
    """Responsible for compiling original changelog markdown into changelog markdown file
    for rendering on the HTML
    """
    logger.info("Generating Changelog page")
    current_changelog = None
    # Read local changelog
    with open("CHANGELOG.md", "r", encoding="utf8") as f:
        current_changelog = f.read()

    changelog_md = website_build_config.changelog_md + current_changelog

    with open(os.path.join(site_config.resources_markdown_path, "changelog.md"), "w", encoding="utf8") as md_file:
        md_file.write(changelog_md)


def pelican_content():
    logger.info("Building website with Pelican")
    pelican_cmd = "pelican content"

    if site_config.subdirectory:
        pelican_cmd = f"{pelican_cmd} -o {site_config.web_directory}"

    google_analytics = site_config.GOOGLE_ANALYTICS
    google_site_verification = site_config.GOOGLE_SITE_VERIFICATION

    if site_config.args.google_analytics:
        google_analytics = site_config.args.google_analytics
    if site_config.args.google_site_verification:
        google_site_verification = site_config.args.google_site_verification

    extra_settings = ""
    if google_analytics:
        extra_settings = f"{extra_settings} GOOGLE_ANALYTICS='\"{google_analytics}\"'"
    if google_site_verification:
        extra_settings = f"{extra_settings} GOOGLE_SITE_VERIFICATION='\"{google_site_verification}\"'"

    if extra_settings:
        pelican_cmd = f"{pelican_cmd} -e {extra_settings}"

    logger.debug(f"{pelican_cmd=}")

    subprocess.check_output(pelican_cmd, shell=True)


def remove_pelican_settings():
    """Remove pelican settings"""
    logger.info("Removing additional Pelican settings")
    pelican_settings_f = os.path.join(site_config.data_directory, "pelican_settings.json")
    if os.path.isfile(pelican_settings_f):
        os.remove(pelican_settings_f)


def remove_unwanted_output():
    """Remove unwanted files from the output directory"""
    logger.info("Removing unwanted files from the output directory")
    # Files to be deleted:
    # archives.html, authors.html, categories.html, tags.html,
    # author\blake-strom.html, category\cyber-threat-intelligence.html

    archives_path = os.path.join(site_config.web_directory, "archives.html")
    authors_path = os.path.join(site_config.web_directory, "authors.html")
    categories_path = os.path.join(site_config.web_directory, "categories.html")
    tags_path = os.path.join(site_config.web_directory, "tags.html")
    author_path = os.path.join(site_config.web_directory, "author")
    category_path = os.path.join(site_config.web_directory, "category")

    if os.path.exists(archives_path):
        logger.debug(f"Removing: {archives_path}")
        os.remove(archives_path)

    if os.path.exists(authors_path):
        logger.debug(f"Removing: {authors_path}")
        os.remove(authors_path)

    if os.path.exists(categories_path):
        logger.debug(f"Removing: {categories_path}")
        os.remove(categories_path)

    if os.path.exists(tags_path):
        logger.debug(f"Removing: {tags_path}")
        os.remove(tags_path)

    if os.path.exists(author_path):
        logger.debug(f"Removing: {author_path}")
        shutil.rmtree(author_path)

    if os.path.exists(category_path):
        logger.debug(f"Removing: {category_path}")
        shutil.rmtree(category_path)


def generate_static_pages():
    """Reads markdown files from the static pages directory and copies them into
    the markdown directory
    """
    logger.info("Generating static pages")
    # Verify if content/pages directory exists
    if not os.path.isdir(website_build_config.website_build_markdown_path):
        os.mkdir(website_build_config.website_build_markdown_path)

    static_pages_dir = os.path.join("modules", website_build_config.module_name, "static_pages")

    for static_page in os.listdir(static_pages_dir):
        with open(os.path.join(static_pages_dir, static_page), "r", encoding="utf8") as md:
            content = md.read()

            with open(
                os.path.join(website_build_config.website_build_markdown_path, static_page), "w", encoding="utf8"
            ) as md_file:
                md_file.write(content)
