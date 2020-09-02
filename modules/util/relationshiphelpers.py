from stix2 import MemoryStore, Filter
import json
from itertools import chain

def query_all(srcs, filters):
    """return the union of a query across multiple memorystores"""
    
    return list(chain.from_iterable(
        src.query(filters) for src in srcs
    ))

def get_related(srcs, src_type, rel_type, target_type, reverse=False):
    """build relationship mappings
       params:
         srcs: memorystores for enterprise and mobile in an array
         src_type: source type for the relationships, e.g "attack-pattern"
         rel_type: relationship type for the relationships, e.g "uses"
         target_type: target type for the relationship, e.g "intrusion-set"
         reverse: build reverse mapping of target to source
    """

    relationships = query_all(srcs, [
        Filter('type', '=', 'relationship'),
        Filter('relationship_type', '=', rel_type),
        Filter('revoked', '=', False)
    ])

    # stix_id => [ ids of objects with relationships with stix_id ]
    id_to_related = {} 

    # build the dict
    for relationship in relationships:
        if (src_type in relationship.source_ref and target_type in relationship.target_ref):
            if (relationship.source_ref in id_to_related and not reverse) or (relationship.target_ref in id_to_related and reverse):
                if not reverse: 
                    id_to_related[relationship.source_ref].append({
                        "relationship": relationship,
                        "id": relationship.target_ref
                    })
                else: 
                    id_to_related[relationship.target_ref].append({
                        "relationship": relationship, 
                        "id": relationship.source_ref
                    })
            else:
                if not reverse: 
                    id_to_related[relationship.source_ref] = [{
                        "relationship": relationship, 
                        "id": relationship.target_ref
                    }]
                else:
                    id_to_related[relationship.target_ref] = [{
                        "relationship": relationship, 
                        "id": relationship.source_ref
                    }]
    # all objects of target type
    if not reverse:
        targets = query_all(srcs, [
            Filter('type', '=', target_type),
            Filter('revoked', '=', False)
        ])
    else:
        targets = query_all(srcs, [
            Filter('type', '=', src_type),
            Filter('revoked', '=', False)
        ])

    id_to_target = {}
    # build the dict
    for target in targets:
        id_to_target[target.id] = target

    output = {}
    for stix_id in id_to_related:
        value = []
        for related in id_to_related[stix_id]:
            if not related["id"] in id_to_target:
                continue # targetting a revoked object
            value.append({
                "object": json.loads(id_to_target[related["id"]].serialize()),
                "relationship": json.loads(related["relationship"].serialize())
            })
        output[stix_id] = value
    return output


# tool:group
def tools_used_by_groups(srcs):
    """returns group_id => {tool, relationship} for each tool used by the 
       group. srcs should be an array of memorystores for enterprise,
       mobile and pre
    """
    return get_related(srcs, "intrusion-set", "uses", "tool")
def groups_using_tool(srcs):
    """returns tool_id => {group, relationship} for each group using the tool.
       srcs should be an array of memorystores for enterprise, mobile and pre
    """
    return get_related(srcs, "intrusion-set", "uses", "tool", reverse=True)
    
# malware:group
def malware_used_by_groups(srcs):
    """returns group_id => {malware, relationship} for each malware used by
       group. srcs should be an array of memorystores for enterprise, 
       mobile and pre
    """
    return get_related(srcs, "intrusion-set", "uses", "malware")
def groups_using_malware(srcs):
    """returns malware_id => {group, relationship} for each group using
       the malware. srcs should be an array of memorystores for enterprise,
       mobile and pre
    """
    return get_related(srcs, "intrusion-set", "uses", "malware", reverse=True)

# technique:group
def techniques_used_by_groups(srcs):
    """returns group_id => {technique, relationship} for each technique used
       by the group. srcs should be an array of memorystores for enterprise, 
       mobile and pre
    """
    return get_related(srcs, "intrusion-set", "uses", "attack-pattern")
def groups_using_technique(srcs):
    """returns technique_id => {group, relationship} for each group using the
       technique. srcs should be an array of memorystores for enterprise, 
       mobile and pre
    """
    return get_related(srcs, "intrusion-set", "uses", "attack-pattern", reverse=True)

# technique:malware
def techniques_used_by_malware(srcs):
    """return malware => {technique, relationship} for each technique
       used by the malware. srcs should be an array of memorystores for
       enterprise, mobile and pre
    """
    return get_related(srcs, "malware", "uses", "attack-pattern")
def malware_using_technique(srcs):
    """return technique_id  => {malware, relationship} for each malware using
       the technique. srcs should be an array of memorystores for enterprise,
       mobile and pre
    """
    return get_related(srcs, "malware", "uses", "attack-pattern", reverse=True)

# technique:tool
def techniques_used_by_tools(srcs):
    """return tool_id => {technique, relationship} for each technique used
       by the tool. srcs should be an array of memorystores for enterprise,
       mobile and pre
    """
    return get_related(srcs, "tool", "uses", "attack-pattern")
def tools_using_technique(srcs):
    """return technique_id => {tool, relationship} for each tool using the
       technique. srcs should be an array of memorystores for enterprise,
       mobile and pre
    """
    return get_related(srcs, "tool", "uses", "attack-pattern", reverse=True)

# technique:mitigation
def mitigation_mitigates_techniques(srcs):
    """return mitigation_id => {technique, relationship} for each technique 
       mitigated by the mitigation. srcs should be an array of memorystores 
       for enterprise, mobile and pre
    """
    return get_related(srcs, "course-of-action", "mitigates", "attack-pattern", reverse=False)
def technique_mitigated_by_mitigation(srcs):
    """return technique_id => {mitigation, relationship} for each mitigation
       of the technique. srcs should be an array of memorystores for 
       enterprise, mobile and pre
    """
    return get_related(srcs, "course-of-action", "mitigates", "attack-pattern", reverse=True)

# technique:technique
def technique_related_to_technique(srcs):
    """return technique_id => {technique, relationship} for each technique 
       related to the technique. srcs should be an array of memorystores for 
       enterprise, mobile and pre
    """
    return get_related(srcs, "attack-pattern", "related-to", "attack-pattern")

# technique:subtechnique
def subtechniques_of(srcs):
    """ return technique_id => {subtechnique, relationship} for each subtechnique
        of the technique. srcs should be an array of memorystores for enterprise,
        mobile and pre
    """
    return get_related(srcs, "attack-pattern", "subtechnique-of", "attack-pattern", reverse=True)

def parent_technique_of(srcs):
    """ return subtechnique_id => {technique, relationship} describing the parent technique
        of the subtechnique. srcs should be an array of memorystores for enterprise,
        mobile and pre
    """
    return get_related(srcs, "attack-pattern", "subtechnique-of", "attack-pattern")

def load(url):
    """Load stix data from file"""
    src = MemoryStore()
    src.load_from_file(url)
    return src
