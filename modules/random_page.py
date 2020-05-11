import os
import json
import html
from . import config

def generate_json():
    json_data = {}
    for root, dirs, files in os.walk("output"):
        object_routes = ["groups", "matrices", "mitigations", "mobile", "pre-attack", "software", "techniques", "tactics"]
        # only walk specified routes for object pages
        for route in object_routes:
            if route in json_data.keys():
                if root.startswith(os.path.join(config.web_directory, route)):
                    for thefile in filter(lambda fname: fname.endswith(".html"), files):
                        thepath = os.path.join(root, thefile).replace(config.web_directory, "")
                        json_data[route].append(thepath)
            else:
                json_data[route] = []
    
    if not os.path.isdir(config.web_directory):
        os.makedirs(config.web_directory)
        
    json.dump(json_data, open(os.path.join(config.web_directory, "random_page.json"), mode="w",  encoding="utf-8"), indent=4)
