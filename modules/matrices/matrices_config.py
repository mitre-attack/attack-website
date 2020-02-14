from string import Template

module_name = "Matrices"
priority = 2

# Matrix markdown path
matrix_markdown_path = "content/pages/matrices/"

# Matrix overview string
matrix_overview_md = ("Title: Matrix Overview \n"
                      "Template: general/redirect-index \n"
                      "RedirectLink: /matrices/enterprise/ \n"
                      "save_as: matrices/index.html")

# String template for main domain matrices
matrix_md = Template("Title: Matrix-${domain}\n"
                     "Template: matrices/matrix\n"
                     "save_as: matrices/${path}/index.html\n"
                     "data: ")

# String template for platform matrices
platform_md = Template("Title: Matrix-${domain}-${platform}\n"
                       "Template: matrices/matrix\n"
                       "save_as: matrices/${domain}/${platform_path}/index.html\n"
                       "data: ")

# The tree of matricies on /matrices/
matrices = [
    {
        "name": "PRE-ATT&CK",
        "type": "local",
        "path": "pre",
        "platforms": [],
        "matrix": "pre-attack",
        "descr": "Below are the tactics and techniques representing the MITRE PRE-ATT&CK Matrix&trade;.",
        "subtypes": [],
    },
    {
        "name": "Enterprise",
        "type": "local",
        "path": "enterprise",
        "matrix": "enterprise-attack",
        "platforms": ["Windows","macOS","Linux",
                      "AWS","GCP","Azure","Azure AD",
                      "Office 365","SaaS"],
        "descr": "Below are the tactics and technique representing the MITRE ATT&CK Matrix&trade; for Enterprise. ",
        "subtypes": [
            {
                "name": "Windows",
                "type": "local",
                "matrix": "enterprise-attack",
                "path": "enterprise/windows",
                "platforms": ["Windows"],
                "descr": "Below are the tactics and technique representing the MITRE ATT&CK Matrix&trade; for Enterprise. ",
                "subtypes": []
            },
            {
                "name" : "macOS",
                "type": "local",
                "matrix": "enterprise-attack",
                "path": "enterprise/macos",
                "platforms": ["macOS"],
                "descr": "Below are the tactics and technique representing the MITRE ATT&CK Matrix&trade; for Enterprise. ",
                "subtypes": []
            },
            {
                "name" : "Linux",
                "type": "local",
                "matrix": "enterprise-attack",
                "platforms": ["Linux"],
                "path": "enterprise/linux",
                "descr": "Below are the tactics and technique representing the MITRE ATT&CK Matrix&trade; for Enterprise. ", 
                "subtypes": []
            },
            {
                "name": "Cloud",
                "type": "local",
                "matrix": "enterprise-attack",
                "path": "enterprise/cloud",
                "platforms": ["AWS","GCP","Azure","Azure AD","Office 365","SaaS"],
                "descr": "Below are the tactics and technique representing the MITRE ATT&CK Matrix&trade; for Enterprise covering cloud-based techniques. ",
                "subtypes": [
                    {
                        "name" : "AWS",
                        "type": "local",
                        "matrix": "enterprise-attack",
                        "path": "enterprise/cloud/aws",
                        "platforms": ["AWS"],
                        "descr": "Below are the tactics and technique representing the MITRE ATT&CK Matrix&trade; for Enterprise covering cloud-based techniques. ",
                        "subtypes": []
                    },
                    {
                        "name" : "GCP",
                        "type": "local",
                        "matrix": "enterprise-attack",
                        "path": "enterprise/cloud/gcp",
                        "platforms": ["GCP"],
                        "descr": "Below are the tactics and technique representing the MITRE ATT&CK Matrix&trade; for Enterprise covering cloud-based techniques. ",
                        "subtypes": []
                    },
                    {
                        "name": "Azure",
                        "type": "local",
                        "matrix": "enterprise-attack",
                        "path": "enterprise/cloud/azure",
                        "platforms": ["Azure"],
                        "descr": "Below are the tactics and technique representing the MITRE ATT&CK Matrix&trade; for Enterprise covering cloud-based techniques. ",
                        "subtypes": []
                    },
                    { 
                        "name" : "Office 365",
                        "type": "local",
                        "matrix": "enterprise-attack",
                        "path": "enterprise/cloud/office365",
                        "platforms": ["Office 365"],
                        "descr": "Below are the tactics and technique representing the MITRE ATT&CK Matrix&trade; for Enterprise covering cloud-based techniques. ",
                        "subtypes": []
                    },
                    {
                        "name" : "Azure AD",
                        "type": "local",
                        "matrix": "enterprise-attack",
                        "path": "enterprise/cloud/azuread",
                        "platforms": ["Azure AD"],
                        "descr": "Below are the tactics and technique representing the MITRE ATT&CK Matrix&trade; for Enterprise covering cloud-based techniques. ",
                        "subtypes": []
                    },
                    {
                        "name" : "SaaS",
                        "type": "local",
                        "matrix": "enterprise-attack",
                        "path": "enterprise/cloud/saas",
                        "platforms": ["SaaS"],
                        "descr": "Below are the tactics and technique representing the MITRE ATT&CK Matrix&trade; for Enterprise covering cloud-based techniques. ",
                        "subtypes": []
                    }
                ]
            }
        ]
    },
    {
        "name": "Mobile",
        "type": "local",
        "matrix": "mobile-attack",
        "path": "mobile",
        "platforms": ["Android", "iOS"],
        "descr": "Below are the tactics and techniques representing the two MITRE ATT&CK Matrices&trade; for Mobile. "
                 "The Matrices cover techniques involving device access and network-based effects that can be used by adversaries without device access. ",
        "subtypes": [
            {
                "name": "Android",
                "type": "local",
                "matrix": "mobile-attack",
                "path": "mobile/android",
                "platforms": ["Android"],
                "descr": "Below are the tactics and techniques representing the two MITRE ATT&CK Matrices&trade; for Mobile. "
                         "The Matrices cover techniques involving device access and network-based effects that can be used by adversaries without device access. ",
                "subtypes": []
            },
            {
                "name" : "iOS",
                "type": "local",
                "matrix": "mobile-attack",
                "path": "mobile/ios",
                "platforms": ["iOS"],
                "descr": "Below are the tactics and techniques representing the two MITRE ATT&CK Matrices&trade; for Mobile. "
                         "The Matrices cover techniques involving device access and network-based effects that can be used by adversaries without device access. ",
                "subtypes": []
            },
        ]
    }, 
    {
        "name": "ICS",
        "type": "external",
        "path": "https://collaborate.mitre.org/attackics",
        "subtypes": []
    }
]