from . import groups_config
from modules import util
import time

def generate_groups():
    """ Generate groups, return True if groups was generated,
        False if nothing was generated
    """

    # First call to lazy loading
    test_start = time.time()
    util.build_helpers.get_malware_used_by_groups()
    test_end = time.time()
    test_time = test_end - test_start
    print(test_time)

    # Second call to lazy loading
    test_start = time.time()
    util.build_helpers.get_malware_used_by_groups()
    test_end = time.time()
    test_time = test_end - test_start
    print(test_time)

    return True
   