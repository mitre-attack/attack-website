from string import Template

module_name = "Techniques"
priority = 4

# Markdown path for techniques
techniques_markdown_path = "content/pages/techniques/"

# Path for templates
techniques_templates_path = "modules/techniques/templates/"

# String template for all techniques
technique_md = Template(
    "Title: ${name}-${domain}\n"
    "Template: techniques/technique\n"
    "save_as: techniques/${attack_id}/index.html\n"
    "data: "
)

# String template for domains
technique_domain_md = Template(
    "Title: Techniques\n"
    "Template: techniques/techniques-domain-index\n"
    "save_as: techniques/${domain}/index.html\n"
    "data: "
)

# Overview md template
technique_overview_md = (
    "Title: Overview \n"
    "Template: general/redirect-index \n"
    "RedirectLink: /techniques/enterprise/ \n"
    "save_as: techniques/index.html \n"
)

techniques_redirection_location = "modules/techniques/techniques_redirections.json"

# String template for all techniques
sub_technique_md = Template(
    "Title: ${name}-${domain}\n"
    "Template: techniques/technique\n"
    "save_as: techniques/${parent_id}/${sub_number}/index.html\n"
    "data: "
)
