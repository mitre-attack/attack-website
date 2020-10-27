from . import relationshiphelpers as rsh
from . import stixhelpers
from modules import site_config

malware_used_by_groups = {}
tools_used_by_groups = {}
techniques_used_by_malware = {}
techniques_used_by_tools = {}
techniques_used_by_groups = {}
groups_using_tool = {}
groups_using_malware = {}
mitigation_mitigates_techniques = {}
technique_mitigated_by_mitigation = {}
technique_related_to_technique = {}
tools_using_technique = {}
malware_using_technique = {}
groups_using_technique = {}
subtechniques_of = {}
parent_technique_of = {}
ms = {}
resources = {}
relationships = []
group_list = []
software_list = []
technique_list = []
mitigation_list = []
technique_to_domain = {}

# Relationship getters

def get_malware_used_by_groups():
    """ malware used by groups getter """
    global malware_used_by_groups

    if not malware_used_by_groups:
        malware_used_by_groups = rsh.malware_used_by_groups(site_config.srcs)

    return malware_used_by_groups

def get_tools_used_by_groups():
    """ tools used by groups getter """
    global tools_used_by_groups

    if not tools_used_by_groups:
        tools_used_by_groups = rsh.tools_used_by_groups(site_config.srcs)
    
    return tools_used_by_groups

def get_techniques_used_by_malware():
    """ techniques used by malware getter """
    global techniques_used_by_malware
    
    if not techniques_used_by_malware:
        techniques_used_by_malware = rsh.techniques_used_by_malware(site_config.srcs)
    
    return techniques_used_by_malware

def get_techniques_used_by_tools():
    """ techniques used by tools getter """
    global techniques_used_by_tools

    if not techniques_used_by_tools:
        techniques_used_by_tools = rsh.techniques_used_by_tools(site_config.srcs)
    
    return techniques_used_by_tools

def get_techniques_used_by_groups():
    """ techniques used by groups getter """
    global techniques_used_by_groups

    if not techniques_used_by_groups:
        techniques_used_by_groups = rsh.techniques_used_by_groups(site_config.srcs)

    return techniques_used_by_groups

def get_groups_using_tool():
    """ groups using tool getter """
    global groups_using_tool

    if not groups_using_tool:
        groups_using_tool = rsh.groups_using_tool(site_config.srcs)

    return groups_using_tool

def get_groups_using_malware():
    """ groups using malware getter """
    global groups_using_malware

    if not groups_using_malware:
        groups_using_malware = rsh.groups_using_malware(site_config.srcs)
    
    return groups_using_malware
        
def get_mitigation_mitigates_techniques():
    """ mitigation migates techniques getter """
    global mitigation_mitigates_techniques

    if not mitigation_mitigates_techniques:
        mitigation_mitigates_techniques = rsh.mitigation_mitigates_techniques(site_config.srcs)

    return mitigation_mitigates_techniques

def get_technique_mitigated_by_mitigation():
    """ technique mitigated by mitigation getter """
    global technique_mitigated_by_mitigation

    if not technique_mitigated_by_mitigation:
        technique_mitigated_by_mitigation = rsh.technique_mitigated_by_mitigation(site_config.srcs)

    return technique_mitigated_by_mitigation

def get_technique_related_to_technique():
    """ technique related to technique """
    global technique_related_to_technique

    if not technique_related_to_technique:
        technique_related_to_technique = rsh.technique_related_to_technique(site_config.srcs)

    return technique_related_to_technique

def get_tools_using_technique():
    """ tools using technique getter """
    global tools_using_technique

    if not tools_using_technique:
        tools_using_technique = rsh.tools_using_technique(site_config.srcs)
    
    return tools_using_technique

def get_malware_using_technique():
    """ malware using technique getter """
    global malware_using_technique

    if not malware_using_technique:
        malware_using_technique = rsh.malware_using_technique(site_config.srcs)
    
    return malware_using_technique

def get_groups_using_technique():
    """ groups using technique getter """
    global groups_using_technique

    if not groups_using_technique:
        groups_using_technique = rsh.groups_using_technique(site_config.srcs)
    
    return groups_using_technique

def get_subtechniques_of():
    """ subtechniques of techniques getter """
    global subtechniques_of

    if not subtechniques_of:
        subtechniques_of = rsh.subtechniques_of(site_config.srcs)
    
    return subtechniques_of

def get_parent_technique_of():
    """ parent of subtechnique getter """
    global parent_technique_of

    if not parent_technique_of:
        parent_technique_of = rsh.parent_technique_of(site_config.srcs)
    
    return parent_technique_of

def get_ms():
    """ memory share getter """
    global ms

    if not ms:
        ms = stixhelpers.get_stix_memory_stores() 
    
    return ms

def get_resources():
    """ resources getter """
    global resources

    if not resources:
       resources = stixhelpers.grab_resources(get_ms())
       
    return resources

def get_relationships():
    """ relationship getter """
    global relationships

    if not relationships:
        relationships = get_resources()['relationships']
    
    return relationships

def get_group_list():
    """ group list getter """
    global group_list

    if not group_list:
        group_list = get_resources()['groups']

    return group_list

def get_software_list():
    """ software list getter """
    global software_list

    if not software_list:
        software_list = get_resources()['software']
    
    return software_list

def get_technique_list():
    """ technique list getter """
    global technique_list

    if not technique_list:
        technique_list = get_resources()['techniques']

    return technique_list 

def get_mitigation_list():
    """ mitigation list getter """
    global mitigation_list

    if not mitigation_list:
        mitigation_list = get_resources()['mitigations']
    
    return mitigation_list

def get_technique_to_domain():
    """ technique to domain getter """
    global technique_to_domain
    
    if not technique_to_domain:
        technique_to_domain = stixhelpers.get_technique_id_domain_map(get_ms())
    
    return technique_to_domain