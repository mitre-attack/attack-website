# MITRE ATT&CK&reg; Website

### See the live site at [attack.mitre.org](https://attack.mitre.org)!

This repository contains the source code used to generate the MITRE ATT&CK&reg; website as seen at `attack.mitre.org`. The source code is flexible to allow users to generate the site with custom content.

## Usage
The [Install and Run](#Install-and-Build) section below explains how to set up a local version of the site. You can also visit the live site at [attack.mitre.org](https://attack.mitre.org). If you want to extend the style, content or functionality of this site, please see our [Customizing the ATT&CK Website](/CUSTOMIZING.md) document for tips and tricks.

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

1. Update ATT&CK markdown from the STIX content, and generate the output HTML from the markdown: `python3 update-attack.py`. _Note: `update-attack.py`, has many optional command line arguments which affect the behavior of the build. Run `python3 update-attack.py -h` for a list of arguments and an explanation of their functionality._
2. Serve the HTML to `localhost:8000`: 
    1. Ensure you are in the root of the repository, e.g. `path/to/attack-website`
    2. `pelican -l`

### (Optional) Build the search module
1. Install Node.js. This is required in order to compile the search service webpack bundle.
2. Generate the search service webpack bundle to enable search functionality:
   ```shell
   cd attack-search/
   npm install # installs all third-party dependencies
   npm run build # generates the webpack bundle
   npm run copy # copies the resultant bundle to the Pelican server output directory
   ```

### Installing, building, and serving the site via Docker 

1. Build the docker image:
    - `docker build -t <your_preferred_image_name> .`
2. Run a docker container:
    - `docker run --name <your_preferred_container_name> -d -p <your_preferred_port>:80 <image_name_from_build_command>`
3. View the site on your preferred localhost port

## Related MITRE Work
#### ATT&CK STIX Data
Data representing the ATT&CK Catalog can be found on the following repositories:
- [Cyber Threat Intelligence repository](https://github.com/mitre/cti) contains the ATT&CK and [CAPEC](https://capec.mitre.org/) datasets expressed in STIX 2.0 JSON.
- [attack-stix-data](https://github.com/mitre-attack/attack-stix-data) contains the ATT&CK dataset expressed in STIX 2.1 Collections.

#### ATT&CK Navigator
The ATT&CK Navigator is an open-source tool providing basic navigation and annotation of ATT&CK matrices, something that people are already doing today in tools like Excel. It is designed to be simple and generic - you can use the Navigator to visualize your defensive coverage, your red/blue team planning, the frequency of detected techniques, and more. 

https://github.com/mitre-attack/attack-navigator

#### STIX
Structured Threat Information Expression (STIX<sup>&trade;</sup>) is a language and serialization format used to exchange cyber threat intelligence (CTI).

STIX enables organizations to share CTI with one another in a consistent and machine readable manner, allowing security communities to better understand what computer-based attacks they are most likely to see and to anticipate and/or respond to those attacks faster and more effectively.

STIX is designed to improve many different capabilities, such as collaborative threat analysis, automated threat exchange, automated detection and response, and more.

https://oasis-open.github.io/cti-documentation/

## Notice
Copyright 2015-2023 The MITRE Corporation

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
