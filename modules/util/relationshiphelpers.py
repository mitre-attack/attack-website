import json
from collections import OrderedDict
from itertools import chain

from loguru import logger
from stix2 import Filter


def query_all(srcs, filters):
    """Return the union of a query across multiple memorystores."""
    return list(chain.from_iterable(src.query(filters) for src in srcs))


def get_related(srcs, src_type, rel_type, target_type, reverse=False):
    """Build relationship mappings.

    params:
        srcs: memorystores for enterprise and mobile in an array
        src_type: source type for the relationships, e.g "attack-pattern"
        rel_type: relationship type for the relationships, e.g "uses"
        target_type: target type for the relationship, e.g "intrusion-set"
        reverse: build reverse mapping of target to source
    """

    relationships_with_dups = query_all(
        srcs,
        [
            Filter("type", "=", "relationship"),
            Filter("relationship_type", "=", rel_type),
            Filter("revoked", "=", False),
        ],
    )

    relationships_dict = OrderedDict()
    for relationship in relationships_with_dups:
        if relationship["id"] not in relationships_dict:
            relationships_dict[relationship["id"]] = relationship

    relationships = relationships_dict.values()

    # stix_id => [ ids of objects with relationships with stix_id ]
    id_to_related = {}

    # build the dict
    for relationship in relationships:
        if relationship.get("x_mitre_deprecated"):
            continue

        if src_type in relationship.source_ref and target_type in relationship.target_ref:
            if (relationship.source_ref in id_to_related and not reverse) or (
                relationship.target_ref in id_to_related and reverse
            ):
                if not reverse:
                    id_to_related[relationship.source_ref].append(
                        {"relationship": relationship, "id": relationship.target_ref}
                    )
                else:
                    id_to_related[relationship.target_ref].append(
                        {"relationship": relationship, "id": relationship.source_ref}
                    )
            else:
                if not reverse:
                    id_to_related[relationship.source_ref] = [
                        {"relationship": relationship, "id": relationship.target_ref}
                    ]
                else:
                    id_to_related[relationship.target_ref] = [
                        {"relationship": relationship, "id": relationship.source_ref}
                    ]
    # all objects of target type
    if not reverse:
        if target_type.startswith("x-mitre"):
            targets = query_all(srcs, [Filter("type", "=", target_type)])
        else:
            targets = query_all(srcs, [Filter("type", "=", target_type), Filter("revoked", "=", False)])
    else:
        if src_type.startswith("x-mitre"):
            targets = query_all(srcs, [Filter("type", "=", src_type)])
        else:
            targets = query_all(srcs, [Filter("type", "=", src_type), Filter("revoked", "=", False)])

    id_to_target = {}
    # build the dict
    for target in targets:
        if target.get("id"):
            id_to_target[target["id"]] = target

    output = {}
    for stix_id in id_to_related:
        value = []
        for related in id_to_related[stix_id]:
            if not related["id"] in id_to_target:
                continue  # targetting a revoked object

            if related["id"].startswith("x-mitre"):
                value.append(
                    {
                        "object": id_to_target[related["id"]],
                        "relationship": json.loads(related["relationship"].serialize()),
                    }
                )
            else:
                value.append(
                    {
                        "object": json.loads(id_to_target[related["id"]].serialize()),
                        "relationship": json.loads(related["relationship"].serialize()),
                    }
                )
        output[stix_id] = value
    return output


# tool:group
def tools_used_by_groups(srcs):
    """Return group_id => {tool, relationship} for each tool used by the group.

    srcs should be an array of memorystores for enterprise, mobile, and pre
    """
    return get_related(srcs, "intrusion-set", "uses", "tool")


def groups_using_tool(srcs):
    """Return tool_id => {group, relationship} for each group using the tool.

    srcs should be an array of memorystores for enterprise, mobile and pre
    """
    return get_related(srcs, "intrusion-set", "uses", "tool", reverse=True)


# tool:campaign
def tools_used_by_campaigns(srcs):
    """Return campaign_id => {tool, relationship} for each tool used by the campaign.

    srcs should be an array of memorystores for enterprise, mobile, and pre
    """
    return get_related(srcs, "campaign", "uses", "tool")


def campaigns_using_tool(srcs):
    """Return tool_id => {campaign, relationship} for each campaign using the tool.

    srcs should be an array of memorystores for enterprise, mobile and pre
    """
    return get_related(srcs, "campaign", "uses", "tool", reverse=True)


# malware:group
def malware_used_by_groups(srcs):
    """Return group_id => {malware, relationship} for each malware used by group.

    srcs should be an array of memorystores for enterprise, mobile, and pre
    """
    return get_related(srcs, "intrusion-set", "uses", "malware")


def groups_using_malware(srcs):
    """Return malware_id => {group, relationship} for each group using the malware.

    srcs should be an array of memorystores for enterprise, mobile, and pre
    """
    return get_related(srcs, "intrusion-set", "uses", "malware", reverse=True)


# malware:campaign
def malware_used_by_campaigns(srcs):
    """Return campaign_id => {malware, relationship} for each malware used by campaign.

    srcs should be an array of memorystores for enterprise, mobile, and pre
    """
    return get_related(srcs, "campaign", "uses", "malware")


def campaigns_using_malware(srcs):
    """Return malware_id => {campaign, relationship} for each campaign using the malware.

    srcs should be an array of memorystores for enterprise, mobile, and pre
    """
    return get_related(srcs, "campaign", "uses", "malware", reverse=True)


# technique:data component
def techniques_detected_by_datacomponent(srcs):
    """Return datacomponent_id => {technique, relationship} for each technique detected by data component.

    srcs should be an array of memorystores for enterprise, mobile, and pre.
    The mobile and pre memorystores should not contain data components nor data sources.
    """
    return get_related(srcs, "x-mitre-data-component", "detects", "attack-pattern")


def datacomponents_detecting_technique(srcs):
    """Return technique => {data component, relationship} for each data component decting a technique.

    srcs should be an array of memorystores for enterprise, mobile, and pre.
    The mobile and pre memorystores should not contain data components nor data sources.
    """
    return get_related(srcs, "x-mitre-data-component", "detects", "attack-pattern", reverse=True)


# technique:group
def techniques_used_by_groups(srcs):
    """Return group_id => {technique, relationship} for each technique used by the group.

    srcs should be an array of memorystores for enterprise, mobile, and pre
    """
    return get_related(srcs, "intrusion-set", "uses", "attack-pattern")


def groups_using_technique(srcs):
    """Return technique_id => {group, relationship} for each group using the technique.

    srcs should be an array of memorystores for enterprise, mobile and pre
    """
    return get_related(srcs, "intrusion-set", "uses", "attack-pattern", reverse=True)


# technique:campaign
def techniques_used_by_campaigns(srcs):
    """Return campaign_id => {technique, relationship} for each technique used by the campaign.

    srcs should be an array of memorystores for enterprise, mobile, and pre
    """
    return get_related(srcs, "campaign", "uses", "attack-pattern")


def campaigns_using_technique(srcs):
    """Return technique_id => {campaign, relationship} for each campaign using the technique.

    srcs should be an array of memorystores for enterprise, mobile and pre
    """
    return get_related(srcs, "campaign", "uses", "attack-pattern", reverse=True)


def groups_attributed_to_campaign(srcs):
    """Return campaign_id => {group, relationship} for each group attributed to the campaign

    srcs should be an array of memorystores for enterprise, mobile, and pre
    """
    return get_related(srcs, "campaign", "attributed-to", "intrusion-set")


def campaigns_attributed_to_group(srcs):
    """Return group_id => {campaign, relationship} for each campaign attributed to the group

    srcs should be an array of memorystores for enterprise, mobile, and pre
    """
    return get_related(srcs, "campaign", "attributed-to", "intrusion-set", reverse=True)


# technique:malware
def techniques_used_by_malware(srcs):
    """Return malware => {technique, relationship} for each technique used by the malware.

    srcs should be an array of memorystores for enterprise, mobile, and pre
    """
    return get_related(srcs, "malware", "uses", "attack-pattern")


def malware_using_technique(srcs):
    """Return technique_id  => {malware, relationship} for each malware using the technique.

    srcs should be an array of memorystores for enterprise, mobile, and pre
    """
    return get_related(srcs, "malware", "uses", "attack-pattern", reverse=True)


# technique:tool
def techniques_used_by_tools(srcs):
    """Return tool_id => {technique, relationship} for each technique used by the tool.

    srcs should be an array of memorystores for enterprise, mobile, and pre
    """
    return get_related(srcs, "tool", "uses", "attack-pattern")


def tools_using_technique(srcs):
    """Return technique_id => {tool, relationship} for each tool using the technique.

    srcs should be an array of memorystores for enterprise, mobile, and pre
    """
    return get_related(srcs, "tool", "uses", "attack-pattern", reverse=True)


# technique:mitigation
def mitigation_mitigates_techniques(srcs):
    """Return mitigation_id => {technique, relationship} for each technique mitigated by the mitigation.

    srcs should be an array of memorystores for enterprise, mobile, and pre
    """
    return get_related(srcs, "course-of-action", "mitigates", "attack-pattern", reverse=False)


def technique_mitigated_by_mitigation(srcs):
    """Return technique_id => {mitigation, relationship} for each mitigation of the technique.

    srcs should be an array of memorystores for enterprise, mobile, and pre
    """
    return get_related(srcs, "course-of-action", "mitigates", "attack-pattern", reverse=True)


# technique:technique
def technique_related_to_technique(srcs):
    """Return technique_id => {technique, relationship} for each technique related to the technique.

    srcs should be an array of memorystores for enterprise, mobile, and pre
    """
    return get_related(srcs, "attack-pattern", "related-to", "attack-pattern")


# technique:subtechnique
def subtechniques_of(srcs):
    """Return technique_id => {subtechnique, relationship} for each subtechnique of the technique.

    srcs should be an array of memorystores for enterprise, mobile, and pre
    """
    return get_related(srcs, "attack-pattern", "subtechnique-of", "attack-pattern", reverse=True)


def parent_technique_of(srcs):
    """Return subtechnique_id => {technique, relationship} describing the parent technique of the subtechnique.

    srcs should be an array of memorystores for enterprise, mobile, and pre
    """
    return get_related(srcs, "attack-pattern", "subtechnique-of", "attack-pattern")


def get_objects_using_notes(srcs):
    """Build note object mapping.

    params:
        srcs: memorystores array
    """
    notes = query_all(srcs, [Filter("type", "=", "note"), Filter("revoked", "=", False)])

    # stix_id => [ ids of objects with relationships with stix_id ]
    id_to_notes = {}

    for note in notes:
        if note.get("object_refs"):
            for obj in note["object_refs"]:
                if obj in id_to_notes:
                    id_to_notes[obj].append(json.loads(note.serialize()))
                else:
                    id_to_notes[obj] = [json.loads(note.serialize())]

    return id_to_notes
