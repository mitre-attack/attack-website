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

    if malware_used_by_groups:
        return malware_used_by_groups
    else:
        return rsh.malware_used_by_groups(site_config.srcs)

def get_tools_used_by_groups():
    """ tools used by groups getter """

    if tools_used_by_groups:
        return tools_used_by_groups
    else:
        return rsh.tools_used_by_groups(site_config.srcs)

def get_techniques_used_by_malware():
    """ techniques used by malware getter """

    if techniques_used_by_malware:
        return techniques_used_by_malware
    else:
        return rsh.techniques_used_by_malware(site_config.srcs)

def get_techniques_used_by_tools():
    """ techniques used by tools getter """

    if techniques_used_by_tools:
        return techniques_used_by_tools
    else:
        return rsh.techniques_used_by_tools(site_config.srcs)

def get_techniques_used_by_groups():
    """ techniques used by groups getter """

    if techniques_used_by_groups:
        return techniques_used_by_groups
    else:
        return rsh.techniques_used_by_groups(site_config.srcs)

def get_groups_using_tool():
    """ groups using tool getter """

    if groups_using_tool:
        return groups_using_tool
    else:
        return rsh.groups_using_tool(site_config.srcs)

def get_groups_using_malware():
    """ groups using malware getter """

    if groups_using_malware:
        return groups_using_malware
    else:
        return rsh.groups_using_malware(site_config.srcs)
        
def get_mitigation_mitigates_techniques():
    """ mitigation migates techniques getter """

    if mitigation_mitigates_techniques:
        return mitigation_mitigates_techniques
    else:
        return rsh.mitigation_mitigates_techniques(site_config.srcs)

def get_technique_mitigated_by_mitigation():
    """ technique mitigated by mitigation getter """

    if technique_mitigated_by_mitigation:
        return technique_mitigated_by_mitigation
    else:
        return rsh.technique_mitigated_by_mitigation(site_config.srcs)

def get_technique_related_to_technique():
    """ technique related to technique """

    if technique_related_to_technique:
        return technique_related_to_technique
    else:
        return rsh.technique_related_to_technique(site_config.srcs)

def get_tools_using_technique():
    """ tools using technique getter """

    if tools_using_technique:
        return tools_using_technique
    else:
        return rsh.tools_using_technique(site_config.srcs)

def get_malware_using_technique():
    """ malware using technique getter """

    if malware_using_technique:
        return malware_using_technique
    else:
        return rsh.malware_using_technique(site_config.srcs)

def get_groups_using_technique():
    """ groups using technique getter """

    if groups_using_technique:
        return groups_using_technique
    else:
        return rsh.groups_using_technique(site_config.srcs)

def get_ms():
    """ memory share getter """

    if ms:
        return ms
    else:
        return stixhelpers.get_stix_memory_stores()

def get_resources():
    """ resources getter """

    if resources:
        return resources
    else:
        return stixhelpers.grab_resources(get_ms())

def get_relationships():
    """ relationship getter """

    if relationships:
        return relationships
    else:
        return get_resources()['relationships']

def get_group_list():
    """ group list getter """

    if group_list:
        return group_list
    else:
        return get_resources()['groups']

def get_software_list():
    """ software list getter """

    if software_list:
        return software_list
    else:
        return get_resources()['software']

def get_technique_list():
    """ technique list getter """

    if technique_list:
        return technique_list
    else:
        return get_resources()['techniques']

def get_mitigation_list():
    """ mitigation list getter """

    if mitigation_list:
        return mitigation_list
    else:
        return get_resources()['mitigations']

def get_technique_to_domain():
    """ technique to domain getter """
    
    if technique_to_domain:
        return technique_to_domain
    else:
        return stixhelpers.get_technique_id_domain_map(get_ms())