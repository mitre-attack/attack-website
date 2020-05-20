import os
import json
import html
import bleach, re
from modules import site_config

skiplines = ["breadcrumb-item", "nav-link"]

def generate_json():
    json_data = {}

    for root, __, files in os.walk("output"):
        all_routes = {"matrices": "Matrix", "tactics": "Tactic", "techniques": "Technique", "mitigations": "Mitigation", "groups": "Group", "software": "Software"}
        routes = {}

        if site_config.args.modules:
            for module in site_config.args.modules:
                if module != "website_build" and module != "random_page":
                    routes[module] = all_routes[module]

        # only walk specified routes for object pages
        for route, value in routes.items():
            if value in json_data.keys():
                if root.startswith(os.path.join(site_config.web_directory, route)):
                    for thefile in filter(lambda fname: fname.endswith(".html"), files):
                        # Get the path of the html files only
                        thepath = os.path.join(root, thefile)
                        # Sanitize first; not all html files are suitable for this random page feature
                        cleancontent, skipindex, title = clean(thepath)
                        if not skipindex:
                            add_to_json = False
                            # Make sure the page isn't an object index page
                            if route == "matrices":
                                add_to_json = True
                            elif route == "tactics" and re.search(r"TA[0-9]{4}", thepath):
                                add_to_json = True
                            elif route == "techniques" and re.search(r"T[0-9]{4}", thepath):
                                add_to_json = True
                            elif route == "mitigations" and re.search(r"M[0-9]{4}", thepath):
                                add_to_json = True
                            elif route == "groups" and re.search(r"G[0-9]{4}", thepath):
                                add_to_json = True
                            elif route == "software" and re.search(r"S[0-9]{4}", thepath):
                                add_to_json = True

                            if add_to_json:
                                json_data[value].append(thepath[6:])
            else:
                json_data[value] = []
    
    if not os.path.isdir(site_config.web_directory):
        os.makedirs(site_config.web_directory)
        
    json.dump(json_data, open(os.path.join(site_config.web_directory, "random_page.json"), mode="w",  encoding="utf-8"), indent=4)

def skipline(line):
    for skip in skiplines:
        if skip in line: return True
    return False

def clean_line(line):
    """clean unicode spaces from line"""
    # Replace unicode spaces
    line = line.replace(u"\u00a0", " ")
    line = line.replace(u"\u202f", " ")
    line = line.replace("&nbsp;", " ")
    line = line.replace("&nbsp", " ")

    return line

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
            content += clean_line(line) + "\n"
        if "<!--start-indexing-for-search-->" in line: 
            indexing = True
        if "<!--stop-indexing-for-search-->" in line: 
            indexing = False
        if "<title>" in line:
            # e.g [Credential Access - Enterprise | MITRE ATT&CK&trade;] becomes [Credential Access - Enterprise]
            match = re.search(r"<title>(.*)\|.*</title>", line)
            if match: title = match.group(1).strip()
        if 'http-equiv="refresh"' in line: skipindex = True

    out = bleach.clean(content, tags=[], strip=True) #remove tags
    out = re.sub(r"[\n ]+", " ", out) # remove extra newlines, smush to 1 line
    out = html.unescape(out) # fix &amp and &#nnn unicode escaping

    skipindex = skipindex or out == "" or out == " "
    return out, skipindex, title