Title: Interfaces for Working with ATT&CK
Template: general/intro-overview
Date: 2018
Category: Cyber Threat Intelligence
Authors: Blake Strom
url: /resources/working-with-attack
save_as: resources/working-with-attack/index.html

There are two different ways for you to access the ATT&CK content:
<br>
#### ATT&CK expressed in STIX 2.0 GitHub repository

There are a few different ways you can interact with the ATT&CK content in this [repo](https://github.com/mitre/cti){:target="_blank"}. If you use Python, the best way is to utilize [cti-python-stix2](https://github.com/oasis-open/cti-python-stix2){:target="_blank"}. We have a [USAGE](https://github.com/mitre/cti/blob/master/USAGE.md){:target="_blank"} doc in this repo to help you with this. Since STIX 2.0 is JSON, you can also use a JSON library in the programming language of your choice and interact with the raw content, like the full set of Enterprise ATT&CK content you can find [here](https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json){:target="_blank"}.

#### TAXII Server

Our TAXII server stays up to date with the content found in our GitHub repository, so you can also access the ATT&CK content here. As the TAXII Server release [blog post](https://medium.com/mitre-attack/att-ck-content-available-in-stix-2-0-via-public-taxii-2-0-server-317e5c41e214){:target="_blank"} states, you can use the [cti-python-stix2](https://github.com/oasis-open/cti-python-stix2){:target="_blank"} and [cti-taxii-client](https://github.com/oasis-open/cti-taxii-client){:target="_blank"} to get the ATT&CK content from the TAXII server.