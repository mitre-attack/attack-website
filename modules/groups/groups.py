from . import groups_config
from modules import util
import time

def generate_groups():
    """ Generate groups, return True if groups was generated,
        False if nothing was generated
    """

    # First call to lazy loading
    util.relationshipgetters.get_malware_used_by_groups()

    return True
   