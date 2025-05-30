from string import Template

module_name = "Groups"
module_tab_name = "CTI"
priority = 6

# Markdown path for groups
group_markdown_path = "content/pages/groups/"

# String template for group index page
group_index_md = "Title: Group overview\nTemplate: groups/groups-index\nsave_as: groups/index.html\ndata: "

# String template for group page
group_md = Template("Title: ${name}\nTemplate: groups/group\nsave_as: groups/${attack_id}/index.html\ndata: ")

# Path for templates
groups_templates_path = "modules/groups/templates/"

groups_redirection_location = "modules/groups/groups_redirections.json"

sidebar_groups_md = (
    "Title: Groups Sidebar\nTemplate: general/sidebar-template \nsave_as: groups/sidebar-groups/index.html\ndata: "
)
