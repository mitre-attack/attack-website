from string import Template

module_name = "Tactics"
priority = 3

# Markdown path for tactics
tactics_markdown_path = "content/pages/tactics/"

# Path for templates
tactics_templates_path = "modules/tactics/templates/"

# String template for domains
tactic_domain_md = Template(
    "Title: Tactics\nTemplate: tactics/tactics-domain-index\nsave_as: tactics/${domain}/index.html\ndata: "
)

# String template for tactics
tactic_md = Template(
    "Title: ${name}-${domain}\nTemplate: tactics/tactic\nsave_as: tactics/${attack_id}/index.html\ndata: "
)

# Tactics overview md template
tactic_overview_md = (
    "Title: Tactics overview \n"
    "Template: general/redirect-index \n"
    "RedirectLink: /tactics/enterprise/ \n"
    "save_as: tactics/index.html \n"
)

tactics_redirection_location = "modules/tactics/tactics_redirections.json"

sidebar_tactics_md = (
    "Title: Tactics Sidebar\nTemplate: general/sidebar-template \nsave_as: tactics/sidebar-tactics/index.html\ndata: "
)
