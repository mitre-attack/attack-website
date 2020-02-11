import os
import bleach, re
import json
import html

def generate_index():
    index = []
    for root, dirs, files in os.walk("output"):
        # don't walk previous route
        if root.startswith(os.path.join("output", "previous")): continue
        
        for thefile in filter(lambda fname: fname.endswith(".html"), files):
            thepath = os.path.join(root, thefile)
            cleancontent, skipindex, title = clean(thepath)
            if not skipindex:
                # if title == "":
                #     print(thepath, "has generic title")
                #     title = "MITRE ATT&CK&trade;"

                index.append({
                    "id": len(index),
                    "title": title,
                    "path": thepath[6:],
                    "content": cleancontent
                })
    if not os.path.isdir("output"):
        os.mkdir("output")
        
    json.dump(index, open(os.path.join("output", "index.json"), mode="w",  encoding="utf8"), indent=2)
    
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
            # e.g [Credential Access - Enterprise | MITRE ATT&CK&trade;] becomes [Credential Access - Enterprise]
            match = re.search(r"<title>(.*)\|.*</title>", line)
            if match: title = match.group(1).strip()
        if 'http-equiv="refresh"' in line: skipindex = True

    out = bleach.clean(content, tags=[], strip=True) #remove tags
    out = re.sub(r"[\n ]+", " ", out) # remove extra newlines, smush to 1 line
    out = html.unescape(out) # fix &amp and &#nnn unicode escaping

    skipindex = skipindex or out == "" or out == " "
    return out, skipindex, title