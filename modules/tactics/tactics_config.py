from string import Template

module_name = "Tactics"
priority = 3

# Markdown path for tactics
tactics_markdown_path = "content/pages/tactics/"

# Path for templates
tactics_templates_path = "modules/tactics/templates/"

# String template for domains
tactic_domain_md = Template(
    "Title: Tactics\n" "Template: tactics/tactics-domain-index\n" "save_as: tactics/${domain}/index.html\n" "data: "
)

# String template for tactics
tactic_md = Template(
    "Title: ${name}-${domain}\n" "Template: tactics/tactic\n" "save_as: tactics/${attack_id}/index.html\n" "data: "
)

# Tactics overview md template
tactic_overview_md = (
    "Title: Tactics overview \n"
    "Template: general/redirect-index \n"
    "RedirectLink: /tactics/enterprise/ \n"
    "save_as: tactics/index.html \n"
)

tactics_redirection_location = "modules/tactics/tactics_redirections.json"
