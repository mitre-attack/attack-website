from . import config
from . import stixhelpers
from . import  util

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
            longest = []
            for tour in tours:
                if len(tour.keys()) > len(longest):
                    longest = tour
            
            return longest
        
        return []

    tour = get_longest_tour()

def get_tour_steps(matrix):

    # steps as array
    steps = {}
    # Get matrix subtechnique
    if is_matrix_with_subtechniques(matrix):
        steps['matrix'] = "/matrices/" + matrix['path']
    
    return steps

def is_matrix_with_subtechniques(matrix):
    """ Return true if matrix has subtechniques """

    ms = config.ms[matrix['matrix']]
    techniques = stixhelpers.get_techniques(ms)
    no_subs_techniques = util.filter_out_subtechniques(techniques)
    
    # Get sub-technique count
    sub_technique_count = util.get_subtechnique_count(no_subs_techniques)

    if sub_technique_count:
        return True 
    
    return False

