from string import Template

module_name = "Data Components"
module_name_no_spaces = "datacomponents"

priority = 5.3

# Markdown path
datacomponent_markdown_path = "content/pages/datacomponents/"

# Path for templates
datacomponents_templates_path = "modules/datacomponents/templates/"

# String template for index/overview page
datacomponent_index_md = (
    "Title: Data Component Overview\n"
    "Template: datacomponents/datacomponents-index\n"
    "save_as: datacomponents/index.html\n"
    "data: "
)

# String template for individual page
datacomponent_md = Template(
    "Title: ${name}\nTemplate: datacomponents/datacomponent\nsave_as: datacomponents/${attack_id}/index.html\ndata: "
)

sidebar_datacomponents_md = (
    "Title: Data Components Sidebar\n"
    "Template: general/sidebar-template \n"
    "save_as: datacomponents/sidebar-datacomponents/index.html\n"
    "data: "
)