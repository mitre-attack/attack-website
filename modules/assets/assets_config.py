from string import Template

module_name = "Assets"
priority = 7.2

# Markdown path for assets
asset_markdown_path = "content/pages/assets/"

# String template for asset index page
asset_index_md = (
    "Title: Asset overview\n" "Template: assets/assets-index\n" "save_as: assets/index.html\n" "data: "
)

# String template for asset page
asset_md = Template(
    "Title: ${name}\n" "Template: assets/asset\n" "save_as: assets/${attack_id}/index.html\n" "data: "
)

# Path for templates
assets_templates_path = "modules/assets/templates/"

assets_redirection_location = "modules/assets/assets_redirections.json"
