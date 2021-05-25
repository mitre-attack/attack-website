import json
import os
import requests
import stix2
import urllib3
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
        if domain['deprecated']: continue
        curr_list = ms[domain['name']].query([
            stix2.Filter('type', '=', 'attack-pattern'),
            stix2.Filter('revoked', '=', False)
        ])
        for val in curr_list:
            technique_id = buildhelpers.get_attack_id(val)
            if technique_id:
                tech_list[technique_id] = domain['name']
    
    return tech_list

def add_replace_or_ignore(obj_list, obj_in_question):
    """ Add if object does not already exist
        Replace if a newer version of the object is found
        Ignore if object already exists but object in question is outdated or deprecated
    """

    def get_conflictive_object():
        """ Return object if already in list if there is a conflict with the STIX ID or ATT&CK ID """
        for obj in obj_list:
            if obj.id == obj_in_question.id or buildhelpers.get_attack_id(obj) == buildhelpers.get_attack_id(obj_in_question):
                return obj
        return []

    object_in_conflict = get_conflictive_object()

    # Object does not exist: Add
    # Verify if object does not appear with STIX ID or ATT&CK ID
    if not object_in_conflict:
        obj_list.append(obj_in_question)
        return obj_list

    # Object already exists: Replace
    # If object in conflict is deprecated and new object is not, select new
    if object_in_conflict.get('x_mitre_deprecated') and not obj_in_question.get('x_mitre_deprecated'):
        # Replace object in conflict with object in question
        obj_list = [obj_in_question if x == object_in_conflict else x for x in obj_list]
        return obj_list

    # If both objects are deprecated, select the most recently modified
    if object_in_conflict.get('x_mitre_deprecated') and obj_in_question.get('x_mitre_deprecated'):

        conflict_modified = object_in_conflict.get('modified')
        in_question_modified = obj_in_question.get('modified')

        if in_question_modified > conflict_modified:
            # Replace object in conflict with object in question
            obj_list = [obj_in_question if x == object_in_conflict else x for x in obj_list]
        return obj_list
    
    # Object will not be replaced: Ignore
    return obj_list

def grab_resources(ms):
    """Returns a dict that contains lists for the software, group,
       technique and mitigation objects.
    """

    #Generates the list of techniques
    tech_list = []
    for domain in site_config.domains:
        if domain['deprecated']: continue
        curr_list = ms[domain['name']].query([
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
        if domain['deprecated']: continue
        curr_list = ms[domain['name']].query([
            stix2.Filter('type', '=', 'malware'),
            stix2.Filter('revoked', '=', False)
        ])
        # Remove duplicates from different domains
        for val in curr_list:
            software_list = add_replace_or_ignore(software_list, val)
        curr_list = ms[domain['name']].query([
            stix2.Filter('type', '=', 'tool'),
            stix2.Filter('revoked', '=', False)
        ])
        # Remove duplicates from different domains
        for val in curr_list:
            software_list = add_replace_or_ignore(software_list, val)
    
    # tech_list = remove_duplicate_attack_ids(techn_list) 
    software_list = sorted(software_list, key=lambda k: k["name"].lower() )

    #Generates list of groups
    group_list = []
    for domain in site_config.domains:
        if domain['deprecated']: continue
        curr_list = ms[domain['name']].query([
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
        if domain['deprecated']: continue
        curr_list = ms[domain['name']].query([
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
        if domain['deprecated']: continue
        curr_list = ms[domain['name']].query([
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

    # suppress InsecureRequestWarning: Unverified HTTPS request is being made
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    ms = {}
    srcs = []

    # Set proxy
    proxy  = ""
    if site_config.args.proxy:
        proxy = site_config.args.proxy
    proxyDict = { 
        "http"  : proxy,
        "https" : proxy
    }

    for domain in site_config.domains:

        # Download json from http or https
        if domain['location'].startswith("http"):
            stix_json = requests.get(domain['location'], verify=False, proxies=proxyDict)
            if stix_json.status_code == 200:
                stix_json = stix_json.json()
                ms[domain['name']] = stix2.MemoryStore(stix_data=stix_json['objects'])
            elif stix_json.status_code == 404:
                exit(f"\n{domain['location']} stix bundle was not found")
            else:
                exit(f"\n{domain['location']} stix bundle download was unsuccessful")
        else:
            if os.path.exists(domain['location']):
                ms[domain['name']] = stix2.MemoryStore()
                ms[domain['name']].load_from_file(domain['location'])
            else:
                exit(f"\n{domain['location']} local file does not exist. If you intended a URL, please include http:// or https://")
        
        if not domain['deprecated']:
            srcs.append(ms[domain['name']])

    return ms, srcs

def get_contributors(ms):
    """Gets all contributors in the STIX content"""

    # contributors not in STIX are stored here:
    contributors = [
        'Craig Aitchison',
        'Elly Searle, CrowdStrike — contributed to tactic definitions'
    ]

    for domain in site_config.domains:
        if domain['deprecated']: continue
        obj_types = ['attack-pattern', 'malware', 'tool', 'intrusion-set']
        src = ms[domain['name']]
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