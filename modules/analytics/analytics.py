import json
import os

from modules import util
from loguru import logger

from .. import site_config
from . import analytics_config


def generate_analytic():
    """Verify analytic directory and generate analytic index markdown."""
    # Create content pages directory if does not already exist
    util.buildhelpers.create_content_pages_dir()

    # Move templates to templates directory
    util.buildhelpers.move_templates(analytics_config.module_name, analytics_config.analytics_templates_path)

    # Verify if directory exists
    if not os.path.isdir(analytics_config.analytic_markdown_path):
        os.mkdir(analytics_config.analytic_markdown_path)

    # Generate markdown files used for page generation
    analytic_generated = generate_markdown_files()
    if not analytic_generated:
        util.buildhelpers.remove_module_from_menu(analytics_config.module_name)


def generate_markdown_files():
    """Generate shared data for all analytics and markdown for analytic pages."""
    data = {}
    has_analytics = False

    analytics = util.relationshipgetters.get_analytic_list()
    active_analytics = util.buildhelpers.filter_deprecated_revoked(analytics)

    if active_analytics:
        has_analytics = True
    
    if has_analytics:
        notes = util.relationshipgetters.get_objects_using_notes()

        # Generate sidebar data
        sidebar_data = util.buildhelpers.get_side_menu_data(
            "Analytics", "/analytics/", active_analytics
        )
        data["sidebar_data"] = sidebar_data

        data["total_count"] = str(len(active_analytics))
        data["analytics_table"] = get_analytic_table(active_analytics)

        subs = analytics_config.analytic_index_md + json.dumps(data)
        with open(os.path.join(analytics_config.analytic_markdown_path, "overview.md"), "w", encoding="utf8") as md_file:
            md_file.write(subs)

        # Create markdown for analytics
        for analytic in analytics:
            generate_analytic_md(analytic, sidebar_data, notes)
    
    return has_analytics


def get_analytic_table(analytics):
    """Generate analytic table for overview page."""
    analytic_table = []

    for analytic in analytics:
        attack_id = util.buildhelpers.get_attack_id(analytic)
        if not attack_id:
            continue

        domains = analytic.get("x_mitre_domains", [])
        domain_names = [util.buildhelpers.get_domain_display_name(domain) for domain in domains]
        row = {
            "id": attack_id,
            "name": analytic.get("name"),
            "platforms": analytic.get("x_mitre_platforms", []),
            "domains": domain_names,
            "description": analytic.get("description", ""),
            "deprecated": analytic.get("x_mitre_deprecated", False),
        }
        analytic_table.append(row)

    # sort by id
    return sorted(analytic_table, key=lambda k: k["id"])

def generate_analytic_md(analytic, sidebar_data, notes):
    """Generate markdown for individual analytic pages."""
    attack_id = util.buildhelpers.get_attack_id(analytic)
    if not attack_id:
        return

    # build reference list
    reference_list = { "current_number": 0 }
    reference_list = util.buildhelpers.update_reference_list(reference_list, analytic)

    dates = util.buildhelpers.get_created_and_modified_dates(analytic)
    domains = analytic.get("x_mitre_domains", [])
    domain_names = [util.buildhelpers.get_domain_display_name(domain) for domain in domains]

    data = {
        "attack_id": attack_id,
        "name": analytic.get("name"),
        "sidebar_data": sidebar_data,
        "notes": notes.get(analytic["id"]),
        "created": dates.get("created"),
        "modified": dates.get("modified"),
        "version": analytic.get("x_mitre_version"),
        "description": analytic.get("description"),
        "deprecated": analytic.get("x_mitre_deprecated", False),
        "detection_strategies": get_related_detection_strategies(analytic["id"]),
        "mutable_elements": analytic.get("x_mitre_mutable_elements", []),
        "platforms": analytic.get("x_mitre_platforms", []),
        "log_sources": build_log_source_table(analytic),
        "domains": domain_names,
        "citations": reference_list,
        "versioning_feature": site_config.check_versions_module(),
    }

    subs = analytics_config.analytic_md.substitute(data)
    subs += json.dumps(data)

    # Write the markdown file
    with open(os.path.join(analytics_config.analytic_markdown_path, attack_id + ".md"), "w", encoding="utf8") as md_file:
        md_file.write(subs)


def get_related_detection_strategies(analytic_ref):
    related_dets = util.stixhelpers.get_related_detection_strategies(analytic_ref)
    det_data = []
    for det in related_dets:
        attack_id = util.buildhelpers.get_attack_id(det)
        det_data.append({
            "attack_id": attack_id,
            "name": det["name"],
            "url": f"/detectionstrategies/{attack_id}"
        })
    return det_data


def build_log_source_table(analytic):
    log_sources = analytic.get("x_mitre_log_source_references")
    log_source_table = []
    for log_source in log_sources:
        log_source_data = {
            "name": log_source.get("name", ""),
            "channel": log_source.get("channel", ""),
        }
        datacomponent_ref = log_source.get("x_mitre_data_component_ref", None)
        datacomponent = util.stixhelpers.get_datacomponent_from_list(datacomponent_ref)
        if not datacomponent:
            logger.debug(f"NOT FOUND: Log source data component {log_source}")
            log_source_data["data_component_not_found"] = True
        else:
            datacomponent_id = util.buildhelpers.get_attack_id(datacomponent)
            log_source_data["data_component_name"] = datacomponent.get("name")
            log_source_data["data_component_id"] = datacomponent_id
            log_source_data["data_component_url"] = f"/datacomponents/{datacomponent_id}"

        log_source_table.append(log_source_data)
    return log_source_table
