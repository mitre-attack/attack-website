from . import techniques 

def get_menu():
    return {
        "name": "Techniques", 
        "url": "/techniques", 
        "external_link": False,
        "priority": 3,
        "children": [
            {
                "name": "PRE-ATT&CK", 
                "url": "/techniques/pre", 
                "external_link": False,
                "children": []
            },
            {
                "name": "Enterprise", 
                "url": "/techniques/enterprise", 
                "external_link": False,
                "children": []
            },
            {
                "name": "Mobile", 
                "url": "/techniques/mobile", 
                "external_link": False,
                "children": []
            }
        ]
    }

def run_module():
    return (techniques.generate_techniques(), "Techniques")