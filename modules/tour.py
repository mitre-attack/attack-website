from . import config
from . import stixhelpers
from . import  util
import os

def generate_tour():
    """Responsible for dynamically generating tour steps
    """

    # Algorithm
    # For each domain:
    # 1. index (start page, doesn't need to be dynamic)
    # 2. A matrix with sub-techniques
    # 3. A technique with sub-techniques
    # 4. One of the sub-techniques of that technique
    # 5. A group/software that meets the following criteria:
    # 5.1. Group has a relationship with a technique but not that technique's sub-techniques
    # 5.2. Group has a relationship with a technique and (preferably) 2+ of that technique's sub-techniques
    # 5.3. Group has a relationship with (preferably) 2+ sub-techniques but not the parent technique.
    #      If any of the above criteria are not met by any software/group, that section of the group/software page of the tour can be skipped.

    tours = []
    for matrix in config.matrices:
        if matrix["type"] == "external": continue # link to externally hosted matrix, ignore it
        tours.append(get_tour_steps(matrix))
    
    # Choose longest tour
    def get_longest_tour():

        if tours:
            longest = {}
            for tour in tours:
                if len(tour.keys()) > len(longest.keys()):
                    longest = tour
            
            return longest
        
        return {}

    tour_steps = get_longest_tour()

    # Write tour steps to settings.js file
    javascript_settings_file = os.path.join(config.javascript_path, "settings.js")

    with open(javascript_settings_file, "a+", encoding='utf8') as js_f:
        js_data = config.js_tour_settings.substitute({"tour_steps": tour_steps})
        js_f.write(js_data)
    
def get_tour_steps(matrix):
    """ Get all the tour steps """

    ms = config.ms[matrix['matrix']]

    # Reads the STIX and creates a list of the techniques
    techniques = stixhelpers.get_techniques(ms)

    techs_no_subtechs = util.filter_out_subtechniques(techniques)
    techs_with_subtechs = util.filter_out_techniques_without_subtechniques(techniques)

    # steps as array
    steps = {}

    # If matrix has techniques with subtechniques
    if techs_with_subtechs:
        steps['matrix'] = "matrices/" + matrix['path']
    else:
        return steps
    
    # Find technique with sub-techniques
    technique = get_technique_with_subtechniques(techs_no_subtechs)

    # Get technique ID and store that as the step
    steps['technique'] = "techniques/{}".format(util.get_attack_id(technique))
    steps['subtechnique'] = steps['technique'] + "/{}".format(get_subtech_n_of_technique(technique))

    # Get group steps
    steps['group'] = get_group_with_subtechniques()

    # If group steps is empty try to find software with subtechniques
    if steps['group']:
        # TODO: Find software with subtechniques
        steps['software'] = get_software_with_subtechniques()

    return steps

def get_technique_with_subtechniques(techs_no_subtechs):
    """ Find first technique with at least 4 sub-techniques and return technique
        Return technique with the most sub-techniques if not the case 
    """

    counter = 0
    chosen_tech = {}
    for tech in techs_no_subtechs:
        if tech["id"] in config.subtechniques_of:

            # Grab sub-technique count from technique
            subtech_count =  len(config.subtechniques_of[tech["id"]])
            # Check if sub-technique count is bigger than counter
            if counter < subtech_count:
                # Quick return if found
                if subtech_count > 3: return tech
                # Set counter and new techique
                counter = subtech_count
                chosen_tech = tech
    
    return chosen_tech

def get_subtech_n_of_technique(technique):
    """ Return ID number of first sub-technique of given technique """

    for subtech in config.subtechniques_of[technique['id']]:
        id = util.get_attack_id(subtech['object'])
        return id.split(".")[1]

def get_group_with_subtechniques():
    """ Find group with the subtechniques to add to the tour """

    groups_tour_list = []

    for group in config.group_list:

        technique_list = {}

        if config.techniques_used_by_groups.get(group.get('id')):
            group_has_subtechniques = False
            for technique in config.techniques_used_by_groups[group['id']]:
                if not technique['object'].get('x_mitre_deprecated'):
                    # Get techniques used list and only update if it has subtechniques
                    if(techniques_used(technique_list, technique)):
                        group_has_subtechniques = True
            
            # Get list of potential tours if group has subtechniques
            if group_has_subtechniques:
                groups_tour = get_groups_tour(technique_list)
                if groups_tour:
                    groups_tour['group_id'] = "groups/" + util.get_attack_id(group)
                    groups_tour_list.append(groups_tour)

    def find_best_group():
        """ Find group with step 2 and 3 with 2 or more subtechniques """

        # Ideal: find Step 2 and Step 3 with most subtechniques
        group_w_largest_step_2_3 = {}
        for group_tour in groups_tour_list:

            # First group
            if not group_w_largest_step_2_3:
                group_w_largest_step_2_3 = group_tour
            
            # Verify if group tour has step 2 and step 3
            elif group_tour.get('step2') and group_tour.get('step3'):
                # Only update if step 2 and 3 where found
                if group_w_largest_step_2_3.get('step2') and group_w_largest_step_2_3.get('step3'):
                    # When new group has same or more subtechniques
                    if (group_w_largest_step_2_3['step2'][1] <= group_tour['step2'][1]) and (group_w_largest_step_2_3['step3'][1] <= group_tour['step3'][1]):
                        group_w_largest_step_2_3 = group_tour
                else:
                    group_w_largest_step_2_3 = group_tour
            # Case when step 2 is available but not step 3
            # Only update if current group does not have a step 3
            elif group_tour.get('step2') and not group_w_largest_step_2_3.get('step3'):
                if not group_w_largest_step_2_3.get('step2'):
                    group_w_largest_step_2_3 = group_tour
                elif group_w_largest_step_2_3['step2'][1] < group_tour['step2'][1]:
                    group_w_largest_step_2_3 = group_tour
            # Case when step 3 is available but not step 1
            # Only update if current group does not have a step 2               
            elif group_tour.get('step3') and not group_w_largest_step_2_3.get('step2'):
                if not group_w_largest_step_2_3.get('step3'):
                    group_w_largest_step_2_3 = group_tour
                elif group_w_largest_step_2_3['step3'][1] < group_tour['step3'][1]:
                    group_w_largest_step_2_3 = group_tour

        return group_w_largest_step_2_3

    return find_best_group()


def techniques_used(technique_list, technique):
    """ Add technique to technique list and make distinction between techniques
        subtechniques
    """

    attack_id = util.get_attack_id(technique['object'])
    has_subtechniques = False

    if attack_id:
        # Check if technique not already in technique_list dict
        if attack_id not in technique_list:

            # Check if attack id is a sub-technique
            if util.is_sub_tid(attack_id):
                has_subtechniques = True

                parent_id = util.get_parent_technique_id(attack_id)

                # If parent technique not already in list, add to list and add current sub-technique
                if parent_id not in technique_list:
                    technique_list[parent_id] = {}
                    technique_list[parent_id]['subtechniques'] = []

                technique_list[parent_id]['subtechniques'].append(attack_id)
            
            # Attack id is regular technique
            else:
                # Add technique to list
                technique_list[attack_id] = {}
                technique_list[attack_id]['subtechniques'] = []

        # Check if parent ID was added by sub-technique
        # parent ID will not have description
        elif 'descr' not in technique_list[attack_id]:
            # Check if it has external references
            if technique['relationship'].get('description'):
                # Get filtered description
                technique_list[attack_id]['descr'] = True
    
    return has_subtechniques

def get_groups_tour(technique_list):
    """ Get steps 1 through 3 if they are available """

    groups = {}

    for technique in technique_list:

        # Step 1
        if not technique_list[technique]['subtechniques']:
            if not groups.get('step1'):
                groups['step1'] = technique
        # Step 2 and 3
        else:
            # If Technique has relationship with group and subtechniques as well (Step 2)
            if technique_list[technique].get('descr'):
                # Check if it has two or more sub-techniques if not it is fine if its the first one found
                if groups.get('step2') and len(technique_list[technique]['subtechniques']) > 1:
                    groups['step2'] = [technique, len(technique_list[technique]['subtechniques'])]
                elif not groups.get('step2'):
                    groups['step2'] = [technique, len(technique_list[technique]['subtechniques'])]
            # Parent technique does not have relationship with group (Step 3)
            else:
                # Check if it has two or more sub-techniques if not it is fine if its the first one found
                if groups.get('step3') and len(technique_list[technique]['subtechniques']) > 1:
                    groups['step3'] = [technique_list[technique]['subtechniques'][0].replace(".", "-"), len(technique_list[technique]['subtechniques'])]
                elif not groups.get('step3'):
                    groups['step3'] = [technique_list[technique]['subtechniques'][0].replace(".", "-"), len(technique_list[technique]['subtechniques'])]

    return groups