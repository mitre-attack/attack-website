Title: Updates - October 2022
Date: October 2022
Category: Cyber Threat Intelligence
Authors: Adam Pennington
Template: resources/update-post
url: /resources/updates/updates-october-2022
save_as: resources/updates/updates-october-2022/index.html

| Version | Start Date | End Date | Data | Changelogs |
|:--------|:-----------|:---------|:-----|:-----------|
| [ATT&CK v12](/versions/v12) | October 25, 2022 | April 24, 2023 | [v12.0 on MITRE/CTI](https://github.com/mitre/cti/releases/tag/ATT%26CK-v12.0)<br />[v12.1 on MITRE/CTI](https://github.com/mitre/cti/releases/tag/ATT%26CK-v12.1) | 11.3 - 12.0 [Details](/docs/changelogs/v11.3-v12.0/changelog-detailed.html) ([JSON](/docs/changelogs/v11.3-v12.0/changelog.json))<br />12.0 - 12.1 [Details](/docs/changelogs/v12.0-v12.1/changelog-detailed.html) ([JSON](/docs/changelogs/v12.0-v12.1/changelog.json)) |

The October 2022 (v12) ATT&CK release updates Techniques, Groups, and Software for Enterprise, Mobile, and ICS. The biggest changes in ATT&CK v12 are the addition of detections to ATT&CK for ICS, and the introduction of Campaigns.

Matching the model introduced to ATT&CK for Enterprise in ATT&CK v11, [ATT&CK for ICS](/matrices/ics/) detections describe ways of detecting various ICS techniques and are each tied to specific Data Sources and Data Components. This detection format was described in detail in our [ATT&CK v11 release blog post](https://medium.com/mitre-attack/attack-goes-to-v11-599a9112a025). The new detections added leverage both traditional host and network-based collection as well as ICS specific sources such as [Asset](/datasources/DS0039/) and [Operational Databases](/datasources/DS0040/). As there are overlaps between the Enterprise and ICS ATT&CK domains some ICS detections include references to Enterprise techniques where the additional context may assist defenders.

This release introduces the Campaign data structure to ATT&CK and an initial limited set of Campaigns. ATT&CK's Campaigns are defined as a grouping of intrusion activity conducted over a specific period of time with common targets and objectives. A key aspect of Campaigns is that the activity may or may not be linked to a specific threat actor. Campaigns are described in detail in the blog post [Introducing Campaigns to MITRE ATT&CK](https://medium.com/mitre-attack/introducing-attack-campaigns-6b15baa6cbb4). Specifics on how Campaigns are implemented in ATT&CK's Enterprise, ICS, and Mobile STIX representations are described in ATT&CK's [STIX 2.0 Data Model](https://github.com/mitre/cti/blob/master/USAGE.md#campaigns) and [STIX 2.1 Data Model](https://github.com/mitre-attack/attack-stix-data/blob/master/USAGE.md#campaigns). Several existing Groups were identified as more closely matching the Campaign than the Group definition and were converted to Campaigns. The 7 impacted groups were deprecated (noted below) and new Campaigns were created in their place.

In this release we have renamed the Enterprise Technique "Indicator Removal on Host" to [Indicator Removal (T1070)](/techniques/T1070) and rescoped it to better account for adversary behavior in cloud environments.

This version of ATT&CK for Enterprise contains 14 Tactics, 193 Techniques, 401 Sub-techniques, 135 Groups, 14 Campaigns, and 718 Pieces of Software.

## New Campaigns in ATT&CK

* [C0010](/campaigns/C0010) <small style="color:#929393">(v1.0)</small>
* [C0011](/campaigns/C0011) <small style="color:#929393">(v1.0)</small>
* [C0015](/campaigns/C0015) <small style="color:#929393">(v1.0)</small>
* [CostaRicto](/campaigns/C0004) <small style="color:#929393">(v1.0)</small> (replaces the group G0132/CostaRicto)
* [Frankenstein](/campaigns/C0001) <small style="color:#929393">(v1.0)</small> (replaces the group G0101/Frankenstein)
* [FunnyDream](/campaigns/C0007) <small style="color:#929393">(v1.0)</small>
* [Night Dragon](/campaigns/C0002) <small style="color:#929393">(v1.0)</small> (replaces the group G0014/Night Dragon)
* [Oldsmar Treatment Plant Intrusion](/campaigns/C0009) <small style="color:#929393">(v1.0)</small>
* [Operation CuckooBees](/campaigns/C0012) <small style="color:#929393">(v1.0)</small>
* [Operation Dust Storm](/campaigns/C0016) <small style="color:#929393">(v1.0)</small> (replaces the group G0031/Dust Storm)
* [Operation Honeybee](/campaigns/C0006) <small style="color:#929393">(v1.0)</small> (replaces the group G0072/HoneyBee)
* [Operation Sharpshooter](/campaigns/C0013) <small style="color:#929393">(v1.0)</small> (replaces the group G0104/Sharpshooter)
* [Operation Spalax](/campaigns/C0005) <small style="color:#929393">(v1.0)</small>
* [Operation Wocao](/campaigns/C0014) <small style="color:#929393">(v1.0)</small> (replaces the group G0116/Operation Wocao)

## Techniques

### Enterprise

#### New Techniques

* Acquire Infrastructure: [Serverless](/techniques/T1583/007) <small style="color:#929393">(v1.0)</small>
* Compromise Accounts: [Cloud Accounts](/techniques/T1586/003) <small style="color:#929393">(v1.0)</small>
* Compromise Infrastructure: [Serverless](/techniques/T1584/007) <small style="color:#929393">(v1.0)</small>
* Establish Accounts: [Cloud Accounts](/techniques/T1585/003) <small style="color:#929393">(v1.0)</small>
* Event Triggered Execution: [Installer Packages](/techniques/T1546/016) <small style="color:#929393">(v1.0)</small>
* Indicator Removal: [Clear Mailbox Data](/techniques/T1070/008) <small style="color:#929393">(v1.0)</small>
* Indicator Removal: [Clear Network Connection History and Configurations](/techniques/T1070/007) <small style="color:#929393">(v1.0)</small>
* Indicator Removal: [Clear Persistence](/techniques/T1070/009) <small style="color:#929393">(v1.0)</small>
* Modify Authentication Process: [Hybrid Identity](/techniques/T1556/007) <small style="color:#929393">(v1.0)</small>
* Modify Authentication Process: [Multi-Factor Authentication](/techniques/T1556/006) <small style="color:#929393">(v1.0)</small>
* Obfuscated Files or Information: [Dynamic API Resolution](/techniques/T1027/007) <small style="color:#929393">(v1.0)</small>
* Obfuscated Files or Information: [Embedded Payloads](/techniques/T1027/009) <small style="color:#929393">(v1.0)</small>
* Obfuscated Files or Information: [Stripped Payloads](/techniques/T1027/008) <small style="color:#929393">(v1.0)</small>
* Search Open Websites/Domains: [Code Repositories](/techniques/T1593/003) <small style="color:#929393">(v1.0)</small>
* [Serverless Execution](/techniques/T1648) <small style="color:#929393">(v1.0)</small>
* Stage Capabilities: [SEO Poisoning](/techniques/T1608/006) <small style="color:#929393">(v1.0)</small>
* [Steal or Forge Authentication Certificates](/techniques/T1649) <small style="color:#929393">(v1.0)</small>
* Traffic Signaling: [Socket Filters](/techniques/T1205/002) <small style="color:#929393">(v1.0)</small>

#### Technique Changes

* Account Discovery: [Domain Account](/techniques/T1087/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Account Discovery: [Local Account](/techniques/T1087/001) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Account Manipulation](/techniques/T1098) <small style="color:#929393">(v2.3&#8594;v2.4)</small>
  * [Additional Cloud Credentials](/techniques/T1098/001) <small style="color:#929393">(v2.3&#8594;v2.4)</small>
  * [Additional Cloud Roles](/techniques/T1098/003) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Acquire Infrastructure: [Domains](/techniques/T1583/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Adversary-in-the-Middle](/techniques/T1557) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
  * [DHCP Spoofing](/techniques/T1557/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [LLMNR/NBT-NS Poisoning and SMB Relay](/techniques/T1557/001) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Application Layer Protocol: [DNS](/techniques/T1071/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [BITS Jobs](/techniques/T1197) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Boot or Logon Autostart Execution: [Registry Run Keys / Startup Folder](/techniques/T1547/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Boot or Logon Autostart Execution: [Shortcut Modification](/techniques/T1547/009) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Credentials from Password Stores: [Windows Credential Manager](/techniques/T1555/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Data Encrypted for Impact](/techniques/T1486) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Data from Cloud Storage](/techniques/T1530) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Data from Information Repositories: [Code Repositories](/techniques/T1213/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Data from Local System](/techniques/T1005) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Data from Network Shared Drive](/techniques/T1039) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Domain Policy Modification: [Domain Trust Modification](/techniques/T1484/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Domain Trust Discovery](/techniques/T1482) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Escape to Host](/techniques/T1611) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Event Triggered Execution](/techniques/T1546) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Exfiltration Over Web Service](/techniques/T1567) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
  * [Exfiltration to Cloud Storage](/techniques/T1567/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Exploitation for Privilege Escalation](/techniques/T1068) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [External Remote Services](/techniques/T1133) <small style="color:#929393">(v2.3&#8594;v2.4)</small>
* [File and Directory Discovery](/techniques/T1083) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [File and Directory Permissions Modification](/techniques/T1222) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Firmware Corruption](/techniques/T1495) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Gather Victim Identity Information: [Email Addresses](/techniques/T1589/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Gather Victim Network Information: [DNS](/techniques/T1590/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Gather Victim Network Information: [Domain Properties](/techniques/T1590/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Impair Defenses](/techniques/T1562) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
  * [Disable or Modify Tools](/techniques/T1562/001) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
  * [Impair Command History Logging](/techniques/T1562/003) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
  * [Indicator Blocking](/techniques/T1562/006) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Indicator Removal](/techniques/T1070) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
  * [Clear Command History](/techniques/T1070/003) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Modify Authentication Process](/techniques/T1556) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Obfuscated Files or Information](/techniques/T1027) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Password Policy Discovery](/techniques/T1201) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* Permission Groups Discovery: [Domain Groups](/techniques/T1069/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Permission Groups Discovery: [Local Groups](/techniques/T1069/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Phishing: [Spearphishing Link](/techniques/T1566/002) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* Phishing for Information: [Spearphishing Link](/techniques/T1598/003) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Process Injection](/techniques/T1055) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
  * [Dynamic-link Library Injection](/techniques/T1055/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
  * [VDSO Hijacking](/techniques/T1055/014) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Remote System Discovery](/techniques/T1018) <small style="color:#929393">(v3.3&#8594;v3.4)</small>
* [Replication Through Removable Media](/techniques/T1091) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Scheduled Task/Job: [Scheduled Task](/techniques/T1053/005) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Search Open Websites/Domains](/techniques/T1593) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Server Software Component](/techniques/T1505) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
  * [Web Shell](/techniques/T1505/003) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Stage Capabilities](/techniques/T1608) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
  * [Link Target](/techniques/T1608/005) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
  * [Upload Tool](/techniques/T1608/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Subvert Trust Controls: [Code Signing](/techniques/T1553/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Subvert Trust Controls: [Gatekeeper Bypass](/techniques/T1553/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [System Information Discovery](/techniques/T1082) <small style="color:#929393">(v2.4&#8594;v2.5)</small>
* [System Network Configuration Discovery](/techniques/T1016) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [System Network Connections Discovery](/techniques/T1049) <small style="color:#929393">(v2.3&#8594;v2.4)</small>
* [System Service Discovery](/techniques/T1007) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [System Shutdown/Reboot](/techniques/T1529) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Traffic Signaling](/techniques/T1205) <small style="color:#929393">(v2.3&#8594;v2.4)</small>
* [Transfer Data to Cloud Account](/techniques/T1537) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Trusted Relationship](/techniques/T1199) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* Use Alternate Authentication Material: [Application Access Token](/techniques/T1550/001) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Valid Accounts](/techniques/T1078) <small style="color:#929393">(v2.4&#8594;v2.5)</small>

#### Minor Technique Changes

* Abuse Elevation Control Mechanism: [Elevated Execution with Prompt](/techniques/T1548/004) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* Adversary-in-the-Middle: [ARP Cache Poisoning](/techniques/T1557/002) <small style="color:#eb6635">(v1.1&#8594;v1.1)</small>
* Brute Force: [Password Guessing](/techniques/T1110/001) <small style="color:#eb6635">(v1.3&#8594;v1.3)</small>
* Command and Scripting Interpreter: [AppleScript](/techniques/T1059/002) <small style="color:#eb6635">(v1.1&#8594;v1.1)</small>
* [Compromise Infrastructure](/techniques/T1584) <small style="color:#eb6635">(v1.2&#8594;v1.2)</small>
* Create or Modify System Process: [Windows Service](/techniques/T1543/003) <small style="color:#eb6635">(v1.2&#8594;v1.2)</small>
* [Data Staged](/techniques/T1074) <small style="color:#eb6635">(v1.4&#8594;v1.4)</small>
* Defacement: [Internal Defacement](/techniques/T1491/001) <small style="color:#eb6635">(v1.1&#8594;v1.1)</small>
* [Disk Wipe](/techniques/T1561) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
  * [Disk Content Wipe](/techniques/T1561/001) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* Hijack Execution Flow: [Path Interception by Unquoted Path](/techniques/T1574/009) <small style="color:#eb6635">(v1.1&#8594;v1.1)</small>
* [Multi-Factor Authentication Request Generation](/techniques/T1621) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* OS Credential Dumping: [LSASS Memory](/techniques/T1003/001) <small style="color:#eb6635">(v1.1&#8594;v1.1)</small>
* OS Credential Dumping: [Security Account Manager](/techniques/T1003/002) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Search Open Technical Databases](/techniques/T1596) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Service Stop](/techniques/T1489) <small style="color:#eb6635">(v1.2&#8594;v1.2)</small>

#### Technique Revocations

* No changes

#### Technique Deprecations

* No changes

### Mobile

#### New Techniques

* No changes

#### Technique Changes

* No changes

#### Minor Technique Changes

* Location Tracking: [Impersonate SS7 Nodes](/techniques/T1430/002) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* Location Tracking: [Remote Device Management Services](/techniques/T1430/001) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>

#### Technique Revocations

* No changes

#### Technique Deprecations

* No changes

### ICS

#### New Techniques

* [Hardcoded Credentials](/techniques/T0891) <small style="color:#929393">(v1.0)</small>

#### Technique Changes

* [Adversary-in-the-Middle](/techniques/T0830) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Alarm Suppression](/techniques/T0878) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Block Serial COM](/techniques/T0805) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Command-Line Interface](/techniques/T0807) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Commonly Used Port](/techniques/T0885) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Connection Proxy](/techniques/T0884) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Data from Information Repositories](/techniques/T0811) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Device Restart/Shutdown](/techniques/T0816) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Execution through API](/techniques/T0871) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Exploitation for Evasion](/techniques/T0820) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Exploitation for Privilege Escalation](/techniques/T0890) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Graphical User Interface](/techniques/T0823) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Hooking](/techniques/T0874) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [I/O Image](/techniques/T0877) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Lateral Tool Transfer](/techniques/T0867) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Manipulate I/O Image](/techniques/T0835) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Masquerading](/techniques/T0849) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Modify Alarm Settings](/techniques/T0838) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Modify Controller Tasking](/techniques/T0821) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Modify Parameter](/techniques/T0836) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Modify Program](/techniques/T0889) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Module Firmware](/techniques/T0839) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Network Connection Enumeration](/techniques/T0840) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Point & Tag Identification](/techniques/T0861) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Program Download](/techniques/T0843) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Remote Services](/techniques/T0886) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Remote System Discovery](/techniques/T0846) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Remote System Information Discovery](/techniques/T0888) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Rogue Master](/techniques/T0848) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Rootkit](/techniques/T0851) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Spearphishing Attachment](/techniques/T0865) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Spoof Reporting Message](/techniques/T0856) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Supply Chain Compromise](/techniques/T0862) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [System Firmware](/techniques/T0857) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Transient Cyber Asset](/techniques/T0864) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Unauthorized Command Message](/techniques/T0855) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [User Execution](/techniques/T0863) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Valid Accounts](/techniques/T0859) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Wireless Compromise](/techniques/T0860) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Wireless Sniffing](/techniques/T0887) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Minor Technique Changes

* [Block Reporting Message](/techniques/T0804) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Brute Force I/O](/techniques/T0806) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Damage to Property](/techniques/T0879) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Data Destruction](/techniques/T0809) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Default Credentials](/techniques/T0812) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Denial of Control](/techniques/T0813) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Denial of Service](/techniques/T0814) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Denial of View](/techniques/T0815) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Drive-by Compromise](/techniques/T0817) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Exploit Public-Facing Application](/techniques/T0819) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Exploitation of Remote Services](/techniques/T0866) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [External Remote Services](/techniques/T0822) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Internet Accessible Device](/techniques/T0883) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Loss of Availability](/techniques/T0826) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Loss of Control](/techniques/T0827) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Loss of Productivity and Revenue](/techniques/T0828) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Loss of Protection](/techniques/T0837) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Loss of Safety](/techniques/T0880) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Manipulation of View](/techniques/T0832) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Native API](/techniques/T0834) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Network Sniffing](/techniques/T0842) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Project File Infection](/techniques/T0873) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Replication Through Removable Media](/techniques/T0847) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Scripting](/techniques/T0853) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>

#### Technique Revocations

* No changes

#### Technique Deprecations

* No changes

## Software

### Enterprise

#### New Software

* [Action RAT](/software/S1028) <small style="color:#929393">(v1.0)</small>
* [Amadey](/software/S1025) <small style="color:#929393">(v1.0)</small>
* [AuTo Stealer](/software/S1029) <small style="color:#929393">(v1.0)</small>
* [Bumblebee](/software/S1039) <small style="color:#929393">(v1.0)</small>
* [Chinoxy](/software/S1041) <small style="color:#929393">(v1.0)</small>
* [CreepyDrive](/software/S1023) <small style="color:#929393">(v1.0)</small>
* [CreepySnail](/software/S1024) <small style="color:#929393">(v1.0)</small>
* [DCSrv](/software/S1033) <small style="color:#929393">(v1.0)</small>
* [DanBot](/software/S1014) <small style="color:#929393">(v1.0)</small>
* [DnsSystem](/software/S1021) <small style="color:#929393">(v1.0)</small>
* [FunnyDream](/software/S1044) <small style="color:#929393">(v1.0)</small>
* [Heyoka Backdoor](/software/S1027) <small style="color:#929393">(v1.0)</small>
* [IceApple](/software/S1022) <small style="color:#929393">(v1.0)</small>
* [Kevin](/software/S1020) <small style="color:#929393">(v1.0)</small>
* [MacMa](/software/S1016) <small style="color:#929393">(v1.0)</small>
* [Milan](/software/S1015) <small style="color:#929393">(v1.0)</small>
* [Mongall](/software/S1026) <small style="color:#929393">(v1.0)</small>
* [Mori](/software/S1047) <small style="color:#929393">(v1.0)</small>
* [OutSteel](/software/S1017) <small style="color:#929393">(v1.0)</small>
* [PcShare](/software/S1050) <small style="color:#929393">(v1.0)</small>
* [PingPull](/software/S1031) <small style="color:#929393">(v1.0)</small>
* [PowGoop](/software/S1046) <small style="color:#929393">(v1.0)</small>
* [PowerLess](/software/S1012) <small style="color:#929393">(v1.0)</small>
* [PyDCrypt](/software/S1032) <small style="color:#929393">(v1.0)</small>
* [Rclone](/software/S1040) <small style="color:#929393">(v1.0)</small>
* [STARWHALE](/software/S1037) <small style="color:#929393">(v1.0)</small>
* [SUGARDUMP](/software/S1042) <small style="color:#929393">(v1.0)</small>
* [SUGARUSH](/software/S1049) <small style="color:#929393">(v1.0)</small>
* [Saint Bot](/software/S1018) <small style="color:#929393">(v1.0)</small>
* [Shark](/software/S1019) <small style="color:#929393">(v1.0)</small>
* [Small Sieve](/software/S1035) <small style="color:#929393">(v1.0)</small>
* [Squirrelwaffle](/software/S1030) <small style="color:#929393">(v1.0)</small>
* [StrifeWater](/software/S1034) <small style="color:#929393">(v1.0)</small>
* [Tarrask](/software/S1011) <small style="color:#929393">(v1.0)</small>
* [ZxxZ](/software/S1013) <small style="color:#929393">(v1.0)</small>
* [ccf32](/software/S1043) <small style="color:#929393">(v1.0)</small>
* [macOS.OSAMiner](/software/S1048) <small style="color:#929393">(v1.0)</small>

#### Software Changes

* [AADInternals](/software/S0677) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [ASPXSpy](/software/S0073) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [AdFind](/software/S0552) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [AppleJeus](/software/S0584) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Azorult](/software/S0344) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [BITSAdmin](/software/S0190) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Bazar](/software/S0534) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [BloodHound](/software/S0521) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Cobalt Strike](/software/S0154) <small style="color:#929393">(v1.8&#8594;v1.9)</small>
* [ComRAT](/software/S0126) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Conti](/software/S0575) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [CostaBricks](/software/S0614) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Crimson](/software/S0115) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Dtrack](/software/S0567) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Empire](/software/S0363) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [FlawedAmmyy](/software/S0381) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Goopy](/software/S0477) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [GrimAgent](/software/S0632) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Impacket](/software/S0357) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Industroyer](/software/S0604) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Invoke-PSImage](/software/S0231) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [KOCTOPUS](/software/S0669) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [MCMD](/software/S0500) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Mimikatz](/software/S0002) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
* [Mis-Type](/software/S0084) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Misdat](/software/S0083) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [OSX/Shlayer](/software/S0402) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [POWERSTATS](/software/S0223) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [PS1](/software/S0613) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Penquin](/software/S0587) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Pillowmint](/software/S0517) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Ping](/software/S0097) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [PoisonIvy](/software/S0012) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [PoshC2](/software/S0378) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [PowerSploit](/software/S0194) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [PsExec](/software/S0029) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Pteranodon](/software/S0147) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [QuasarRAT](/software/S0262) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* [RTM](/software/S0148) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Reg](/software/S0075) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Remcos](/software/S0332) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Rising Sun](/software/S0448) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [S-Type](/software/S0085) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [SDBbot](/software/S0461) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [SMOKEDHAM](/software/S0649) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [SUNBURST](/software/S0559) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* [SYSCON](/software/S0464) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [ShadowPad](/software/S0596) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [SombRAT](/software/S0615) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Stuxnet](/software/S0603) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Systeminfo](/software/S0096) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Tasklist](/software/S0057) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Tor](/software/S0183) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Wevtutil](/software/S0645) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [XCSSET](/software/S0658) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [ZLib](/software/S0086) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [at](/software/S0110) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [cmd](/software/S0106) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [dsquery](/software/S0105) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [gh0st RAT](/software/S0032) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [gsecdump](/software/S0008) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [ipconfig](/software/S0100) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [netstat](/software/S0104) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [njRAT](/software/S0385) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [zwShell](/software/S0350) <small style="color:#929393">(v1.1&#8594;v2.0)</small>

#### Minor Software Changes

* [Backdoor.Oldrea](/software/S0093) <small style="color:#eb6635">(v2.0&#8594;v2.0)</small>
* [Bad Rabbit](/software/S0606) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [BlackEnergy](/software/S0089) <small style="color:#eb6635">(v1.3&#8594;v1.3)</small>
* [CSPY Downloader](/software/S0527) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [DarkWatchman](/software/S0673) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [ELMER](/software/S0064) <small style="color:#eb6635">(v1.1&#8594;v1.1)</small>
* [Flame](/software/S0143) <small style="color:#eb6635">(v1.1&#8594;v1.1)</small>
* [Grandoreiro](/software/S0531) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [HermeticWiper](/software/S0697) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Metamorfo](/software/S0455) <small style="color:#eb6635">(v2.0&#8594;v2.0)</small>
* [MirageFox](/software/S0280) <small style="color:#eb6635">(v1.1&#8594;v1.1)</small>
* [Mivast](/software/S0080) <small style="color:#eb6635">(v1.1&#8594;v1.1)</small>
* [Net Crawler](/software/S0056) <small style="color:#eb6635">(v1.1&#8594;v1.1)</small>
* [POWERSOURCE](/software/S0145) <small style="color:#eb6635">(v1.1&#8594;v1.1)</small>
* [REvil](/software/S0496) <small style="color:#eb6635">(v2.0&#8594;v2.0)</small>
* [RawDisk](/software/S0364) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Ryuk](/software/S0446) <small style="color:#eb6635">(v1.3&#8594;v1.3)</small>
* [Sibot](/software/S0589) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [TEXTMATE](/software/S0146) <small style="color:#eb6635">(v1.1&#8594;v1.1)</small>
* [TinyZBot](/software/S0004) <small style="color:#eb6635">(v1.1&#8594;v1.1)</small>

#### Software Revocations

* No changes

#### Software Deprecations

* No changes

### Mobile

#### New Software

* No changes

#### Software Changes

* No changes

#### Minor Software Changes

* No changes

#### Software Revocations

* No changes

#### Software Deprecations

* No changes

### ICS

#### New Software

* [INCONTROLLER](/software/S1045) <small style="color:#929393">(v1.0)</small>

#### Software Changes

* [Industroyer](/software/S0604) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Stuxnet](/software/S0603) <small style="color:#929393">(v1.1&#8594;v1.2)</small>

#### Minor Software Changes

* [ACAD/Medre.A](/software/S1000) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Backdoor.Oldrea](/software/S0093) <small style="color:#eb6635">(v2.0&#8594;v2.0)</small>
* [Bad Rabbit](/software/S0606) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [BlackEnergy](/software/S0089) <small style="color:#eb6635">(v1.3&#8594;v1.3)</small>
* [Flame](/software/S0143) <small style="color:#eb6635">(v1.1&#8594;v1.1)</small>
* [PLC-Blaster](/software/S1006) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Triton](/software/S1009) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [VPNFilter](/software/S1010) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>

#### Software Revocations

* No changes

#### Software Deprecations

* No changes

## Groups

### Enterprise

#### New Groups

* [Aoqin Dragon](/groups/G1007) <small style="color:#929393">(v1.0)</small>
* [BITTER](/groups/G1002) <small style="color:#929393">(v1.0)</small>
* [EXOTIC LILY](/groups/G1011) <small style="color:#929393">(v1.0)</small>
* [Earth Lusca](/groups/G1006) <small style="color:#929393">(v1.0)</small>
* [Ember Bear](/groups/G1003) <small style="color:#929393">(v1.0)</small>
* [HEXANE](/groups/G1001) <small style="color:#eb6635">(v2.0)</small>
* [LAPSUS$](/groups/G1004) <small style="color:#929393">(v1.0)</small>
* [Moses Staff](/groups/G1009) <small style="color:#929393">(v1.0)</small>
* [POLONIUM](/groups/G1005) <small style="color:#929393">(v1.0)</small>
* [SideCopy](/groups/G1008) <small style="color:#929393">(v1.0)</small>

#### Group Changes

* [APT29](/groups/G0016) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [CopyKittens](/groups/G0052) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
* [Darkhotel](/groups/G0012) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Dragonfly](/groups/G0035) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [GALLIUM](/groups/G0093) <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* [HAFNIUM](/groups/G0125) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Lazarus Group](/groups/G0032) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [Magic Hound](/groups/G0059) <small style="color:#929393">(v4.1&#8594;v5.0)</small>
* [MuddyWater](/groups/G0069) <small style="color:#929393">(v3.0&#8594;v4.0)</small>
* [TA505](/groups/G0092) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* [TeamTNT](/groups/G0139) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Transparent Tribe](/groups/G0134) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Minor Group Changes

* [APT16](/groups/G0023) <small style="color:#eb6635">(v1.1&#8594;v1.1)</small>
* [APT39](/groups/G0087) <small style="color:#eb6635">(v3.1&#8594;v3.1)</small>
* [APT41](/groups/G0096) <small style="color:#eb6635">(v3.0&#8594;v3.0)</small>
* [Aquatic Panda](/groups/G0143) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Cleaver](/groups/G0003) <small style="color:#eb6635">(v1.3&#8594;v1.3)</small>
* [Confucius](/groups/G0142) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Deep Panda](/groups/G0009) <small style="color:#eb6635">(v1.2&#8594;v1.2)</small>
* [FIN6](/groups/G0037) <small style="color:#eb6635">(v3.2&#8594;v3.2)</small>
* [FIN7](/groups/G0046) <small style="color:#eb6635">(v2.1&#8594;v2.1)</small>
* [Fox Kitten](/groups/G0117) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Indrik Spider](/groups/G0119) <small style="color:#eb6635">(v2.1&#8594;v2.1)</small>
* [Ke3chang](/groups/G0004) <small style="color:#eb6635">(v2.0&#8594;v2.0)</small>
* [Nomadic Octopus](/groups/G0133) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [OilRig](/groups/G0049) <small style="color:#eb6635">(v3.0&#8594;v3.0)</small>
* [Patchwork](/groups/G0040) <small style="color:#eb6635">(v1.4&#8594;v1.4)</small>
* [Sandworm Team](/groups/G0034) <small style="color:#eb6635">(v2.2&#8594;v2.2)</small>
* [Silence](/groups/G0091) <small style="color:#eb6635">(v2.1&#8594;v2.1)</small>
* [Turla](/groups/G0010) <small style="color:#eb6635">(v3.0&#8594;v3.0)</small>
* [menuPass](/groups/G0045) <small style="color:#eb6635">(v2.1&#8594;v2.1)</small>

#### Group Revocations

* No changes

#### Group Deprecations

* [CostaRicto](/groups/G0132) <small style="color:#929393">(v1.0)</small>
* [Dust Storm](/groups/G0031) <small style="color:#929393">(v1.0)</small>
* [Frankenstein](/groups/G0101) <small style="color:#929393">(v1.1)</small>
* [Honeybee](/groups/G0072) <small style="color:#929393">(v1.1)</small>
* [Night Dragon](/groups/G0014) <small style="color:#929393">(v1.4)</small>
* [Operation Wocao](/groups/G0116) <small style="color:#929393">(v1.0)</small>
* [Sharpshooter](/groups/G0104) <small style="color:#929393">(v1.0)</small>

### Mobile

#### New Groups

* [Earth Lusca](/groups/G1006) <small style="color:#929393">(v1.0)</small>

#### Group Changes

* No changes

#### Minor Group Changes

* [Sandworm Team](/groups/G0034) <small style="color:#eb6635">(v2.2&#8594;v2.2)</small>

#### Group Revocations

* No changes

#### Group Deprecations

* No changes

### ICS

#### New Groups

* No changes

#### Group Changes

* [Dragonfly](/groups/G0035) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [HEXANE](/groups/G1001) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Lazarus Group](/groups/G0032) <small style="color:#929393">(v3.0&#8594;v3.1)</small>

#### Minor Group Changes

* [FIN6](/groups/G0037) <small style="color:#eb6635">(v3.2&#8594;v3.2)</small>
* [FIN7](/groups/G0046) <small style="color:#eb6635">(v2.1&#8594;v2.1)</small>
* [OilRig](/groups/G0049) <small style="color:#eb6635">(v3.0&#8594;v3.0)</small>
* [Sandworm Team](/groups/G0034) <small style="color:#eb6635">(v2.2&#8594;v2.2)</small>

#### Group Revocations

* No changes

#### Group Deprecations

* No changes

## Mitigations

### Enterprise

#### New Mitigations

* No changes

#### Mitigation Changes

* No changes

#### Minor Mitigation Changes

* [Account Use Policies](/mitigations/M1036) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Audit](/mitigations/M1047) <small style="color:#eb6635">(v1.1&#8594;v1.1)</small>
* [Credential Access Protection](/mitigations/M1043) <small style="color:#eb6635">(v1.1&#8594;v1.1)</small>
* [Multi-factor Authentication](/mitigations/M1032) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>
* [Password Policies](/mitigations/M1027) <small style="color:#eb6635">(v1.0&#8594;v1.0)</small>

#### Mitigation Revocations

* No changes

#### Mitigation Deprecations

* No changes

### Mobile

#### New Mitigations

* No changes

#### Mitigation Changes

* No changes

#### Minor Mitigation Changes

* No changes

#### Mitigation Revocations

* No changes

#### Mitigation Deprecations

* No changes

### ICS

#### New Mitigations

* No changes

#### Mitigation Changes

* No changes

#### Minor Mitigation Changes

* No changes

#### Mitigation Revocations

* No changes

#### Mitigation Deprecations

* No changes

## Data Sources and/or Components

### Enterprise

#### New Data Sources and/or Components

* No changes

#### Data Source and/or Component Changes

* [Command](/datasources/DS0017) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Command Execution](/datasources/DS0017/#Command%20Execution) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Logon Session](/datasources/DS0028) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Logon Session Creation](/datasources/DS0028/#Logon%20Session%20Creation) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Malware Repository](/datasources/DS0004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Malware Content](/datasources/DS0004/#Malware%20Content) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Malware Metadata](/datasources/DS0004/#Malware%20Metadata) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Network Traffic](/datasources/DS0029) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Network Connection Creation](/datasources/DS0029/#Network%20Connection%20Creation) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Process](/datasources/DS0009) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Process Creation](/datasources/DS0009/#Process%20Creation) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Script](/datasources/DS0012) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Script Execution](/datasources/DS0012/#Script%20Execution) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Sensor Health](/datasources/DS0013) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Host Status](/datasources/DS0013/#Host%20Status) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [User Account](/datasources/DS0002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [User Account Authentication](/datasources/DS0002/#User%20Account%20Authentication) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Minor Data Source and/or Component Changes

* No changes

#### Data Source and/or Component Revocations

* No changes

#### Data Source and/or Component Deprecations

* [Cluster](/datasources/DS0031) <small style="color:#929393">(v1.0)</small>
  * [Cluster Metadata](/datasources/DS0031/#Cluster%20Metadata) <small style="color:#929393">(v1.0)</small>

### Mobile

ATT&CK for Mobile does not support structured data sources

### ICS

#### New Data Sources and/or Components

* [Asset](/datasources/DS0039) <small style="color:#929393">(v1.0)</small>
  * [Asset Inventory](/datasources/DS0039/#Asset%20Inventory) <small style="color:#929393">(v1.0)</small>
  * [Software](/datasources/DS0039/#Software) <small style="color:#929393">(v1.0)</small>
* Scheduled Job: [Scheduled Job Creation](/datasources/DS0003/#Scheduled%20Job%20Creation) <small style="color:#929393">(v1.0)</small>
* Service: [Service Modification](/datasources/DS0019/#Service%20Modification) <small style="color:#929393">(v1.0)</small>

#### Data Source and/or Component Changes

* [Command](/datasources/DS0017) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Command Execution](/datasources/DS0017/#Command%20Execution) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Logon Session](/datasources/DS0028) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Logon Session Creation](/datasources/DS0028/#Logon%20Session%20Creation) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Network Traffic](/datasources/DS0029) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Network Connection Creation](/datasources/DS0029/#Network%20Connection%20Creation) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Process](/datasources/DS0009) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Process Creation](/datasources/DS0009/#Process%20Creation) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Script](/datasources/DS0012) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Script Execution](/datasources/DS0012/#Script%20Execution) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [User Account](/datasources/DS0002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [User Account Authentication](/datasources/DS0002/#User%20Account%20Authentication) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Minor Data Source and/or Component Changes

* No changes

#### Data Source and/or Component Revocations

* No changes

#### Data Source and/or Component Deprecations

* No changes

## Contributors to this release

* Aagam Shah, @neutrinoguy, ABB
* Andrea Serrano Urea, Telefónica Tech
* Andrew Allen, @whitehat_zero
* AppOmni
* AttackIQ
* Austin Clark, @c2defense
* Awake Security
* Blake Strom, Microsoft 365 Defender
* Boominathan Sundaram
* Brandon Dalton @PartyD0lphin
* Catherine Williams, BT Security
* Chris Heald
* Cian Heasley
* Cisco
* CrowdStrike
* CrowdStrike Falcon OverWatch
* Daniel Feichter, @VirtualAllocEx, Infosec Tirol
* Daniyal Naeem, BT Security
* Darin Smith, Cisco
* David Hughes, BT Security
* David Tayouri
* Dragos Threat Intelligence
* Dray Agha, @Purp1eW0lf, Huntress Labs
* Edward Millington
* Eran Ayalon, Cybereason
* Erik Schamper, @Schamperr, Fox-IT
* ExtraHop
* Flavio Costa, Cisco
* Francesco Bigarella
* Goldstein Menachem
* Hannah Simes, BT Security
* Harry Hill, BT Security
* Harshal Tupsamudre, Qualys
* Hiroki Nagahama, NEC Corporation
* Ian Davila, Tidal Cyber
* Ian McKay
* Ilan Sokol, Cybereason
* Jannie Li, Microsoft Threat Intelligence Center (MSTIC)
* Joas Antonio dos Santos, @Cr4zyC0d3
* Kyaw Pyiyt Htet, @KyawPyiytHtet
* Lee Christensen, SpecterOps
* Liran Ravich, CardinalOps
* Lucas Heiligenstein
* Maarten van Dantzig, @MaartenVDantzig, Fox-IT
* Manikanran Srinivasan, NEC Corporation India
* Matt Brenton, Zurich Insurance Group
* Matt Burrough, @mattburrough, Microsoft
* Menachem Goldstein
* Mindaugas Gudzis, BT Security
* Miriam Wiesner, @miriamxyra, Microsoft Security
* Nick Cairns, @grotezinfosec
* Oleg Kolesnikov, Securonix
* Oren Ofer, Cybereason
* Ozer Sarilar, @ozersarilar, STM
* Phill Taylor, BT Security
* Pooja Natarajan, NEC Corporation India
* Praetorian
* Raphaël Lheureux
* SarathKumar Rajendran, Trimble Inc
* Sebastian Showell-Westrip, BT Security
* Sekhar Sarukkai, McAfee
* Shailesh Tiwary (Indian Army)
* Shanief Webb
* Sittikorn Sangrattanapitak
* Swasti Bhushan Deb, IBM India Pvt. Ltd.
* Thirumalai Natarajan, Mandiant
* Tim (Wadhwa-)Brown
* Tristan Bennett, Seamless Intelligence
* Uriel Kosayev
* Vadim Khrykov
* Varonis Threat Labs
* Vijay Lalwani
* Vinayak Wadhwa, Lucideus
* Will Thomas, Equinix Threat Analysis Center (ETAC)
* Yoshihiro Kori, NEC Corporation
