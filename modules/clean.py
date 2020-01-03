import shutil
import os
from . import config

def clean_website_build():
    """Clean content directory and remove output directory"""

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
    
    # Remove contribute markdown file
    contribute_path = os.path.join(config.resources_markdown_path, "contribute.md")
    if os.path.isfile(contribute_path):
        os.remove(contribute_path)
    # Remove resources markdown file
    resources_path = os.path.join(config.resources_markdown_path, "resources.md")
    if os.path.isfile(resources_path):
        os.remove(resources_path)
           # Remove resources markdown file
    previous_path = os.path.join(config.resources_markdown_path, "previous.md")
    if os.path.isfile(previous_path):
        os.remove(previous_path)

    # Remove website directory
    if os.path.isdir(config.web_directory):
        shutil.rmtree(config.web_directory)