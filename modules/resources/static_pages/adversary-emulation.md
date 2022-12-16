Title: Adversary Emulation Plans
Template: general/intro-overview
Date: 2018
Category: Cyber Threat Intelligence
Authors: Blake Strom
url: /resources/adversary-emulation-plans
save_as: resources/adversary-emulation-plans/index.html

To showcase the practical use of ATT&CK for offensive operators and defenders, MITRE created Adversary Emulation Plans. These are prototype documents of what can be done with publicly available threat reports and ATT&CK. The purpose of this activity is to allow defenders to more effectively test their networks and defenses by enabling red teams to more actively model adversary behavior, as described by ATT&CK. This is part of a larger process to help more effectively test products and environments, as well as create analytics for ATT&CK behaviors rather than detecting a specific indicator of compromise (IOC) or specific tool.

There are many threat intel reports that focus on malware reverse engineering, initial compromise, and command and control (C2) explanations; however, there are not many threat reports on how attackers are chaining techniques together or how attackers operate on keyboard. Because these prototypes are built on these open threat reports, they have the same limitations. To help with this, we provided a sample way to string the ATT&CK tactics together based on general red teaming experience. To create these plans, the team drilled down on specific APT groups listed in ATT&CK and see what kind of plans could be generated for an operator to emulate those APTs. After reading what capabilities were provided by an APT's tools, we compiled a list of other ways to exhibit the same behavior. We wanted operators to behave generally like a specific adversary (sticking to that adversary's known TTPs and behaviors), but having some latitude in actual implementation. To help with this, we also provided a cheat sheet for commands that can be executed for similar behavior in some of the most commonly used red teaming tools. An example, high-level diagram below highlights one possible way to structure an APT3 emulation plan.

<center>
![APT3 Emulation Plan](/theme/images/APT3_phase_diagram.png)
</center>

We will not be going through this for every group on ATT&CK, rather select a subset we feel offer a unique perspective for defenses to be measured. We hope that the community finds use in these prototypes, and builds on them to make ATT&CK actionable. These are living documents that can be updated with newer information, format, or changed for other uses. Please reach out to <attack@mitre.org> for anything relating to these prototypes.

#### Emulation Plan Documents

##### [APT3](/groups/G0022)

The MITRE APT3 Adversary Emulation Plans outline the behavior of persistent threat groups mapped to ATT&CK. They are used by adversary emulation teams to test an organizations network security and security products against specific threats.

[APT3 Adversary Emulation Plan](/docs/APT3_Adversary_Emulation_Plan.pdf){:target="_blank"}

The Adversary Emulation Field Manual is a companion document to the Adversary Emulation Plan for a particular adversary group. It breaks out command-by-command actions that the group is known to use or example commands to exhibit the same behavior as their tools, mapped to ATT&CK and related commands from public and commercially available offensive testing frameworks.

[APT3 Adversary Emulation Field Manual](/docs/APT3_Adversary_Emulation_Field_Manual.xlsx)