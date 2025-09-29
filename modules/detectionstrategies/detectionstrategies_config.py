from string import Template

module_name = "Detection Strategies"
module_name_no_spaces = "detectionstrategies"
module_tab_name = "Defenses"
priority = 4.1

# Markdown path
detectionstrategy_markdown_path = "content/pages/detectionstrategies/"

# Path for templates
detectionstrategies_templates_path = "modules/detectionstrategies/templates/"

# String template for index/overview page
detectionstrategy_index_md = (
    "Title: Detection Strategy Overview\n"
    "Template: detectionstrategies/detectionstrategies-index\n"
    "save_as: detectionstrategies/index.html\n"
    "data: "
)

# String template for individual page
detectionstrategy_md = Template(
    "Title: ${name}\nTemplate: detectionstrategies/detectionstrategy\nsave_as: detectionstrategies/${attack_id}/index.html\ndata: "
)

sidebar_detectionstrategies_md = (
    "Title: Detection Strategies Sidebar\n"
    "Template: general/sidebar-template \n"
    "save_as: detectionstrategies/sidebar-detectionstrategies/index.html\n"
    "data: "
)