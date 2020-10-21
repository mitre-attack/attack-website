from string import Template

module_name = "Software"
priority = 7

# Markdown path for software
software_markdown_path = "content/pages/software/"

# Path for templates
software_templates_path = "modules/software/templates/"

# String template for software index page
software_index_md = ("Title: Software overview\n"
                     "Template: software/software-index\n"
                     "save_as: software/index.html\n"
                     "data: ")

# String template for group page
software_md = Template("Title: ${name}\n"
                       "Template: software/software\n"
                       "save_as: software/${attack_id}/index.html\n"
                       "data: ")

software_redirection_location = "modules/software/software_redirections.json"