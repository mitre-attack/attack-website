from string import Template

module_name = "Analytics"
module_tab_name = "Defenses"
priority = 4.2

# Markdown path
analytic_markdown_path = "content/pages/analytics/"

# Path for templates
analytics_templates_path = "modules/analytics/templates/"

# String template for index/overview page
analytic_index_md = (
    "Title: Analytic Overview\n"
    "Template: analytics/analytics-index\n"
    "save_as: analytics/index.html\n"
    "data: "
)

# String template for individual page
analytic_md = Template(
    "Title: ${attack_id}\nTemplate: analytics/analytic\nsave_as: analytics/${attack_id}/index.html\ndata: "
)
