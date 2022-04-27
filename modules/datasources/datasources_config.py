from string import Template

module_name = "Data Sources"
module_name_no_spaces = "datasources"

priority = 4.1

# Markdown path for groups
datasource_markdown_path = "content/pages/datasources/"

# String template for data sources index page
datasource_index_md = (
    "Title: Data Sources overview\n"
    "Template: datasources/datasources-index\n"
    "save_as: datasources/index.html\n"
    "data: "
)

# String template for data source page
datasource_md = Template(
    "Title: ${name}\n" "Template: datasources/datasource\n" "save_as: datasources/${attack_id}/index.html\n" "data: "
)

# Path for templates
datasources_templates_path = "modules/datasources/templates/"
