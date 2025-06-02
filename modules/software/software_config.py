from string import Template

module_name = "Software"
priority = 7

# Markdown path for software
software_markdown_path = "content/pages/software/"

# Path for templates
software_templates_path = "modules/software/templates/"

# String template for software index page
software_index_md = "Title: Software overview\nTemplate: software/software-index\nsave_as: software/index.html\ndata: "

# String template for group page
software_md = Template("Title: ${name}\nTemplate: software/software\nsave_as: software/${attack_id}/index.html\ndata: ")

software_redirection_location = "modules/software/software_redirections.json"

sidebar_software_md = (
    "Title: Software Sidebar\n"
    "Template: general/sidebar-template \n"
    "save_as: software/sidebar-software/index.html\n"
    "data: "
)
