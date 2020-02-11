from . import groups_config
from modules import util

def generate_groups():
    """ Generate groups, return True if groups was generated,
        False if nothing was generated
    """

    # First call to lazy loading
    util.relationshipgetters.get_malware_used_by_groups()

    # Call function to generate groups
    # Return True if a group was generated, False if not

    group_generated = True

    if not group_generated:
        util.buildhelpers.remove_module_from_menu(groups_config.module_name)   