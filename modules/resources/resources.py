import json
import math
import os
import re
import shutil
import urllib.parse
from datetime import datetime

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
    os.makedirs(site_config.resources_markdown_path, exist_ok=True)

    # Verify if resources directory exists
    os.makedirs(resources_config.updates_markdown_path, exist_ok=True)

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
    logger.info(f"Copying docs from {module_docs_path} to {site_config.docs_dir}")
    if os.path.isdir(module_docs_path):
        os.makedirs(site_config.content_dir, exist_ok=True)
        os.makedirs(site_config.docs_dir, exist_ok=True)

        shutil.copytree(module_docs_path, site_config.docs_dir, dirs_exist_ok=True)


def extract_video_id(url):
    if "=" in url and "&" in url:
        start = url.find("=") + 1
        end = url.find("&", start)
        return url[start:end]
    return url


def extract_playlist_id(url):
    parsed_url = urllib.parse.urlparse(url)
    query_params = urllib.parse.parse_qs(parsed_url.query)
    return query_params.get("list", [None])[0]


def generate_training_pages():
    """Responsible for generating the markdown pages of the training pages."""
    logger.info("Generating training pages")

    # load training data
    with open(os.path.join(site_config.data_directory, "trainings.json"), "r", encoding="utf8") as f:
        trainings = json.load(f)

    for training_main in trainings:
        for module in trainings[training_main]:
            if "lessons" in trainings[training_main][module]:
                if trainings[training_main][module]["is_youtube"]:
                    # if videos are in a playlist
                    if (
                        "playlist" in trainings[training_main][module]
                        and trainings[training_main][module]["playlist"] == True
                    ):
                        trainings[training_main][module]["first_video_id"] = extract_video_id(
                            trainings[training_main][module]["lessons"][0]["youtube"]
                        )
                        trainings[training_main][module]["playlist_id"] = extract_playlist_id(
                            trainings[training_main][module]["lessons"][0]["youtube"]
                        )
                    # if videos are not in a playlist
                    else:
                        for lesson_idx in range(len(trainings[training_main][module]["lessons"])):
                            trainings[training_main][module]["lessons"][lesson_idx]["video_id"] = extract_video_id(
                                trainings[training_main][module]["lessons"][lesson_idx]["youtube"]
                            )

    # Define a dictionary of training pages and their corresponding markdown templates
    training_pages = {
        "training": resources_config.training_md,
        "training_cti": resources_config.training_cti_md,
        "training_purple_teaming_fundamentals": resources_config.training_purple_teaming_fundamentals_md,
        "training_attack_fundamentals": resources_config.training_attack_fundamentals_md,
        "training_adversary_emulation": resources_config.training_adversary_emulation_md,
        "training_access_tokens": resources_config.training_access_tokens_md,
        "training_soc_assessments": resources_config.training_soc_assessments_md,
        "training_threat_hunting": resources_config.training_threat_hunting_md,
        "training_detection_engineering": resources_config.training_detection_engineering_md,
    }

    # Generate markdown for each training page and write it to a file
    for page_name, page_template in training_pages.items():
        page_content = page_template + json.dumps(trainings)
        with open(
            os.path.join(site_config.resources_markdown_path, f"{page_name}.md"), "w", encoding="utf8"
        ) as md_file:
            md_file.write(page_content)


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
        template = "Template: resources/attackcon-overview\n"
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
    learnmore_index = 0
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
    """Read markdown files from the static pages directory and copies them into the markdown directory."""
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
    docs_dir = os.path.join(site_config.docs_dir)
    os.makedirs(docs_dir, exist_ok=True)

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
        src_dir = os.path.join(docs_dir, f"{domain_name}-{site_config.full_attack_version}")
        if not os.path.isdir(src_dir):
            logger.error(f"Excel files not generated/found in: {src_dir}")

        # TODO: delete this block if we end up with greater control of how to generate output in mitreattack-python
        dst_dir = os.path.join(docs_dir, "attack-excel-files", site_config.full_attack_version, domain_name)
        os.makedirs(dst_dir, exist_ok=True)
        for fname in os.listdir(src_dir):
            if fname.endswith(".xlsx"):
                old_path = os.path.join(src_dir, fname)
                new_path = os.path.join(dst_dir, fname)
                logger.debug(f"Moving {old_path} to {new_path}")
                shutil.move(old_path, new_path)
        try:
            logger.debug(f"Removing directory: {src_dir}")
            os.rmdir(src_dir)
        except OSError:
            pass

    attack_excel_root = "content/docs/attack-excel-files"
    logger.debug(f"Scanning for ATT&CK Excel files in: {attack_excel_root}")

    versions = sorted(
        [d for d in os.listdir(attack_excel_root) if os.path.isdir(os.path.join(attack_excel_root, d))],
        key=lambda v: tuple(map(int, re.findall(r"\d+", v))),
        reverse=True,
    )

    excel_files_by_version = {}
    for version in versions:
        version_path = os.path.join(attack_excel_root, version)
        if not os.path.isdir(version_path):
            continue
        domain_list = []
        for domain in sorted(os.listdir(version_path)):
            domain_path = os.path.join(version_path, domain)
            if not os.path.isdir(domain_path):
                continue
            files = []
            for fname in sorted(os.listdir(domain_path)):
                if fname.endswith(".xlsx"):
                    url = f"/docs/attack-excel-files/{version}/{domain}/{fname}"
                    files.append(
                        {
                            "label": fname,
                            "url": url,
                        }
                    )
            if files:
                master_label = f"{domain}-{version}.xlsx"
                master_file = next((f for f in files if f["label"] == master_label), None)
                master_url = master_file["url"] if master_file else ""
                children = [f for f in files if f["label"] != master_label] if master_file else files

                domain_dict = {"label": master_label, "url": master_url, "children": children}
                domain_list.append(domain_dict)
        if domain_list:
            excel_files_by_version[version] = domain_list

    files_json = {"excel_files_by_version": excel_files_by_version}
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
    with open(
        os.path.join(site_config.resources_markdown_path, "sidebar_resources.md"), "w", encoding="utf8"
    ) as md_file:
        md_file.write(sidebar_resources_md)


def generate_contribute_page():
    """Responsible for generating the markdown pages of the contribute pages."""
    logger.info("Generating contributing page")

    ms = util.relationshipgetters.get_ms()
    contributors = util.stixhelpers.get_contributors(ms)

    data = {}

    data["contributors"] = []

    contributors_first_col = []
    contributors_second_col = []
    contributors_third_col = []

    third = math.ceil(len(contributors) / 3)

    for index in range(0, third):
        contributors_first_col.append(contributors[index])

    for index in range(third, 2 * third):
        contributors_second_col.append(contributors[index])

    for index in range(2 * third, len(contributors)):
        contributors_third_col.append(contributors[index])

    data["contributors"].append(contributors_first_col)
    data["contributors"].append(contributors_second_col)
    data["contributors"].append(contributors_third_col)

    subs = resources_config.contribute_md + json.dumps(data)

    # Open markdown file for the contribute page
    with open(os.path.join(site_config.resources_markdown_path, "contribute.md"), "w", encoding="utf8") as md_file:
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
        os.path.join(site_config.resources_markdown_path, "presentation_archive.md"), "w", encoding="utf8"
    ) as md_file:
        md_file.write(resources_content)


def generate_use_case_page():
    """Responsible for compiling use cases json into use cases markdown file for rendering on the HMTL."""
    logger.info("Generating get started pages")

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
        name = use_case_data[i]["title"].lower().replace(" ", "-").replace("&", "a")
        template = "Template: resources/use-cases\n"
        use_case_path.append("/resources/get-started/" + name + "/")
        save_as = "save_as: resources/get-started/" + name + "/index.html\n"
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
        f_name = "use-case-" + use_case_data[i]["title"].lower().replace(" ", "-") + ".md"
        with open(os.path.join(site_config.resources_markdown_path, f_name), "w", encoding="utf8") as md_file:
            md_file.write(use_case_content)
