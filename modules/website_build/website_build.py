import hashlib
import json
import os
import subprocess
from string import Template

from loguru import logger

import modules
from modules import matrices, site_config, util

from . import website_build_config


def generate_website():
    """Generate the website.

    This function:
        - generates base template for HTML pages
        - generates the index page of the website
        - runs pelican content to convert markdown pages into html
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
    generate_sidebar_html()
    generate_index_page()
    generate_static_pages()
    generate_changelog_page()
    store_pelican_settings()
    pelican_content()
    # this is nice to have if you want to run pelican manually later
    # remove_pelican_settings()


def generate_uuid_from_seeds(content_version, website_version):
    """
    Generate a UUID based on the given content_version and website_version.

    Args:
    - content_version (str): Semantic version of the content without a leading 'v'.
    - website_version (str): Semantic version of the website with a leading 'v'.

    Returns
    -------
    - str: A UUID generated based on the two versions.
    """
    # Combine and hash the values
    seed = f"{content_version}-{website_version}".encode("utf-8")
    hashed_seed = hashlib.md5(seed).hexdigest()

    # Convert the first 32 characters of the hash to a UUID format
    return "-".join([hashed_seed[i : i + length] for i, length in zip([0, 8, 12, 16, 20], [8, 4, 4, 4, 12])])


def generate_javascript_settings():
    """Create JavaScript settings file that will be used to other JavaScript files."""
    logger.info("Generating JavaScript settings.js")
    javascript_settings_file = os.path.join(site_config.javascript_path, "settings.js")

    # Check if file already exists
    # Copy all lines that do not have base_url in it
    data = ""
    if os.path.exists(javascript_settings_file):
        with open(javascript_settings_file, "r", encoding="utf8") as js_f:
            for line in js_f:
                if "base_url" not in line and "build_uuid" not in line:
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

        # Use the content and website versions as a seed for the build UUID to ensure that the UUID is idempotent.
        CONTENT_VERSION = website_build_config.base_page_data["CONTENT_VERSION"]
        WEBSITE_VERSION = website_build_config.base_page_data["WEBSITE_VERSION"]

        build_uuid = generate_uuid_from_seeds(CONTENT_VERSION, WEBSITE_VERSION)

        js_build_uuid = website_build_config.js_build_uuid.substitute({"build_uuid": build_uuid})
        js_data += js_build_uuid
        js_f.write(js_data)

        # Add trailing data
        js_f.write(data)


def generate_base_html():
    """Responsible for generating the header and footer of website pages."""
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
    ) as base_template_file:
        base_template_str = base_template_file.read()
        base_template = Template(base_template_str)
        subs = base_template.substitute(website_build_config.base_page_data)

    with open(os.path.join(website_build_config.template_dir, "base.html"), "w", encoding="utf8") as base_file:
        base_file.write(subs)


def generate_sidebar_html():
    """Create the sidebar html file."""
    with open(
        os.path.join(website_build_config.template_dir, "sidebar-resources-template.html"), "r", encoding="utf8"
    ) as sidebar_template_f:
        sidebar_template = sidebar_template_f.read()
        sidebar_template = Template(sidebar_template)
        subs = sidebar_template.substitute(website_build_config.sidebar_page_data)

    with open(
        os.path.join(website_build_config.template_dir, "sidebar-resources.html"), "w", encoding="utf8"
    ) as sidebar_template_f:
        sidebar_template_f.write(subs)


def generate_index_page():
    """Create the landing page."""
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
        "assets": "Asset",
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
    """Store pelican settings."""
    logger.info("Storing additional Pelican settings")
    pelican_settings_f = os.path.join(site_config.data_directory, "pelican_settings.json")
    with open(pelican_settings_f, "w", encoding="utf8") as json_f:
        json_f.write(json.dumps(site_config.staged_pelican))


def generate_changelog_page():
    """Responsible for compiling original changelog markdown into changelog markdown file for rendering on the HTML."""
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
    include_osano = site_config.INCLUDE_OSANO

    if site_config.args.google_analytics:
        google_analytics = site_config.args.google_analytics
    if site_config.args.google_site_verification:
        google_site_verification = site_config.args.google_site_verification
    if site_config.args.include_osano:
        include_osano = site_config.args.include_osano

    extra_settings = ""
    if google_analytics:
        extra_settings = f"{extra_settings} GOOGLE_ANALYTICS='\"{google_analytics}\"'"
    if google_site_verification:
        extra_settings = f"{extra_settings} GOOGLE_SITE_VERIFICATION='\"{google_site_verification}\"'"
    if include_osano:
        extra_settings = f"{extra_settings} INCLUDE_OSANO='\"{include_osano}\"'"

    if extra_settings:
        pelican_cmd = f"{pelican_cmd} -e {extra_settings}"

    logger.debug(f"{pelican_cmd=}")

    subprocess.check_output(pelican_cmd, shell=True)


def remove_pelican_settings():
    """Remove pelican settings."""
    logger.info("Removing additional Pelican settings")
    pelican_settings_f = os.path.join(site_config.data_directory, "pelican_settings.json")
    if os.path.isfile(pelican_settings_f):
        os.remove(pelican_settings_f)


def generate_static_pages():
    """Read markdown files from the static pages directory and copies them into the markdown directory."""
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
