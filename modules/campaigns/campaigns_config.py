from string import Template

module_name = "Campaigns"
priority = 7.1

# Markdown path for groups
campaign_markdown_path = "content/pages/campaigns/"

# String template for group index page
campaign_index_md = (
    "Title: Campaign overview\n" "Template: campaigns/campaigns-index\n" "save_as: campaigns/index.html\n" "data: "
)

# String template for group page
campaign_md = Template(
    "Title: ${name}\n" "Template: campaigns/campaign\n" "save_as: campaigns/${attack_id}/index.html\n" "data: "
)

# Path for templates
campaigns_templates_path = "modules/campaigns/templates/"

campaigns_redirection_location = "modules/campaigns/campaigns_redirections.json"
