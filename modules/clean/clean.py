import shutil
import os
from . import clean_config

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
        if filename != "static":
            # Generate full file path
            full_file_path = os.path.join(content_pages_path, filename)
            if os.path.isdir(full_file_path):
                shutil.rmtree(full_file_path)
            else:
                os.remove(full_file_path)

    # Remove output directory
    output_path = "output"
    if os.path.isdir(output_path):
        shutil.rmtree(output_path)