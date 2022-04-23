from string import Template

module_name = "Matrices"
priority = 2

# Matrix markdown path
matrix_markdown_path = "content/pages/matrices/"

# Path for templates
matrices_templates_path = "modules/matrices/templates/"

# Matrix overview string
matrix_overview_md = (
    "Title: Matrix Overview \n"
    "Template: general/redirect-index \n"
    "RedirectLink: /matrices/enterprise/ \n"
    "save_as: matrices/index.html"
)

# String template for main domain matrices
matrix_md = Template(
    "Title: Matrix-${domain}\n" "Template: matrices/matrix\n" "save_as: matrices/${path}/index.html\n" "data: "
)

# String template for platform matrices
platform_md = Template(
    "Title: Matrix-${domain}-${platform}\n"
    "Template: matrices/matrix\n"
    "save_as: matrices/${domain}/${platform_path}/index.html\n"
    "data: "
)

# The tree of matricies on /matrices/
matrices = [
    {
        "name": "Enterprise",
        "type": "local",
        "path": "enterprise",
        "matrix": "enterprise-attack",
        "platforms": [
            "Windows",
            "macOS",
            "Linux",
            "PRE",
            "Azure AD",
            "Office 365",
            "Google Workspace",
            "SaaS",
            "IaaS",
            "Network",
            "Containers",
        ],
        "descr": "Below are the tactics and techniques representing the MITRE ATT&CK<sup>&reg;</sup> Matrix for Enterprise.",
        "subtypes": [
            {
                "name": "PRE",
                "type": "local",
                "matrix": "enterprise-attack",
                "path": "enterprise/pre",
                "platforms": ["PRE"],
                "descr": "Below are the tactics and techniques representing the MITRE ATT&CK<sup>&reg;</sup> Matrix for Enterprise covering preparatory techniques.",
                "subtypes": [],
            },
            {
                "name": "Windows",
                "type": "local",
                "matrix": "enterprise-attack",
                "path": "enterprise/windows",
                "platforms": ["Windows"],
                "descr": "Below are the tactics and techniques representing the MITRE ATT&CK<sup>&reg;</sup> Matrix for Enterprise. ",
                "subtypes": [],
            },
            {
                "name": "macOS",
                "type": "local",
                "matrix": "enterprise-attack",
                "path": "enterprise/macos",
                "platforms": ["macOS"],
                "descr": "Below are the tactics and techniques representing the MITRE ATT&CK<sup>&reg;</sup> Matrix for Enterprise. ",
                "subtypes": [],
            },
            {
                "name": "Linux",
                "type": "local",
                "matrix": "enterprise-attack",
                "platforms": ["Linux"],
                "path": "enterprise/linux",
                "descr": "Below are the tactics and techniques representing the MITRE ATT&CK<sup>&reg;</sup> Matrix for Enterprise. ",
                "subtypes": [],
            },
            {
                "name": "Cloud",
                "type": "local",
                "matrix": "enterprise-attack",
                "path": "enterprise/cloud",
                "platforms": ["Azure AD", "Office 365", "Google Workspace", "SaaS", "IaaS"],
                "descr": "Below are the tactics and techniques representing the MITRE ATT&CK<sup>&reg;</sup> Matrix for Enterprise covering cloud-based techniques.",
                "subtypes": [
                    {
                        "name": "Office 365",
                        "type": "local",
                        "matrix": "enterprise-attack",
                        "path": "enterprise/cloud/office365",
                        "platforms": ["Office 365"],
                        "descr": "Below are the tactics and techniques representing the MITRE ATT&CK<sup>&reg;</sup> Matrix for Enterprise covering cloud-based techniques. ",
                        "subtypes": [],
                    },
                    {
                        "name": "Azure AD",
                        "type": "local",
                        "matrix": "enterprise-attack",
                        "path": "enterprise/cloud/azuread",
                        "platforms": ["Azure AD"],
                        "descr": "Below are the tactics and techniques representing the MITRE ATT&CK<sup>&reg;</sup> Matrix for Enterprise covering cloud-based techniques. ",
                        "subtypes": [],
                    },
                    {
                        "name": "Google Workspace",
                        "type": "local",
                        "matrix": "enterprise-attack",
                        "path": "enterprise/cloud/googleworkspace",
                        "platforms": ["Google Workspace"],
                        "descr": "Below are the tactics and techniques representing the MITRE ATT&CK<sup>&reg;</sup> Matrix for Enterprise covering cloud-based techniques. ",
                        "subtypes": [],
                    },
                    {
                        "name": "SaaS",
                        "type": "local",
                        "matrix": "enterprise-attack",
                        "path": "enterprise/cloud/saas",
                        "platforms": ["SaaS"],
                        "descr": "Below are the tactics and techniques representing the MITRE ATT&CK<sup>&reg;</sup> Matrix for Enterprise covering cloud-based techniques. ",
                        "subtypes": [],
                    },
                    {
                        "name": "IaaS",
                        "type": "local",
                        "matrix": "enterprise-attack",
                        "path": "enterprise/cloud/iaas",
                        "platforms": ["IaaS"],
                        "descr": "Below are the tactics and techniques representing the MITRE ATT&CK<sup>&reg;</sup> Matrix for Enterprise covering cloud-based techniques. ",
                        "subtypes": [],
                    },
                ],
            },
            {
                "name": "Network",
                "type": "local",
                "matrix": "enterprise-attack",
                "path": "enterprise/network",
                "platforms": ["Network"],
                "descr": "Below are the tactics and techniques representing the MITRE ATT&CK<sup>&reg;</sup> Matrix for Enterprise covering techniques against network infrastructure devices. ",
                "subtypes": [],
            },
            {
                "name": "Containers",
                "type": "local",
                "matrix": "enterprise-attack",
                "path": "enterprise/containers",
                "platforms": ["Containers"],
                "descr": "Below are the tactics and techniques representing the MITRE ATT&CK<sup>&reg;</sup> Matrix for Enterprise covering techniques against container technologies. ",
                "subtypes": [],
            },
        ],
    },
    {
        "name": "Mobile",
        "type": "local",
        "matrix": "mobile-attack",
        "path": "mobile",
        "platforms": ["Android", "iOS"],
        "descr": "Below are the tactics and techniques representing the two MITRE ATT&CK<sup>&reg;</sup> Matrices for Mobile. "
        "The Matrices cover techniques involving device access and network-based effects that can be used by adversaries without device access. ",
        "subtypes": [
            {
                "name": "Android",
                "type": "local",
                "matrix": "mobile-attack",
                "path": "mobile/android",
                "platforms": ["Android"],
                "descr": "Below are the tactics and techniques representing the two MITRE ATT&CK<sup>&reg;</sup> Matrices for Mobile. "
                "The Matrices cover techniques involving device access and network-based effects that can be used by adversaries without device access. ",
                "subtypes": [],
            },
            {
                "name": "iOS",
                "type": "local",
                "matrix": "mobile-attack",
                "path": "mobile/ios",
                "platforms": ["iOS"],
                "descr": "Below are the tactics and techniques representing the two MITRE ATT&CK<sup>&reg;</sup> Matrices for Mobile. "
                "The Matrices cover techniques involving device access and network-based effects that can be used by adversaries without device access. ",
                "subtypes": [],
            },
        ],
    },
    {
        "name": "ICS",
        "type": "local",
        "path": "ics",
        "matrix": "ics-attack",
        "platforms": [],
        "descr": "Below are the tactics and techniques representing the MITRE ATT&CK<sup>&reg;</sup> Matrix for ICS.",
        "subtypes": [],
    },
]

deprecated_matrices = [
    {
        "name": "PRE-ATT&CK",
        "matrix": "pre-attack",
        "path": "pre",
    }
]

platform_to_path = {
    "PRE": "enterprise/pre",
    "Windows": "enterprise/windows",
    "macOS": "enterprise/macos",
    "Linux": "enterprise/linux",
    "Azure AD": "enterprise/cloud/azuread",
    "Office 365": "enterprise/cloud/office365",
    "Google Workspace": "enterprise/cloud/googleworkspace",
    "SaaS": "enterprise/cloud/saas",
    "IaaS": "enterprise/cloud/iaas",
    "Network": "enterprise/network",
    "Containers": "enterprise/containers",
    "Android": "mobile/android",
    "iOS": "mobile/ios",
}
