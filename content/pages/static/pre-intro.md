Title: PRE-ATT&CK
Template: general/intro-overview
Date: 2018
Category: Cyber Threat Intelligence
Authors: Blake Strom
url: /resources/pre-introduction
save_as: resources/pre-introduction/index.html

Most companies secure their enterprise to ward off cyber adversaries by using perimeter defenses and blocking known adversary indicators of compromise (IOC). Heavy reliance on collecting and black listing using IOCs (e.g., IP addresses, domains, malware hashes) as a way to detect and block the adversary provides only limited protection. For example, the Verizon DBIR 2016 Report<sup>[[1]](http://www.verizonenterprise.com/resources/reports/rp_DBIR_2016_Report_en_xg.pdf){:target="_blank"}</sup> states that 99% of malware hashes are seen for just 58 seconds or less. A comprehensive security plan does not begin or end at the perimeter, but instead leverages an understanding of the full lifecycle of a cyber adversary.


Adversary pre-compromise activities are largely executed outside the enterprise’s field of view, making them more difficult to detect. Cyber adversaries case their victims using the wealth of information available on the internet and take advantage of an enterprise’s third-party relationships to gain access to a target’s infrastructure. Defenders must expand their ability to monitor and understand adversary actions outside the boundaries of their enterprise.

<center>
![PRE Tactics](/theme/images/enterprise-pre-lifecycle.png)
</center>

#### Purpose
Building on [ATT&CK®](/resources/enterprise-introduction), PRE-ATT&CK provides the ability to prevent an attack before the adversary has a chance to get in. The 15 tactic categories for PRE-ATT&CK were derived from the first two stages (recon and weaponize) of a seven-stage Cyber Attack Lifecycle<sup>[[2]](https://www.mitre.org/capabilities/cybersecurity/threat-based-defense){:target="_blank"}</sup> (first articulated by Lockheed Martin as the Cyber Kill Chain®<sup>[[3]](http://www.lockheedmartin.com/content/dam/lockheed/data/corporate/documents/LM-White-Paper-Intel-Driven-Defense.pdf){:target="_blank"}</sup> ). This framework captures the tactics, techniques, and procedures adversaries use to select a target, obtain information, and launch a campaign. The framework lists the ways that adversaries perform each tactic and provides the ability to track and organize adversary statistics and patterns. Ultimately, this arms defenders with a broader understanding of adversary actions that they can use to determine technical or policy-based mitigations and evaluate the quality and utility of cyber threat intelligence data sources.

<br>
PRE-ATT&CK provides defenders with the ability to answer questions such as:

* Are there signs that the adversary might be targeting you?
* What commonly used techniques does the adversary use against you?
* How should you prioritize cyber threat intelligence data acquisitions and analytics to gain additional insights to “see” the adversary before the exploit occurs?

<Br>
PRE-ATT&CK is a constantly growing common reference for pre-compromise techniques that brings greater awareness of what actions may be seen prior to a network intrusion. It enables a comprehensive evaluation of computer network defense (CND) technologies, data, processes, and policies against a common enterprise threat model.

We do not claim that PRE-ATT&CK is a comprehensive compilation of techniques, only an approximation of what is publicly known. We invite and encourage the broader community to contribute additional details and information to continue developing the body of knowledge. Contributions could include:

* New techniques
* Categories of actions
* Clarifying information
* Examples
* Other platforms or environments
* Methods of detection or mitigation
* Data sources

See the [Contribute](/resources/contribute) page to learn how to get involved.

The result will help focus community efforts on areas that are not well understood or covered by current defensive technologies and best practices. Developers of current defensive tools and policies can identify where their value and strengths are in relation to the PRE-ATT&CK framework. Likewise, cyber security researchers can use PRE-ATT&CK as a grounded reference point to drive future investigation.

#### PRE-ATT&CK Use Cases

PRE-ATT&CK describes 15 categories of high-level tactics, derived from the first four stages of the cyber attack life cycle. With a more granular understanding of adversary activities, defenders can make more informed decisions about the potential technical and policy-based mitigations they can adopt to reduce adversary success in the pre-compromise phases of the cyber attack lifecycle, thus reducing targeted attacks. Defenders consume multiple cyber threat intelligence reporting sources with varying detail and lack a consolidated means to assess their value. PRE-ATT&CK provides the structure and breadth required for defenders to track adversary behaviors and assess data sets that will increase their insight into adversary activity.

<center>
![PRE Graph](/theme/images/Pre_graph.png)
</center>
<br>

#### ATT&CK and PRE-ATT&CK Comparison

PRE-ATT&CK is associated with ATT&CK since it adopts the same model structure and complements ATT&CK by focusing on the left of exploit stages of the Cyber Attack Lifecycle. PRE-ATT&CK and ATT&CK have several fundamental differences, namely:

* ATT&CK is tightly coupled to a specific enterprise network (e.g., Microsoft Windows, Linux, or mobility environment) and therefore provides detailed technical information relative to the adversary actions and defender mitigations for each technique. PRE-ATT&CK is agnostic to these differences since the adversary can operate across any of these environments for their pre-compromise preparation activities.
* The mitigations in ATT&CK can be very specific and effective. PRE-ATT&CK mitigations are under development and will encompass technical and policy-based mitigations. In many cases, these mitigations will not be as precise or comprehensive given the inability to fully capture all adversary activities, data, and tools.
* While many of the ATT&CK mitigations required increased end point monitoring, PRE-ATT&CK largely requires additional data sources to obtain information about adversarial objectives and activities.

<br>
#### References

[1] [Verizon Enterprise Solutions. (2016). 2016 Data Breach Investigations Report. Retrieved February 8, 2017.](http://www.verizonenterprise.com/resources/reports/rp_DBIR_2016_Report_en_xg.pdf){:target="_blank"}

[2] [The MITRE Corporation. (2017). Threat-based Defense - Understanding an attacker’s tactics and techniques is key to successful cyber defense. Retrieved February 8, 2017.](https://www.mitre.org/capabilities/cybersecurity/threat-based-defense){:target="_blank"}

[3] [Hutchins et al.. (2011). Intelligence-driven computer network defense informed by analysis of adversary campaigns and intrusion kill chains. Retrieved August 18, 2016.](http://www.lockheedmartin.com/content/dam/lockheed/data/corporate/documents/LM-White-Paper-Intel-Driven-Defense.pdf){:target="_blank"}