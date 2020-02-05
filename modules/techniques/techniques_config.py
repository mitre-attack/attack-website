from string import Template

# Constants used by techniques.py
# ----------------------------------------------------------------------------

# Markdown path for techniques
techniques_markdown_path = "content/pages/techniques/"	

# String template for all techniques
technique_md = Template("Title: ${name}-${tactics}-${domain}\n"
                        "Template: techniques/technique\n"
                        "save_as: techniques/${attack_id}/index.html\n"
                        "data: ")

# String template for domains	
technique_domain_md = Template("Title: Techniques\n"
                               "Template: techniques/techniques-domain-index\n"
                               "save_as: techniques/${domain}/index.html\n"
                               "data: ")

# Overview md template
technique_overview_md = ("Title: Overview \n"
                         "Template: general/redirect-index \n"
                         "RedirectLink: /techniques/enterprise/ \n"
                         "save_as: techniques/index.html \n")