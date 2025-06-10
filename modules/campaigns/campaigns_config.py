from string import Template

module_name = "Campaigns"
priority = 7.1

# Markdown path for campaigns
campaign_markdown_path = "content/pages/campaigns/"

# String template for campaign index page
campaign_index_md = (
    "Title: Campaign overview\nTemplate: campaigns/campaigns-index\nsave_as: campaigns/index.html\ndata: "
)

# String template for campaign page
campaign_md = Template(
    "Title: ${name}\nTemplate: campaigns/campaign\nsave_as: campaigns/${attack_id}/index.html\ndata: "
)

# Path for templates
campaigns_templates_path = "modules/campaigns/templates/"

campaigns_redirection_location = "modules/campaigns/campaigns_redirections.json"

sidebar_campaigns_md = (
    "Title: Campaigns Sidebar\n"
    "Template: general/sidebar-template \n"
    "save_as: campaigns/sidebar-campaigns/index.html\n"
    "data: "
)
