from . import relationshiphelpers as rsh
from . import stixhelpers

malware_used_by_groups = {}
tools_used_by_groups = {}
malware_used_by_campaigns = {}
tools_used_by_campaigns = {}
techniques_used_by_malware = {}
techniques_used_by_tools = {}
techniques_used_by_groups = {}
techniques_used_by_campaigns = {}
techniques_targeting_assets = {}
techniques_detected_by_datacomponent = {}
techniques_detected_by_detectionstrategy = {}
groups_using_tool = {}
groups_using_malware = {}
mitigation_mitigates_techniques = {}
technique_mitigated_by_mitigation = {}
datacomponents_detecting_technique = {}
detectionstrategies_detecting_technique = {}
tools_using_technique = {}
malware_using_technique = {}
groups_using_technique = {}
assets_targeted_by_techniques = {}
campaigns_using_technique = {}
campaigns_using_tool = {}
campaigns_using_malware = {}
groups_attributed_to_campaign = {}
campaigns_attributed_to_group = {}
subtechniques_of = {}
datacomponent_of = {}
datasource_of = {}
parent_technique_of = {}
objects_using_notes = {}

ms = {}
srcs = []

resources = {}
relationships = []

group_list = []
software_list = []
technique_list = []
datasource_list = []
datacomponent_list = []
mitigation_list = []
campaign_list = []
asset_list = []
analytic_list = []
detectionstrategy_list = []

technique_to_domain = {}

# Relationship getters


def get_malware_used_by_groups():
    """Return malware used by groups."""
    global malware_used_by_groups

    if not malware_used_by_groups:
        malware_used_by_groups = rsh.malware_used_by_groups(get_srcs())

    return malware_used_by_groups


def get_tools_used_by_groups():
    """Return tools used by groups."""
    global tools_used_by_groups

    if not tools_used_by_groups:
        tools_used_by_groups = rsh.tools_used_by_groups(get_srcs())

    return tools_used_by_groups


def get_malware_used_by_campaigns():
    """Return malware used by campaigns."""
    global malware_used_by_campaigns

    if not malware_used_by_campaigns:
        malware_used_by_campaigns = rsh.malware_used_by_campaigns(get_srcs())

    return malware_used_by_campaigns


def get_tools_used_by_campaigns():
    """Return tools used by campaigns."""
    global tools_used_by_campaigns

    if not tools_used_by_campaigns:
        tools_used_by_campaigns = rsh.tools_used_by_campaigns(get_srcs())

    return tools_used_by_campaigns


def get_techniques_used_by_malware():
    """Return techniques used by malware."""
    global techniques_used_by_malware

    if not techniques_used_by_malware:
        techniques_used_by_malware = rsh.techniques_used_by_malware(get_srcs())

    return techniques_used_by_malware


def get_techniques_used_by_tools():
    """Return techniques used by tools."""
    global techniques_used_by_tools

    if not techniques_used_by_tools:
        techniques_used_by_tools = rsh.techniques_used_by_tools(get_srcs())

    return techniques_used_by_tools


def get_techniques_used_by_groups():
    """Return techniques used by groups."""
    global techniques_used_by_groups

    if not techniques_used_by_groups:
        techniques_used_by_groups = rsh.techniques_used_by_groups(get_srcs())

    return techniques_used_by_groups


def get_techniques_used_by_campaigns():
    """Return techniques used by campaigns."""
    global techniques_used_by_campaigns

    if not techniques_used_by_campaigns:
        techniques_used_by_campaigns = rsh.techniques_used_by_campaigns(get_srcs())

    return techniques_used_by_campaigns


def get_techniques_targeting_assets():
    """Return techniques targeting assets."""
    global techniques_targeting_assets

    if not techniques_targeting_assets:
        techniques_targeting_assets = rsh.techniques_targeting_assets(get_srcs())

    return techniques_targeting_assets


def get_assets_targeted_by_techniques():
    """Return assets targeted by techniques."""
    global assets_targeted_by_techniques

    if not assets_targeted_by_techniques:
        assets_targeted_by_techniques = rsh.assets_targeted_by_techniques(get_srcs())

    return assets_targeted_by_techniques


def get_techniques_detected_by_datacomponent():
    """Return techniques detected by data components."""
    global techniques_detected_by_datacomponent

    if not techniques_detected_by_datacomponent:
        techniques_detected_by_datacomponent = rsh.techniques_detected_by_datacomponent(get_srcs())

    return techniques_detected_by_datacomponent


def get_datacomponents_detecting_technique():
    """Return data components that detect techniques."""
    global datacomponents_detecting_technique

    if not datacomponents_detecting_technique:
        datacomponents_detecting_technique = rsh.datacomponents_detecting_technique(get_srcs())

    return datacomponents_detecting_technique


def get_techniques_detected_by_detectionstrategy():
    global techniques_detected_by_detectionstrategy

    if not techniques_detected_by_detectionstrategy:
        techniques_detected_by_detectionstrategy = rsh.techniques_detected_by_detectionstrategy(get_srcs())

    return techniques_detected_by_detectionstrategy


def get_detectionstrategies_detecting_technique():
    global detectionstrategies_detecting_technique

    if not detectionstrategies_detecting_technique:
        detectionstrategies_detecting_technique = rsh.detectionstrategy_detecting_technique(get_srcs())

    return detectionstrategies_detecting_technique


def get_groups_using_tool():
    """Return groups using a tool."""
    global groups_using_tool

    if not groups_using_tool:
        groups_using_tool = rsh.groups_using_tool(get_srcs())

    return groups_using_tool


def get_groups_using_malware():
    """Return groups using malware."""
    global groups_using_malware

    if not groups_using_malware:
        groups_using_malware = rsh.groups_using_malware(get_srcs())

    return groups_using_malware


def get_mitigation_mitigates_techniques():
    """Return mapping of mitigations that mitigate techniques."""
    global mitigation_mitigates_techniques

    if not mitigation_mitigates_techniques:
        mitigation_mitigates_techniques = rsh.mitigation_mitigates_techniques(get_srcs())

    return mitigation_mitigates_techniques


def get_technique_mitigated_by_mitigation():
    """Return techniques mitigated by mitigations."""
    global technique_mitigated_by_mitigation

    if not technique_mitigated_by_mitigation:
        technique_mitigated_by_mitigation = rsh.technique_mitigated_by_mitigation(get_srcs())

    return technique_mitigated_by_mitigation


def get_tools_using_technique():
    """Return tools using a technique."""
    global tools_using_technique

    if not tools_using_technique:
        tools_using_technique = rsh.tools_using_technique(get_srcs())

    return tools_using_technique


def get_malware_using_technique():
    """Return malware using a technique."""
    global malware_using_technique

    if not malware_using_technique:
        malware_using_technique = rsh.malware_using_technique(get_srcs())

    return malware_using_technique


def get_groups_using_technique():
    """Return groups using a technique."""
    global groups_using_technique

    if not groups_using_technique:
        groups_using_technique = rsh.groups_using_technique(get_srcs())

    return groups_using_technique


def get_campaigns_using_technique():
    """Return campaigns using a technique."""
    global campaigns_using_technique

    if not campaigns_using_technique:
        campaigns_using_technique = rsh.campaigns_using_technique(get_srcs())

    return campaigns_using_technique


def get_campaigns_using_tool():
    """Return campaigns using a tool."""
    global campaigns_using_tool

    if not campaigns_using_tool:
        campaigns_using_tool = rsh.campaigns_using_tool(get_srcs())

    return campaigns_using_tool


def get_campaigns_using_malware():
    """Return campaigns using malware."""
    global campaigns_using_malware

    if not campaigns_using_malware:
        campaigns_using_malware = rsh.campaigns_using_malware(get_srcs())

    return campaigns_using_malware


def get_groups_attributed_to_campaigns():
    """Return groups attributed to campaigns."""
    global groups_attributed_to_campaign

    if not groups_attributed_to_campaign:
        groups_attributed_to_campaign = rsh.groups_attributed_to_campaign(get_srcs())

    return groups_attributed_to_campaign


def get_campaigns_attributed_to_group():
    """Return campaigns attributed to a group."""
    global campaigns_attributed_to_group

    if not campaigns_attributed_to_group:
        campaigns_attributed_to_group = rsh.campaigns_attributed_to_group(get_srcs())

    return campaigns_attributed_to_group


def get_subtechniques_of():
    """Return subtechniques for techniques."""
    global subtechniques_of

    if not subtechniques_of:
        subtechniques_of = rsh.subtechniques_of(get_srcs())

    return subtechniques_of


def get_datacomponent_of():
    """Return data components of data sources."""
    global datacomponent_of

    if not datacomponent_of:
        datacomponent_of = stixhelpers.datacomponent_of()

    return datacomponent_of


def get_datasource_of():
    """Return the data source for a data component."""
    global datasource_of

    if not datasource_of:
        datasource_of = stixhelpers.datasource_of()

    return datasource_of


def get_parent_technique_of():
    """Return parent technique for subtechniques."""
    global parent_technique_of

    if not parent_technique_of:
        parent_technique_of = rsh.parent_technique_of(get_srcs())

    return parent_technique_of


def get_objects_using_notes():
    """Return objects using notes."""
    global objects_using_notes

    if not objects_using_notes:
        objects_using_notes = rsh.get_objects_using_notes(get_srcs())

    return objects_using_notes


def get_ms():
    """Return STIX memory stores."""
    global ms
    global srcs

    if not ms:
        # Update both of them if one was not already declared
        ms, srcs = stixhelpers.get_stix_memory_stores()

    return ms


def get_srcs():
    """Return STIX memory stores without domain."""
    global ms
    global srcs

    if not srcs:
        # Update both of them if one was not already declared
        ms, srcs = stixhelpers.get_stix_memory_stores()

    return srcs


def get_resources():
    """Return grabbed resources."""
    global resources

    if not resources:
        resources = stixhelpers.grab_resources(get_ms())

    return resources


def get_relationships():
    """Return relationships from resources."""
    global relationships

    if not relationships:
        relationships = get_resources()["relationships"]

    return relationships


def get_group_list():
    """Return the group list."""
    global group_list

    if not group_list:
        group_list = get_resources()["groups"]

    return group_list


def get_software_list():
    """Return the software list."""
    global software_list

    if not software_list:
        software_list = get_resources()["software"]

    return software_list


def get_technique_list():
    """Return the technique list."""
    global technique_list

    if not technique_list:
        technique_list = get_resources()["techniques"]

    return technique_list


def get_datasource_list():
    """Return the data source list."""
    global datasource_list

    if not datasource_list:
        datasource_list = stixhelpers.get_datasources(get_srcs())

    return datasource_list


def get_datacomponent_list():
    """Return the data component list."""
    global datacomponent_list

    if not datacomponent_list:
        datacomponent_list = stixhelpers.get_datacomponents(get_srcs())

    return datacomponent_list


def get_mitigation_list():
    """Return the mitigation list."""
    global mitigation_list

    if not mitigation_list:
        mitigation_list = get_resources()["mitigations"]

    return mitigation_list


def get_campaign_list():
    """Return the campaign list."""
    global campaign_list

    if not campaign_list:
        campaign_list = get_resources()["campaigns"]

    return campaign_list


def get_asset_list():
    """Return the asset list."""
    global asset_list

    if not asset_list:
        asset_list = get_resources()["assets"]

    return asset_list


def get_detectionstrategy_list():
    """detection strategy list getter"""
    global detectionstrategy_list

    if not detectionstrategy_list:
        detectionstrategy_list = get_resources()["detectionstrategies"]

    return detectionstrategy_list


def get_analytic_list():
    """analytic list getter"""
    global analytic_list

    if not analytic_list:
        analytic_list = get_resources()["analytics"]

    return analytic_list


def get_technique_to_domain():
    """Return mapping of technique to domain."""
    global technique_to_domain

    if not technique_to_domain:
        technique_to_domain = stixhelpers.get_technique_id_domain_map(get_ms())

    return technique_to_domain
