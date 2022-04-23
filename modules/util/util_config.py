import shutil

import colorama

# Not found constant
NOT_FOUND = -1

# Template for HTML references inside of sentences
reference_marker_template = (
    "<span onclick=scrollToRef('scite-{}') "
    'id="scite-ref-{}-a" class="scite'
    '-citeref-number" '
    'data-reference="{}"><sup><a href="{}" '
    'target="_blank" data-hasqtip="{}" '
    'aria-describedby="qtip-{}">[{}]</a></sup></span>'
)
reference_marker_template_no_url = (
    "<span onclick=scrollToRef('scite-{}') "
    'id="scite-ref-{}-a" '
    'class="scite-citeref-number" '
    'data-reference="{}">'
    "<sup>[{}]</sup></span>"
)

# Window sizes
# Space for tests report
# Get windows width size and divide it by the three columns
window_size = shutil.get_terminal_size((80, 20))[0]
column_space = int(window_size / 3) - 1
status_space = int(float(column_space) * 0.80)
other_column_space = int(float(column_space) * 1.10)
