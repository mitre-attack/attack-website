import json
import stix2
from modules import site_config
from . import buildhelpers

def get_mitigation_list(src):
    """Reads the STIX and returns a list of all mitigations in the STIX"""

    mitigations = src.query([
        stix2.Filter('type', '=', 'course-of-action'),
        stix2.Filter('revoked', '=', False)
    ])

    #Filter out deprecated objects for mitigation pages
    mitigations = [x for x in mitigations if not hasattr(x, 'x_mitre_deprecated') or x.x_mitre_deprecated == False]
    
    return sorted(mitigations, key=lambda k: k['name'].lower())

def get_matrices(src):
    """Reads the STIX and returns a list of all matrices in the STIX"""

    matrices = src.query([
        stix2.Filter('type', '=', 'x-mitre-matrix'),
    ])

    return matrices

def get_tactic_list(src, matrix_id=None):
    """Reads the STIX and returns a list of all tactics in the STIX"""

    tactics = []
    matrix = src.query([
        stix2.Filter('type', '=', 'x-mitre-matrix'),
    ])

    if matrix_id:
        for curr_matrix in matrix:
            if curr_matrix['id'] == matrix_id:
                for tactic_id in curr_matrix['tactic_refs']:
                    tactics.append(src.query([stix2.Filter('id', '=', tactic_id)])[0])    
    else:
        for i in range(len(matrix)):
            for tactic_id in matrix[i]['tactic_refs']:
                tactics.append(src.query([stix2.Filter('id', '=', tactic_id)])[0])    
    
    return tactics

def get_all_of_type(src, obj_type):
    """Reads the STIX and returns a list of all of a particular
       type of object in the STIX
    """

    return src.query([stix2.Filter('type', '=', obj_type)])

def get_techniques(src):
    """Reads the STIX and returns a list of all techniques in the STIX"""

    tech_list = src.query([
        stix2.Filter('type', '=', 'attack-pattern'),
        stix2.Filter('revoked', '=', False)
    ])

    tech_list = sorted(tech_list, key=lambda k: k['name'].lower())
    return tech_list

def get_revoked_by(stix_id, src):
    """Given a stix_id, return an object that revokes it,
       if no object is found, return None
    """

    relations = src.relationships(stix_id, 'revoked-by', source_only=True)
    revoked_by = src.query([
        stix2.Filter('id', 'in', [r.target_ref for r in relations]),
        stix2.Filter('revoked', '=', False)
    ])
    if revoked_by:
        try:
            revoked_by = revoked_by[0]
        except IndexError:
            print("Malformed STIX content detected")
            print(stix_id)
            revoked_by = revoked_by[0]
    return revoked_by

def get_examples(tech_stix_id, src):
    """Given a technique stix id, return a list of examples with their 
       external references.
    """

    examples = []
    ext_refs = []
    for r in src.relationships(tech_stix_id, 'uses', target_only=True):
        if stix2.utils.get_type_from_id(r.source_ref) in ['intrusion-set', 'tool', 'malware']:
            curr_refs = None
            attack_id = None
            if 'external_references' in r:
                curr_refs = r.external_references
            example = src.query([
                stix2.Filter('id', '=', r.source_ref), 
                stix2.Filter('revoked', '=', False)
            ])[0]
            attack_id = buildhelpers.get_attack_id(example)
            examples.append({'name': example.name, 
                             'id': attack_id, 
                             'description': r.description, 
                             'ext_refs': curr_refs})
    
    examples = sorted(examples, key=lambda k: k['name'].lower())
    for example in examples:
        if example['ext_refs']:
            ext_refs += example['ext_refs']

    return examples, ext_refs

def get_technique_id_domain_map(ms):
    """Create map from technique_id to domain"""
    
    tech_list = {}

    for domain in site_config.domains:
        curr_list = ms[domain].query([
            stix2.Filter('type', '=', 'attack-pattern'),
            stix2.Filter('revoked', '=', False)
        ])
        for val in curr_list:
            technique_id = buildhelpers.get_attack_id(val)
            if technique_id:
                tech_list[technique_id] = domain
    
    return tech_list

def grab_resources(ms):
    """Returns a dict that contains lists for the software, group,
       technique and mitigation objects.
    """

    #Generates the list of techniques
    tech_list = []
    for domain in site_config.domains:
        curr_list = ms[domain].query([
            stix2.Filter('type', '=', 'attack-pattern'),
            stix2.Filter('revoked', '=', False)
        ])
        for val in curr_list:
            if next((x for x in tech_list if x.id == val.id), None) is None:
                tech_list.append(val)   
    tech_list = sorted(tech_list, key=lambda k: k['name'].lower())

    #Generates list of software
    software_list = []
    for domain in site_config.domains:
        curr_list = ms[domain].query([
            stix2.Filter('type', '=', 'malware'),
            stix2.Filter('revoked', '=', False)
        ])
        # Remove duplicates from different domains
        for val in curr_list:
            if next((x for x in software_list if x.id == val.id), None) is None:
                software_list.append(val)
        curr_list = ms[domain].query([
            stix2.Filter('type', '=', 'tool'),
            stix2.Filter('revoked', '=', False)
        ])
        # Remove duplicates from different domains
        for val in curr_list:
            if next((x for x in software_list if x.id == val.id), None) is None:
                software_list.append(val)   
    software_list = sorted(software_list, key=lambda k: k["name"].lower() )

    #Generates list of groups
    group_list = []
    for domain in site_config.domains:
        curr_list = ms[domain].query([
            stix2.Filter('type', '=', 'intrusion-set'),
            stix2.Filter('revoked', '=', False)
        ])
        # Remove duplicates from different domains
        for val in curr_list:
            if next((x for x in group_list if x.id == val.id), None) is None:
                group_list.append(val)
    group_list = sorted(group_list, key=lambda k: k["name"].lower())

    #Generates a list of CoA
    coa_list = []
    for domain in site_config.domains:
        curr_list = ms[domain].query([
            stix2.Filter("type", "=", "course-of-action"),
            stix2.Filter('revoked', '=', False)
        ])
        #remove duplicates from different domains
        for val in curr_list:
            if next((x for x in coa_list if x.id == val.id), None) is None:
                coa_list.append(val)
    coa_list = sorted(coa_list, key=lambda k: k["name"].lower() )

    #Generates list of relationships
    rel_list = []
    for domain in site_config.domains:
        curr_list = ms[domain].query([
            stix2.Filter('type', '=', 'relationship'),
        ])
        rel_list = rel_list + curr_list
    resources = {
        "relationships": rel_list, 
        "groups": group_list, 
        "software": software_list, 
        "techniques": tech_list, 
        "mitigations": coa_list
    }
    return resources

def get_stix_memory_stores():
    """This function reads the json files for each domain and creates a dict
       that contains the memory stores for each domain.
    """

    src = {}

    for domain in site_config.bundles:
        src[domain] = stix2.MemoryStore()
        src[domain].load_from_file(site_config.attack_path[domain])

    return src

def get_contributors(ms):
    """Gets all contributors in the STIX content"""

    # contributors not in STIX are stored here:
    contributors = [
        'Craig Aitchison',
        'Elly Searle, CrowdStrike — contributed to tactic definitions'
    ]

    for domain in site_config.domains:
        obj_types = ['attack-pattern', 'malware', 'tool', 'intrusion-set']
        src = ms[domain]
        obj_list = []
        for curr_type in obj_types:
            obj_list += src.query([
                stix2.Filter('type', '=', curr_type)
            ])

        for obj in obj_list:
            if 'x_mitre_contributors' in obj:
                contributors += obj['x_mitre_contributors']
    contributors = list(set(contributors))
    
    return sorted(contributors, key=lambda k: k.lower())