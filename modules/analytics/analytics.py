import json
import os

from modules import util
from loguru import logger

from . import analytics_config


def generate_analytic_overview():
    """Verify analytic directory and generate analytic index markdown."""
    # Create content pages directory if does not already exist
    util.buildhelpers.create_content_pages_dir()

    # Move templates to templates directory
    util.buildhelpers.move_templates(analytics_config.module_name, analytics_config.analytics_templates_path)

    # Verify if directory exists
    if not os.path.isdir(analytics_config.analytic_markdown_path):
        os.mkdir(analytics_config.analytic_markdown_path)

    # Generate markdown files used for page generation
    analytic_generated = generate_markdown_file()
    if not analytic_generated:
        util.buildhelpers.remove_module_from_menu(analytics_config.module_name)


def generate_markdown_file():
    """Generate table data for all analytics."""
    has_analytics = False

    analytics = util.relationshipgetters.get_analytic_list()
    active_analytics = util.buildhelpers.filter_deprecated_revoked(analytics)

    if active_analytics:
        has_analytics = True
    else:
        logger.debug("No analytics found")
    
    if has_analytics:
        # Generate sidebar data
        data = {
            "sidebar_data": util.buildhelpers.get_side_menu_data("Analytics", "/analytics/", []),
            "total_count": str(len(active_analytics)),
            "analytics_table": get_analytic_table(active_analytics),
        }
        subs = analytics_config.analytic_index_md + json.dumps(data)
        with open(os.path.join(analytics_config.analytic_markdown_path, "overview.md"), "w", encoding="utf8") as md_file:
            md_file.write(subs)
    
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
            "detection_strategy": get_related_detection_strategies(analytic["id"]),
            "url": util.buildhelpers.get_analytic_url(analytic),
        }
        analytic_table.append(row)

    # sort by id
    return sorted(analytic_table, key=lambda k: k["id"])


def get_related_detection_strategies(analytic_ref):
    related_dets = util.stixhelpers.get_related_detection_strategies(analytic_ref)
    if not related_dets:
        logger.debug(f"No related detection strategy found for analytic {analytic_ref}")

    det_data = []
    for det in related_dets:
        attack_id = util.buildhelpers.get_attack_id(det)
        det_data.append({
            "id": attack_id,
            "url": f"/detectionstrategies/{attack_id}"
        })
    return det_data
