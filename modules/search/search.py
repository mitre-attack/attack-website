import html
import json
import os
import re

import bleach
from loguru import logger

import modules
from modules import site_config, versions

types = ["software", "datasources", "groups", "tactics", "techniques"]
sub_types = ["mobile", "enterprise", "ics"]
dist_words = 0


def generate_index():
    logger.info("Creating searchable index for the site")
    index = []

    # os.walk(site_config.web_directory) is a function that generates the file names in a directory tree, and it returns
    # a 3-tuple (root, dirs, files), where root is a string representing the root directory, dirs is a list of the
    # directories in the root directory, and files is a list of the files in the root directory.
    #
    # The code is using the for loop to iterate over the results of os.walk(site_config.web_directory) and access the
    # files in each directory. The root and files values are then used in the loop body to perform some operation.
    # The __ placeholder is used to ignore the dirs value, which is not needed in this code.
    #
    # EXAMPLE:
    #
    # import os
    #
    # root_dir = '/path/to/root/directory'
    #
    # for root, dirs, files in os.walk(root_dir):
    #     print(f'Root directory: {root}')
    #     print(f'Directories in root: {dirs}')
    #     print(f'Files in root: {files}')
    #     print()
    #
    # If the directory tree rooted at root_dir looks like this:
    #
    # /path/to/root/directory/
    #     dir1/
    #         file1.txt
    #         file2.txt
    #     dir2/
    #         file3.txt
    #         file4.txt
    #     file5.txt
    #
    # Then the output of the code would be:
    #
    # Root directory: /path/to/root/directory/
    # Directories in root: ['dir1', 'dir2']
    # Files in root: ['file5.txt']
    #
    # Root directory: /path/to/root/directory/dir1/
    # Directories in root: []
    # Files in root: ['file1.txt', 'file2.txt']
    #
    # Root directory: /path/to/root/directory/dir2/
    # Directories in root: []
    # Files in root: ['file3.txt', 'file4.txt']

    # TL;DR This code is processing the HTML files in a directory tree, cleaning their content, and appending relevant
    # information to an index list, skipping certain files and directories if necessary.

    for root, __, files in os.walk(site_config.web_directory):
        # don't walk previous routes
        skip = False
        for versions_dir in ["previous", "versions"]:
            if root.startswith(os.path.join(site_config.web_directory, versions_dir)):
                skip = True
        if skip:
            continue

        # The next line is using a for loop to iterate over the files in the current directory (files) and applying a
        # filter to select only the files that end with the .html extension. In other words, this line of code is
        # selecting only the HTML files from the files list and iterating over them.

        for html_file in filter(lambda filename: filename.endswith(".html"), files):

            # Example: If `root` equals "/foo/bar/" and `html_file` equals "hello_world.html" then `absolute_path` will
            # equal "/foo/bar/hello_world.html"

            absolute_path = os.path.join(root, html_file)

            global dist_words

            # It is worth noting that the `any` function and the .index method used in the code have a time complexity
            # of O(n), where n is the length of the list being searched.

            if any(file_name in absolute_path for file_name in types_hash):

                file_name_split = absolute_path.split("/")

                if any(file_name in file_name_split for file_name in sub_types):
                    file_name_split = absolute_path.split("/")
                    type_temp = [file_name_split.index(val) for val in file_name_split if val in sub_types]
                    if "index.html" in file_name_split:
                        dist_words = file_name_split.index("index.html") - type_temp[0]
                else:
                    file_name_split = absolute_path.split("/")
                    type_temp = [file_name_split.index(val) for val in file_name_split if val in types]
                    if "index.html" in file_name_split:
                        dist_words = file_name_split.index("index.html") - type_temp[0]
            cleancontent, skipindex, title = clean(absolute_path)
            if dist_words == 1:
                skipindex = True
                dist_words = 0
            if absolute_path[6:] == "/index.html":
                skipindex = True
                dist_words = 0
            if not skipindex:
                # if title == "":
                #     print(absolute_path, "has generic title")
                #     title = "MITRE ATT&CK&trade;"

                index.append(
                    {
                        "id": len(index),
                        "title": title,
                        "path": absolute_path[6:],
                        "content": cleancontent,
                    }
                )
    if not os.path.isdir(site_config.web_directory):
        os.makedirs(site_config.web_directory)

    json.dump(index, open(os.path.join(site_config.web_directory, "index.json"), mode="w", encoding="utf8"), indent=0)

    if site_config.subdirectory:
        # update search base url to subdirectory
        search_file_path = os.path.join(site_config.web_directory, "theme", "scripts", "search.js")

        if os.path.exists(search_file_path):
            search_contents = ""

            with open(search_file_path, mode="r", encoding="utf8") as search_file:
                search_contents = search_file.read()
                search_contents = re.sub(
                    'site_base_url ?= ? ""', f'site_base_url = "/{site_config.subdirectory}/"', search_contents
                )

            with open(search_file_path, mode="w", encoding="utf8") as search_file:
                search_file.write(search_contents)

    preserve_current_version()


skiplines = ["breadcrumb-item", "nav-link"]


def skipline(line):
    for skip in skiplines:
        if skip in line:
            return True
    return False


def clean_line(line):
    """Clean unicode spaces from line."""
    # Replace unicode spaces
    line = line.replace("\u00a0", " ")
    line = line.replace("\u202f", " ")
    line = line.replace("&nbsp;", " ")
    line = line.replace("&nbsp", " ")

    return line


def clean(filepath):
    """Clean the file of all HTML tags and unnecessary data."""
    with open(filepath, mode="r", encoding="utf8") as f:
        lines = f.readlines()

    content = ""
    count = 0
    title = ""
    skipindex = False
    indexing = False

    for line in lines:
        if (not skipline(line)) and indexing:
            content += clean_line(line) + "\n"
        if "<!--start-indexing-for-search-->" in line:
            indexing = True
        if "<!--stop-indexing-for-search-->" in line:
            indexing = False
        if "<title>" in line:
            # e.g [Credential Access - Enterprise | MITRE ATT&CK&trade;] becomes [Credential Access - Enterprise]
            match = re.search(r"<title>(.*)\|.*</title>", line)
            if match:
                title = match.group(1).strip()
        if 'http-equiv="refresh"' in line:
            skipindex = True
            break
        if '<h5 class="mb-0">Deprecation Warning</h5>' in line:
            skipindex = True
            break

    # content = ps.stem(content)
    out = bleach.clean(content, tags=[], strip=True)  # remove tags
    out = re.sub(r"[\n ]+", " ", out)  # remove extra newlines, smush to 1 line
    out = html.unescape(out)  # fix &amp and &#nnn unicode escaping
    skipindex = skipindex or out == "" or out == " "
    count = count + 1
    return out, skipindex, title


def preserve_current_version():
    """Preserve current version"""

    # Check for intermodule dependency
    if [key["module_name"] for key in modules.run_ptr if key["module_name"] == "versions"]:
        versions.versions.deploy_current_version()
