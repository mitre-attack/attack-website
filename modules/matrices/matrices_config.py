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
matrix_md = Template("Title: Matrix-${domain}\nTemplate: matrices/matrix\nsave_as: matrices/${path}/index.html\ndata: ")

# String template for platform matrices
platform_md = Template(
    "Title: Matrix-${domain}-${platform}\n"
    "Template: matrices/matrix\n"
    "save_as: matrices/${domain}/${platform_path}/index.html\n"
    "data: "
)

sidebar_matrices_md = (
    "Title: Matrices Sidebar\n"
    "Template: general/sidebar-template \n"
    "save_as: matrices/sidebar-matrices/index.html\n"
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
            "Office Suite",
            "Identity Provider",
            "SaaS",
            "IaaS",
            "Network Devices",
            "Containers",
            "ESXi",
        ],
        "descr": "Below are the tactics and techniques representing the MITRE ATT&CK<sup>&reg;</sup> Matrix for Enterprise.",
        "subtypes": [
            {
                "name": "PRE",
                "type": "local",
                "matrix": "enterprise-attack",
                "path": "enterprise/pre",
                "platforms": ["PRE"],
                "descr": "Below are the tactics and techniques representing the MITRE ATT&CK<sup>&reg;</sup> PRE platform. The techniques below take place outside of the victim environment, often as a preparatory measure to support targeting.",
                "subtypes": [],
            },
            {
                "name": "Windows",
                "type": "local",
                "matrix": "enterprise-attack",
                "path": "enterprise/windows",
                "platforms": ["Windows"],
                "descr": "Below are the tactics and techniques representing the MITRE ATT&CK<sup>&reg;</sup> Windows platform. The techniques below are known to target hosts running Microsoft Windows operating systems.",
                "subtypes": [],
            },
            {
                "name": "macOS",
                "type": "local",
                "matrix": "enterprise-attack",
                "path": "enterprise/macos",
                "platforms": ["macOS"],
                "descr": "Below are the tactics and techniques representing the MITRE ATT&CK<sup>&reg;</sup> macOS platform. The techniques below are known to target hosts running macOS operating systems.",
                "subtypes": [],
            },
            {
                "name": "Linux",
                "type": "local",
                "matrix": "enterprise-attack",
                "platforms": ["Linux"],
                "path": "enterprise/linux",
                "descr": "Below are the tactics and techniques representing the MITRE ATT&CK<sup>&reg;</sup> Linux platform. The techniques below are known to target hosts running Linux operating systems.",
                "subtypes": [],
            },
            {
                "name": "Cloud",
                "type": "local",
                "matrix": "enterprise-attack",
                "path": "enterprise/cloud",
                "platforms": ["Office Suite", "Identity Provider", "SaaS", "IaaS"],
                "descr": "Below are the tactics and techniques representing the MITRE ATT&CK<sup>&reg;</sup> cloud platforms.",
                "subtypes": [
                    {
                        "name": "Office Suite",
                        "type": "local",
                        "matrix": "enterprise-attack",
                        "path": "enterprise/cloud/officesuite",
                        "platforms": ["Office Suite"],
                        "descr": "Below are the tactics and techniques representing the MITRE ATT&CK<sup>&reg;</sup> Office Suite platform. The techniques below are known to target cloud-based office application suites such as Microsoft 365 and Google Workspace. Office application suites are SaaS platforms that typically combine email, chat, document management, and automation functionality for use in a collaborative environment.",
                        "subtypes": [],
                    },
                    {
                        "name": "Identity Provider",
                        "type": "local",
                        "matrix": "enterprise-attack",
                        "path": "enterprise/cloud/identityprovider",
                        "platforms": ["Identity Provider"],
                        "descr": "Below are the tactics and techniques representing the MITRE ATT&CK<sup>&reg;</sup> Identity Provider platform. The techniques below are known to target cloud-based identity-as-a-service (IDaaS) platforms such as Microsoft Entra ID and Okta. Identity providers are SaaS platforms that support identity management and single sign-on across multiple applications.",
                        "subtypes": [],
                    },
                    {
                        "name": "SaaS",
                        "type": "local",
                        "matrix": "enterprise-attack",
                        "path": "enterprise/cloud/saas",
                        "platforms": ["SaaS"],
                        "descr": "Below are the tactics and techniques representing the MITRE ATT&CK<sup>&reg;</sup> SaaS platform. The techniques below are known to target cloud-based software-as-a-service (SaaS) platforms. SaaS encompasses cloud-hosted applications with a variety of functionality.",
                        "subtypes": [],
                    },
                    {
                        "name": "IaaS",
                        "type": "local",
                        "matrix": "enterprise-attack",
                        "path": "enterprise/cloud/iaas",
                        "platforms": ["IaaS"],
                        "descr": "Below are the tactics and techniques representing the MITRE ATT&CK<sup>&reg;</sup> IaaS platform. The techniques below are known to target cloud-based infrastructure-as-a-service (IaaS) platforms. IaaS encompasses cloud-hosted infrastructure, such as virtual machines, object storage, databases, and serverless functionality.",
                        "subtypes": [],
                    },
                ],
            },
            {
                "name": "Network Devices",
                "type": "local",
                "matrix": "enterprise-attack",
                "path": "enterprise/network-devices",
                "platforms": ["Network Devices"],
                "descr": "Below are the tactics and techniques representing the MITRE ATT&CK<sup>&reg;</sup> Network Devices platform. The techniques below are known to target network devices such as routers, switches, and load balancers.",
                "subtypes": [],
            },
            {
                "name": "Containers",
                "type": "local",
                "matrix": "enterprise-attack",
                "path": "enterprise/containers",
                "platforms": ["Containers"],
                "descr": "Below are the tactics and techniques representing the MITRE ATT&CK<sup>&reg;</sup> Containers platform. The techniques below are known to target containers and container orchestration systems such as Kubernetes.",
                "subtypes": [],
            },
            {
                "name": "ESXi",
                "type": "local",
                "matrix": "enterprise-attack",
                "path": "enterprise/esxi",
                "platforms": ["ESXi"],
                "descr": "Below are the tactics and techniques representing the MITRE ATT&CK<sup>&reg;</sup> ESXi platform. The techniques below are known to target VMware ESXi hypervisors. The Matrix contains information for the ESXi platform.",
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
        "descr": "Below are the tactics and techniques representing the MITRE ATT&CK<sup>&reg;</sup> Matrix for Mobile. The Matrix covers techniques involving device access and network-based effects that can be used by adversaries without device access.",
        "subtypes": [
            {
                "name": "Android",
                "type": "local",
                "matrix": "mobile-attack",
                "path": "mobile/android",
                "platforms": ["Android"],
                "descr": "Below are the tactics and techniques representing the MITRE ATT&CK<sup>&reg;</sup> Android platform. The techniques below are known to target mobile devices running Android operating systems.",
                "subtypes": [],
            },
            {
                "name": "iOS",
                "type": "local",
                "matrix": "mobile-attack",
                "path": "mobile/ios",
                "platforms": ["iOS"],
                "descr": "Below are the tactics and techniques representing the MITRE ATT&CK<sup>&reg;</sup> iOS platform. The techniques below are known to target mobile devices running iOS operating systems.",
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
    "Office Suite": "enterprise/cloud/officesuite",
    "Identity Provider": "enterprise/cloud/identityprovider",
    "SaaS": "enterprise/cloud/saas",
    "IaaS": "enterprise/cloud/iaas",
    "Network Devices": "enterprise/network-devices",
    "Containers": "enterprise/containers",
    "ESXi": "enterprise/esxi",
    "Android": "mobile/android",
    "iOS": "mobile/ios",
}
