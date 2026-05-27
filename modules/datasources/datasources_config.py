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
    "Title: ${name}\n"
    "Slug: datasource-${attack_id}\n"
    "url: /datasources/${attack_id}/\n"
    "Template: datasources/datasource\n"
    "save_as: datasources/${attack_id}/index.html\n"
    "data: "
)

# Path for templates
datasources_templates_path = "modules/datasources/templates/"
