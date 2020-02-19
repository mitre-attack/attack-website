from . import blog_config

def get_priority():
    return blog_config.priority

def get_menu():
    return {
        "name": "Blog", 
        "url": "https://medium.com/mitre-attack/", 
        "external_link": True,
        "priority": blog_config.priority,
        "children": []
    }