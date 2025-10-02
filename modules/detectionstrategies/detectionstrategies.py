import json
import os

from modules import util
from loguru import logger

from .. import site_config
from . import detectionstrategies_config


def generate_detectionstrategy():
    """Verify detection strategy directory and generate detection strategy index markdown."""
    # Create content pages directory if does not already exist
    util.buildhelpers.create_content_pages_dir()

    # Move templates to templates directory
    util.buildhelpers.move_templates(detectionstrategies_config.module_name_no_spaces, detectionstrategies_config.detectionstrategies_templates_path)

    # Verify if directory exists
    if not os.path.isdir(detectionstrategies_config.detectionstrategy_markdown_path):
        os.mkdir(detectionstrategies_config.detectionstrategy_markdown_path)

    # Generate markdown files used for page generation
    detectionstrategy_generated = generate_markdown_files()
    if not detectionstrategy_generated:
        util.buildhelpers.remove_module_from_menu(detectionstrategies_config.module_name_no_spaces)


def generate_markdown_files():
    """Generate shared data for all detection strategies and markdown for detection strategy."""
    data = {}
    has_detection_strategies = False

    detection_strategy_list = util.relationshipgetters.get_detectionstrategy_list()
    active_detection_strategy_list = util.buildhelpers.filter_deprecated_revoked(detection_strategy_list)

    detection_strategies = {}
    ms = util.relationshipgetters.get_ms()
    for domain in site_config.domains:
        if domain["deprecated"]:
            continue
        # Reads the STIX and creates a list of the ATT&CK detection strategies filtered by domain
        detection_strategies[domain["name"]] = util.stixhelpers.get_detection_strategy_list_from_src(ms[domain["name"]], sort_by_id=True)
    if active_detection_strategy_list:
        has_detection_strategies = True
    else:
        logger.debug("No detection strategies found")

    if has_detection_strategies:
        notes = util.relationshipgetters.get_objects_using_notes()

        # Generate sidebar data
        sidebar_data = util.buildhelpers.get_side_nav_domains_data("detection strategies", detection_strategies, domain_page=False, use_name_or_id="id")
        generate_sidebar_detectionstrategies(sidebar_data)

        data["total_count"] = str(len(active_detection_strategy_list))
        data["detection_strategy_table"] = get_detection_strategy_table(active_detection_strategy_list)

        subs = detectionstrategies_config.detectionstrategy_index_md + json.dumps(data)
        with open(os.path.join(detectionstrategies_config.detectionstrategy_markdown_path, "overview.md"), "w", encoding="utf8") as md_file:
            md_file.write(subs)

        # Create markdown for detection strategies
        for detection_strategy in detection_strategy_list:
            generate_detection_strategy_md(detection_strategy, notes)
    
    return has_detection_strategies


def get_detection_strategy_table(detection_strategy_list):
    """Generate detection strategy table for the overview page."""
    detection_strategy_table = []

    for detection_strategy in detection_strategy_list:
        attack_id = util.buildhelpers.get_attack_id(detection_strategy)
        if not attack_id:
            continue

        domains = detection_strategy.get("x_mitre_domains", [])
        domain_names = [util.buildhelpers.get_domain_display_name(domain) for domain in domains]
        row = {
            "id": attack_id,
            "name": detection_strategy.get("name"),
            "domains": domain_names,
            "deprecated": detection_strategy.get("x_mitre_deprecated", False),
        }
        detection_strategy_table.append(row)
    
    # sort by detection strategy name
    return sorted(detection_strategy_table, key=lambda k: k["name"].lower())


def generate_detection_strategy_md(detection_strategy, notes):
    """Generate markdown for individual detection strategies."""
    attack_id = util.buildhelpers.get_attack_id(detection_strategy)
    if not attack_id:
        return
    
    dates = util.buildhelpers.get_created_and_modified_dates(detection_strategy)

    # Build reference list
    reference_list = { "current_number": 0 }
    reference_list = util.buildhelpers.update_reference_list(reference_list, detection_strategy)

    domains = detection_strategy.get("x_mitre_domains", [])
    domain_names = [util.buildhelpers.get_domain_display_name(domain) for domain in domains]
    analytics_by_platform, analytic_ids = build_analytics_by_platform(detection_strategy, reference_list)
    data = {
        "attack_id": attack_id,
        "notes": notes.get(detection_strategy["id"]),
        "created": dates.get("created"),
        "modified": dates.get("modified"),
        "name": detection_strategy.get("name"),
        "domains": domain_names,
        "version": detection_strategy.get("x_mitre_version"),
        "contributors": detection_strategy.get("x_mitre_contributors", []),
        "deprecated": detection_strategy.get("x_mitre_deprecated", False),
        "citations": reference_list,
        "technique_detected": get_technique_detected_data(detection_strategy, reference_list),
        "analytics": analytics_by_platform,
        "analytic_ids": analytic_ids,
        "versioning_feature": site_config.check_versions_module(),
    }

    subs = detectionstrategies_config.detectionstrategy_md.substitute(data)
    subs += json.dumps(data)

    # Write the markdown file
    with open(os.path.join(detectionstrategies_config.detectionstrategy_markdown_path, attack_id + ".md"), "w", encoding="utf8") as md_file:
        md_file.write(subs)


def get_technique_detected_data(detection_strategy, reference_list):
    """Get techniques detected by this detection strategy and add any missing citations."""
    technique_detected = util.relationshipgetters.get_techniques_detected_by_detectionstrategy().get(detection_strategy["id"], [None])
    if not technique_detected[0]:
        return {}
    
    technique = technique_detected[0]["object"]
    attack_id = util.buildhelpers.get_attack_id(technique)
    relationship = technique_detected[0]["relationship"]
    technique_data = {
        "name": technique["name"],
        "attack_id": attack_id,
        "detects": relationship.get("description", ""),
        "url": f"/techniques/{attack_id.replace('.', '/')}",
    }
    reference_list = util.buildhelpers.update_reference_list(reference_list, relationship)
    return technique_data


def build_analytics_by_platform(detection_strategy, reference_list):
    """Generate analytic table by platform."""
    analytics_map = util.stixhelpers.get_analytics_from_detection_strategy(detection_strategy)
    platform_dict = {}
    analytic_ids = []

    for analytic in analytics_map.values():
        if analytic is None: continue # skip missing analytics

        platforms = analytic.get("x_mitre_platforms", [])
        if not platforms:
            continue # skip analytics with no platform
        platform = platforms[0]

        attack_id = util.buildhelpers.get_attack_id(analytic)
        analytic_ids.append(attack_id)
        analytic_data = {
            "id": attack_id,
            "description": analytic.get("description", ""),
            "url": f"/analytics/{attack_id}",
            "log_source_table": build_log_source_table(analytic),
            "mutable_elements": analytic.get("x_mitre_mutable_elements", [])
        }
        reference_list = util.buildhelpers.update_reference_list(reference_list, analytic)

        if platform not in platform_dict:
            platform_dict[platform] = []
        platform_dict[platform].append(analytic_data)

    return platform_dict, analytic_ids


def generate_sidebar_detectionstrategies(side_nav_data):
    """Responsible for generating the sidebar for the detectionstrategies pages."""
    logger.info("Generating detectionstrategies sidebar")
    data = {}
    data["menu"] = side_nav_data

    # Sidebar Overview
    sidebar_detectionstrategies_md = detectionstrategies_config.sidebar_detectionstrategies_md + json.dumps(data)

    # write markdown to file
    with open(
        os.path.join(detectionstrategies_config.detectionstrategy_markdown_path, "sidebar_detectionstrategies.md"), "w", encoding="utf8"
    ) as md_file:
        md_file.write(sidebar_detectionstrategies_md)


def build_log_source_table(analytic):
    log_source_dict = {}
    log_sources = analytic.get("x_mitre_log_source_references")
    if not log_sources:
        logger.debug(f"No log source references found on Analytic {analytic['id']}")
        return log_source_dict

    for log_source in log_sources:
        datacomponent_ref = log_source.get("x_mitre_data_component_ref", None)
        datacomponent = util.stixhelpers.get_datacomponent_from_list(datacomponent_ref)
        if not datacomponent:
            logger.debug(f"Log source data component not found: {log_source}")
            continue # skip log source with no data component

        datacomponent_id = util.buildhelpers.get_attack_id(datacomponent)
        if datacomponent_id not in log_source_dict:
            log_source_dict[datacomponent_id] = {
                "datacomponent": {
                    "name": datacomponent.get("name"),
                    "url": f"/datacomponents/{datacomponent_id}",
                },
                "log_sources": []
            }
        log_source_dict[datacomponent_id]["log_sources"].append(log_source)
    return log_source_dict
