# MITRE ATT&CK&reg; Website

### See the live site at [attack.mitre.org](https://attack.mitre.org)!

This repository contains the source code used to generate the MITRE ATT&CK&reg; website as seen at `attack.mitre.org`. The source code is flexible to allow users to generate the site with custom content.

## Usage
The [Install and Run](#Install-and-Build) section below explains how to set up a local version of the site. You can also visit the live site at [attack.mitre.org](https://attack.mitre.org). If you want to extend the style, content or functionality of this site, please see our [Customizing the ATT&CK Website](/CUSTOMIZING.md) document for tips and tricks.

Use our [Github Issue Tracker](https://github.com/mitre-attack/attack-website/issues) to let us know of any bugs or other issues you encounter. We also encourage pull requests if you've extended the site in a cool way and want to share back to the community!

If you find errors or typos in the site content, please let us know by sending an email to attack@mitre.org with the subject **Website Content Error**, and make sure to include both a description of the error and the URL at which it can be found. 

_See [CONTRIBUTING.md](/CONTRIBUTING.md) for more information on making contributions to the ATT&CK website._

## Prerequisites

- Docker
- Node.js and npm (for local build)
- Python 3 and pip (for local build)

## Workflow 1: Build and Run Using Docker

1. Build the Docker image:

    ```
    docker build -t attack_website .
    ```

2. Run the Docker container:

    ```
    docker run -p 80:80 attack_website
    ```

   This will start a Docker container with the image you built and forward port 80 from the container to your host machine.

3. Now, you should be able to view the website by opening a web browser and navigating to `http://localhost`.

## Workflow 2: Build Locally and Serve Using Docker

1. Ensure you have Node.js, npm, Python 3, and pip installed on your local machine.

2. Build the static web content locally. The web application is composed of two modules: the Pelican content, and the ATT&CK search module.

    - Build the Pelican content by running the following command from the root of the project:

        ```
        python3 update-attack.py --attack-brand --extras --no-test-exitstatus
        ```

      The static web content will be written to a folder called "output".

    - Build the search module by running the following commands:

        ```
        cd attack-search
        npm ci
        npm run build
        cp dist/search_bundle.js ../output/theme/scripts/
        cd ..
        ```

3. Build the Docker image for the test environment:

    ```
    cd test
    docker build -t attack-website-test .
    ```

4. Run the Docker container for the test environment:

    ```
    docker run -p 80:80 -v $(pwd)/../output:/workspace attack-website-test
    ```

   This will start a Docker container with the test environment image, forward port 80 from the container to your host machine, and mount the "output" directory from your local workspace to the "/workspace" directory inside the container. This allows Nginx to serve the static web content you built.

   Please see [test/README.md](./test/README.md) for further usage details on the test environment image.

5. Now, you should be able to view the website by opening a web browser and navigating to `http://localhost`.

Please note that Workflow 1 is the preferred method as it closely emulates our production environment. Workflow 2 is recommended for those who prefer or need to build the website locally before testing it.

## Disclaimer: Do Not Use Pelican's Built-in Web Server

It is important to avoid using Pelican's built-in web server for serving the website. This is because Pelican uses a different set of rules for path matching compared to Nginx, which is used in our production environment. As a result, the behavior of the built-in server may differ from the production environment, potentially leading to discrepancies and overlooked issues.

To ensure that your testing environment is as close as possible to the production environment, we recommend using the workflows outlined in this README. Both workflows leverage Nginx, which more closely emulate the behavior of the production environment, improving your ability to catch potential issues before they reach production.


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
