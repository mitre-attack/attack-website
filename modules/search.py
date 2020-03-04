import os
import bleach, re
import json
import html
from . import config

def generate_index():
    index = []
    for root, dirs, files in os.walk("output"):
        # don't walk previous route
        if root.startswith(os.path.join(config.web_directory, "previous")): continue
        
        for thefile in filter(lambda fname: fname.endswith(".html"), files):
            thepath = os.path.join(root, thefile)
            cleancontent, skipindex, title = clean(thepath)
            if not skipindex:
                # if title == "":
                #     print(thepath, "has generic title")
                #     title = "MITRE ATT&CK&reg;"

                index.append({
                    "id": len(index),
                    "title": title,
                    "path": thepath[6:], # strip output prefix
                    "content": cleancontent
                })
    if not os.path.isdir(config.web_directory):
        os.makedirs(config.web_directory)
        
    json.dump(index, open(os.path.join(config.web_directory, "index.json"), mode="w",  encoding="utf8"), indent=2)

    if (config.subdirectory):
        # update search base url to subdirectory
        search_file_path = os.path.join(config.web_directory, "theme", "scripts", "search_babelized.js")
        
        if os.path.exists(search_file_path):
            search_contents = ""

            with open(search_file_path, mode="r", encoding='utf8') as search_file:
                search_contents = search_file.read()
                search_contents = re.sub('site_base_url ?= ? ""', f'site_base_url = "/{config.subdirectory}/"', search_contents)

            with open(search_file_path, mode="w", encoding='utf8') as search_file:
                search_file.write(search_contents)

    
skiplines = ["breadcrumb-item", "nav-link"]
def skipline(line):
    for skip in skiplines:
        if skip in line: return True
    return False

def clean(filepath):
    """clean the file of all HTML tags and unnecessary data"""
    f = open(filepath, mode="r", encoding="utf8")
    lines = f.readlines()
    f.close()

    content = ""
    title = ""
    skipindex = False
    indexing = False
    for line in lines:
        if (not skipline(line)) and indexing: 
            content += line + "\n"
        if "<!--start-indexing-for-search-->" in line: 
            indexing = True
        if "<!--stop-indexing-for-search-->" in line: 
            indexing = False
        if "<title>" in line:
            # e.g [Credential Access - Enterprise | MITRE ATT&CK&reg;] becomes [Credential Access - Enterprise]
            match = re.search(r"<title>(.*)\|.*</title>", line)
            if match: title = match.group(1).strip()
        if 'http-equiv="refresh"' in line: skipindex = True

    out = bleach.clean(content, tags=[], strip=True) #remove tags
    out = re.sub(r"[\n ]+", " ", out) # remove extra newlines, smush to 1 line
    out = html.unescape(out) # fix &amp and &#nnn unicode escaping

    skipindex = skipindex or out == "" or out == " "
    return out, skipindex, title
