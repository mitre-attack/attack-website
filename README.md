# MITRE ATT&CK&reg; Website

### See the live site at [attack.mitre.org](https://attack.mitre.org)!

This repository contains the source code used to generate the MITRE ATT&CK&reg; website as seen at `attack.mitre.org`. The source code is flexible to allow users to generate the site with custom content.

## Usage
The [Install and Run](#Install-and-Build) section below explains how to set up a local version of the site. You can also visit the live site at [attack.mitre.org](https://attack.mitre.org). See [Building the site with custom content](#Building-the-site-with-custom-content) for information about building the site with custom content.

Use our [Github Issue Tracker](https://github.com/mitre-attack/attack-website/issues) to let us know of any bugs or other issues you encounter. We also encourage pull requests if you've extended the site in a cool way and want to share back to the community!

If you find errors or typos in the site content, please let us know by sending an email to attack@mitre.org with the subject **Website Content Error**, and make sure to include both a description of the error and the URL at which it can be found. 

_See [CONTRIBUTING.md](/CONTRIBUTING.md) for more information on making contributions to the ATT&CK website._

## Requirements

- [python](https://www.python.org/) 3.6 or greater

## Install and Build

### Install requirements

1. Create a virtual environment: 
    - macOS and Linux: `python3 -m venv env`
    - Windows: `py -m venv env`
2. Activate the virtual environment: 
    - macOS and Linux: `source env/bin/activate`
    - Windows: `env/Scripts/activate.bat`
3. Install requirement packages: `pip3 install -r requirements.txt`

### Build and serve the local site

1. Update ATT&CK markdown from the STIX content, and generate the output html from the markdown: `python3 update-attack.py`. _Note: `update-attack.py`, has many optional command line arguments which affect the behavior of the build. Run `python3 update-attack.py -h` for a list of arguments and an explanation of their functionality._
2. Serve the html to `localhost:8000`: 
    1. `cd output`
    2. `python3 -m pelican.server`

### Installing, building, and serving the site via Docker 

1. Build the docker image:
    - `docker build -t <your_preferred_image_name> .`
2. Run a docker container:
    - `docker run --name <your_preferred_container_name -d -p <your_preferred_port>:80 <image_name_from_build_command>`
3. View the site on your preferred localhost port

## Implementation Overview

The ATT&CK site uses a combination of Python, Pelican and Jinja to convert the STIX content into a set of static HTML files. When `update-attack.py` is run, it generates a set of markdown files in `content` containing the parsed STIX content. Pelican then reads these markdown files and uses them with the Jinja templates in `attack-theme/templates` to build the site HTML in the output directory. 

### Modules

The website is built from different modules. These modules can be found inside the `modules` directory. If the `update-attack.py` script is ran without any arguments, it will automatically look for modules inside the `modules` directory and build them.  Modules are divided in two classes, active and supportive modules. Active modules appends a link to the website's main menu and typically generates markdown files. For example, the `techniques` module is reponsible for generating all Technique related markdown pages. Supportive modules are those who do not appear on the website menu but are critical to the general website build. An example of a supportive module is the `util` module which has methods and API calls to interface with the STIX bundles.

Modules that are not present on the `modules` directory will not get built and will not appear on the website's main navigation menu. You can also select specific modules to be ran without removing modules from the directory by running the `update-attack.py` script with the `-m` flag followed by the names of the modules. For example, run `python3 update-attack.py -m clean techniques website_build` to run a fresh build, generate the techniques markdown files, and generate the HTML files.

### Building your own module

To build your own module, create a folder inside of the `modules` directory with the name of the module. Typically a module will have three files: `__init__py`, `your_module-s_name.py`, `your_module-s_name_config.py`. The `__init__.py` file contains methods that are used to determine the run priority or if they will appear on websites's main menu. For example, if it is an active module that will appear on the website's menu, be sure to include `get_menu()`, `get_priority()`, and `run_module()` in the `__init__.py` file (see the following code snippet for an example). The module can be added to the website's menu as a single link to the main module page and/or can include links to subpages in a hoverable dropdown menu. 

```python
from . import your_module-s_name
from . import your_module-s_name_config

def get_priority():
    return your_module-s_name_config.priority

def get_menu():
    return {
        "name": "Your module's name", 
        "url": "/your_module-s_name/", 
        "external_link": False,
        "priority": your_module-s_name_config.priority,
        "children": [
            {
                "name": "Module sub-menu page",
                "url": "/your_module-s_name/subpage",
                "external_link": False,
                "children": []
            },
            ...
            {
                "name": "Module sub-menu external page",
                "url": "https://attack.mitre.org",
                "external_link": True,
                "children": []            
            }
        ]
    }

def run_module():
    return (your_module-s_name.generate_your_module-s_name(), your_module-s_name_config.module_name)
```

Every module has a given priority number. This number is used to determine the order on which the modules are ran. The build script will run the modules in an ascending priority order (lowest priority number will run first). The priority inside of the `get_menu()` will determine the website's main menu order from left to right; module with the lowest priority number will be on the left.

## Building the site with custom content

The ATT&CK Website is designed support an evolving knowledge base. The content seen on the site is generated from data in STIX2.0 JSON format. The data used on the live site at [attack.mitre.org](https://attack.mitre.org) can be found on our [mitre/cti](https://github.com/mitre/cti) github repo. 

You can generate the website using custom content by replacing the STIX bundles in `/data/stix/`:
- `enterprise-attack.json` is the bundle for the enterprise domain.
- `mobile-attack.json` is the bundle for the mobile domain.
- the `*_old.json` bundles are updated automatically when the site is built, and are used for generating Matrix timestamps. `old_dates.json` is used for fallback timestamps for the matrices. You typically won't need to replace these files.

Users wishing to make changes to the ATT&CK website visual theme should take a look at our scss source files in `attack-theme/static/style`. Changes to the colors defined in `_colors.scss` should automatically propagate across the site. Users wishing to make changes to the layout of pages should modify the templates found in `attack-theme/templates`. Major additions or changes will typically require modification of the python modules in `modules/` in addition to the templates.

The logos used in the header, footer, and on the landing page of the website can be easily changed. Simply find their keys in the `settings_dict` of `modules/config.py`, and update their values to point to the new images.

## Related MITRE Work
#### CTI
[Cyber Threat Intelligence repository](https://github.com/mitre/cti) of the ATT&CK catalog expressed in STIX 2.0 JSON.

#### ATT&CK Navigator
The ATT&CK Navigator is an open-source tool providing basic navigation and annotation of ATT&CK matrices, something that people are already doing today in tools like Excel. It is designed to be simple and generic - you can use the Navigator to visualize your defensive coverage, your red/blue team planning, the frequency of detected techniques, and more. 

https://github.com/mitre-attack/attack-navigator

#### STIX
Structured Threat Information Expression (STIX<sup>&trade;</sup>) is a language and serialization format used to exchange cyber threat intelligence (CTI).

STIX enables organizations to share CTI with one another in a consistent and machine readable manner, allowing security communities to better understand what computer-based attacks they are most likely to see and to anticipate and/or respond to those attacks faster and more effectively.

STIX is designed to improve many different capabilities, such as collaborative threat analysis, automated threat exchange, automated detection and response, and more.

https://oasis-open.github.io/cti-documentation/

## Notice
Copyright 2015-2020 The MITRE Corporation

Approved for Public Release; Distribution Unlimited. Case Number 19-3504.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

This project makes use of ATT&CK&reg;

[ATT&CK Terms of Use](https://attack.mitre.org/resources/terms-of-use/)