import shutil
import os
from . import config

def clean_website_build():
    """Clean content directory and remove web directory"""

    content_path = "content"
    content_pages_path = os.path.join(content_path, "pages")

    # Clean content directory
    for filename in os.listdir(content_path):
        if filename != "docs" and filename != "pages":
            # Generate full file path
            full_file_path = os.path.join(content_path, filename)
            if os.path.isdir(full_file_path):
                shutil.rmtree(full_file_path)
            else:
                os.remove(full_file_path)
        
    # Clean content/pages directory
    for filename in os.listdir(content_pages_path):
        if filename != "resources" and filename != "static" and \
                                                        filename != "updates":
            # Generate full file path
            full_file_path = os.path.join(content_pages_path, filename)
            if os.path.isdir(full_file_path):
                shutil.rmtree(full_file_path)
            else:
                os.remove(full_file_path)
    
    # Remove dynamic javascript file
    settings_js = os.path.join(config.javascript_path, "settings.js")
    if os.path.isfile(settings_js):
        os.remove(settings_js)
    
    # Remove contribute markdown file
    contribute_path = os.path.join(config.resources_markdown_path, "contribute.md")
    if os.path.isfile(contribute_path):
        os.remove(contribute_path)
    # Remove resources markdown file
    resources_path = os.path.join(config.resources_markdown_path, "resources.md")
    if os.path.isfile(resources_path):
        os.remove(resources_path)
    # Remove attackcon markdown file
    attackcon_path = os.path.join(config.resources_markdown_path, "attackcon.md")
    if os.path.isfile(attackcon_path):
        os.remove(attackcon_path)
    # Remove versions markdown file
    versions_path = os.path.join(config.resources_markdown_path, "versions.md")
    if os.path.isfile(versions_path):
        os.remove(versions_path)
    # remove FAQ markdown file
    faq_path = os.path.join(config.resources_markdown_path, "faq.md")
    if os.path.isfile(faq_path):
        os.remove(faq_path)
    # Remove training markdown file
    training_path = os.path.join(config.resources_markdown_path, "training.md")
    if os.path.isfile(training_path):
        os.remove(training_path)
    # Remove training markdown file
    training_cti_path = os.path.join(config.resources_markdown_path, "training_cti.md")
    if os.path.isfile(training_cti_path):
        os.remove(training_cti_path)

    # Remove website directory
    if os.path.isdir(config.web_directory):
        shutil.rmtree(config.web_directory)