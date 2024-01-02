import json
import math
import os
import shutil
from datetime import datetime
from pathlib import Path

from loguru import logger
from mitreattack.attackToExcel import attackToExcel

import modules
from modules import site_config, util

from . import resources_config


def generate_resources():
    """Responsible for generating the resources pages."""
    logger.info("Generating Resources")
    # Create content pages directory if does not already exist
    util.buildhelpers.create_content_pages_dir()

    # Verify if resources directory exists
    if not os.path.isdir(site_config.resources_markdown_path):
        os.mkdir(site_config.resources_markdown_path)

    # Verify if resources directory exists
    if not os.path.isdir(resources_config.updates_markdown_path):
        os.mkdir(resources_config.updates_markdown_path)

    # Verify if versions module is in the running pool, if not remove it.
    build_versions_module = False
    for module_info in modules.run_ptr:
        if module_info["module_name"] == "versions":
            build_versions_module = True
    if not build_versions_module:
        for i, child in enumerate(site_config.resource_nav["children"]):
            if site_config.resource_nav["children"][i]["id"] == "versions":
                del site_config.resource_nav["children"][i]

    build_benefactors_module = False
    for module_info in modules.run_ptr:
        if module_info["module_name"] == "benefactors":
            build_benefactors_module = True
    if not build_benefactors_module:
        for i, child in enumerate(site_config.resource_nav["children"]):
            if site_config.resource_nav["children"][i]["id"] == "benefactors":
                del site_config.resource_nav["children"][i]

    # Move templates to templates directory
    util.buildhelpers.move_templates(resources_config.module_name, resources_config.resources_templates_path)
    copy_docs(module_docs_path=resources_config.docs_path)
    generate_working_with_attack()
    generate_general_information()
    generate_presentation_archive()
    generate_contribute_page()
    generate_training_pages()
    generate_brand_page()
    generate_attackcon_page()
    generate_faq_page()
    generate_static_pages()
    generate_use_case_page()
    generate_sidebar_resources()


def copy_docs(module_docs_path):
    """Move module specific docs into the website's content directory for pelican."""
    logger.info("Copying files to docs directory")
    if os.path.isdir(module_docs_path):
        # Check that content directory exist
        if not os.path.exists(site_config.content_dir):
            os.mkdir(site_config.content_dir)
        # Check that docs directory exist
        if not os.path.exists(site_config.docs_dir):
            os.mkdir(site_config.docs_dir)

        for doc in os.listdir(module_docs_path):
            if os.path.isdir(os.path.join(module_docs_path, doc)):
                shutil.copytree(os.path.join(module_docs_path, doc), os.path.join(site_config.docs_dir, doc))
            else:
                shutil.copyfile(os.path.join(module_docs_path, doc), os.path.join(site_config.docs_dir, doc))


def generate_general_information():
    """Responsible for compiling resources json into resources markdown files for rendering on the HMTL."""
    logger.info("Generating general information")
    # load presentations list
    with open(os.path.join(site_config.data_directory, "resources.json"), "r", encoding="utf8") as f:
        resources = json.load(f)

    # get presentations in sorted date order
    presentations = sorted(
        resources["presentations"], key=lambda p: datetime.strptime(p["date"], "%B %Y"), reverse=True
    )
    # get markdown
    resources_content = resources_config.general_information_md + json.dumps({"presentations": presentations})
    # write markdown to file
    with open(
        os.path.join(site_config.resources_markdown_path, "general_information.md"), "w", encoding="utf8"
    ) as md_file:
        md_file.write(resources_content)


def generate_training_pages():
    """Responsible for generating the markdown pages of the training pages."""
    logger.info("Generating training pages")

    # Training Overview
    training_md = resources_config.training_md

    # write markdown to file
    with open(os.path.join(site_config.resources_markdown_path, "training.md"), "w", encoding="utf8") as md_file:
        md_file.write(training_md)

    # CTI training
    training_cti_md = resources_config.training_cti_md

    # write markdown to file
    with open(os.path.join(site_config.resources_markdown_path, "training_cti.md"), "w", encoding="utf8") as md_file:
        md_file.write(training_cti_md)


def generate_brand_page():
    """Responsible for generating the markdown pages of the training pages."""
    logger.info("Generating brand")

    # Training Overview
    brand_md = resources_config.brand_md

    # write markdown to file
    with open(os.path.join(site_config.resources_markdown_path, "brand.md"), "w", encoding="utf8") as md_file:
        md_file.write(brand_md)


def generate_attackcon_page():
    """Responsible for compiling ATT&CKcon json into attackcon markdown file for rendering on the HTML."""
    logger.info("Generating ATT&CKcon page")

    attackcon_md = []
    attackcon_name = []
    attackcon_path = []
    attackcon_dict_list = {}
    # load ATT&CKcon data
    with open(os.path.join(site_config.data_directory, "attackcon.json"), "r", encoding="utf8") as f:
        attackcon = json.load(f)
    attackcon = sorted(attackcon, key=lambda a: datetime.strptime(a["date"], "%B %Y"), reverse=True)

    # Below code used to get a list of all attackcon children
    for i in range(len(attackcon)):
        attackcon_name.append(attackcon[i]["title"])
        title = "Title: " + attackcon[i]["title"] + "\n"
        name = attackcon[i]["date"].lower().replace(" ", "-")
        template = "Template: general/attackcon-overview\n"
        attackcon_path.append("/resources/attackcon/" + name + "/")
        save_as = "save_as: resources/attackcon/" + name + "/index.html\n"
        data = "data: "
        content = title + template + save_as + data
        attackcon_md.append(content)
    attackcon_dict_list["attackcon_name"] = attackcon_name
    attackcon_dict_list["attackcon_path"] = attackcon_path
    attackcon_dict_list["attackcon_md"] = attackcon_md
    attackcon_list = attackcon_dict_list["attackcon_md"]

    # Below code used to add the attackcon children to the resources sidebar
    attackcon_index = 0
    temp_dict = {}
    for i in range(len(site_config.resource_nav["children"])):
        if site_config.resource_nav["children"][i]["name"] == "ATT&CKcon":
            attackcon_index = i

    for i in range(len(attackcon_dict_list["attackcon_name"])):
        temp_dict["name"] = attackcon_dict_list["attackcon_name"][i]
        temp_dict["path"] = attackcon_dict_list["attackcon_path"][i]
        temp_dict["children"] = []
        site_config.resource_nav["children"][attackcon_index]["children"].append(temp_dict.copy())
        temp_dict = {}

    attackcon_content = resources_config.attackcon_md + json.dumps(attackcon[0])

    # write markdown to file
    with open(os.path.join(site_config.resources_markdown_path, "attackcon.md"), "w", encoding="utf8") as md_file:
        md_file.write(attackcon_content)
    for i in range(len(attackcon_list)):
        attackcon_content = attackcon_list[i] + json.dumps(attackcon[i])
        f_name = "attackcon-" + attackcon[i]["date"].lower().replace(" ", "-") + ".md"
        with open(os.path.join(site_config.resources_markdown_path, f_name), "w", encoding="utf8") as md_file:
            md_file.write(attackcon_content)


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
    faq_content = resources_config.faq_md + json.dumps(faqdata)

    # write markdown to file
    with open(os.path.join(site_config.resources_markdown_path, "faq.md"), "w", encoding="utf8") as md_file:
        md_file.write(faq_content)

def generate_static_pages():
    """Reads markdown files from the static pages directory and copies them into the markdown directory."""
    logger.info("Generating static pages")
    static_pages_dir = os.path.join("modules", "resources", "static_pages")

    if not [key["module_name"] for key in modules.run_ptr if key["module_name"] == "versions"]:
        util.buildhelpers.remove_element_from_sub_menu(resources_config.module_name, "Version History")

    # Below code used to get a list of all updates children
    updates_dict_list = {}
    updates_name = []
    updates_path = []
    for static_page in os.listdir(static_pages_dir):
        with open(os.path.join(static_pages_dir, static_page), "r", encoding="utf8") as md:
            content = md.read()
            if static_page.startswith("updates-"):
                temp_string = static_page.replace(".md", "")
                temp_string = temp_string.split("-")
                temp_string = temp_string[1].capitalize() + " " + temp_string[2]
                updates_name.append(temp_string)
                temp_string = static_page.replace(".md", "")
                updates_path.append("/resources/updates/" + temp_string + "/")
    updates_name.sort(key=lambda date: datetime.strptime(date, "%B %Y"), reverse=True)
    updates_path.sort(key=lambda date: datetime.strptime(date, "/resources/updates/updates-%B-%Y/"), reverse=True)
    updates_dict_list["updates_name"] = updates_name
    updates_dict_list["updates_path"] = updates_path

    # Below code used to add the updates children to the resources sidebar
    updates_index = 0
    temp_dict = {}
    for i in range(len(site_config.resource_nav["children"])):
        if site_config.resource_nav["children"][i]["name"] == "Updates":
            updates_index = i

    for i in range(len(updates_dict_list["updates_name"])):
        temp_dict["name"] = updates_dict_list["updates_name"][i]
        temp_dict["path"] = updates_dict_list["updates_path"][i]
        temp_dict["children"] = []
        site_config.resource_nav["children"][updates_index]["children"].append(temp_dict.copy())
        temp_dict = {}

    for static_page in os.listdir(static_pages_dir):
        with open(os.path.join(static_pages_dir, static_page), "r", encoding="utf8") as md:
            content = md.read()

            if static_page.startswith("updates-"):
                with open(
                    os.path.join(resources_config.updates_markdown_path, static_page), "w", encoding="utf8"
                ) as md_file:
                    logger.debug(f"{md.name} >>> {md_file.name}")
                    md_file.write(content)
            else:
                with open(
                    os.path.join(site_config.resources_markdown_path, static_page), "w", encoding="utf8"
                ) as md_file:
                    logger.debug(f"{md.name} >>> {md_file.name}")
                    md_file.write(content)


def generate_working_with_attack():
    """Responsible for generating Access Data & Tools and creating Excel files."""
    logger.info("Generating Access Data & Tools page")
    excel_dirs = [
        f"enterprise-attack-{site_config.full_attack_version}",
        f"mobile-attack-{site_config.full_attack_version}",
        f"ics-attack-{site_config.full_attack_version}",
    ]
    files_types = [
        "matrices",
        "mitigations",
        "relationships",
        "software",
        "groups",
        "tactics",
        "techniques",
        "datasources",
        "campaigns",
        "assets"
    ]

    # Verify if directories exists
    if not os.path.isdir(site_config.web_directory):
        os.makedirs(site_config.web_directory)

    docs_dir = os.path.join(site_config.web_directory, "docs")
    if not os.path.isdir(docs_dir):
        os.makedirs(docs_dir)

    ms = util.relationshipgetters.get_ms()

    for domain in site_config.domains:
        if domain["deprecated"]:
            continue

        domain_name = domain["name"]
        attackToExcel.export(
            domain=domain_name,
            version=site_config.full_attack_version,
            output_dir=docs_dir,
            mem_store=ms[domain_name],
        )

    files_json = {"excel_files": []}
    for excel_dir in excel_dirs:
        excel_json = {"label": f"{excel_dir}.xlsx", "url": f"/docs/{excel_dir}/{excel_dir}.xlsx", "children": []}
        for file_type in files_types:
            child_json = {
                "label": f"{excel_dir}-{file_type}.xlsx",
                "url": f"/docs/{excel_dir}/{excel_dir}-{file_type}.xlsx",
            }
            if os.path.exists(site_config.web_directory + child_json["url"]):
                excel_json["children"].append(child_json)
        files_json["excel_files"].append(excel_json)

    working_with_attack_content = resources_config.working_with_attack_md + json.dumps(files_json)
    # write markdown to file
    with open(
        os.path.join(site_config.resources_markdown_path, "working_with_attack.md"), "w", encoding="utf8"
    ) as md_file:
        md_file.write(working_with_attack_content)


def generate_sidebar_resources():
    """Responsible for generating the sidebar for the resource pages."""
    logger.info("Generating resource sidebar")

    # Sidebar Overview
    sidebar_resources_md = resources_config.sidebar_resources_md

    # write markdown to file
    with open(os.path.join(site_config.resources_markdown_path, "sidebar_resources.md"), "w", encoding="utf8") as md_file:
        md_file.write(sidebar_resources_md)


def generate_contribute_page():
    """Responsible for generating the markdown pages of the contribute pages."""
    logger.info("Generating contributing page")

    # Generate redirections
    util.buildhelpers.generate_redirections(
        redirections_filename=resources_config.contribute_redirection_location, redirect_md=site_config.redirect_md
    )

    ms = util.relationshipgetters.get_ms()
    contributors = util.stixhelpers.get_contributors(ms)

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

    subs = resources_config.contribute_md + json.dumps(data)

    # Open markdown file for the contribute page
    with open(
        os.path.join(site_config.resources_markdown_path, "contribute.md"), "w", encoding="utf8"
    ) as md_file:
        md_file.write(subs)

def generate_presentation_archive():
    """Responsible for compiling resources json into resources markdown files for rendering on the HMTL."""
    logger.info("Generating presentation archive")
    # load presentations list
    with open(os.path.join(site_config.data_directory, "resources.json"), "r", encoding="utf8") as f:
        resources = json.load(f)

    # get presentations in sorted date order
    presentations = sorted(
        resources["presentations"], key=lambda p: datetime.strptime(p["date"], "%B %Y"), reverse=True
    )
    # get markdown
    resources_content = resources_config.presentation_archive_md + json.dumps({"presentations": presentations})
    # write markdown to file
    with open(
        os.path.join(site_config.resources_markdown_path, "presenation_archive.md"), "w", encoding="utf8"
    ) as md_file:
        md_file.write(resources_content)

def generate_use_case_page():
    """Responsible for compiling use cases json into use cases markdown file for rendering on the HMTL."""
    logger.info("Generating getting started pages")

    # load use case data from json
    with open(os.path.join(site_config.data_directory, "use_cases.json"), "r", encoding="utf8") as f:
        use_case_data = json.load(f)

    # Below code used to get a list of all use_case children
    use_case_md = []
    use_case_name = []
    use_case_path = []
    use_case_dict_list = {}
    for i in range(len(use_case_data)):
        use_case_name.append(use_case_data[i]["title"])
        title = "Title: " + use_case_data[i]["title"] + "\n"
        name = use_case_data[i]["title"].lower().replace(' ','-').replace("&", "a")
        template = "Template: resources/use-cases\n"
        use_case_path.append("/resources/getting-started/" + name + "/")
        save_as = "save_as: resources/getting-started/" + name + "/index.html\n"
        data = "data: "
        content = title + template + save_as + data
        use_case_md.append(content)
    use_case_dict_list["use_case_name"] = use_case_name
    use_case_dict_list["use_case_path"] = use_case_path
    use_case_dict_list["use_case_md"] = use_case_md

    # write markdown to file
    use_case_list = use_case_dict_list["use_case_md"]
    for i in range(len(use_case_list)):
        use_case_content = use_case_list[i] + json.dumps(use_case_data[i])
        f_name = "use-case-" + use_case_data[i]["title"].lower().replace(' ','-') + ".md"
        with open(os.path.join(site_config.resources_markdown_path, f_name), "w", encoding="utf8") as md_file:
            md_file.write(use_case_content)