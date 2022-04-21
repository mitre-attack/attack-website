from string import Template

module_name = "Groups"
priority = 6

# Markdown path for groups
group_markdown_path = "content/pages/groups/"

# String template for group index page
group_index_md = "Title: Group overview\n" "Template: groups/groups-index\n" "save_as: groups/index.html\n" "data: "

# String template for group page
group_md = Template("Title: ${name}\n" "Template: groups/group\n" "save_as: groups/${attack_id}/index.html\n" "data: ")

# Path for templates
groups_templates_path = "modules/groups/templates/"

groups_redirection_location = "modules/groups/groups_redirections.json"
