Title: Updates - October 2026
Date: October 2026
Category: Cyber Threat Intelligence
Authors: Adam Pennington
Template: resources/update-post
url: /resources/updates/updates-october-2026
save_as: resources/updates/updates-october-2026/index.html

| Version | Start Date | End Date | Data | Changelogs |
|:--------|:-----------|:---------|:-----|:-----------|
| [ATT&CK v20](/versions/v20) | October 13, 2026 | Current version of ATT&CK | [v20.0 on MITRE/CTI](https://github.com/mitre/cti/releases/tag/ATT%26CK-v20.0) | 19.2 - 20.0 [Details](/docs/changelogs/v19.2-v20.0/changelog-detailed.html) ([JSON](/docs/changelogs/v19.2-v20.0/changelog.json)) |

The October 2026 (v20) ATT&CK release updates Techniques, Groups, Campaigns and Software for Enterprise, Mobile, and ICS.

The biggest change in ATT&CK v20 is expanded coverage of recent adversary activity and tradecraft, including new Campaigns covering attacks on U.S. water utilities and an AI-assisted breach of Mexican government infrastructure, along with AI-focused and AI-enabled Techniques in Enterprise and execution and command and control Techniques in ICS.

It also un-deprecates the Mobile Technique Deliver Malicious Application via Other Means, last seen in ATT&CK v11. ICS Detection Strategies now include platform and Asset context, and Mobile Detection Strategies account for the visibility limits of Android and iOS.

An [accompanying blog post](https://medium.com/mitre-attack/attack-v20-9701dd75ffb4) describes these changes as well as additional improvements across ATT&CK's various domains and platforms.

This release also includes a human-readable detailed changelog showing more specifically what changed in updated ATT&CK objects, and a machine-readable JSON changelog, whose format is described in [ATT&CK's GitHub](https://github.com/mitre-attack/mitreattack-python/blob/main/mitreattack/diffStix/README.md).

This version of ATT&CK contains 971 Software, 182 Groups, and 61 Campaigns.

Broken out by domain:

* Enterprise: 15 Tactics, 227 Techniques, 479 Sub-Techniques, 178 Groups, 842 Pieces of Software, 57 Campaigns, 44 Mitigations, 703 Detection Strategies, 1770 Analytics, and 106 Data Components
* Mobile: 12 Tactics, 78 Techniques, 47 Sub-Techniques, 20 Groups, 128 Pieces of Software, 3 Campaigns, 13 Mitigations, 124 Detection Strategies, 211 Analytics, and 29 Data Components
* ICS: 12 Tactics, 78 Techniques, 26 Sub-Techniques, 14 Groups, 25 Pieces of Software, 10 Campaigns, 53 Mitigations, 18 Assets, 106 Detection Strategies, 302 Analytics, and 36 Data Components

## Key

* New objects: ATT&CK objects which are only present in the new release.
* Major version changes: ATT&CK objects that have a major version change. (e.g. 1.0 → 2.0)
* Minor version changes: ATT&CK objects that have a minor version change. (e.g. 1.0 → 1.1)
* Other version changes: ATT&CK objects that have a version change of any other kind. (e.g. 1.0 → 1.2)
* Patches: ATT&CK objects that have been patched while keeping the version the same. (e.g., 1.0 → 1.0 but something like a typo, a URL, or some metadata was fixed)
* Object revocations: ATT&CK objects which are revoked by a different object.
* Object deprecations: ATT&CK objects which are deprecated and no longer in use, and not replaced.
* Object deletions: ATT&CK objects which are no longer found in the STIX data.

## Table of Contents

[TOC]

## Techniques

### Enterprise

#### New Techniques

* [AI-Enabled Exfiltration](/techniques/T1700) <small style="color:#929393">(v1.0)</small>
* [Anti-Automation Evasion](/techniques/T1696) <small style="color:#929393">(v1.0)</small>
* Anti-Automation Evasion: [Automate CAPTCHA Completion](/techniques/T1696/001) <small style="color:#929393">(v1.0)</small>
* Anti-Automation Evasion: [Avoid CAPTCHA](/techniques/T1696/002) <small style="color:#929393">(v1.0)</small>
* [Direct Prompt Injection](/techniques/T1699) <small style="color:#929393">(v1.0)</small>
* Disable or Modify Tools: [Impair Autonomous Defenses](/techniques/T1685/007) <small style="color:#929393">(v1.0)</small>
* [Indirect Prompt Injection](/techniques/T1698) <small style="color:#929393">(v1.0)</small>
* Stage Capabilities: [AI Result Poisoning](/techniques/T1608/007) <small style="color:#929393">(v1.0)</small>
* [Steal Application Specific Passwords](/techniques/T1697) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* Supply Chain Compromise: [Compromise Software Dependencies and Development Tools](/techniques/T1195/001) <small style="color:#929393">(v1.3&#8594;v2.0)</small>

#### Minor Version Changes

* Command and Scripting Interpreter: [PowerShell](/techniques/T1059/001) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
* [Data Transfer Size Limits](/techniques/T1030) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Data from Information Repositories: [Confluence](/techniques/T1213/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Data from Information Repositories: [Sharepoint](/techniques/T1213/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Data from Network Shared Drive](/techniques/T1039) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
* [Defacement](/techniques/T1491) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Develop Capabilities](/techniques/T1587) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Develop Capabilities: [Digital Certificates](/techniques/T1587/003) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Email Collection: [Remote Email Collection](/techniques/T1114/002) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* Encrypted Channel: [Asymmetric Cryptography](/techniques/T1573/002) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Encrypted Channel: [Symmetric Cryptography](/techniques/T1573/001) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Exfiltration Over Alternative Protocol: [Exfiltration Over Asymmetric Encrypted Non-C2 Protocol](/techniques/T1048/002) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Exfiltration Over Alternative Protocol: [Exfiltration Over Symmetric Encrypted Non-C2 Protocol](/techniques/T1048/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Exfiltration Over C2 Channel](/techniques/T1041) <small style="color:#929393">(v2.3&#8594;v2.4)</small>
* [Exfiltration Over Physical Medium](/techniques/T1052) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* Exfiltration Over Physical Medium: [Exfiltration over USB](/techniques/T1052/001) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Hijack Execution Flow](/techniques/T1574) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Modify System Image](/techniques/T1601) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Obfuscated Files or Information: [Indicator Removal from Tools](/techniques/T1027/005) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Obtain Capabilities: [Artificial Intelligence](/techniques/T1588/007) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Obtain Capabilities: [Malware](/techniques/T1588/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Phishing](/techniques/T1566) <small style="color:#929393">(v2.7&#8594;v2.8)</small>
* Remote Services: [SSH](/techniques/T1021/004) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Scheduled Transfer](/techniques/T1029) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Web Service: [Dead Drop Resolver](/techniques/T1102/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>

#### Patches

* Account Manipulation: [Additional Cloud Credentials](/techniques/T1098/001) <small style="color:#929393">(v2.8)</small>
* [Acquire Infrastructure](/techniques/T1583) <small style="color:#929393">(v1.5)</small>
* Acquire Infrastructure: [Domains](/techniques/T1583/001) <small style="color:#929393">(v1.4)</small>
* Acquire Infrastructure: [Server](/techniques/T1583/004) <small style="color:#929393">(v1.3)</small>
* Acquire Infrastructure: [Virtual Private Server](/techniques/T1583/003) <small style="color:#929393">(v1.1)</small>
* Acquire Infrastructure: [Web Services](/techniques/T1583/006) <small style="color:#929393">(v1.3)</small>
* [Application Layer Protocol](/techniques/T1071) <small style="color:#929393">(v2.4)</small>
* Application Layer Protocol: [DNS](/techniques/T1071/004) <small style="color:#929393">(v1.4)</small>
* Application Layer Protocol: [File Transfer Protocols](/techniques/T1071/002) <small style="color:#929393">(v1.4)</small>
* Application Layer Protocol: [Mail Protocols](/techniques/T1071/003) <small style="color:#929393">(v1.2)</small>
* Application Layer Protocol: [Web Protocols](/techniques/T1071/001) <small style="color:#929393">(v1.5)</small>
* [Automated Collection](/techniques/T1119) <small style="color:#929393">(v1.4)</small>
* [Browser Information Discovery](/techniques/T1217) <small style="color:#929393">(v2.0)</small>
* [Build Image on Host](/techniques/T1612) <small style="color:#929393">(v2.0)</small>
* [Compromise Infrastructure](/techniques/T1584) <small style="color:#929393">(v1.6)</small>
* Compromise Infrastructure: [Server](/techniques/T1584/004) <small style="color:#929393">(v1.2)</small>
* Compromise Infrastructure: [Virtual Private Server](/techniques/T1584/003) <small style="color:#929393">(v1.1)</small>
* Compromise Infrastructure: [Web Services](/techniques/T1584/006) <small style="color:#929393">(v1.2)</small>
* [Create or Modify System Process](/techniques/T1543) <small style="color:#929393">(v1.2)</small>
* Credentials from Password Stores: [Credentials from Web Browsers](/techniques/T1555/003) <small style="color:#929393">(v1.2)</small>
* [Data Encoding](/techniques/T1132) <small style="color:#929393">(v1.3)</small>
* Data Encoding: [Standard Encoding](/techniques/T1132/001) <small style="color:#929393">(v1.1)</small>
* [Data Obfuscation](/techniques/T1001) <small style="color:#929393">(v1.2)</small>
* Data Obfuscation: [Junk Data](/techniques/T1001/001) <small style="color:#929393">(v1.1)</small>
* Data Obfuscation: [Protocol or Service Impersonation](/techniques/T1001/003) <small style="color:#929393">(v2.1)</small>
* Data Staged: [Local Data Staging](/techniques/T1074/001) <small style="color:#929393">(v1.2)</small>
* [Data from Local System](/techniques/T1005) <small style="color:#929393">(v1.8)</small>
* [Debugger Evasion](/techniques/T1622) <small style="color:#929393">(v2.0)</small>
* [Delay Execution](/techniques/T1678) <small style="color:#929393">(v2.0)</small>
* [Deobfuscate/Decode Files or Information](/techniques/T1140) <small style="color:#929393">(v2.0)</small>
* [Disable or Modify Tools](/techniques/T1685) <small style="color:#929393">(v1.0)</small>
* [Encrypted Channel](/techniques/T1573) <small style="color:#929393">(v1.2)</small>
* Establish Accounts: [Email Accounts](/techniques/T1585/002) <small style="color:#929393">(v1.1)</small>
* [Exfiltration Over Alternative Protocol](/techniques/T1048) <small style="color:#929393">(v1.6)</small>
* Exfiltration Over Alternative Protocol: [Exfiltration Over Unencrypted Non-C2 Protocol](/techniques/T1048/003) <small style="color:#929393">(v2.2)</small>
* [Fallback Channels](/techniques/T1008) <small style="color:#929393">(v1.1)</small>
* [File and Directory Discovery](/techniques/T1083) <small style="color:#929393">(v1.7)</small>
* File and Directory Permissions Modification: [Windows Permissions](/techniques/T1222/001) <small style="color:#929393">(v2.0)</small>
* [Gather Victim Host Information](/techniques/T1592) <small style="color:#929393">(v1.2)</small>
* Gather Victim Host Information: [Client Configurations](/techniques/T1592/004) <small style="color:#929393">(v1.1)</small>
* Gather Victim Host Information: [Hardware](/techniques/T1592/001) <small style="color:#929393">(v1.1)</small>
* Gather Victim Host Information: [Software](/techniques/T1592/002) <small style="color:#929393">(v1.2)</small>
* Hijack Execution Flow: [DLL](/techniques/T1574/001) <small style="color:#929393">(v3.0)</small>
* Indicator Removal: [File Deletion](/techniques/T1070/004) <small style="color:#929393">(v2.0)</small>
* [Ingress Tool Transfer](/techniques/T1105) <small style="color:#929393">(v2.6)</small>
* [Lateral Tool Transfer](/techniques/T1570) <small style="color:#929393">(v1.4)</small>
* Masquerading: [Invalid Code Signature](/techniques/T1036/001) <small style="color:#929393">(v2.0)</small>
* Masquerading: [Match Legitimate Resource Name or Location](/techniques/T1036/005) <small style="color:#929393">(v3.0)</small>
* [Modify Registry](/techniques/T1112) <small style="color:#929393">(v3.0)</small>
* [Native API](/techniques/T1106) <small style="color:#929393">(v2.3)</small>
* [Non-Application Layer Protocol](/techniques/T1095) <small style="color:#929393">(v2.4)</small>
* [Non-Standard Port](/techniques/T1571) <small style="color:#929393">(v1.3)</small>
* [Obfuscated Files or Information](/techniques/T1027) <small style="color:#929393">(v2.0)</small>
* Obfuscated Files or Information: [Binary Padding](/techniques/T1027/001) <small style="color:#929393">(v2.0)</small>
* Obfuscated Files or Information: [Encrypted/Encoded File](/techniques/T1027/013) <small style="color:#929393">(v2.0)</small>
* Obfuscated Files or Information: [Software Packing](/techniques/T1027/002) <small style="color:#929393">(v2.0)</small>
* Phishing: [Spearphishing Attachment](/techniques/T1566/001) <small style="color:#929393">(v2.2)</small>
* Phishing: [Spearphishing Link](/techniques/T1566/002) <small style="color:#929393">(v2.8)</small>
* [Process Discovery](/techniques/T1057) <small style="color:#929393">(v1.6)</small>
* [Process Injection](/techniques/T1055) <small style="color:#929393">(v2.0)</small>
* Process Injection: [Process Hollowing](/techniques/T1055/012) <small style="color:#929393">(v2.0)</small>
* Process Injection: [Thread Execution Hijacking](/techniques/T1055/003) <small style="color:#929393">(v2.0)</small>
* [Protocol Tunneling](/techniques/T1572) <small style="color:#929393">(v1.1)</small>
* [Proxy](/techniques/T1090) <small style="color:#929393">(v3.2)</small>
* Proxy: [External Proxy](/techniques/T1090/002) <small style="color:#929393">(v1.3)</small>
* Proxy: [Internal Proxy](/techniques/T1090/001) <small style="color:#929393">(v1.2)</small>
* [Service Stop](/techniques/T1489) <small style="color:#929393">(v1.4)</small>
* [Shared Modules](/techniques/T1129) <small style="color:#929393">(v2.3)</small>
* [System Information Discovery](/techniques/T1082) <small style="color:#929393">(v3.0)</small>
* [System Location Discovery](/techniques/T1614) <small style="color:#929393">(v1.1)</small>
* System Services: [Service Execution](/techniques/T1569/002) <small style="color:#929393">(v1.3)</small>
* [System Time Discovery](/techniques/T1124) <small style="color:#929393">(v1.5)</small>
* Unsecured Credentials: [Credentials In Files](/techniques/T1552/001) <small style="color:#929393">(v1.3)</small>
* User Execution: [Malicious Image](/techniques/T1204/003) <small style="color:#929393">(v1.2)</small>
* User Execution: [Malicious Link](/techniques/T1204/001) <small style="color:#929393">(v1.2)</small>
* [Virtualization/Sandbox Evasion](/techniques/T1497) <small style="color:#929393">(v2.0)</small>
* Virtualization/Sandbox Evasion: [System Checks](/techniques/T1497/001) <small style="color:#929393">(v3.0)</small>
* [Web Service](/techniques/T1102) <small style="color:#929393">(v1.3)</small>
* Web Service: [Bidirectional Communication](/techniques/T1102/002) <small style="color:#929393">(v1.1)</small>
* Web Service: [One-Way Communication](/techniques/T1102/003) <small style="color:#929393">(v1.1)</small>

### Mobile

#### Major Version Changes

* [Deliver Malicious Application via Other Means](/techniques/T1476) <small style="color:#929393">(v1.2&#8594;v2.0)</small>

#### Patches

* Encrypted Channel: [Asymmetric Cryptography](/techniques/T1521/002) <small style="color:#929393">(v1.0)</small>

### ICS

#### New Techniques

* [Command and Scripting Interpreter](/techniques/T1701) <small style="color:#929393">(v1.0)</small>
* Command and Scripting Interpreter: [JavaScript](/techniques/T1701/006) <small style="color:#929393">(v1.0)</small>
* Command and Scripting Interpreter: [PowerShell](/techniques/T1701/001) <small style="color:#929393">(v1.0)</small>
* Command and Scripting Interpreter: [Python](/techniques/T1701/005) <small style="color:#929393">(v1.0)</small>
* Command and Scripting Interpreter: [Unix Shell](/techniques/T1701/003) <small style="color:#929393">(v1.0)</small>
* Command and Scripting Interpreter: [Visual Basic](/techniques/T1701/004) <small style="color:#929393">(v1.0)</small>
* Command and Scripting Interpreter: [Windows Command Shell](/techniques/T1701/002) <small style="color:#929393">(v1.0)</small>
* Standard Application Layer Protocol: [DNS](/techniques/T0869/001) <small style="color:#929393">(v1.0)</small>
* Standard Application Layer Protocol: [Publish/Subscribe Protocols](/techniques/T0869/002) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* Unauthorized Message: [Command Message](/techniques/T1692/001) <small style="color:#929393">(v1.0&#8594;v2.0)</small>

#### Patches

* [Activate Firmware Update Mode](/techniques/T0800) <small style="color:#929393">(v1.0)</small>
* [Adversary-in-the-Middle](/techniques/T0830) <small style="color:#929393">(v2.0)</small>
* [Alarm Suppression](/techniques/T0878) <small style="color:#929393">(v1.2)</small>
* [Automated Collection](/techniques/T0802) <small style="color:#929393">(v1.1)</small>
* [Autorun Image](/techniques/T0895) <small style="color:#929393">(v1.0)</small>
* [Block Communications](/techniques/T1695) <small style="color:#929393">(v1.0)</small>
* Block Communications: [Ethernet](/techniques/T1695/002) <small style="color:#929393">(v1.0)</small>
* Block Communications: [Serial COM](/techniques/T1695/001) <small style="color:#929393">(v1.0)</small>
* Block Communications: [Wi-Fi](/techniques/T1695/003) <small style="color:#929393">(v1.0)</small>
* [Block Operational Technology Message](/techniques/T1691) <small style="color:#929393">(v1.0)</small>
* Block Operational Technology Message: [Command Message](/techniques/T1691/001) <small style="color:#929393">(v1.0)</small>
* Block Operational Technology Message: [Reporting Message](/techniques/T1691/002) <small style="color:#929393">(v1.0)</small>
* [Brute Force I/O](/techniques/T0806) <small style="color:#929393">(v1.1)</small>
* [Change Credential](/techniques/T0892) <small style="color:#929393">(v1.0)</small>
* [Change Operating Mode](/techniques/T0858) <small style="color:#929393">(v1.0)</small>
* [Commonly Used Port](/techniques/T0885) <small style="color:#929393">(v1.1)</small>
* [Connection Proxy](/techniques/T0884) <small style="color:#929393">(v1.1)</small>
* [Data Destruction](/techniques/T0809) <small style="color:#929393">(v1.0)</small>
* [Data from Information Repositories](/techniques/T0811) <small style="color:#929393">(v1.2)</small>
* [Data from Local System](/techniques/T0893) <small style="color:#929393">(v1.0)</small>
* [Denial of Service](/techniques/T0814) <small style="color:#929393">(v1.1)</small>
* [Detect Operating Mode](/techniques/T0868) <small style="color:#929393">(v1.0)</small>
* [Device Restart/Shutdown](/techniques/T0816) <small style="color:#929393">(v1.1)</small>
* [Drive-by Compromise](/techniques/T0817) <small style="color:#929393">(v1.0)</small>
* [Execution through API](/techniques/T0871) <small style="color:#929393">(v1.1)</small>
* [Exploit Public-Facing Application](/techniques/T0819) <small style="color:#929393">(v1.0)</small>
* [Exploitation for Evasion](/techniques/T0820) <small style="color:#929393">(v1.1)</small>
* [Exploitation for Privilege Escalation](/techniques/T0890) <small style="color:#929393">(v1.1)</small>
* [Exploitation of Remote Services](/techniques/T0866) <small style="color:#929393">(v1.0)</small>
* [External Remote Services](/techniques/T0822) <small style="color:#929393">(v1.1)</small>
* [Graphical User Interface](/techniques/T0823) <small style="color:#929393">(v1.1)</small>
* [Hooking](/techniques/T0874) <small style="color:#929393">(v1.2)</small>
* [I/O Image](/techniques/T0877) <small style="color:#929393">(v1.1)</small>
* [Indicator Removal on Host](/techniques/T0872) <small style="color:#929393">(v1.0)</small>
* [Insecure Credentials](/techniques/T1694) <small style="color:#929393">(v1.0)</small>
* Insecure Credentials: [Default Credentials](/techniques/T1694/001) <small style="color:#929393">(v1.0)</small>
* Insecure Credentials: [Hardcoded Credentials](/techniques/T1694/002) <small style="color:#929393">(v1.0)</small>
* [Internet Accessible Device](/techniques/T0883) <small style="color:#929393">(v1.0)</small>
* [Lateral Tool Transfer](/techniques/T0867) <small style="color:#929393">(v1.1)</small>
* [Manipulate I/O Image](/techniques/T0835) <small style="color:#929393">(v1.1)</small>
* [Masquerading](/techniques/T0849) <small style="color:#929393">(v1.1)</small>
* [Modify Alarm Settings](/techniques/T0838) <small style="color:#929393">(v1.2)</small>
* [Modify Controller Tasking](/techniques/T0821) <small style="color:#929393">(v1.2)</small>
* [Modify Firmware](/techniques/T1693) <small style="color:#929393">(v1.0)</small>
* Modify Firmware: [Module Firmware](/techniques/T1693/002) <small style="color:#929393">(v1.0)</small>
* Modify Firmware: [System Firmware](/techniques/T1693/001) <small style="color:#929393">(v1.0)</small>
* [Modify Parameter](/techniques/T0836) <small style="color:#929393">(v1.3)</small>
* [Modify Program](/techniques/T0889) <small style="color:#929393">(v1.2)</small>
* [Monitor Process State](/techniques/T0801) <small style="color:#929393">(v1.0)</small>
* [Native API](/techniques/T0834) <small style="color:#929393">(v1.0)</small>
* [Network Connection Enumeration](/techniques/T0840) <small style="color:#929393">(v1.2)</small>
* [Network Sniffing](/techniques/T0842) <small style="color:#929393">(v1.0)</small>
* [Point & Tag Identification](/techniques/T0861) <small style="color:#929393">(v1.1)</small>
* [Program Download](/techniques/T0843) <small style="color:#929393">(v1.1)</small>
* Program Download: [Download All](/techniques/T0843/001) <small style="color:#929393">(v1.0)</small>
* Program Download: [Online Edit](/techniques/T0843/002) <small style="color:#929393">(v1.0)</small>
* Program Download: [Program Append](/techniques/T0843/003) <small style="color:#929393">(v1.0)</small>
* [Program Upload](/techniques/T0845) <small style="color:#929393">(v1.0)</small>
* [Project File Infection](/techniques/T0873) <small style="color:#929393">(v1.1)</small>
* Project File Infection: [Siemens Project File Format](/techniques/T0873/001) <small style="color:#929393">(v1.0)</small>
* [Remote Services](/techniques/T0886) <small style="color:#929393">(v1.1)</small>
* [Remote System Discovery](/techniques/T0846) <small style="color:#929393">(v1.1)</small>
* Remote System Discovery: [Broadcast Discovery](/techniques/T0846/002) <small style="color:#929393">(v1.0)</small>
* Remote System Discovery: [Multicast Discovery](/techniques/T0846/003) <small style="color:#929393">(v1.0)</small>
* Remote System Discovery: [Port Scan](/techniques/T0846/001) <small style="color:#929393">(v1.0)</small>
* [Remote System Information Discovery](/techniques/T0888) <small style="color:#929393">(v1.1)</small>
* [Replication Through Removable Media](/techniques/T0847) <small style="color:#929393">(v1.0)</small>
* [Rogue Master](/techniques/T0848) <small style="color:#929393">(v1.2)</small>
* [Rootkit](/techniques/T0851) <small style="color:#929393">(v1.1)</small>
* [Screen Capture](/techniques/T0852) <small style="color:#929393">(v1.0)</small>
* [Service Stop](/techniques/T0881) <small style="color:#929393">(v1.1)</small>
* [Spearphishing Attachment](/techniques/T0865) <small style="color:#929393">(v1.1)</small>
* [Standard Application Layer Protocol](/techniques/T0869) <small style="color:#929393">(v1.0)</small>
* [Supply Chain Compromise](/techniques/T0862) <small style="color:#929393">(v1.1)</small>
* [System Binary Proxy Execution](/techniques/T0894) <small style="color:#929393">(v1.0)</small>
* [Transient Cyber Asset](/techniques/T0864) <small style="color:#929393">(v1.2)</small>
* [Unauthorized Message](/techniques/T1692) <small style="color:#929393">(v1.0)</small>
* Unauthorized Message: [Reporting Message](/techniques/T1692/002) <small style="color:#929393">(v1.0)</small>
* [User Execution](/techniques/T0863) <small style="color:#929393">(v1.1)</small>
* [Valid Accounts](/techniques/T0859) <small style="color:#929393">(v1.1)</small>
* [Wireless Compromise](/techniques/T0860) <small style="color:#929393">(v1.2)</small>
* [Wireless Sniffing](/techniques/T0887) <small style="color:#929393">(v1.1)</small>

#### Deprecations

* [Command-Line Interface](/techniques/T0807) <small style="color:#929393">(v1.1)</small>
* [Scripting](/techniques/T0853) <small style="color:#929393">(v1.0)</small>

## Software

### Enterprise

#### New Software

* [BACKUPOSINT v9.0 APEX PREDATOR](/software/S9045) <small style="color:#929393">(v1.0)</small>
* [CRASHPAD](/software/S9057) <small style="color:#929393">(v1.0)</small>
* [DCSYNCER.SLICK](/software/S9065) <small style="color:#929393">(v1.0)</small>
* [DEEPROOT](/software/S9063) <small style="color:#929393">(v1.0)</small>
* [IOControl](/software/S9046) <small style="color:#929393">(v1.0)</small>
* [LIGHTRAIL](/software/S9061) <small style="color:#929393">(v1.0)</small>
* [MiniBike](/software/S9059) <small style="color:#929393">(v1.0)</small>
* [MiniBrowse](/software/S9062) <small style="color:#929393">(v1.0)</small>
* [MiniBus](/software/S9060) <small style="color:#929393">(v1.0)</small>
* [MiniFast](/software/S9052) <small style="color:#929393">(v1.0)</small>
* [MiniJunk](/software/S9053) <small style="color:#929393">(v1.0)</small>
* [POLLBLEND](/software/S9066) <small style="color:#929393">(v1.0)</small>
* [SIGHTGRAB](/software/S9058) <small style="color:#929393">(v1.0)</small>
* [TRUSTTRAP](/software/S9064) <small style="color:#929393">(v1.0)</small>
* [TWOSTROKE](/software/S9067) <small style="color:#929393">(v1.0)</small>
* [The Gentlemen Ransomware](/software/S9051) <small style="color:#929393">(v1.0)</small>
* [Vidar](/software/S9050) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [StrongPity](/software/S0491) <small style="color:#929393">(v1.1&#8594;v2.0)</small>

### Mobile

#### New Software

* [NGate](/software/S9040) <small style="color:#929393">(v1.0)</small>
* [StrongPity](/software/S0491) <small style="color:#eb6635">(v2.0)</small>

#### Patches

* [Agent Smith](/software/S0440) <small style="color:#929393">(v1.0)</small>
* [Android/Chuli.A](/software/S0304) <small style="color:#929393">(v1.2)</small>
* [AndroidOS/MalLocker.B](/software/S0524) <small style="color:#929393">(v1.0)</small>
* [Anubis](/software/S0422) <small style="color:#929393">(v1.3)</small>
* [Asacub](/software/S0540) <small style="color:#929393">(v1.0)</small>
* [Cerberus](/software/S0480) <small style="color:#929393">(v1.1)</small>
* [Exobot](/software/S0522) <small style="color:#929393">(v1.0)</small>
* [FakeSpy](/software/S0509) <small style="color:#929393">(v1.0)</small>
* [GolfSpy](/software/S0421) <small style="color:#929393">(v1.0)</small>
* [Gustuff](/software/S0406) <small style="color:#929393">(v1.0)</small>
* [HenBox](/software/S0544) <small style="color:#929393">(v1.0)</small>
* [MazarBOT](/software/S0303) <small style="color:#929393">(v1.0)</small>
* [Pallas](/software/S0399) <small style="color:#929393">(v1.1)</small>
* [Red Alert 2.0](/software/S0539) <small style="color:#929393">(v1.0)</small>
* [RedDrop](/software/S0326) <small style="color:#929393">(v1.2)</small>
* [Riltok](/software/S0403) <small style="color:#929393">(v1.0)</small>
* [Rotexy](/software/S0411) <small style="color:#929393">(v1.1)</small>
* [RuMMS](/software/S0313) <small style="color:#929393">(v1.0)</small>
* [SimBad](/software/S0419) <small style="color:#929393">(v1.0)</small>
* [Tiktok Pro](/software/S0558) <small style="color:#929393">(v1.0)</small>
* [Twitoor](/software/S0302) <small style="color:#929393">(v2.0)</small>
* [ViceLeaker](/software/S0418) <small style="color:#929393">(v1.0)</small>
* [ViperRAT](/software/S0506) <small style="color:#929393">(v1.0)</small>
* [XLoader for Android](/software/S0318) <small style="color:#929393">(v2.0)</small>
* [XLoader for iOS](/software/S0490) <small style="color:#929393">(v1.1)</small>
* [YiSpecter](/software/S0311) <small style="color:#929393">(v2.0)</small>
* [ZergHelper](/software/S0287) <small style="color:#929393">(v1.0)</small>
* [eSurv](/software/S0507) <small style="color:#929393">(v1.1)</small>

### ICS

#### New Software

* [BACKUPOSINT v9.0 APEX PREDATOR](/software/S9045) <small style="color:#929393">(v1.0)</small>
* [IOControl](/software/S9046) <small style="color:#929393">(v1.0)</small>

## Groups

### Enterprise

#### New Groups

* [NIMBUS MANTICORE](/groups/G1059) <small style="color:#929393">(v1.0)</small>
* [The Gentlemen](/groups/G1058) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [APT38](/groups/G0082) <small style="color:#929393">(v3.1&#8594;v4.0)</small>
* [Salt Typhoon](/groups/G1045) <small style="color:#929393">(v1.0&#8594;v2.0)</small>

#### Minor Version Changes

* [APT42](/groups/G1044) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Gamaredon Group](/groups/G0047) <small style="color:#929393">(v3.3&#8594;v3.4)</small>

#### Patches

* [Dark Caracal](/groups/G0070) <small style="color:#929393">(v1.4)</small>
* [Scattered Spider](/groups/G1015) <small style="color:#929393">(v3.0)</small>
* [TeamPCP](/groups/G1056) <small style="color:#929393">(v1.0)</small>
* [Windshift](/groups/G0112) <small style="color:#929393">(v1.1)</small>

### Mobile

#### Patches

* [Bouncing Golf](/groups/G0097) <small style="color:#929393">(v1.0)</small>
* [Dark Caracal](/groups/G0070) <small style="color:#929393">(v1.4)</small>
* [Scattered Spider](/groups/G1015) <small style="color:#929393">(v3.0)</small>
* [Windshift](/groups/G0112) <small style="color:#929393">(v1.1)</small>

### ICS

#### Major Version Changes

* [APT38](/groups/G0082) <small style="color:#929393">(v3.1&#8594;v4.0)</small>

#### Minor Version Changes

* [CyberAv3ngers](/groups/G1027) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

## Campaigns

### Enterprise

#### New Campaigns

* [AI-Assisted Breach of Mexico's Government Infrastructure](/campaigns/C0064) <small style="color:#929393">(v1.0)</small>

#### Patches

* [Operation AkaiRyū](/campaigns/C0060) <small style="color:#929393">(v1.0)</small>
* [Salesforce Data Exfiltration](/campaigns/C0059) <small style="color:#929393">(v1.0)</small>

### ICS

#### New Campaigns

* [2026 U.S. Water Utilities Attacks](/campaigns/C0066) <small style="color:#929393">(v1.0)</small>
* [AI-Assisted Breach of Mexico's Government Infrastructure](/campaigns/C0064) <small style="color:#929393">(v1.0)</small>

## Assets

### ICS

#### Patches

* [Data Gateway](/assets/A0009) <small style="color:#929393">(v2.1)</small>
* [Firewall](/assets/A0016) <small style="color:#929393">(v1.1)</small>
* [Routers](/assets/A0014) <small style="color:#929393">(v2.1)</small>
* [Switch](/assets/A0015) <small style="color:#929393">(v1.1)</small>

## Mitigations

### Enterprise

#### Patches

* [Network Intrusion Prevention](/mitigations/M1031) <small style="color:#929393">(v1.0)</small>

### ICS

#### New Mitigations

* [Limit Software/Package Installation](/mitigations/M1061) <small style="color:#929393">(v1.0)</small>

#### Minor Version Changes

* [Disable or Remove Feature or Program](/mitigations/M0942) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Execution Prevention](/mitigations/M0938) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Exploit Protection](/mitigations/M0950) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Restrict Web-Based Content](/mitigations/M0921) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

## Data Components

### Enterprise

#### Minor Version Changes

* Application Log Content <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* Command Execution <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* File Access <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* File Creation <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* Host Status <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* Logon Session Creation <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Module Load <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* Network Connection Creation <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* Network Traffic Content <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* Network Traffic Flow <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* OS API Execution <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* Process Creation <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* Process Metadata <small style="color:#929393">(v2.1&#8594;v2.2)</small>

#### Patches

* Cloud Service Enumeration <small style="color:#929393">(v3.0)</small>
* Drive Creation <small style="color:#929393">(v2.0)</small>
* Driver Load <small style="color:#929393">(v2.0)</small>
* File Deletion <small style="color:#929393">(v3.0)</small>
* File Metadata <small style="color:#929393">(v2.1)</small>
* File Modification <small style="color:#929393">(v3.0)</small>
* Firewall Metadata <small style="color:#929393">(v2.0)</small>
* Firewall Rule Modification <small style="color:#929393">(v2.0)</small>
* Firmware Modification <small style="color:#929393">(v2.0)</small>
* Logon Session Metadata <small style="color:#929393">(v2.0)</small>
* Network Share Access <small style="color:#929393">(v2.0)</small>
* Process Access <small style="color:#929393">(v3.0)</small>
* Process Termination <small style="color:#929393">(v2.0)</small>
* Scheduled Job Creation <small style="color:#929393">(v3.0)</small>
* Script Execution <small style="color:#929393">(v2.0)</small>
* Service Creation <small style="color:#929393">(v2.0)</small>
* Service Metadata <small style="color:#929393">(v2.0)</small>
* User Account Authentication <small style="color:#929393">(v3.0)</small>
* User Account Modification <small style="color:#929393">(v2.0)</small>
* Windows Registry Key Modification <small style="color:#929393">(v2.0)</small>

### Mobile

#### Minor Version Changes

* Application Log Content <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* Application Permission <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* Application State <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Command Execution <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* File Access <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* File Creation <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* Host Status <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* Module Load <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* Network Connection Creation <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* Network Traffic Content <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* Network Traffic Flow <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* OS API Execution <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* Process Creation <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* Process Metadata <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* System Settings <small style="color:#929393">(v2.1&#8594;v2.2)</small>

#### Patches

* API Calls <small style="color:#929393">(v2.1)</small>
* Cloud Service Enumeration <small style="color:#929393">(v3.0)</small>
* File Deletion <small style="color:#929393">(v3.0)</small>
* File Metadata <small style="color:#929393">(v2.1)</small>
* File Modification <small style="color:#929393">(v3.0)</small>
* Network Communication <small style="color:#929393">(v2.1)</small>
* Permissions Request <small style="color:#929393">(v2.0)</small>
* Process Access <small style="color:#929393">(v3.0)</small>
* Process Termination <small style="color:#929393">(v2.0)</small>
* Protected Configuration <small style="color:#929393">(v2.1)</small>
* Scheduled Job Creation <small style="color:#929393">(v3.0)</small>
* System Notifications <small style="color:#929393">(v2.1)</small>
* User Account Authentication <small style="color:#929393">(v3.0)</small>

### ICS

#### Minor Version Changes

* Application Log Content <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* Command Execution <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* File Access <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* File Creation <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* Logon Session Creation <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Module Load <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* Network Connection Creation <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* Network Traffic Content <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* Network Traffic Flow <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* OS API Execution <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* Process Creation <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* Process Metadata <small style="color:#929393">(v2.1&#8594;v2.2)</small>

#### Patches

* Asset Inventory <small style="color:#929393">(v2.0)</small>
* Device Alarm <small style="color:#929393">(v2.0)</small>
* Drive Creation <small style="color:#929393">(v2.0)</small>
* File Deletion <small style="color:#929393">(v3.0)</small>
* File Metadata <small style="color:#929393">(v2.1)</small>
* File Modification <small style="color:#929393">(v3.0)</small>
* Firmware Modification <small style="color:#929393">(v2.0)</small>
* Logon Session Metadata <small style="color:#929393">(v2.0)</small>
* Network Share Access <small style="color:#929393">(v2.0)</small>
* Process History/Live Data <small style="color:#929393">(v2.1)</small>
* Process Termination <small style="color:#929393">(v2.0)</small>
* Process/Event Alarm <small style="color:#929393">(v2.1)</small>
* Scheduled Job Creation <small style="color:#929393">(v3.0)</small>
* Script Execution <small style="color:#929393">(v2.0)</small>
* Service Creation <small style="color:#929393">(v2.0)</small>
* Service Metadata <small style="color:#929393">(v2.0)</small>
* Software <small style="color:#929393">(v2.0)</small>
* User Account Authentication <small style="color:#929393">(v3.0)</small>
* Windows Registry Key Modification <small style="color:#929393">(v2.0)</small>

## Detection Strategies

### Enterprise

#### New Detection Strategies

* [Detect AI-Enabled Exfiltration](/detectionstrategies/DET0927) <small style="color:#929393">(v1.0)</small>
* [Detection of AI Result Poisoning](/detectionstrategies/DET0922) <small style="color:#929393">(v1.0)</small>
* [Detection of Anti-Automation Evasion](/detectionstrategies/DET0939) <small style="color:#929393">(v1.0)</small>
* [Detection of Automated CAPTCHA](/detectionstrategies/DET0937) <small style="color:#929393">(v1.0)</small>
* [Detection of Avoid CAPTCHA](/detectionstrategies/DET0938) <small style="color:#929393">(v1.0)</small>
* [Suspicious Acquisition and Use of Application-Specific Passwords](/detectionstrategies/DET0926) <small style="color:#929393">(v1.0)</small>

### ICS

#### New Detection Strategies

* [Behavioral Detection of Command and Scripting Abuse in ICS](/detectionstrategies/DET0928) <small style="color:#929393">(v1.0)</small>
* [Behavioral Detection of DNS Protocol Misuse for Command and Control](/detectionstrategies/DET0934) <small style="color:#929393">(v1.0)</small>
* [Behavioral Detection of JavaScript Execution in ICS](/detectionstrategies/DET0936) <small style="color:#929393">(v1.0)</small>
* [Behavioral Detection of PowerShell Execution in ICS](/detectionstrategies/DET0929) <small style="color:#929393">(v1.0)</small>
* [Behavioral Detection of Publish/Subscribe Protocol Misuse for Command and Control](/detectionstrategies/DET0935) <small style="color:#929393">(v1.0)</small>
* [Behavioral Detection of Python Execution in ICS](/detectionstrategies/DET0933) <small style="color:#929393">(v1.0)</small>
* [Behavioral Detection of Unix Shell Execution in ICS](/detectionstrategies/DET0931) <small style="color:#929393">(v1.0)</small>
* [Behavioral Detection of Visual Basic Execution in ICS](/detectionstrategies/DET0932) <small style="color:#929393">(v1.0)</small>
* [Behavioral Detection of Windows Command Shell Execution in ICS](/detectionstrategies/DET0930) <small style="color:#929393">(v1.0)</small>

#### Patches

* [Detection of Activate Firmware Update Mode](/detectionstrategies/DET0802) <small style="color:#929393">(v1.0)</small>
* [Detection of Adversary-in-the-Middle](/detectionstrategies/DET0764) <small style="color:#929393">(v1.0)</small>
* [Detection of Alarm Suppression](/detectionstrategies/DET0728) <small style="color:#929393">(v1.0)</small>
* [Detection of Automated Collection](/detectionstrategies/DET0734) <small style="color:#929393">(v1.0)</small>
* [Detection of Autorun Image](/detectionstrategies/DET0748) <small style="color:#929393">(v1.0)</small>
* [Detection of Block Command Message](/detectionstrategies/DET0784) <small style="color:#929393">(v1.0)</small>
* [Detection of Block Communications](/detectionstrategies/DET0910) <small style="color:#929393">(v1.0)</small>
* [Detection of Block Ethernet](/detectionstrategies/DET0911) <small style="color:#929393">(v1.0)</small>
* [Detection of Block Operational Technology Message](/detectionstrategies/DET0903) <small style="color:#929393">(v1.0)</small>
* [Detection of Block Reporting Message](/detectionstrategies/DET0789) <small style="color:#929393">(v1.0)</small>
* [Detection of Block Serial COM](/detectionstrategies/DET0797) <small style="color:#929393">(v1.0)</small>
* [Detection of Block Wi-Fi](/detectionstrategies/DET0912) <small style="color:#929393">(v1.0)</small>
* [Detection of Broadcast Discovery](/detectionstrategies/DET0908) <small style="color:#929393">(v1.0)</small>
* [Detection of Brute Force I/O](/detectionstrategies/DET0737) <small style="color:#929393">(v1.0)</small>
* [Detection of Change Credential](/detectionstrategies/DET0771) <small style="color:#929393">(v1.0)</small>
* [Detection of Commonly Used Port](/detectionstrategies/DET0736) <small style="color:#929393">(v1.0)</small>
* [Detection of Connection Proxy](/detectionstrategies/DET0759) <small style="color:#929393">(v1.0)</small>
* [Detection of Data Destruction](/detectionstrategies/DET0758) <small style="color:#929393">(v1.0)</small>
* [Detection of Data from Information Repositories](/detectionstrategies/DET0754) <small style="color:#929393">(v1.0)</small>
* [Detection of Data from Local System](/detectionstrategies/DET0749) <small style="color:#929393">(v1.0)</small>
* [Detection of Default Credentials](/detectionstrategies/DET0756) <small style="color:#929393">(v1.0)</small>
* [Detection of Denial of Service](/detectionstrategies/DET0723) <small style="color:#929393">(v1.0)</small>
* [Detection of Device Restart/Shutdown](/detectionstrategies/DET0801) <small style="color:#929393">(v1.0)</small>
* [Detection of Drive-by Compromise](/detectionstrategies/DET0782) <small style="color:#929393">(v1.0)</small>
* [Detection of Execution through API](/detectionstrategies/DET0742) <small style="color:#929393">(v1.0)</small>
* [Detection of Exploit Public-Facing Application](/detectionstrategies/DET0740) <small style="color:#929393">(v1.0)</small>
* [Detection of Exploitation for Evasion](/detectionstrategies/DET0795) <small style="color:#929393">(v1.0)</small>
* [Detection of Exploitation for Privilege Escalation](/detectionstrategies/DET0738) <small style="color:#929393">(v1.0)</small>
* [Detection of Exploitation of Remote Services](/detectionstrategies/DET0767) <small style="color:#929393">(v1.0)</small>
* [Detection of External Remote Services](/detectionstrategies/DET0803) <small style="color:#929393">(v1.0)</small>
* [Detection of Graphical User Interface](/detectionstrategies/DET0772) <small style="color:#929393">(v1.0)</small>
* [Detection of Hooking](/detectionstrategies/DET0722) <small style="color:#929393">(v1.0)</small>
* [Detection of Indicator Removal on Host](/detectionstrategies/DET0750) <small style="color:#929393">(v1.0)</small>
* [Detection of Insecure Credentials](/detectionstrategies/DET0905) <small style="color:#929393">(v1.0)</small>
* [Detection of Internet Accessible Device](/detectionstrategies/DET0796) <small style="color:#929393">(v1.0)</small>
* [Detection of Lateral Tool Transfer](/detectionstrategies/DET0745) <small style="color:#929393">(v1.0)</small>
* [Detection of Masquerading](/detectionstrategies/DET0725) <small style="color:#929393">(v1.0)</small>
* [Detection of Modify Alarm Settings](/detectionstrategies/DET0777) <small style="color:#929393">(v1.0)</small>
* [Detection of Modify Parameter](/detectionstrategies/DET0776) <small style="color:#929393">(v1.0)</small>
* [Detection of Monitor Process State](/detectionstrategies/DET0727) <small style="color:#929393">(v1.0)</small>
* [Detection of Multicast Discovery](/detectionstrategies/DET0909) <small style="color:#929393">(v1.0)</small>
* [Detection of Native API](/detectionstrategies/DET0753) <small style="color:#929393">(v1.0)</small>
* [Detection of Network Connection Enumeration](/detectionstrategies/DET0770) <small style="color:#929393">(v1.0)</small>
* [Detection of Network Sniffing](/detectionstrategies/DET0800) <small style="color:#929393">(v1.0)</small>
* [Detection of Point & Tag Identification](/detectionstrategies/DET0788) <small style="color:#929393">(v1.0)</small>
* [Detection of Port Scan](/detectionstrategies/DET0907) <small style="color:#929393">(v1.0)</small>
* [Detection of Project File Infection](/detectionstrategies/DET0766) <small style="color:#929393">(v1.0)</small>
* [Detection of Remote Services](/detectionstrategies/DET0804) <small style="color:#929393">(v1.0)</small>
* [Detection of Remote System Discovery](/detectionstrategies/DET0739) <small style="color:#929393">(v1.0)</small>
* [Detection of Remote System Information Discovery](/detectionstrategies/DET0787) <small style="color:#929393">(v1.0)</small>
* [Detection of Replication Through Removable Media](/detectionstrategies/DET0733) <small style="color:#929393">(v1.0)</small>
* [Detection of Rogue Master](/detectionstrategies/DET0792) <small style="color:#929393">(v1.0)</small>
* [Detection of Rootkit](/detectionstrategies/DET0780) <small style="color:#929393">(v1.0)</small>
* [Detection of Screen Capture](/detectionstrategies/DET0751) <small style="color:#929393">(v1.0)</small>
* [Detection of Service Stop](/detectionstrategies/DET0765) <small style="color:#929393">(v1.0)</small>
* [Detection of Siemens Project File Format Infection](/detectionstrategies/DET0906) <small style="color:#929393">(v1.0)</small>
* [Detection of Spearphishing Attachment](/detectionstrategies/DET0781) <small style="color:#929393">(v1.0)</small>
* [Detection of Spoof Reporting Message](/detectionstrategies/DET0746) <small style="color:#929393">(v1.0)</small>
* [Detection of Standard Application Layer Protocol](/detectionstrategies/DET0799) <small style="color:#929393">(v1.0)</small>
* [Detection of Supply Chain Compromise](/detectionstrategies/DET0730) <small style="color:#929393">(v1.0)</small>
* [Detection of System Binary Proxy Execution](/detectionstrategies/DET0793) <small style="color:#929393">(v1.0)</small>
* [Detection of System Firmware](/detectionstrategies/DET0731) <small style="color:#929393">(v1.0)</small>
* [Detection of Transient Cyber Asset](/detectionstrategies/DET0744) <small style="color:#929393">(v1.0)</small>
* [Detection of Unauthorized Command Message](/detectionstrategies/DET0794) <small style="color:#929393">(v1.0)</small>
* [Detection of Unauthorized Message](/detectionstrategies/DET0902) <small style="color:#929393">(v1.0)</small>
* [Detection of User Execution](/detectionstrategies/DET0791) <small style="color:#929393">(v1.0)</small>
* [Detection of Valid Accounts](/detectionstrategies/DET0724) <small style="color:#929393">(v1.0)</small>
* [Detection of Wireless Compromise](/detectionstrategies/DET0726) <small style="color:#929393">(v1.0)</small>
* [Detection of Wireless Sniffing](/detectionstrategies/DET0743) <small style="color:#929393">(v1.0)</small>

## Analytics

### Enterprise

#### New Analytics

* [Analytic 2068](/detectionstrategies/DET0922) <small style="color:#929393">(v1.0)</small>
* [Analytic 2070](/detectionstrategies/DET0923) <small style="color:#929393">(v1.0)</small>
* [Analytic 2074](/detectionstrategies/DET0925) <small style="color:#929393">(v1.0)</small>
* [Analytic 2075](/detectionstrategies/DET0926) <small style="color:#929393">(v1.0)</small>
* [Analytic 2076](/detectionstrategies/DET0926) <small style="color:#929393">(v1.0)</small>
* [Analytic 2077](/detectionstrategies/DET0926) <small style="color:#929393">(v1.0)</small>
* [Analytic 2078](/detectionstrategies/DET0927) <small style="color:#929393">(v1.0)</small>
* [Analytic 2079](/detectionstrategies/DET0927) <small style="color:#929393">(v1.0)</small>
* [Analytic 2080](/detectionstrategies/DET0927) <small style="color:#929393">(v1.0)</small>
* [Analytic 2104](/detectionstrategies/DET0937) <small style="color:#929393">(v1.0)</small>
* [Analytic 2105](/detectionstrategies/DET0938) <small style="color:#929393">(v1.0)</small>
* [Analytic 2106](/detectionstrategies/DET0939) <small style="color:#929393">(v1.0)</small>

#### Minor Version Changes

* [Analytic 0339](/detectionstrategies/DET0120) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Patches

* [Analytic 1952](/detectionstrategies/DET0820) <small style="color:#929393">(v1.0)</small>
* [Analytic 1958](/detectionstrategies/DET0826) <small style="color:#929393">(v1.0)</small>
* [Analytic 1961](/detectionstrategies/DET0829) <small style="color:#929393">(v1.0)</small>
* [Analytic 1970](/detectionstrategies/DET0838) <small style="color:#929393">(v1.0)</small>
* [Analytic 1986](/detectionstrategies/DET0854) <small style="color:#929393">(v1.0)</small>
* [Analytic 1991](/detectionstrategies/DET0859) <small style="color:#929393">(v1.0)</small>
* [Analytic 1996](/detectionstrategies/DET0864) <small style="color:#929393">(v1.0)</small>
* [Analytic 2003](/detectionstrategies/DET0871) <small style="color:#929393">(v1.0)</small>
* [Analytic 2006](/detectionstrategies/DET0874) <small style="color:#929393">(v1.0)</small>
* [Analytic 2014](/detectionstrategies/DET0882) <small style="color:#929393">(v1.0)</small>
* [Analytic 2017](/detectionstrategies/DET0885) <small style="color:#929393">(v1.0)</small>
* [Analytic 2019](/detectionstrategies/DET0887) <small style="color:#929393">(v1.0)</small>
* [Analytic 2020](/detectionstrategies/DET0888) <small style="color:#929393">(v1.0)</small>
* [Analytic 2024](/detectionstrategies/DET0892) <small style="color:#929393">(v1.0)</small>
* [Analytic 2027](/detectionstrategies/DET0895) <small style="color:#929393">(v1.0)</small>
* [Analytic 2028](/detectionstrategies/DET0896) <small style="color:#929393">(v1.0)</small>

### Mobile

#### Minor Version Changes

* [Analytic 1673](/detectionstrategies/DET0616) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1674](/detectionstrategies/DET0616) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1679](/detectionstrategies/DET0619) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1680](/detectionstrategies/DET0619) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1685](/detectionstrategies/DET0622) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1686](/detectionstrategies/DET0622) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1703](/detectionstrategies/DET0632) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1704](/detectionstrategies/DET0632) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1705](/detectionstrategies/DET0633) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1745](/detectionstrategies/DET0657) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1746](/detectionstrategies/DET0657) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1757](/detectionstrategies/DET0664) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1835](/detectionstrategies/DET0710) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1836](/detectionstrategies/DET0710) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Patches

* [Analytic 1644](/detectionstrategies/DET0598) <small style="color:#929393">(v1.1)</small>
* [Analytic 1646](/detectionstrategies/DET0600) <small style="color:#929393">(v1.1)</small>
* [Analytic 1647](/detectionstrategies/DET0600) <small style="color:#929393">(v1.1)</small>
* [Analytic 1648](/detectionstrategies/DET0601) <small style="color:#929393">(v1.1)</small>
* [Analytic 1649](/detectionstrategies/DET0601) <small style="color:#929393">(v1.1)</small>
* [Analytic 1650](/detectionstrategies/DET0602) <small style="color:#929393">(v2.0)</small>
* [Analytic 1651](/detectionstrategies/DET0602) <small style="color:#929393">(v1.0)</small>
* [Analytic 1652](/detectionstrategies/DET0603) <small style="color:#929393">(v1.1)</small>
* [Analytic 1653](/detectionstrategies/DET0604) <small style="color:#929393">(v1.1)</small>
* [Analytic 1654](/detectionstrategies/DET0604) <small style="color:#929393">(v1.1)</small>
* [Analytic 1655](/detectionstrategies/DET0605) <small style="color:#929393">(v1.0)</small>
* [Analytic 1656](/detectionstrategies/DET0606) <small style="color:#929393">(v1.0)</small>
* [Analytic 1657](/detectionstrategies/DET0607) <small style="color:#929393">(v1.1)</small>
* [Analytic 1658](/detectionstrategies/DET0607) <small style="color:#929393">(v1.1)</small>
* [Analytic 1659](/detectionstrategies/DET0608) <small style="color:#929393">(v1.0)</small>
* [Analytic 1660](/detectionstrategies/DET0608) <small style="color:#929393">(v1.0)</small>
* [Analytic 1661](/detectionstrategies/DET0609) <small style="color:#929393">(v1.0)</small>
* [Analytic 1662](/detectionstrategies/DET0609) <small style="color:#929393">(v1.0)</small>
* [Analytic 1663](/detectionstrategies/DET0610) <small style="color:#929393">(v1.1)</small>
* [Analytic 1664](/detectionstrategies/DET0610) <small style="color:#929393">(v1.1)</small>
* [Analytic 1665](/detectionstrategies/DET0611) <small style="color:#929393">(v1.1)</small>
* [Analytic 1666](/detectionstrategies/DET0612) <small style="color:#929393">(v1.1)</small>
* [Analytic 1667](/detectionstrategies/DET0613) <small style="color:#929393">(v1.0)</small>
* [Analytic 1668](/detectionstrategies/DET0613) <small style="color:#929393">(v1.0)</small>
* [Analytic 1669](/detectionstrategies/DET0614) <small style="color:#929393">(v1.1)</small>
* [Analytic 1670](/detectionstrategies/DET0614) <small style="color:#929393">(v1.1)</small>
* [Analytic 1675](/detectionstrategies/DET0617) <small style="color:#929393">(v1.1)</small>
* [Analytic 1676](/detectionstrategies/DET0617) <small style="color:#929393">(v1.1)</small>
* [Analytic 1677](/detectionstrategies/DET0618) <small style="color:#929393">(v1.1)</small>
* [Analytic 1678](/detectionstrategies/DET0618) <small style="color:#929393">(v1.1)</small>
* [Analytic 1681](/detectionstrategies/DET0620) <small style="color:#929393">(v1.1)</small>
* [Analytic 1682](/detectionstrategies/DET0620) <small style="color:#929393">(v1.1)</small>
* [Analytic 1683](/detectionstrategies/DET0621) <small style="color:#929393">(v1.1)</small>
* [Analytic 1684](/detectionstrategies/DET0621) <small style="color:#929393">(v1.1)</small>
* [Analytic 1687](/detectionstrategies/DET0623) <small style="color:#929393">(v1.0)</small>
* [Analytic 1688](/detectionstrategies/DET0623) <small style="color:#929393">(v1.0)</small>
* [Analytic 1689](/detectionstrategies/DET0624) <small style="color:#929393">(v1.0)</small>
* [Analytic 1690](/detectionstrategies/DET0624) <small style="color:#929393">(v1.0)</small>
* [Analytic 1691](/detectionstrategies/DET0625) <small style="color:#929393">(v1.0)</small>
* [Analytic 1692](/detectionstrategies/DET0625) <small style="color:#929393">(v1.0)</small>
* [Analytic 1693](/detectionstrategies/DET0626) <small style="color:#929393">(v2.0)</small>
* [Analytic 1694](/detectionstrategies/DET0626) <small style="color:#929393">(v2.0)</small>
* [Analytic 1695](/detectionstrategies/DET0627) <small style="color:#929393">(v1.0)</small>
* [Analytic 1696](/detectionstrategies/DET0627) <small style="color:#929393">(v1.0)</small>
* [Analytic 1697](/detectionstrategies/DET0628) <small style="color:#929393">(v1.1)</small>
* [Analytic 1698](/detectionstrategies/DET0628) <small style="color:#929393">(v1.1)</small>
* [Analytic 1699](/detectionstrategies/DET0629) <small style="color:#929393">(v1.0)</small>
* [Analytic 1700](/detectionstrategies/DET0629) <small style="color:#929393">(v1.0)</small>
* [Analytic 1701](/detectionstrategies/DET0630) <small style="color:#929393">(v1.1)</small>
* [Analytic 1702](/detectionstrategies/DET0631) <small style="color:#929393">(v1.1)</small>
* [Analytic 1706](/detectionstrategies/DET0634) <small style="color:#929393">(v1.1)</small>
* [Analytic 1707](/detectionstrategies/DET0634) <small style="color:#929393">(v1.0)</small>
* [Analytic 1708](/detectionstrategies/DET0635) <small style="color:#929393">(v2.0)</small>
* [Analytic 1709](/detectionstrategies/DET0635) <small style="color:#929393">(v1.0)</small>
* [Analytic 1710](/detectionstrategies/DET0636) <small style="color:#929393">(v1.1)</small>
* [Analytic 1711](/detectionstrategies/DET0637) <small style="color:#929393">(v1.1)</small>
* [Analytic 1712](/detectionstrategies/DET0638) <small style="color:#929393">(v1.1)</small>
* [Analytic 1713](/detectionstrategies/DET0639) <small style="color:#929393">(v1.1)</small>
* [Analytic 1714](/detectionstrategies/DET0639) <small style="color:#929393">(v1.1)</small>
* [Analytic 1715](/detectionstrategies/DET0640) <small style="color:#929393">(v1.1)</small>
* [Analytic 1716](/detectionstrategies/DET0641) <small style="color:#929393">(v1.1)</small>
* [Analytic 1718](/detectionstrategies/DET0642) <small style="color:#929393">(v1.1)</small>
* [Analytic 1719](/detectionstrategies/DET0643) <small style="color:#929393">(v1.1)</small>
* [Analytic 1720](/detectionstrategies/DET0643) <small style="color:#929393">(v1.1)</small>
* [Analytic 1721](/detectionstrategies/DET0644) <small style="color:#929393">(v1.1)</small>
* [Analytic 1722](/detectionstrategies/DET0644) <small style="color:#929393">(v1.1)</small>
* [Analytic 1723](/detectionstrategies/DET0645) <small style="color:#929393">(v1.1)</small>
* [Analytic 1724](/detectionstrategies/DET0645) <small style="color:#929393">(v1.1)</small>
* [Analytic 1725](/detectionstrategies/DET0646) <small style="color:#929393">(v1.1)</small>
* [Analytic 1726](/detectionstrategies/DET0646) <small style="color:#929393">(v1.1)</small>
* [Analytic 1727](/detectionstrategies/DET0647) <small style="color:#929393">(v1.1)</small>
* [Analytic 1730](/detectionstrategies/DET0649) <small style="color:#929393">(v1.1)</small>
* [Analytic 1733](/detectionstrategies/DET0651) <small style="color:#929393">(v1.1)</small>
* [Analytic 1734](/detectionstrategies/DET0651) <small style="color:#929393">(v1.1)</small>
* [Analytic 1735](/detectionstrategies/DET0652) <small style="color:#929393">(v1.0)</small>
* [Analytic 1736](/detectionstrategies/DET0652) <small style="color:#929393">(v1.0)</small>
* [Analytic 1737](/detectionstrategies/DET0653) <small style="color:#929393">(v1.1)</small>
* [Analytic 1738](/detectionstrategies/DET0653) <small style="color:#929393">(v1.1)</small>
* [Analytic 1739](/detectionstrategies/DET0654) <small style="color:#929393">(v1.1)</small>
* [Analytic 1740](/detectionstrategies/DET0654) <small style="color:#929393">(v1.1)</small>
* [Analytic 1741](/detectionstrategies/DET0655) <small style="color:#929393">(v1.1)</small>
* [Analytic 1742](/detectionstrategies/DET0655) <small style="color:#929393">(v1.1)</small>
* [Analytic 1743](/detectionstrategies/DET0656) <small style="color:#929393">(v1.1)</small>
* [Analytic 1744](/detectionstrategies/DET0656) <small style="color:#929393">(v1.0)</small>
* [Analytic 1747](/detectionstrategies/DET0658) <small style="color:#929393">(v1.1)</small>
* [Analytic 1748](/detectionstrategies/DET0658) <small style="color:#929393">(v1.1)</small>
* [Analytic 1750](/detectionstrategies/DET0660) <small style="color:#929393">(v1.0)</small>
* [Analytic 1751](/detectionstrategies/DET0661) <small style="color:#929393">(v1.1)</small>
* [Analytic 1752](/detectionstrategies/DET0661) <small style="color:#929393">(v1.1)</small>
* [Analytic 1753](/detectionstrategies/DET0662) <small style="color:#929393">(v1.1)</small>
* [Analytic 1754](/detectionstrategies/DET0662) <small style="color:#929393">(v1.1)</small>
* [Analytic 1755](/detectionstrategies/DET0663) <small style="color:#929393">(v1.1)</small>
* [Analytic 1756](/detectionstrategies/DET0663) <small style="color:#929393">(v1.1)</small>
* [Analytic 1758](/detectionstrategies/DET0665) <small style="color:#929393">(v1.1)</small>
* [Analytic 1759](/detectionstrategies/DET0665) <small style="color:#929393">(v1.1)</small>
* [Analytic 1760](/detectionstrategies/DET0666) <small style="color:#929393">(v1.0)</small>
* [Analytic 1761](/detectionstrategies/DET0666) <small style="color:#929393">(v1.0)</small>
* [Analytic 1762](/detectionstrategies/DET0667) <small style="color:#929393">(v1.1)</small>
* [Analytic 1764](/detectionstrategies/DET0668) <small style="color:#929393">(v1.1)</small>
* [Analytic 1765](/detectionstrategies/DET0669) <small style="color:#929393">(v1.0)</small>
* [Analytic 1766](/detectionstrategies/DET0669) <small style="color:#929393">(v1.0)</small>
* [Analytic 1767](/detectionstrategies/DET0670) <small style="color:#929393">(v1.1)</small>
* [Analytic 1768](/detectionstrategies/DET0670) <small style="color:#929393">(v1.1)</small>
* [Analytic 1769](/detectionstrategies/DET0671) <small style="color:#929393">(v1.0)</small>
* [Analytic 1770](/detectionstrategies/DET0672) <small style="color:#929393">(v1.1)</small>
* [Analytic 1771](/detectionstrategies/DET0672) <small style="color:#929393">(v1.1)</small>
* [Analytic 1772](/detectionstrategies/DET0673) <small style="color:#929393">(v1.1)</small>
* [Analytic 1773](/detectionstrategies/DET0673) <small style="color:#929393">(v1.1)</small>
* [Analytic 1774](/detectionstrategies/DET0674) <small style="color:#929393">(v2.0)</small>
* [Analytic 1775](/detectionstrategies/DET0674) <small style="color:#929393">(v1.0)</small>
* [Analytic 1776](/detectionstrategies/DET0675) <small style="color:#929393">(v1.1)</small>
* [Analytic 1777](/detectionstrategies/DET0675) <small style="color:#929393">(v1.1)</small>
* [Analytic 1778](/detectionstrategies/DET0676) <small style="color:#929393">(v1.1)</small>
* [Analytic 1779](/detectionstrategies/DET0676) <small style="color:#929393">(v1.1)</small>
* [Analytic 1780](/detectionstrategies/DET0677) <small style="color:#929393">(v1.1)</small>
* [Analytic 1781](/detectionstrategies/DET0678) <small style="color:#929393">(v1.1)</small>
* [Analytic 1782](/detectionstrategies/DET0679) <small style="color:#929393">(v2.0)</small>
* [Analytic 1783](/detectionstrategies/DET0679) <small style="color:#929393">(v1.0)</small>
* [Analytic 1784](/detectionstrategies/DET0680) <small style="color:#929393">(v1.1)</small>
* [Analytic 1785](/detectionstrategies/DET0680) <small style="color:#929393">(v1.1)</small>
* [Analytic 1786](/detectionstrategies/DET0681) <small style="color:#929393">(v1.0)</small>
* [Analytic 1787](/detectionstrategies/DET0681) <small style="color:#929393">(v1.0)</small>
* [Analytic 1788](/detectionstrategies/DET0682) <small style="color:#929393">(v1.1)</small>
* [Analytic 1789](/detectionstrategies/DET0682) <small style="color:#929393">(v1.1)</small>
* [Analytic 1790](/detectionstrategies/DET0683) <small style="color:#929393">(v1.0)</small>
* [Analytic 1791](/detectionstrategies/DET0684) <small style="color:#929393">(v1.0)</small>
* [Analytic 1792](/detectionstrategies/DET0684) <small style="color:#929393">(v1.0)</small>
* [Analytic 1793](/detectionstrategies/DET0685) <small style="color:#929393">(v1.1)</small>
* [Analytic 1794](/detectionstrategies/DET0685) <small style="color:#929393">(v1.1)</small>
* [Analytic 1795](/detectionstrategies/DET0686) <small style="color:#929393">(v2.0)</small>
* [Analytic 1796](/detectionstrategies/DET0686) <small style="color:#929393">(v1.0)</small>
* [Analytic 1797](/detectionstrategies/DET0687) <small style="color:#929393">(v1.1)</small>
* [Analytic 1798](/detectionstrategies/DET0688) <small style="color:#929393">(v1.0)</small>
* [Analytic 1799](/detectionstrategies/DET0688) <small style="color:#929393">(v1.0)</small>
* [Analytic 1800](/detectionstrategies/DET0689) <small style="color:#929393">(v1.1)</small>
* [Analytic 1801](/detectionstrategies/DET0690) <small style="color:#929393">(v1.1)</small>
* [Analytic 1802](/detectionstrategies/DET0691) <small style="color:#929393">(v1.1)</small>
* [Analytic 1803](/detectionstrategies/DET0691) <small style="color:#929393">(v1.1)</small>
* [Analytic 1804](/detectionstrategies/DET0692) <small style="color:#929393">(v1.1)</small>
* [Analytic 1805](/detectionstrategies/DET0692) <small style="color:#929393">(v1.1)</small>
* [Analytic 1806](/detectionstrategies/DET0693) <small style="color:#929393">(v1.1)</small>
* [Analytic 1807](/detectionstrategies/DET0694) <small style="color:#929393">(v1.1)</small>
* [Analytic 1812](/detectionstrategies/DET0697) <small style="color:#929393">(v1.1)</small>
* [Analytic 1815](/detectionstrategies/DET0699) <small style="color:#929393">(v1.1)</small>
* [Analytic 1816](/detectionstrategies/DET0700) <small style="color:#929393">(v1.1)</small>
* [Analytic 1817](/detectionstrategies/DET0700) <small style="color:#929393">(v1.1)</small>
* [Analytic 1820](/detectionstrategies/DET0702) <small style="color:#929393">(v1.1)</small>
* [Analytic 1821](/detectionstrategies/DET0702) <small style="color:#929393">(v1.1)</small>
* [Analytic 1822](/detectionstrategies/DET0703) <small style="color:#929393">(v1.1)</small>
* [Analytic 1823](/detectionstrategies/DET0704) <small style="color:#929393">(v1.1)</small>
* [Analytic 1824](/detectionstrategies/DET0704) <small style="color:#929393">(v1.1)</small>
* [Analytic 1825](/detectionstrategies/DET0705) <small style="color:#929393">(v1.1)</small>
* [Analytic 1826](/detectionstrategies/DET0705) <small style="color:#929393">(v1.1)</small>
* [Analytic 1827](/detectionstrategies/DET0706) <small style="color:#929393">(v1.1)</small>
* [Analytic 1828](/detectionstrategies/DET0706) <small style="color:#929393">(v1.1)</small>
* [Analytic 1829](/detectionstrategies/DET0707) <small style="color:#929393">(v1.1)</small>
* [Analytic 1830](/detectionstrategies/DET0707) <small style="color:#929393">(v1.1)</small>
* [Analytic 1831](/detectionstrategies/DET0708) <small style="color:#929393">(v1.0)</small>
* [Analytic 1832](/detectionstrategies/DET0708) <small style="color:#929393">(v1.0)</small>
* [Analytic 1833](/detectionstrategies/DET0709) <small style="color:#929393">(v1.0)</small>
* [Analytic 1834](/detectionstrategies/DET0709) <small style="color:#929393">(v1.0)</small>
* [Analytic 1837](/detectionstrategies/DET0711) <small style="color:#929393">(v1.1)</small>
* [Analytic 1838](/detectionstrategies/DET0712) <small style="color:#929393">(v1.0)</small>
* [Analytic 1839](/detectionstrategies/DET0712) <small style="color:#929393">(v1.0)</small>
* [Analytic 1840](/detectionstrategies/DET0713) <small style="color:#929393">(v1.1)</small>
* [Analytic 1841](/detectionstrategies/DET0713) <small style="color:#929393">(v1.1)</small>
* [Analytic 1842](/detectionstrategies/DET0714) <small style="color:#929393">(v1.1)</small>
* [Analytic 1843](/detectionstrategies/DET0715) <small style="color:#929393">(v1.0)</small>
* [Analytic 1844](/detectionstrategies/DET0715) <small style="color:#929393">(v1.0)</small>
* [Analytic 1845](/detectionstrategies/DET0716) <small style="color:#929393">(v1.0)</small>
* [Analytic 1846](/detectionstrategies/DET0716) <small style="color:#929393">(v1.0)</small>
* [Analytic 1847](/detectionstrategies/DET0717) <small style="color:#929393">(v1.1)</small>
* [Analytic 1848](/detectionstrategies/DET0718) <small style="color:#929393">(v1.1)</small>
* [Analytic 1849](/detectionstrategies/DET0718) <small style="color:#929393">(v1.1)</small>
* [Analytic 1850](/detectionstrategies/DET0719) <small style="color:#929393">(v1.1)</small>
* [Analytic 1851](/detectionstrategies/DET0720) <small style="color:#929393">(v1.1)</small>
* [Analytic 1852](/detectionstrategies/DET0720) <small style="color:#929393">(v1.1)</small>
* [Analytic 1853](/detectionstrategies/DET0721) <small style="color:#929393">(v1.1)</small>
* [Analytic 1854](/detectionstrategies/DET0721) <small style="color:#929393">(v1.1)</small>

### ICS

#### New Analytics

* [Analytic 2082](/detectionstrategies/DET0928) <small style="color:#929393">(v1.0)</small>
* [Analytic 2083](/detectionstrategies/DET0928) <small style="color:#929393">(v1.0)</small>
* [Analytic 2084](/detectionstrategies/DET0928) <small style="color:#929393">(v1.0)</small>
* [Analytic 2085](/detectionstrategies/DET0928) <small style="color:#929393">(v1.0)</small>
* [Analytic 2086](/detectionstrategies/DET0929) <small style="color:#929393">(v1.0)</small>
* [Analytic 2087](/detectionstrategies/DET0930) <small style="color:#929393">(v1.0)</small>
* [Analytic 2088](/detectionstrategies/DET0931) <small style="color:#929393">(v1.0)</small>
* [Analytic 2089](/detectionstrategies/DET0931) <small style="color:#929393">(v1.0)</small>
* [Analytic 2090](/detectionstrategies/DET0931) <small style="color:#929393">(v1.0)</small>
* [Analytic 2091](/detectionstrategies/DET0932) <small style="color:#929393">(v1.0)</small>
* [Analytic 2092](/detectionstrategies/DET0936) <small style="color:#929393">(v1.0)</small>
* [Analytic 2093](/detectionstrategies/DET0936) <small style="color:#929393">(v1.0)</small>
* [Analytic 2094](/detectionstrategies/DET0933) <small style="color:#929393">(v1.0)</small>
* [Analytic 2095](/detectionstrategies/DET0933) <small style="color:#929393">(v1.0)</small>
* [Analytic 2096](/detectionstrategies/DET0934) <small style="color:#929393">(v1.0)</small>
* [Analytic 2097](/detectionstrategies/DET0934) <small style="color:#929393">(v1.0)</small>
* [Analytic 2098](/detectionstrategies/DET0934) <small style="color:#929393">(v1.0)</small>
* [Analytic 2099](/detectionstrategies/DET0934) <small style="color:#929393">(v1.0)</small>
* [Analytic 2100](/detectionstrategies/DET0935) <small style="color:#929393">(v1.0)</small>
* [Analytic 2101](/detectionstrategies/DET0935) <small style="color:#929393">(v1.0)</small>
* [Analytic 2102](/detectionstrategies/DET0935) <small style="color:#929393">(v1.0)</small>
* [Analytic 2103](/detectionstrategies/DET0935) <small style="color:#929393">(v1.0)</small>
* [Analytic 2107](/detectionstrategies/DET0728) <small style="color:#929393">(v1.0)</small>
* [Analytic 2108](/detectionstrategies/DET0728) <small style="color:#929393">(v1.0)</small>
* [Analytic 2109](/detectionstrategies/DET0730) <small style="color:#929393">(v1.0)</small>
* [Analytic 2110](/detectionstrategies/DET0722) <small style="color:#929393">(v1.0)</small>
* [Analytic 2111](/detectionstrategies/DET0730) <small style="color:#929393">(v1.0)</small>
* [Analytic 2112](/detectionstrategies/DET0748) <small style="color:#929393">(v1.0)</small>
* [Analytic 2113](/detectionstrategies/DET0750) <small style="color:#929393">(v1.0)</small>
* [Analytic 2114](/detectionstrategies/DET0754) <small style="color:#929393">(v1.0)</small>
* [Analytic 2115](/detectionstrategies/DET0764) <small style="color:#929393">(v1.0)</small>
* [Analytic 2116](/detectionstrategies/DET0766) <small style="color:#929393">(v1.0)</small>
* [Analytic 2117](/detectionstrategies/DET0777) <small style="color:#929393">(v1.0)</small>
* [Analytic 2118](/detectionstrategies/DET0784) <small style="color:#929393">(v1.0)</small>
* [Analytic 2119](/detectionstrategies/DET0797) <small style="color:#929393">(v1.0)</small>
* [Analytic 2120](/detectionstrategies/DET0906) <small style="color:#929393">(v1.0)</small>
* [Analytic 2121](/detectionstrategies/DET0723) <small style="color:#929393">(v1.0)</small>
* [Analytic 2122](/detectionstrategies/DET0724) <small style="color:#929393">(v1.0)</small>
* [Analytic 2123](/detectionstrategies/DET0725) <small style="color:#929393">(v1.0)</small>
* [Analytic 2124](/detectionstrategies/DET0726) <small style="color:#929393">(v1.0)</small>
* [Analytic 2125](/detectionstrategies/DET0727) <small style="color:#929393">(v1.0)</small>
* [Analytic 2126](/detectionstrategies/DET0731) <small style="color:#929393">(v1.0)</small>
* [Analytic 2127](/detectionstrategies/DET0733) <small style="color:#929393">(v1.0)</small>
* [Analytic 2128](/detectionstrategies/DET0734) <small style="color:#929393">(v1.0)</small>
* [Analytic 2129](/detectionstrategies/DET0736) <small style="color:#929393">(v1.0)</small>
* [Analytic 2130](/detectionstrategies/DET0737) <small style="color:#929393">(v1.0)</small>
* [Analytic 2131](/detectionstrategies/DET0738) <small style="color:#929393">(v1.0)</small>
* [Analytic 2132](/detectionstrategies/DET0739) <small style="color:#929393">(v1.0)</small>
* [Analytic 2133](/detectionstrategies/DET0740) <small style="color:#929393">(v1.0)</small>
* [Analytic 2134](/detectionstrategies/DET0743) <small style="color:#929393">(v1.0)</small>
* [Analytic 2135](/detectionstrategies/DET0745) <small style="color:#929393">(v1.0)</small>
* [Analytic 2136](/detectionstrategies/DET0746) <small style="color:#929393">(v1.0)</small>
* [Analytic 2137](/detectionstrategies/DET0749) <small style="color:#929393">(v1.0)</small>
* [Analytic 2138](/detectionstrategies/DET0753) <small style="color:#929393">(v1.0)</small>
* [Analytic 2139](/detectionstrategies/DET0758) <small style="color:#929393">(v1.0)</small>
* [Analytic 2140](/detectionstrategies/DET0765) <small style="color:#929393">(v1.0)</small>
* [Analytic 2141](/detectionstrategies/DET0767) <small style="color:#929393">(v1.0)</small>
* [Analytic 2142](/detectionstrategies/DET0770) <small style="color:#929393">(v1.0)</small>
* [Analytic 2143](/detectionstrategies/DET0771) <small style="color:#929393">(v1.0)</small>
* [Analytic 2144](/detectionstrategies/DET0772) <small style="color:#929393">(v1.0)</small>
* [Analytic 2145](/detectionstrategies/DET0776) <small style="color:#929393">(v1.0)</small>
* [Analytic 2146](/detectionstrategies/DET0780) <small style="color:#929393">(v1.0)</small>
* [Analytic 2147](/detectionstrategies/DET0782) <small style="color:#929393">(v1.0)</small>
* [Analytic 2148](/detectionstrategies/DET0787) <small style="color:#929393">(v1.0)</small>
* [Analytic 2149](/detectionstrategies/DET0788) <small style="color:#929393">(v1.0)</small>
* [Analytic 2150](/detectionstrategies/DET0791) <small style="color:#929393">(v1.0)</small>
* [Analytic 2151](/detectionstrategies/DET0792) <small style="color:#929393">(v1.0)</small>
* [Analytic 2152](/detectionstrategies/DET0793) <small style="color:#929393">(v1.0)</small>
* [Analytic 2153](/detectionstrategies/DET0794) <small style="color:#929393">(v1.0)</small>
* [Analytic 2154](/detectionstrategies/DET0795) <small style="color:#929393">(v1.0)</small>
* [Analytic 2155](/detectionstrategies/DET0799) <small style="color:#929393">(v1.0)</small>
* [Analytic 2156](/detectionstrategies/DET0800) <small style="color:#929393">(v1.0)</small>
* [Analytic 2157](/detectionstrategies/DET0801) <small style="color:#929393">(v1.0)</small>
* [Analytic 2158](/detectionstrategies/DET0802) <small style="color:#929393">(v1.0)</small>
* [Analytic 2159](/detectionstrategies/DET0804) <small style="color:#929393">(v1.0)</small>
* [Analytic 2160](/detectionstrategies/DET0902) <small style="color:#929393">(v1.0)</small>
* [Analytic 2161](/detectionstrategies/DET0907) <small style="color:#929393">(v1.0)</small>
* [Analytic 2162](/detectionstrategies/DET0908) <small style="color:#929393">(v1.0)</small>
* [Analytic 2163](/detectionstrategies/DET0909) <small style="color:#929393">(v1.0)</small>
* [Analytic 2164](/detectionstrategies/DET0910) <small style="color:#929393">(v1.0)</small>
* [Analytic 2165](/detectionstrategies/DET0911) <small style="color:#929393">(v1.0)</small>
* [Analytic 2166](/detectionstrategies/DET0912) <small style="color:#929393">(v1.0)</small>
* [Analytic 2167](/detectionstrategies/DET0780) <small style="color:#929393">(v1.0)</small>
* [Analytic 2168](/detectionstrategies/DET0723) <small style="color:#929393">(v1.0)</small>
* [Analytic 2169](/detectionstrategies/DET0727) <small style="color:#929393">(v1.0)</small>
* [Analytic 2170](/detectionstrategies/DET0731) <small style="color:#929393">(v1.0)</small>
* [Analytic 2171](/detectionstrategies/DET0739) <small style="color:#929393">(v1.0)</small>
* [Analytic 2172](/detectionstrategies/DET0739) <small style="color:#929393">(v1.0)</small>
* [Analytic 2173](/detectionstrategies/DET0740) <small style="color:#929393">(v1.0)</small>
* [Analytic 2174](/detectionstrategies/DET0749) <small style="color:#929393">(v1.0)</small>
* [Analytic 2175](/detectionstrategies/DET0759) <small style="color:#929393">(v1.0)</small>
* [Analytic 2176](/detectionstrategies/DET0764) <small style="color:#929393">(v1.0)</small>
* [Analytic 2177](/detectionstrategies/DET0788) <small style="color:#929393">(v1.0)</small>
* [Analytic 2178](/detectionstrategies/DET0792) <small style="color:#929393">(v1.0)</small>
* [Analytic 2179](/detectionstrategies/DET0802) <small style="color:#929393">(v1.0)</small>
* [Analytic 2180](/detectionstrategies/DET0804) <small style="color:#929393">(v1.0)</small>
* [Analytic 2181](/detectionstrategies/DET0907) <small style="color:#929393">(v1.0)</small>
* [Analytic 2182](/detectionstrategies/DET0724) <small style="color:#929393">(v1.0)</small>
* [Analytic 2183](/detectionstrategies/DET0753) <small style="color:#929393">(v1.0)</small>
* [Analytic 2184](/detectionstrategies/DET0770) <small style="color:#929393">(v1.0)</small>
* [Analytic 2185](/detectionstrategies/DET0780) <small style="color:#929393">(v1.0)</small>
* [Analytic 2186](/detectionstrategies/DET0787) <small style="color:#929393">(v1.0)</small>
* [Analytic 2187](/detectionstrategies/DET0801) <small style="color:#929393">(v1.0)</small>
* [Analytic 2188](/detectionstrategies/DET0728) <small style="color:#929393">(v1.0)</small>
* [Analytic 2189](/detectionstrategies/DET0730) <small style="color:#929393">(v1.0)</small>
* [Analytic 2190](/detectionstrategies/DET0733) <small style="color:#929393">(v1.0)</small>
* [Analytic 2191](/detectionstrategies/DET0738) <small style="color:#929393">(v1.0)</small>
* [Analytic 2192](/detectionstrategies/DET0750) <small style="color:#929393">(v1.0)</small>
* [Analytic 2193](/detectionstrategies/DET0756) <small style="color:#929393">(v1.0)</small>
* [Analytic 2194](/detectionstrategies/DET0758) <small style="color:#929393">(v1.0)</small>
* [Analytic 2195](/detectionstrategies/DET0765) <small style="color:#929393">(v1.0)</small>
* [Analytic 2196](/detectionstrategies/DET0771) <small style="color:#929393">(v1.0)</small>
* [Analytic 2197](/detectionstrategies/DET0772) <small style="color:#929393">(v1.0)</small>
* [Analytic 2198](/detectionstrategies/DET0789) <small style="color:#929393">(v1.0)</small>
* [Analytic 2199](/detectionstrategies/DET0795) <small style="color:#929393">(v1.0)</small>
* [Analytic 2200](/detectionstrategies/DET0797) <small style="color:#929393">(v1.0)</small>
* [Analytic 2201](/detectionstrategies/DET0800) <small style="color:#929393">(v1.0)</small>
* [Analytic 2202](/detectionstrategies/DET0800) <small style="color:#929393">(v1.0)</small>
* [Analytic 2203](/detectionstrategies/DET0905) <small style="color:#929393">(v1.0)</small>
* [Analytic 2204](/detectionstrategies/DET0911) <small style="color:#929393">(v1.0)</small>
* [Analytic 2205](/detectionstrategies/DET0912) <small style="color:#929393">(v1.0)</small>
* [Analytic 2206](/detectionstrategies/DET0727) <small style="color:#929393">(v1.0)</small>
* [Analytic 2207](/detectionstrategies/DET0737) <small style="color:#929393">(v1.0)</small>
* [Analytic 2208](/detectionstrategies/DET0742) <small style="color:#929393">(v1.0)</small>
* [Analytic 2209](/detectionstrategies/DET0776) <small style="color:#929393">(v1.0)</small>
* [Analytic 2210](/detectionstrategies/DET0788) <small style="color:#929393">(v1.0)</small>
* [Analytic 2211](/detectionstrategies/DET0777) <small style="color:#929393">(v1.0)</small>
* [Analytic 2212](/detectionstrategies/DET0794) <small style="color:#929393">(v1.0)</small>
* [Analytic 2213](/detectionstrategies/DET0903) <small style="color:#929393">(v1.0)</small>
* [Analytic 2214](/detectionstrategies/DET0911) <small style="color:#929393">(v1.0)</small>
* [Analytic 2215](/detectionstrategies/DET0746) <small style="color:#929393">(v1.0)</small>
* [Analytic 2216](/detectionstrategies/DET0789) <small style="color:#929393">(v1.0)</small>
* [Analytic 2217](/detectionstrategies/DET0724) <small style="color:#929393">(v1.0)</small>
* [Analytic 2218](/detectionstrategies/DET0756) <small style="color:#929393">(v1.0)</small>
* [Analytic 2219](/detectionstrategies/DET0905) <small style="color:#929393">(v1.0)</small>
* [Analytic 2220](/detectionstrategies/DET0791) <small style="color:#929393">(v1.0)</small>
* [Analytic 2221](/detectionstrategies/DET0736) <small style="color:#929393">(v1.0)</small>
* [Analytic 2222](/detectionstrategies/DET0796) <small style="color:#929393">(v1.0)</small>
* [Analytic 2223](/detectionstrategies/DET0799) <small style="color:#929393">(v1.0)</small>
* [Analytic 2224](/detectionstrategies/DET0803) <small style="color:#929393">(v1.0)</small>
* [Analytic 2225](/detectionstrategies/DET0804) <small style="color:#929393">(v1.0)</small>
* [Analytic 2226](/detectionstrategies/DET0907) <small style="color:#929393">(v1.0)</small>
* [Analytic 2227](/detectionstrategies/DET0910) <small style="color:#929393">(v1.0)</small>
* [Analytic 2228](/detectionstrategies/DET0733) <small style="color:#929393">(v1.0)</small>
* [Analytic 2229](/detectionstrategies/DET0745) <small style="color:#929393">(v1.0)</small>
* [Analytic 2230](/detectionstrategies/DET0765) <small style="color:#929393">(v1.0)</small>
* [Analytic 2231](/detectionstrategies/DET0725) <small style="color:#929393">(v1.0)</small>
* [Analytic 2232](/detectionstrategies/DET0770) <small style="color:#929393">(v1.0)</small>
* [Analytic 2233](/detectionstrategies/DET0908) <small style="color:#929393">(v1.0)</small>
* [Analytic 2234](/detectionstrategies/DET0909) <small style="color:#929393">(v1.0)</small>
* [Analytic 2235](/detectionstrategies/DET0740) <small style="color:#929393">(v1.0)</small>
* [Analytic 2236](/detectionstrategies/DET0746) <small style="color:#929393">(v1.0)</small>
* [Analytic 2237](/detectionstrategies/DET0759) <small style="color:#929393">(v1.0)</small>
* [Analytic 2238](/detectionstrategies/DET0764) <small style="color:#929393">(v1.0)</small>
* [Analytic 2239](/detectionstrategies/DET0742) <small style="color:#929393">(v1.0)</small>
* [Analytic 2240](/detectionstrategies/DET0767) <small style="color:#929393">(v1.0)</small>
* [Analytic 2241](/detectionstrategies/DET0781) <small style="color:#929393">(v1.0)</small>
* [Analytic 2242](/detectionstrategies/DET0793) <small style="color:#929393">(v1.0)</small>
* [Analytic 2243](/detectionstrategies/DET0722) <small style="color:#929393">(v1.0)</small>
* [Analytic 2244](/detectionstrategies/DET0749) <small style="color:#929393">(v1.0)</small>
* [Analytic 2245](/detectionstrategies/DET0750) <small style="color:#929393">(v1.0)</small>
* [Analytic 2246](/detectionstrategies/DET0753) <small style="color:#929393">(v1.0)</small>
* [Analytic 2247](/detectionstrategies/DET0754) <small style="color:#929393">(v1.0)</small>
* [Analytic 2248](/detectionstrategies/DET0758) <small style="color:#929393">(v1.0)</small>
* [Analytic 2249](/detectionstrategies/DET0787) <small style="color:#929393">(v1.0)</small>
* [Analytic 2250](/detectionstrategies/DET0751) <small style="color:#929393">(v1.0)</small>
* [Analytic 2251](/detectionstrategies/DET0772) <small style="color:#929393">(v1.0)</small>
* [Analytic 2252](/detectionstrategies/DET0912) <small style="color:#929393">(v1.0)</small>
* [Analytic 2253](/detectionstrategies/DET0796) <small style="color:#929393">(v1.0)</small>
* [Analytic 2254](/detectionstrategies/DET0744) <small style="color:#929393">(v1.0)</small>
* [Analytic 2255](/detectionstrategies/DET0756) <small style="color:#929393">(v1.0)</small>
* [Analytic 2256](/detectionstrategies/DET0796) <small style="color:#929393">(v1.0)</small>
* [Analytic 2257](/detectionstrategies/DET0803) <small style="color:#929393">(v1.0)</small>
* [Analytic 2258](/detectionstrategies/DET0905) <small style="color:#929393">(v1.0)</small>
* [Analytic 2259](/detectionstrategies/DET0731) <small style="color:#929393">(v1.0)</small>
* [Analytic 2260](/detectionstrategies/DET0801) <small style="color:#929393">(v1.0)</small>
* [Analytic 2261](/detectionstrategies/DET0738) <small style="color:#929393">(v1.0)</small>
* [Analytic 2262](/detectionstrategies/DET0771) <small style="color:#929393">(v1.0)</small>
* [Analytic 2263](/detectionstrategies/DET0784) <small style="color:#929393">(v1.0)</small>
* [Analytic 2264](/detectionstrategies/DET0789) <small style="color:#929393">(v1.0)</small>
* [Analytic 2265](/detectionstrategies/DET0803) <small style="color:#929393">(v1.0)</small>
* [Analytic 2266](/detectionstrategies/DET0903) <small style="color:#929393">(v1.0)</small>
* [Analytic 2267](/detectionstrategies/DET0910) <small style="color:#929393">(v1.0)</small>
* [Analytic 2268](/detectionstrategies/DET0723) <small style="color:#929393">(v1.0)</small>
* [Analytic 2269](/detectionstrategies/DET0726) <small style="color:#929393">(v1.0)</small>
* [Analytic 2270](/detectionstrategies/DET0734) <small style="color:#929393">(v1.0)</small>
* [Analytic 2271](/detectionstrategies/DET0736) <small style="color:#929393">(v1.0)</small>
* [Analytic 2272](/detectionstrategies/DET0743) <small style="color:#929393">(v1.0)</small>
* [Analytic 2273](/detectionstrategies/DET0748) <small style="color:#929393">(v1.0)</small>
* [Analytic 2274](/detectionstrategies/DET0751) <small style="color:#929393">(v1.0)</small>
* [Analytic 2275](/detectionstrategies/DET0759) <small style="color:#929393">(v1.0)</small>
* [Analytic 2276](/detectionstrategies/DET0777) <small style="color:#929393">(v1.0)</small>
* [Analytic 2277](/detectionstrategies/DET0781) <small style="color:#929393">(v1.0)</small>
* [Analytic 2278](/detectionstrategies/DET0792) <small style="color:#929393">(v1.0)</small>
* [Analytic 2279](/detectionstrategies/DET0795) <small style="color:#929393">(v1.0)</small>
* [Analytic 2280](/detectionstrategies/DET0797) <small style="color:#929393">(v1.0)</small>
* [Analytic 2281](/detectionstrategies/DET0799) <small style="color:#929393">(v1.0)</small>
* [Analytic 2282](/detectionstrategies/DET0802) <small style="color:#929393">(v1.0)</small>
* [Analytic 2283](/detectionstrategies/DET0902) <small style="color:#929393">(v1.0)</small>
* [Analytic 2284](/detectionstrategies/DET0908) <small style="color:#929393">(v1.0)</small>
* [Analytic 2285](/detectionstrategies/DET0909) <small style="color:#929393">(v1.0)</small>
* [Analytic 2286](/detectionstrategies/DET0722) <small style="color:#929393">(v1.0)</small>
* [Analytic 2287](/detectionstrategies/DET0725) <small style="color:#929393">(v1.0)</small>
* [Analytic 2288](/detectionstrategies/DET0767) <small style="color:#929393">(v1.0)</small>
* [Analytic 2289](/detectionstrategies/DET0742) <small style="color:#929393">(v1.0)</small>

#### Patches

* [Analytic 1855](/detectionstrategies/DET0722) <small style="color:#929393">(v1.0)</small>
* [Analytic 1856](/detectionstrategies/DET0723) <small style="color:#929393">(v1.0)</small>
* [Analytic 1857](/detectionstrategies/DET0724) <small style="color:#929393">(v1.0)</small>
* [Analytic 1858](/detectionstrategies/DET0725) <small style="color:#929393">(v1.0)</small>
* [Analytic 1859](/detectionstrategies/DET0726) <small style="color:#929393">(v1.0)</small>
* [Analytic 1860](/detectionstrategies/DET0727) <small style="color:#929393">(v1.0)</small>
* [Analytic 1861](/detectionstrategies/DET0728) <small style="color:#929393">(v1.0)</small>
* [Analytic 1863](/detectionstrategies/DET0730) <small style="color:#929393">(v1.0)</small>
* [Analytic 1864](/detectionstrategies/DET0731) <small style="color:#929393">(v1.1)</small>
* [Analytic 1866](/detectionstrategies/DET0733) <small style="color:#929393">(v1.0)</small>
* [Analytic 1867](/detectionstrategies/DET0734) <small style="color:#929393">(v1.0)</small>
* [Analytic 1869](/detectionstrategies/DET0736) <small style="color:#929393">(v1.0)</small>
* [Analytic 1870](/detectionstrategies/DET0737) <small style="color:#929393">(v1.0)</small>
* [Analytic 1871](/detectionstrategies/DET0738) <small style="color:#929393">(v1.0)</small>
* [Analytic 1872](/detectionstrategies/DET0739) <small style="color:#929393">(v1.0)</small>
* [Analytic 1873](/detectionstrategies/DET0740) <small style="color:#929393">(v1.0)</small>
* [Analytic 1874](/detectionstrategies/DET0741) <small style="color:#929393">(v1.0)</small>
* [Analytic 1875](/detectionstrategies/DET0742) <small style="color:#929393">(v1.0)</small>
* [Analytic 1876](/detectionstrategies/DET0743) <small style="color:#929393">(v1.0)</small>
* [Analytic 1877](/detectionstrategies/DET0744) <small style="color:#929393">(v1.0)</small>
* [Analytic 1878](/detectionstrategies/DET0745) <small style="color:#929393">(v1.0)</small>
* [Analytic 1879](/detectionstrategies/DET0746) <small style="color:#929393">(v1.0)</small>
* [Analytic 1881](/detectionstrategies/DET0749) <small style="color:#929393">(v1.0)</small>
* [Analytic 1882](/detectionstrategies/DET0750) <small style="color:#929393">(v1.0)</small>
* [Analytic 1883](/detectionstrategies/DET0751) <small style="color:#929393">(v1.0)</small>
* [Analytic 1884](/detectionstrategies/DET0752) <small style="color:#929393">(v1.0)</small>
* [Analytic 1885](/detectionstrategies/DET0753) <small style="color:#929393">(v1.0)</small>
* [Analytic 1886](/detectionstrategies/DET0754) <small style="color:#929393">(v1.0)</small>
* [Analytic 1887](/detectionstrategies/DET0755) <small style="color:#929393">(v1.0)</small>
* [Analytic 1888](/detectionstrategies/DET0756) <small style="color:#929393">(v1.0)</small>
* [Analytic 1890](/detectionstrategies/DET0758) <small style="color:#929393">(v1.0)</small>
* [Analytic 1891](/detectionstrategies/DET0759) <small style="color:#929393">(v1.0)</small>
* [Analytic 1893](/detectionstrategies/DET0761) <small style="color:#929393">(v1.0)</small>
* [Analytic 1896](/detectionstrategies/DET0764) <small style="color:#929393">(v1.0)</small>
* [Analytic 1897](/detectionstrategies/DET0765) <small style="color:#929393">(v1.0)</small>
* [Analytic 1898](/detectionstrategies/DET0766) <small style="color:#929393">(v1.0)</small>
* [Analytic 1899](/detectionstrategies/DET0767) <small style="color:#929393">(v1.0)</small>
* [Analytic 1900](/detectionstrategies/DET0768) <small style="color:#929393">(v1.0)</small>
* [Analytic 1902](/detectionstrategies/DET0770) <small style="color:#929393">(v1.0)</small>
* [Analytic 1903](/detectionstrategies/DET0771) <small style="color:#929393">(v1.0)</small>
* [Analytic 1904](/detectionstrategies/DET0772) <small style="color:#929393">(v1.0)</small>
* [Analytic 1905](/detectionstrategies/DET0773) <small style="color:#929393">(v1.0)</small>
* [Analytic 1906](/detectionstrategies/DET0774) <small style="color:#929393">(v1.0)</small>
* [Analytic 1908](/detectionstrategies/DET0776) <small style="color:#929393">(v1.0)</small>
* [Analytic 1909](/detectionstrategies/DET0777) <small style="color:#929393">(v1.0)</small>
* [Analytic 1912](/detectionstrategies/DET0780) <small style="color:#929393">(v1.0)</small>
* [Analytic 1913](/detectionstrategies/DET0781) <small style="color:#929393">(v1.0)</small>
* [Analytic 1914](/detectionstrategies/DET0782) <small style="color:#929393">(v1.0)</small>
* [Analytic 1915](/detectionstrategies/DET0783) <small style="color:#929393">(v1.0)</small>
* [Analytic 1916](/detectionstrategies/DET0784) <small style="color:#929393">(v1.0)</small>
* [Analytic 1919](/detectionstrategies/DET0787) <small style="color:#929393">(v1.0)</small>
* [Analytic 1920](/detectionstrategies/DET0788) <small style="color:#929393">(v1.0)</small>
* [Analytic 1921](/detectionstrategies/DET0789) <small style="color:#929393">(v1.0)</small>
* [Analytic 1922](/detectionstrategies/DET0790) <small style="color:#929393">(v1.1)</small>
* [Analytic 1923](/detectionstrategies/DET0791) <small style="color:#929393">(v1.0)</small>
* [Analytic 1924](/detectionstrategies/DET0792) <small style="color:#929393">(v1.0)</small>
* [Analytic 1925](/detectionstrategies/DET0793) <small style="color:#929393">(v1.0)</small>
* [Analytic 1926](/detectionstrategies/DET0794) <small style="color:#929393">(v1.0)</small>
* [Analytic 1927](/detectionstrategies/DET0795) <small style="color:#929393">(v1.0)</small>
* [Analytic 1928](/detectionstrategies/DET0796) <small style="color:#929393">(v1.0)</small>
* [Analytic 1929](/detectionstrategies/DET0797) <small style="color:#929393">(v1.0)</small>
* [Analytic 1930](/detectionstrategies/DET0798) <small style="color:#929393">(v1.0)</small>
* [Analytic 1931](/detectionstrategies/DET0799) <small style="color:#929393">(v1.0)</small>
* [Analytic 1932](/detectionstrategies/DET0800) <small style="color:#929393">(v1.0)</small>
* [Analytic 1933](/detectionstrategies/DET0801) <small style="color:#929393">(v1.0)</small>
* [Analytic 1934](/detectionstrategies/DET0802) <small style="color:#929393">(v1.0)</small>
* [Analytic 1935](/detectionstrategies/DET0803) <small style="color:#929393">(v1.0)</small>
* [Analytic 1936](/detectionstrategies/DET0804) <small style="color:#929393">(v1.0)</small>
* [Analytic 2045](/detectionstrategies/DET0902) <small style="color:#929393">(v1.0)</small>
* [Analytic 2046](/detectionstrategies/DET0903) <small style="color:#929393">(v1.0)</small>
* [Analytic 2047](/detectionstrategies/DET0904) <small style="color:#929393">(v1.0)</small>
* [Analytic 2048](/detectionstrategies/DET0905) <small style="color:#929393">(v1.0)</small>
* [Analytic 2049](/detectionstrategies/DET0906) <small style="color:#929393">(v1.0)</small>
* [Analytic 2050](/detectionstrategies/DET0907) <small style="color:#929393">(v1.0)</small>
* [Analytic 2051](/detectionstrategies/DET0908) <small style="color:#929393">(v1.0)</small>
* [Analytic 2052](/detectionstrategies/DET0909) <small style="color:#929393">(v1.0)</small>
* [Analytic 2053](/detectionstrategies/DET0910) <small style="color:#929393">(v1.0)</small>
* [Analytic 2054](/detectionstrategies/DET0911) <small style="color:#929393">(v1.0)</small>
* [Analytic 2055](/detectionstrategies/DET0912) <small style="color:#929393">(v1.0)</small>
* [Analytic 2056](/detectionstrategies/DET0913) <small style="color:#929393">(v1.0)</small>
* [Analytic 2057](/detectionstrategies/DET0914) <small style="color:#929393">(v1.0)</small>
* [Analytic 2058](/detectionstrategies/DET0915) <small style="color:#929393">(v1.0)</small>
* [Analytic 2066](/detectionstrategies/DET0748) <small style="color:#929393">(v1.0)</small>

## Contributors to this release

* Alberto Arroba García
* Bridger Hackworth (NR Labs)
* Caio Silva
* Girshel Chokhonelidze
* Jeremy Ang
* Liran Ravich, Cribl
* Menachem Goldstein
* Pooja Natarajan, NEC Corporation India
* Riku Katsuse, NEC Corporation
* Sareena Karapoola, NEC Corporation India
* Stephan H. Wenderlich, Gray-Hat IT-Security Consulting
* Vijay Lalwani
