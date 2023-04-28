import json
import os
import re

from modules import site_config


def generate_json():
    json_data = {}
    all_routes = {
        "matrices": "Matrix",
        "tactics": "Tactic",
        "techniques": "Technique",
        "datasources": "Data Source",
        "mitigations": "Mitigation",
        "groups": "Group",
        "software": "Software",
        "campaigns": "Campaign",
    }
    routes = {}

    if site_config.args.modules:
        for module in site_config.args.modules:
            if all_routes.get(module):
                routes[module] = all_routes[module]
    else:
        routes = all_routes

    for root, __, files in os.walk("output"):
        # only walk specified routes for object pages
        for route, value in routes.items():
            if value not in json_data.keys():
                json_data[value] = []

            if root.startswith(os.path.join(site_config.web_directory, route)):
                for thefile in filter(lambda fname: fname.endswith(".html"), files):
                    # Get the path of the html files only
                    thepath = os.path.join(root, thefile)
                    # Sanitize first; not all html files are suitable for this random page feature
                    skipindex = check_skipindex(thepath)
                    if not skipindex:
                        add_to_json = False
                        # Make sure the page isn't an object index page
                        if route == "matrices":
                            add_to_json = True
                        elif route == "tactics" and re.search(r"TA[0-9]{4}", thepath):
                            add_to_json = True
                        elif route == "techniques" and re.search(r"T[0-9]{4}", thepath):
                            add_to_json = True
                        elif route == "datasources" and re.search(r"DS[0-9]{4}", thepath):
                            add_to_json = True
                        elif route == "mitigations" and re.search(r"M[0-9]{4}", thepath):
                            add_to_json = True
                        elif route == "groups" and re.search(r"G[0-9]{4}", thepath):
                            add_to_json = True
                        elif route == "software" and re.search(r"S[0-9]{4}", thepath):
                            add_to_json = True
                        elif route == "campaigns" and re.search(r"C[0-9]{4}", thepath):
                            add_to_json = True

                        if add_to_json:
                            json_data[value].append(thepath[6:])

    if not os.path.isdir(site_config.web_directory):
        os.makedirs(site_config.web_directory)

    json.dump(
        json_data,
        open(os.path.join(site_config.web_directory, "random_page.json"), mode="w", encoding="utf-8"),
        indent=4,
    )


def check_skipindex(filepath):
    """clean the file of all HTML tags and unnecessary data"""
    f = open(filepath, mode="r", encoding="utf8")
    lines = f.readlines()
    f.close()

    skipindex = False
    for line in lines:
        if 'http-equiv="refresh"' in line:
            skipindex = True
        if '<meta name="robots" content="noindex, nofollow">' in line:
            skipindex = True

    return skipindex
