Title: ATT&CK for Mobile Introduction
Template: general/intro-overview
Date: 2018
Category: Cyber Threat Intelligence
Authors: Blake Strom
url: /resources/mobile-introduction
save_as: resources/mobile-introduction/index.html

ATT&CK<sup>&reg;</sup> is a model and framework for describing the actions an adversary may take while operating within an enterprise network. This overview covers ATT&CK for Mobile, a profile of ATT&CK for the mobile environment.

NIST published [Draft NISTIR 8144, Assessing Threats to Mobile Devices & Infrastructure: The Mobile Threat Catalogue](http://csrc.nist.gov/publications/drafts/nistir-8144/nistir8144_draft.pdf){:target="_blank"} and the accompanying [Mobile Threat Catalogue website](https://pages.nist.gov/mobile-threat-catalogue/){:target="_blank"}, a detailed list of threats against mobile devices and other elements of the mobile ecosystem, intended to support development of mobile security capabilities, solutions, and best practices to protect enterprises as they deploy mobile devices.

ATT&CK for Mobile builds upon NIST's Mobile Threat Catalogue, providing a model of adversarial tactics and techniques used to gain access to mobile devices as well as tactics and techniques to then take advantage of that access in order to accomplish adversarial objectives. ATT&CK for Mobile also depicts network-based effects, which are adversarial tactics and techniques that an adversary can employ without access to the mobile device itself. Each adversarial technique includes a technical description along with applicable mitigation/countermeasure approaches, applicable detection analytics, and examples of use.

The tactic categories for ATT&CK were derived from the stages of a seven-stage Cyber Attack Lifecycle<sup>[[1]](https://www.mitre.org/capabilities/cybersecurity/threat-based-defense){:target="_blank"}</sup> (first articulated by Lockheed Martin as the Cyber Kill Chain<sup>&reg;</sup><sup>[[2]](https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf){:target="_blank"}</sup>). The ATT&CK tactic categories and techniques provide a deeper level of granularity in describing adversary actions.

Many security architecture differences exist between traditional enterprise PCs and today's mobile devices that necessitate a mobile-specific profile of ATT&CK. Mobile devices benefit from lessons learned in the PC environment, notably with sandbox capabilities that provide protection from vulnerabilities and malicious behavior by controlling the allowed interactions between applications and between each application and underlying device components. However, the unique attributes and advanced capabilities of mobile devices, including their almost always powered-on state, ubiquitous network connectivity, multiple radio interfaces, and environmental sensors introduce new threats. The sandboxing capabilities of mobile devices, while providing critical security protections, severely limit the capabilities of third-party host-based security products (e.g. antivirus software or other endpoint detection and response products) to detect and respond to threats. Network-based security monitoring also faces challenges in the mobile environment. Mobile devices are only sometimes connected to an enterprise network while at other times are connected to cellular networks or public Wi-Fi networks that cannot be monitored by an enterprise. Mobile devices and applications typically treat the network as untrusted, encrypting most or all network communication and often using techniques such as certificate pinning to resist network-based attacks but also increasing the difficulty of monitoring network traffic. These security architecture differences mean that the same detection and mitigation approaches used in the traditional enterprise PC environment may not work in the mobile environment and alternative approaches must be used.

Development of ATT&CK for Mobile was sponsored by the [National Cybersecurity Center of Excellence (NCCoE) at the National Institute of Standards and Technology (NIST)](https://nccoe.nist.gov/){:target="_blank"} in support of the Study on Mobile Device Security by the [Department of Homeland Security](https://www.dhs.gov/csd-mobile){:target="_blank"}.

#### Purpose
ATT&CK for Mobile is a constantly growing common reference for tactics and techniques that may be used by adversaries in the mobile environment. It enables a comprehensive evaluation of computer network defense (CND) technologies, processes, and policies against a common enterprise threat model. We do not claim that it is a comprehensive list of techniques, only an approximation of what is publicly known; therefore, it is also an invitation for the community to contribute additional details and information to continue developing the body of knowledge. Contributions could include new techniques, categories of actions, clarifying information, examples, other platforms or environments, methods of detection or mitigation, and data sources. See the [Contribute](/resources/contribute) page for instructions on how to get involved.

The result will help focus community efforts on areas that are not well understood or covered by current defensive technologies and best practices. Developers of current defensive tools and policies can identify where their value and strengths are in relation to the ATT&CK framework. Likewise, cyber security research can use ATT&CK as a grounded reference point to drive future investigation.

#### ATT&CK for Mobile Use Cases

* Prioritize development and/or acquisition efforts of defensive capabilities
* Conduct analyses of alternatives between defensive capabilities
* Determine “coverage” of a set of defensive capabilities
* Describe an intrusion chain of events based on the technique used from start to finish with a common reference
* Identify commonalities between adversary tradecraft, as well as distinguishing characteristics
* Connect mitigations, weaknesses, and adversaries
* Determine effective security testing strategies
* Identify defensive gap areas for which adequate countermeasures do not yet exist

#### Notice
This software (or technical data) was produced for the U. S. Government under contract SB-1341-14-CQ-0010, and is subject to the Rights in Data-General Clause 52.227-14, Alt. IV (DEC 2007)

&copy; 2018 The MITRE Corporation. All Rights Reserved. Approved for Public Release; Distribution Unlimited. Case Number 17-0836

<br>
#### References

[1] [The MITRE Corporation. (2017). Threat-based Defense - Understanding an attacker’s tactics and techniques is key to successful cyber defense. Retrieved February 8, 2017.](https://www.mitre.org/capabilities/cybersecurity/threat-based-defense){:target="_blank"}

[2] [Hutchins et al.. (2011). Intelligence-driven computer network defense informed by analysis of adversary campaigns and intrusion kill chains. Retrieved August 18, 2016.](http://www.lockheedmartin.com/content/dam/lockheed/data/corporate/documents/LM-White-Paper-Intel-Driven-Defense.pdf){:target="_blank"}