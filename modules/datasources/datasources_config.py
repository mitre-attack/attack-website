from string import Template

module_name = "Data Sources"
module_name_no_spaces = "datasources"
module_tab_name = "Defenses"

priority = 4.1

# Markdown path for groups
datasource_markdown_path = "content/pages/datasources/"

# String template for data sources index page
datasource_index_md = (
    "Title: Data Sources overview\nTemplate: datasources/datasources-index\nsave_as: datasources/index.html\ndata: "
)

# String template for data source page
datasource_md = Template(
    "Title: ${name}\nTemplate: datasources/datasource\nsave_as: datasources/${attack_id}/index.html\ndata: "
)

# Path for templates
datasources_templates_path = "modules/datasources/templates/"
