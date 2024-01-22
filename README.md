# MITRE ATT&CK&reg; Website

This repository contains the source code used to generate the MITRE ATT&CK&reg; website as seen at `attack.mitre.org`. The source code is flexible to allow users to generate the site with custom content.

## Visit the Site

You can view the live site at [attack.mitre.org](https://attack.mitre.org)!

## Reporting Issues

If you encounter any bugs or other issues, please use our [Github Issue Tracker](https://github.com/mitre-attack/attack-website/issues).

If you find errors or typos in the site content, let us know by sending an email to <attack@mitre.org> with the subject **Website Content Error**. Include a description of the error and the URL at which it can be found.

## Development

Check out our [developer guide](DEVELOPMENT.md) if you are interested in extending the style, content, or functionality of this site.
It includes instructions on setting up a local version of the site, and workflows for building and running the site using Docker or locally.

We also have the additional following guides:

* A [deployment guide](./test/README.md) for setting up our testing environment
* A [release guide](./docs/RELEASE.md) for the release process

## Related MITRE Work

### ATT&CK STIX Data

Data representing the ATT&CK Catalog can be found on the following repositories:

* [Cyber Threat Intelligence repository](https://github.com/mitre/cti) contains the ATT&CK and [CAPEC](https://capec.mitre.org/) datasets expressed in STIX 2.0 JSON.
* [attack-stix-data](https://github.com/mitre-attack/attack-stix-data) contains the ATT&CK dataset expressed in STIX 2.1 Collections.

### ATT&CK Navigator

The ATT&CK Navigator is an open-source tool providing basic navigation and annotation of ATT&CK matrices, something that people are already doing today in tools like Excel. It is designed to be simple and generic - you can use the Navigator to visualize your defensive coverage, your red/blue team planning, the frequency of detected techniques, and more.

<https://github.com/mitre-attack/attack-navigator>

### STIX

Structured Threat Information Expression (STIX<sup>&trade;</sup>) is a language and serialization format used to exchange cyber threat intelligence (CTI).

STIX enables organizations to share CTI with one another in a consistent and machine readable manner, allowing security communities to better understand what computer-based attacks they are most likely to see and to anticipate and/or respond to those attacks faster and more effectively.

STIX is designed to improve many different capabilities, such as collaborative threat analysis, automated threat exchange, automated detection and response, and more.

<https://oasis-open.github.io/cti-documentation/>

## Notice

Copyright 2015-2024 The MITRE Corporation

Approved for Public Release; Distribution Unlimited. Case Number 19-3504.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   <http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

This project makes use of ATT&CK&reg;

[ATT&CK Terms of Use](https://attack.mitre.org/resources/legal-and-branding/terms-of-use/)
