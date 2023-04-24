from modules import site_config

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
techniques_detected_by_datacomponent = {}
groups_using_tool = {}
groups_using_malware = {}
mitigation_mitigates_techniques = {}
technique_mitigated_by_mitigation = {}
datacomponents_detecting_technique = {}
tools_using_technique = {}
malware_using_technique = {}
groups_using_technique = {}
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

technique_to_domain = {}

# Relationship getters


def get_malware_used_by_groups():
    """malware used by groups getter"""
    global malware_used_by_groups

    if not malware_used_by_groups:
        malware_used_by_groups = rsh.malware_used_by_groups(get_srcs())

    return malware_used_by_groups


def get_tools_used_by_groups():
    """tools used by groups getter"""
    global tools_used_by_groups

    if not tools_used_by_groups:
        tools_used_by_groups = rsh.tools_used_by_groups(get_srcs())

    return tools_used_by_groups


def get_malware_used_by_campaigns():
    """malware used by campaigns getter"""
    global malware_used_by_campaigns

    if not malware_used_by_campaigns:
        malware_used_by_campaigns = rsh.malware_used_by_campaigns(get_srcs())

    return malware_used_by_campaigns


def get_tools_used_by_campaigns():
    """tools used by campaigns getter"""
    global tools_used_by_campaigns

    if not tools_used_by_campaigns:
        tools_used_by_campaigns = rsh.tools_used_by_campaigns(get_srcs())

    return tools_used_by_campaigns


def get_techniques_used_by_malware():
    """techniques used by malware getter"""
    global techniques_used_by_malware

    if not techniques_used_by_malware:
        techniques_used_by_malware = rsh.techniques_used_by_malware(get_srcs())

    return techniques_used_by_malware


def get_techniques_used_by_tools():
    """techniques used by tools getter"""
    global techniques_used_by_tools

    if not techniques_used_by_tools:
        techniques_used_by_tools = rsh.techniques_used_by_tools(get_srcs())

    return techniques_used_by_tools


def get_techniques_used_by_groups():
    """techniques used by groups getter"""
    global techniques_used_by_groups

    if not techniques_used_by_groups:
        techniques_used_by_groups = rsh.techniques_used_by_groups(get_srcs())

    return techniques_used_by_groups


def get_techniques_used_by_campaigns():
    """techniques used by campaigns getter"""
    global techniques_used_by_campaigns

    if not techniques_used_by_campaigns:
        techniques_used_by_campaigns = rsh.techniques_used_by_campaigns(get_srcs())

    return techniques_used_by_campaigns


def get_techniques_detected_by_datacomponent():
    global techniques_detected_by_datacomponent

    if not techniques_detected_by_datacomponent:
        techniques_detected_by_datacomponent = rsh.techniques_detected_by_datacomponent(get_srcs())

    return techniques_detected_by_datacomponent


def get_datacomponents_detecting_technique():
    global datacomponents_detecting_technique

    if not datacomponents_detecting_technique:
        datacomponents_detecting_technique = rsh.datacomponents_detecting_technique(get_srcs())

    return datacomponents_detecting_technique


def get_groups_using_tool():
    """groups using tool getter"""
    global groups_using_tool

    if not groups_using_tool:
        groups_using_tool = rsh.groups_using_tool(get_srcs())

    return groups_using_tool


def get_groups_using_malware():
    """groups using malware getter"""
    global groups_using_malware

    if not groups_using_malware:
        groups_using_malware = rsh.groups_using_malware(get_srcs())

    return groups_using_malware


def get_mitigation_mitigates_techniques():
    """mitigation migates techniques getter"""
    global mitigation_mitigates_techniques

    if not mitigation_mitigates_techniques:
        mitigation_mitigates_techniques = rsh.mitigation_mitigates_techniques(get_srcs())

    return mitigation_mitigates_techniques


def get_technique_mitigated_by_mitigation():
    """technique mitigated by mitigation getter"""
    global technique_mitigated_by_mitigation

    if not technique_mitigated_by_mitigation:
        technique_mitigated_by_mitigation = rsh.technique_mitigated_by_mitigation(get_srcs())

    return technique_mitigated_by_mitigation


def get_tools_using_technique():
    """tools using technique getter"""
    global tools_using_technique

    if not tools_using_technique:
        tools_using_technique = rsh.tools_using_technique(get_srcs())

    return tools_using_technique


def get_malware_using_technique():
    """malware using technique getter"""
    global malware_using_technique

    if not malware_using_technique:
        malware_using_technique = rsh.malware_using_technique(get_srcs())

    return malware_using_technique


def get_groups_using_technique():
    """groups using technique getter"""
    global groups_using_technique

    if not groups_using_technique:
        groups_using_technique = rsh.groups_using_technique(get_srcs())

    return groups_using_technique


def get_campaigns_using_technique():
    """campaigns using technique getter"""
    global campaigns_using_technique

    if not campaigns_using_technique:
        campaigns_using_technique = rsh.campaigns_using_technique(get_srcs())

    return campaigns_using_technique


def get_campaigns_using_tool():
    """campaigns using tool getter"""
    global campaigns_using_tool

    if not campaigns_using_tool:
        campaigns_using_tool = rsh.campaigns_using_tool(get_srcs())

    return campaigns_using_tool


def get_campaigns_using_malware():
    """campaigns using malware getter"""
    global campaigns_using_malware

    if not campaigns_using_malware:
        campaigns_using_malware = rsh.campaigns_using_malware(get_srcs())

    return campaigns_using_malware


def get_groups_attributed_to_campaigns():
    """groups attributed to campaign getter"""
    global groups_attributed_to_campaign

    if not groups_attributed_to_campaign:
        groups_attributed_to_campaign = rsh.groups_attributed_to_campaign(get_srcs())

    return groups_attributed_to_campaign


def get_campaigns_attributed_to_group():
    """campaigns attributed to group getter"""
    global campaigns_attributed_to_group

    if not campaigns_attributed_to_group:
        campaigns_attributed_to_group = rsh.campaigns_attributed_to_group(get_srcs())

    return campaigns_attributed_to_group


def get_subtechniques_of():
    """subtechniques of techniques getter"""
    global subtechniques_of

    if not subtechniques_of:
        subtechniques_of = rsh.subtechniques_of(get_srcs())

    return subtechniques_of


def get_datacomponent_of():
    """data components of data sources getter"""
    global datacomponent_of

    if not datacomponent_of:
        datacomponent_of = stixhelpers.datacomponent_of()

    return datacomponent_of


def get_datasource_of():
    """data source of data component getter"""
    global datasource_of

    if not datasource_of:
        datasource_of = stixhelpers.datasource_of()

    return datasource_of


def get_parent_technique_of():
    """parent of subtechnique getter"""
    global parent_technique_of

    if not parent_technique_of:
        parent_technique_of = rsh.parent_technique_of(get_srcs())

    return parent_technique_of


def get_objects_using_notes():
    """get objects using notes"""
    global objects_using_notes

    if not objects_using_notes:
        objects_using_notes = rsh.get_objects_using_notes(get_srcs())

    return objects_using_notes


def get_ms():
    """memory shares getter"""
    global ms
    global srcs

    if not ms:
        # Update both of them if one was not already declared
        ms, srcs = stixhelpers.get_stix_memory_stores()

    return ms


def get_srcs():
    """memory shares without domain getter"""
    global ms
    global srcs

    if not srcs:
        # Update both of them if one was not already declared
        ms, srcs = stixhelpers.get_stix_memory_stores()

    return srcs


def get_resources():
    """resources getter"""
    global resources

    if not resources:
        resources = stixhelpers.grab_resources(get_ms())

    return resources


def get_relationships():
    """relationship getter"""
    global relationships

    if not relationships:
        relationships = get_resources()["relationships"]

    return relationships


def get_group_list():
    """group list getter"""
    global group_list

    if not group_list:
        group_list = get_resources()["groups"]

    return group_list


def get_software_list():
    """software list getter"""
    global software_list

    if not software_list:
        software_list = get_resources()["software"]

    return software_list


def get_technique_list():
    """technique list getter"""
    global technique_list

    if not technique_list:
        technique_list = get_resources()["techniques"]

    return technique_list


def get_datasource_list():
    """data source list getter"""
    global datasource_list

    if not datasource_list:
        datasource_list = stixhelpers.get_datasources(get_srcs())

    return datasource_list


def get_datacomponent_list():
    """data component list getter"""
    global datacomponent_list

    if not datacomponent_list:
        datacomponent_list = stixhelpers.get_datacomponents(get_srcs())

    return datacomponent_list


def get_mitigation_list():
    """mitigation list getter"""
    global mitigation_list

    if not mitigation_list:
        mitigation_list = get_resources()["mitigations"]

    return mitigation_list


def get_campaign_list():
    """campaign list getter"""
    global campaign_list

    if not campaign_list:
        campaign_list = get_resources()["campaigns"]

    return campaign_list


def get_technique_to_domain():
    """technique to domain getter"""
    global technique_to_domain

    if not technique_to_domain:
        technique_to_domain = stixhelpers.get_technique_id_domain_map(get_ms())

    return technique_to_domain
