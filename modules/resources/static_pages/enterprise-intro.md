Title: ATT&CK for Enterprise Introduction
Date: 2018
Category: Cyber Threat Intelligence
Authors: Blake Strom
Template: general/intro-overview
url: /resources/enterprise-introduction
save_as: resources/enterprise-introduction/index.html

ATT&CK<sup>&reg;</sup> for Enterprise is an adversary model and framework for describing the actions an adversary may take to compromise and operate within an enterprise network. The model can be used to better characterize and describe post-compromise adversary behavior. It both expands the knowledge of network defenders and assists in prioritizing network defense by detailing the tactics, techniques, and procedures (TTPs) cyber threats use to gain access and execute their objectives while operating inside a network.

ATT&CK for Enterprise incorporates information on cyber adversaries gathered through MITRE research, as well as from other disciplines such as penetration testing and red teaming to establish a collection of knowledge characterizing the activities adversaries use against enterprise networks. While there is significant research on initial exploitation and use of perimeter defenses, there is a gap in central knowledge of adversary process after initial access has been gained. ATT&CK for Enterprise focuses on TTPs adversaries use to make decisions, expand access, and execute their objectives. It aims to describe an adversary's steps at a high enough level to be applied widely across platforms, but still maintain enough details to be technically useful.

<img alt="enterprise tactics" class="w-100" src="/theme/images/enterprise-pre-lifecycle.png">

The 11 tactic categories within ATT&CK for Enterprise were derived from the later stages (exploit, control, maintain, and execute) of a seven-stage Cyber Attack Lifecycle<sup>[[1]](https://www.mitre.org/capabilities/cybersecurity/threat-based-defense){:target="_blank"}</sup> (first articulated by Lockheed Martin as the Cyber Kill Chain<sup>&reg;</sup><sup>[[2]](https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf){:target="_blank"}</sup>). This provides a deeper level of granularity in describing what can occur during an intrusion.

Each category contains a list of techniques that an adversary could use to perform that tactic. Techniques are broken down to provide a technical description, indicators, useful defensive sensor data, detection analytics, and potential mitigations. Applying intrusion data to the model then helps focus defense on the commonly used techniques across groups of activity and helps identify gaps in security. Defenders and decision makers can use the information in ATT&CK for Enterprise for various purposes, not just as a checklist of specific adversarial techniques.

ATT&CK for Enterprise incorporates details from multiple operating system platforms commonly found within enterprise networks, including Microsoft Windows, macOS, and Linux. The framework and higher level categories may also be applied to other platforms and environments. To view the contents of ATT&CK for Enterprise, use the left navigation pane, which breaks out techniques by tactic category or view [All Techniques](/techniques/enterprise/).

#### Purpose
ATT&CK for Enterprise is a constantly growing common reference for adversary behavior that brings greater awareness of what actions may be seen during an enterprise network intrusion. It enables a comprehensive evaluation of computer network defense (CND) technologies, processes, and policies against a common enterprise adversary model. We do not claim that it is a comprehensive list of techniques, only an approximation of what is publicly known; therefore, it is also an invitation for the community to contribute additional details and information to continue developing the body of knowledge. Contributions could include new techniques, categories of actions, clarifying information, examples, other platforms or environments, methods of detection or mitigation, and data sources. See the [Contribute](/resources/contribute) page for instructions on how to get involved.

The result will help focus community efforts on areas that are not well understood or covered by current defensive technologies and best practices. Developers of current defensive tools and policies can identify where their value and strengths are in relation to the ATT&CK for Enterprise adversary model. Likewise, cyber security research can use ATT&CK for Enterprise as a grounded reference point to drive future investigation.

#### ATT&CK for Enterprise Use Cases

* Prioritize development and/or acquisition efforts for CND capabilities
* Conduct analyses of alternatives between CND capabilities
* Determine “coverage” of a set of CND capabilities
* Describe an intrusion chain of events based on the technique used from start to finish with a common reference
* Identify commonalities between adversary tradecraft, as well as distinguishing characteristics
* Connect mitigations, weaknesses, and adversaries

<br>
#### References

[1] [The MITRE Corporation. (2017). Threat-based Defense - Understanding an attacker’s tactics and techniques is key to successful cyber defense. Retrieved February 8, 2017.](https://www.mitre.org/capabilities/cybersecurity/threat-based-defense){:target="_blank"}

[2] [Hutchins et al.. (2011). Intelligence-driven computer network defense informed by analysis of adversary campaigns and intrusion kill chains. Retrieved August 18, 2016.](http://www.lockheedmartin.com/content/dam/lockheed/data/corporate/documents/LM-White-Paper-Intel-Driven-Defense.pdf){:target="_blank"}