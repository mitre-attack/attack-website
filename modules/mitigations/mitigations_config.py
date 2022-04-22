from string import Template

module_name = "Mitigations"
priority = 5

# Markdown path for mitigations
mitigation_markdown_path = "content/pages/mitigations/"

# Path for templates
mititgations_templates_path = "modules/mitigations/templates/"

# Mitigation overview string
mitigation_overview_md = (
    "Title: Mitigation Overview \n"
    "Template: general/redirect-index \n"
    "RedirectLink: /mitigations/enterprise/ \n"
    "save_as: mitigations/index.html \n"
)

# String template for domains
mitigation_domain_md = Template(
    "Title: Mitigations\n"
    "Template: mitigations/mitigations-domain-index\n"
    "save_as: mitigations/${domain}/index.html\n"
    "data: "
)

# String template for all mitigations
mitigation_md = Template(
    "Title: ${name}-${domain}\n"
    "Template: mitigations/mitigation\n"
    "save_as: mitigations/${attack_id}/index.html\n"
    "data: "
)
