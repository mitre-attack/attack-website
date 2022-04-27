import os
import re

from modules import site_config


def generate_subdirectory():
    """Build website to subdirectory"""

    if site_config.args.subdirectory:
        replace()


allowed_in_link = "".join(
    list(
        map(
            lambda s: s.strip(),
            [
                "   -   ",
                "   ?   ",
                "   \w   ",
                "   \\   ",
                "   $   ",
                "   \.   ",
                "   !   ",
                "   \*   ",
                "   '   ",
                "   ()   ",
                "   /    ",
            ],
        )
    )
)


def replace_links(filepath):
    """In the given file, replace the in-site links to reference
    the correct previous version
    """

    # read file contents
    with open(filepath, mode="r", encoding="utf8") as html:
        html_str = html.read()

    # subdirectory link format
    dest_link_format = f"/{site_config.subdirectory}\g<1>"

    def substitute(prefix, html_str):
        from_str = f"{prefix}=[\"']([{allowed_in_link}]+)[\"']"
        to_str = f'{prefix}="{dest_link_format}"'
        return re.sub(from_str, to_str, html_str)

    def substitute_redirection(prefix, html_str):
        from_str = f"{prefix}=([{allowed_in_link}]+)[\"']"
        to_str = f'{prefix}={dest_link_format}"'
        return re.sub(from_str, to_str, html_str)

    html_str = substitute("src", html_str)
    html_str = substitute("href", html_str)
    html_str = substitute_redirection('content="0; url', html_str)

    with open(filepath, mode="w", encoding="utf8") as updated_html:
        updated_html.write(html_str)


def replace():
    """Replace local hyperlinks with subdirectory"""
    for directory, _, files in os.walk(site_config.web_directory):
        for filename in filter(lambda f: f.endswith(".html"), files):
            filepath = os.path.join(directory, filename)
            replace_links(filepath)
