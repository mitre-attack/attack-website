Title: Updates - April 2024
Date: April 2024
Category: Cyber Threat Intelligence
Authors: Adam Pennington
Template: resources/update-post
url: /resources/updates/updates-april-2024
save_as: resources/updates/updates-april-2024/index.html

| Version | Start Date | End Date | Data | Changelogs |
|:--------|:-----------|:---------|:-----|:-----------|
| [ATT&CK v15](/versions/v15) | April 23, 2024 | October 30, 2024 | [v15.0 on MITRE/CTI](https://github.com/mitre/cti/releases/tag/ATT%26CK-v15.0)<br />[v15.1 on MITRE/CTI](https://github.com/mitre/cti/releases/tag/ATT%26CK-v15.1) | v14.1 - v15.0 [Details](/docs/changelogs/v14.1-v15.0/changelog-detailed.html) ([JSON](/docs/changelogs/v14.1-v15.0/changelog.json))<br />v15.0 - v15.1 [Details](/docs/changelogs/v15.0-v15.1/changelog-detailed.html) ([JSON](/docs/changelogs/v15.0-v15.1/changelog.json)) |

The April 2024 (v15) ATT&CK release updates Techniques, Groups, Campaigns and Software for Enterprise, Mobile, and ICS.

The biggest changes in ATT&CK v15 are a shift in language (from CAR pseudocode to real-world query languages) for analytics in Enterprise detections, detection notes and analytics added to [Enterprise Execution](https://attack.mitre.org/tactics/TA0002/) techniques, improved defensive recommendations for [Cloud](https://attack.mitre.org/matrices/enterprise/cloud/) techniques, and the addition of activity from a number of cyber-criminal and underreported threat groups. An [accompanying blog post](https://medium.com/mitre-attack/attack-v15-26685f300acc) describes these changes as well as additional improvements across ATT&CK's various domains and platforms.

This release also includes a [human-readable detailed changelog](/docs/changelogs/v14.1-v15.0/changelog-detailed.html) showing more specifically what changed in updated ATT&CK objects, and a [machine-readable JSON changelog](/docs/changelogs/v14.1-v15.0/changelog.json), whose format is described in [ATT&CK's Github](https://github.com/mitre-attack/mitreattack-python/blob/master/mitreattack/diffStix/README.md).

This version of ATT&CK contains 794 Pieces of Software, 152 Groups, and 30 Campaigns. Broken out by domain:

* Enterprise: 14 Tactics, 202 Techniques, 435 Sub-Techniques, 148 Groups, 677 Pieces of Software, 28 Campaigns, 43 Mitigations, and 37 Data Sources
* Mobile: 12 Tactics, 73 Techniques, 46 Sub-Techniques, 13 Groups, 113 Pieces of Software, 2 Campaigns, 13 Mitigations, and 6 Data Sources
* ICS: 12 Tactics, 83 Techniques, 0 Sub-Techniques, 14 Groups, 21 Pieces of Software, 6 Campaigns, 52 Mitigations, 14 Assets, and 17 Data Sources

## Release Notes Terminology

* New: ATT&CK objects which are only present in the new release.
* Major version changes: ATT&CK objects that have a major version change. (e.g. 1.0 → 2.0)
* Minor version changes: ATT&CK objects that have a minor version change. (e.g. 1.0 → 1.1)
* Other version changes: ATT&CK objects that have a version change of any other kind. (e.g. 1.0 → 1.2)
* Patches: ATT&CK objects that have been patched while keeping the version the same. (e.g., 1.0 → 1.0 but something immaterial like a typo, a URL, or some metadata was fixed)
* Revocations: ATT&CK objects which are revoked by a different object.
* Deprecations: ATT&CK objects which are deprecated and no longer in use, and not replaced.
* Deletions: ATT&CK objects which are no longer found in the STIX data.

## Techniques

### Enterprise

#### New Techniques

* Abuse Elevation Control Mechanism: [TCC Manipulation](/techniques/T1548/006) <small style="color:#929393">(v1.0)</small>
* Command and Scripting Interpreter: [AutoHotKey & AutoIT](/techniques/T1059/010) <small style="color:#929393">(v1.0)</small>
* Compromise Infrastructure: [Network Devices](/techniques/T1584/008) <small style="color:#929393">(v1.0)</small>
* Create or Modify System Process: [Container Service](/techniques/T1543/005) <small style="color:#929393">(v1.0)</small>
* Hide Artifacts: [File/Path Exclusions](/techniques/T1564/012) <small style="color:#929393">(v1.0)</small>
* [Hide Infrastructure](/techniques/T1665) <small style="color:#929393">(v1.0)</small>
* Hijack Execution Flow: [AppDomainManager](/techniques/T1574/014) <small style="color:#929393">(v1.0)</small>
* Modify Authentication Process: [Conditional Access Policies](/techniques/T1556/009) <small style="color:#929393">(v1.0)</small>
* Obfuscated Files or Information: [Encrypted/Encoded File](/techniques/T1027/013) <small style="color:#929393">(v1.0)</small>
* Obtain Capabilities: [Artificial Intelligence](/techniques/T1588/007) <small style="color:#929393">(v1.0)</small>
* System Binary Proxy Execution: [Electron Applications](/techniques/T1218/015) <small style="color:#929393">(v1.0)</small>
* System Script Proxy Execution: [SyncAppvPublishingServer](/techniques/T1216/002) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [Cloud Administration Command](/techniques/T1651) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Compromise Host Software Binary](/techniques/T1554) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Domain or Tenant Policy Modification](/techniques/T1484) <small style="color:#929393">(v2.0&#8594;v3.0)</small>
    * [Trust Modification](/techniques/T1484/002) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Software Deployment Tools](/techniques/T1072) <small style="color:#929393">(v2.2&#8594;v3.0)</small>

#### Minor Version Changes

* [Abuse Elevation Control Mechanism](/techniques/T1548) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [Temporary Elevated Cloud Access](/techniques/T1548/005) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Account Manipulation: [Additional Cloud Credentials](/techniques/T1098/001) <small style="color:#929393">(v2.6&#8594;v2.7)</small>
* Account Manipulation: [Additional Cloud Roles](/techniques/T1098/003) <small style="color:#929393">(v2.3&#8594;v2.4)</small>
* [Acquire Infrastructure](/techniques/T1583) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
    * [Domains](/techniques/T1583/001) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [Server](/techniques/T1583/004) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Adversary-in-the-Middle](/techniques/T1557) <small style="color:#929393">(v2.3&#8594;v2.4)</small>
* [Application Layer Protocol](/techniques/T1071) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
    * [DNS](/techniques/T1071/004) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [File Transfer Protocols](/techniques/T1071/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Mail Protocols](/techniques/T1071/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Web Protocols](/techniques/T1071/001) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Automated Collection](/techniques/T1119) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Boot or Logon Autostart Execution](/techniques/T1547) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Port Monitors](/techniques/T1547/010) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Time Providers](/techniques/T1547/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Winlogon Helper DLL](/techniques/T1547/004) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Boot or Logon Initialization Scripts](/techniques/T1037) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
    * [RC Scripts](/techniques/T1037/004) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Browser Extensions](/techniques/T1176) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Brute Force: [Credential Stuffing](/techniques/T1110/004) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* Brute Force: [Password Spraying](/techniques/T1110/003) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Cloud Service Dashboard](/techniques/T1538) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Command and Scripting Interpreter: [AppleScript](/techniques/T1059/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Command and Scripting Interpreter: [PowerShell](/techniques/T1059/001) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* Command and Scripting Interpreter: [Unix Shell](/techniques/T1059/004) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Command and Scripting Interpreter: [Windows Command Shell](/techniques/T1059/003) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Compromise Infrastructure](/techniques/T1584) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* Create Account: [Cloud Account](/techniques/T1136/003) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Create or Modify System Process](/techniques/T1543) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Systemd Service](/techniques/T1543/002) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
    * [Windows Service](/techniques/T1543/003) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Credentials from Password Stores](/techniques/T1555) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Securityd Memory](/techniques/T1555/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Data from Information Repositories](/techniques/T1213) <small style="color:#929393">(v3.2&#8594;v3.3)</small>
* [Deploy Container](/techniques/T1610) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Direct Volume Access](/techniques/T1006) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* Disk Wipe: [Disk Content Wipe](/techniques/T1561/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Encrypted Channel](/techniques/T1573) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Asymmetric Cryptography](/techniques/T1573/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Symmetric Cryptography](/techniques/T1573/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Escape to Host](/techniques/T1611) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Establish Accounts](/techniques/T1585) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [Email Accounts](/techniques/T1585/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Event Triggered Execution](/techniques/T1546) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [Installer Packages](/techniques/T1546/016) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Windows Management Instrumentation Event Subscription](/techniques/T1546/003) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Exploit Public-Facing Application](/techniques/T1190) <small style="color:#929393">(v2.4&#8594;v2.5)</small>
* [File and Directory Discovery](/techniques/T1083) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
* [Financial Theft](/techniques/T1657) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Forge Web Credentials: [SAML Tokens](/techniques/T1606/002) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Gather Victim Identity Information](/techniques/T1589) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Hide Artifacts](/techniques/T1564) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Hidden Window](/techniques/T1564/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [NTFS File Attributes](/techniques/T1564/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Hijack Execution Flow: [DLL Search Order Hijacking](/techniques/T1574/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Impair Defenses: [Disable or Modify System Firewall](/techniques/T1562/004) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Impair Defenses: [Indicator Blocking](/techniques/T1562/006) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* Indicator Removal: [Clear Command History](/techniques/T1070/003) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* Indicator Removal: [Clear Windows Event Logs](/techniques/T1070/001) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Ingress Tool Transfer](/techniques/T1105) <small style="color:#929393">(v2.3&#8594;v2.4)</small>
* [Inhibit System Recovery](/techniques/T1490) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* Input Capture: [GUI Input Capture](/techniques/T1056/002) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Internal Spearphishing](/techniques/T1534) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Masquerading](/techniques/T1036) <small style="color:#929393">(v1.6&#8594;v1.7)</small>
* [Modify Authentication Process](/techniques/T1556) <small style="color:#929393">(v2.3&#8594;v2.4)</small>
    * [Multi-Factor Authentication](/techniques/T1556/006) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Multi-Factor Authentication Request Generation](/techniques/T1621) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Network Sniffing](/techniques/T1040) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
* [OS Credential Dumping](/techniques/T1003) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
    * [Cached Domain Credentials](/techniques/T1003/005) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [LSASS Memory](/techniques/T1003/001) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
    * [Proc Filesystem](/techniques/T1003/007) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Obfuscated Files or Information](/techniques/T1027) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
    * [Stripped Payloads](/techniques/T1027/008) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Office Application Startup: [Office Test](/techniques/T1137/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Phishing](/techniques/T1566) <small style="color:#929393">(v2.4&#8594;v2.5)</small>
    * [Spearphishing Link](/techniques/T1566/002) <small style="color:#929393">(v2.5&#8594;v2.6)</small>
* Phishing for Information: [Spearphishing Link](/techniques/T1598/003) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
* [Pre-OS Boot](/techniques/T1542) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [System Firmware](/techniques/T1542/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Process Discovery](/techniques/T1057) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* Proxy: [External Proxy](/techniques/T1090/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Proxy: [Internal Proxy](/techniques/T1090/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Proxy: [Multi-hop Proxy](/techniques/T1090/003) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Reflective Code Loading](/techniques/T1620) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Remote Access Software](/techniques/T1219) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* [Remote Service Session Hijacking](/techniques/T1563) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Remote Services](/techniques/T1021) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Resource Hijacking](/techniques/T1496) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Scheduled Task/Job](/techniques/T1053) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
    * [At](/techniques/T1053/002) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
    * [Scheduled Task](/techniques/T1053/005) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* Server Software Component: [Web Shell](/techniques/T1505/003) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Software Discovery](/techniques/T1518) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
    * [Security Software Discovery](/techniques/T1518/001) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* Stage Capabilities: [Link Target](/techniques/T1608/005) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Steal Application Access Token](/techniques/T1528) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Steal Web Session Cookie](/techniques/T1539) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Steal or Forge Kerberos Tickets](/techniques/T1558) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Subvert Trust Controls](/techniques/T1553) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Supply Chain Compromise](/techniques/T1195) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
    * [Compromise Software Dependencies and Development Tools](/techniques/T1195/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [System Binary Proxy Execution](/techniques/T1218) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [System Time Discovery](/techniques/T1124) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Transfer Data to Cloud Account](/techniques/T1537) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Use Alternate Authentication Material](/techniques/T1550) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [Application Access Token](/techniques/T1550/001) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
* [User Execution](/techniques/T1204) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
* Valid Accounts: [Cloud Accounts](/techniques/T1078/004) <small style="color:#929393">(v1.6&#8594;v1.7)</small>
* Valid Accounts: [Default Accounts](/techniques/T1078/001) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Virtualization/Sandbox Evasion: [System Checks](/techniques/T1497/001) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Windows Management Instrumentation](/techniques/T1047) <small style="color:#929393">(v1.4&#8594;v1.5)</small>

#### Patches

* Access Token Manipulation: [Make and Impersonate Token](/techniques/T1134/003) <small style="color:#929393">(v1.1)</small>
* Access Token Manipulation: [Token Impersonation/Theft](/techniques/T1134/001) <small style="color:#929393">(v1.2)</small>
* [Account Discovery](/techniques/T1087) <small style="color:#929393">(v2.4)</small>
    * [Domain Account](/techniques/T1087/002) <small style="color:#929393">(v1.2)</small>
    * [Local Account](/techniques/T1087/001) <small style="color:#929393">(v1.4)</small>
* [Account Manipulation](/techniques/T1098) <small style="color:#929393">(v2.6)</small>
    * [Additional Email Delegate Permissions](/techniques/T1098/002) <small style="color:#929393">(v2.1)</small>
* Acquire Infrastructure: [Web Services](/techniques/T1583/006) <small style="color:#929393">(v1.2)</small>
* [Archive Collected Data](/techniques/T1560) <small style="color:#929393">(v1.0)</small>
* [Audio Capture](/techniques/T1123) <small style="color:#929393">(v1.0)</small>
* [Automated Exfiltration](/techniques/T1020) <small style="color:#929393">(v1.2)</small>
* [Brute Force](/techniques/T1110) <small style="color:#929393">(v2.5)</small>
* Command and Scripting Interpreter: [Python](/techniques/T1059/006) <small style="color:#929393">(v1.0)</small>
* [Communication Through Removable Media](/techniques/T1092) <small style="color:#929393">(v1.0)</small>
* Compromise Infrastructure: [Server](/techniques/T1584/004) <small style="color:#929393">(v1.2)</small>
* [Create Account](/techniques/T1136) <small style="color:#929393">(v2.4)</small>
    * [Domain Account](/techniques/T1136/002) <small style="color:#929393">(v1.1)</small>
* [Data Manipulation](/techniques/T1565) <small style="color:#929393">(v1.1)</small>
* [Data Obfuscation](/techniques/T1001) <small style="color:#929393">(v1.1)</small>
    * [Junk Data](/techniques/T1001/001) <small style="color:#929393">(v1.0)</small>
* [Group Policy Discovery](/techniques/T1615) <small style="color:#929393">(v1.1)</small>
* [Hijack Execution Flow](/techniques/T1574) <small style="color:#929393">(v1.2)</small>
* Impair Defenses: [Disable or Modify Cloud Logs](/techniques/T1562/008) <small style="color:#929393">(v2.0)</small>
* Impair Defenses: [Disable or Modify Tools](/techniques/T1562/001) <small style="color:#929393">(v1.5)</small>
* Phishing: [Spearphishing Attachment](/techniques/T1566/001) <small style="color:#929393">(v2.2)</small>
* Phishing: [Spearphishing via Service](/techniques/T1566/003) <small style="color:#929393">(v2.0)</small>
* [Serverless Execution](/techniques/T1648) <small style="color:#929393">(v1.0)</small>
* Subvert Trust Controls: [Install Root Certificate](/techniques/T1553/004) <small style="color:#929393">(v1.2)</small>
* [Unsecured Credentials](/techniques/T1552) <small style="color:#929393">(v1.3)</small>
    * [Credentials In Files](/techniques/T1552/001) <small style="color:#929393">(v1.2)</small>
* [Unused/Unsupported Cloud Regions](/techniques/T1535) <small style="color:#929393">(v1.1)</small>

### Mobile

#### New Techniques

* Encrypted Channel: [SSL Pinning](/techniques/T1521/003) <small style="color:#929393">(v1.0)</small>
* [Exploitation for Initial Access](/techniques/T1664) <small style="color:#929393">(v1.0)</small>
* Hide Artifacts: [Conceal Multimedia Files](/techniques/T1628/003) <small style="color:#929393">(v1.0)</small>
* System Network Configuration Discovery: [Internet Connection Discovery](/techniques/T1422/001) <small style="color:#929393">(v1.0)</small>
* System Network Configuration Discovery: [Wi-Fi Discovery](/techniques/T1422/002) <small style="color:#929393">(v1.0)</small>

#### Minor Version Changes

* [Adversary-in-the-Middle](/techniques/T1638) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Steal Application Access Token](/techniques/T1635) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [System Network Configuration Discovery](/techniques/T1422) <small style="color:#929393">(v2.3&#8594;v2.4)</small>

### ICS

#### New Techniques

* [Autorun Image](/techniques/T0895) <small style="color:#929393">(v1.0)</small>
* [System Binary Proxy Execution](/techniques/T0894) <small style="color:#929393">(v1.0)</small>

#### Minor Version Changes

* [Automated Collection](/techniques/T0802) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Network Connection Enumeration](/techniques/T0840) <small style="color:#929393">(v1.1&#8594;v1.2)</small>

#### Patches

* [Data from Local System](/techniques/T0893) <small style="color:#929393">(v1.0)</small>

## Software

### Enterprise

#### New Software

* [AcidRain](/software/S1125) <small style="color:#929393">(v1.0)</small>
* [Akira](/software/S1129) <small style="color:#929393">(v1.0)</small>
* [BUSHWALK](/software/S1118) <small style="color:#929393">(v1.0)</small>
* [COATHANGER](/software/S1105) <small style="color:#929393">(v1.0)</small>
* [Cheerscrypt](/software/S1096) <small style="color:#929393">(v1.0)</small>
* [DarkGate](/software/S1111) <small style="color:#929393">(v1.0)</small>
* [FRAMESTING](/software/S1120) <small style="color:#929393">(v1.0)</small>
* [GLASSTOKEN](/software/S1117) <small style="color:#929393">(v1.0)</small>
* [HUI Loader](/software/S1097) <small style="color:#929393">(v1.0)</small>
* [LIGHTWIRE](/software/S1119) <small style="color:#929393">(v1.0)</small>
* [LITTLELAMB.WOOLTEA](/software/S1121) <small style="color:#929393">(v1.0)</small>
* [LoFiSe](/software/S1101) <small style="color:#929393">(v1.0)</small>
* [Mispadu](/software/S1122) <small style="color:#929393">(v1.0)</small>
* [NGLite](/software/S1106) <small style="color:#929393">(v1.0)</small>
* [NKAbuse](/software/S1107) <small style="color:#929393">(v1.0)</small>
* [Ninja](/software/S1100) <small style="color:#929393">(v1.0)</small>
* [PACEMAKER](/software/S1109) <small style="color:#929393">(v1.0)</small>
* [PITSTOP](/software/S1123) <small style="color:#929393">(v1.0)</small>
* [PULSECHECK](/software/S1108) <small style="color:#929393">(v1.0)</small>
* [Pcexter](/software/S1102) <small style="color:#929393">(v1.0)</small>
* [RAPIDPULSE](/software/S1113) <small style="color:#929393">(v1.0)</small>
* [SLIGHTPULSE](/software/S1110) <small style="color:#929393">(v1.0)</small>
* [SLOWPULSE](/software/S1104) <small style="color:#929393">(v1.0)</small>
* [STEADYPULSE](/software/S1112) <small style="color:#929393">(v1.0)</small>
* [Samurai](/software/S1099) <small style="color:#929393">(v1.0)</small>
* [SocGholish](/software/S1124) <small style="color:#929393">(v1.0)</small>
* [WARPWIRE](/software/S1116) <small style="color:#929393">(v1.0)</small>
* [WIREFIRE](/software/S1115) <small style="color:#929393">(v1.0)</small>
* [ZIPLINE](/software/S1114) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [Bazar](/software/S0534) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [Diavol](/software/S0659) <small style="color:#929393">(v1.0&#8594;v2.0)</small>

#### Minor Version Changes

* [AdFind](/software/S0552) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Anchor](/software/S0504) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Aria-body](/software/S0456) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Astaroth](/software/S0373) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* [Attor](/software/S0438) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [AuditCred](/software/S0347) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Avenger](/software/S0473) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [BADHATCH](/software/S1081) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [BISCUIT](/software/S0017) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [BLINDINGCAN](/software/S0520) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [BLUELIGHT](/software/S0657) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [BOOSTWRITE](/software/S0415) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [BendyBear](/software/S0574) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Bisonal](/software/S0268) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [BitPaymer](/software/S0570) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [CARROTBAT](/software/S0462) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [CaddyWiper](/software/S0693) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Carberp](/software/S0484) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Cardinal RAT](/software/S0348) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [China Chopper](/software/S0020) <small style="color:#929393">(v2.4&#8594;v2.5)</small>
* [Chinoxy](/software/S1041) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Chrommme](/software/S0667) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Cobalt Strike](/software/S0154) <small style="color:#929393">(v1.11&#8594;v1.12)</small>
* [CozyCar](/software/S0046) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [CrackMapExec](/software/S0488) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [DCSrv](/software/S1033) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [DEADEYE](/software/S1052) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [DOGCALL](/software/S0213) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Dacls](/software/S0497) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [DanBot](/software/S1014) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [DarkWatchman](/software/S0673) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Elise](/software/S0081) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Emissary](/software/S0082) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [EnvyScout](/software/S0634) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Exaramel for Linux](/software/S0401) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [FELIXROOT](/software/S0267) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [FIVEHANDS](/software/S0618) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [FlawedGrace](/software/S0383) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [FoggyWeb](/software/S0661) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [FunnyDream](/software/S1044) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Fysbis](/software/S0410) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Gazer](/software/S0168) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Gelsemium](/software/S0666) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [GoldMax](/software/S0588) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* [GoldenSpy](/software/S0493) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Grandoreiro](/software/S0531) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [GravityRAT](/software/S0237) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [GreyEnergy](/software/S0342) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [HAWKBALL](/software/S0391) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [HOMEFRY](/software/S0232) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [HOPLIGHT](/software/S0376) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Helminth](/software/S0170) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [HermeticWiper](/software/S0697) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [HermeticWizard](/software/S0698) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Heyoka Backdoor](/software/S1027) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Hi-Zor](/software/S0087) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [HiddenWasp](/software/S0394) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Hildegard](/software/S0601) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [HotCroissant](/software/S0431) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [HyperBro](/software/S0398) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [IcedID](/software/S0483) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Impacket](/software/S0357) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
* [IronNetInjector](/software/S0581) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [JHUHUGIT](/software/S0044) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [KEYPLUG](/software/S1051) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [KGH_SPY](/software/S0526) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [KONNI](/software/S0356) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Kessel](/software/S0487) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Kevin](/software/S1020) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [KeyBoy](/software/S0387) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Kwampirs](/software/S0236) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [LaZagne](/software/S0349) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
* [LightNeuron](/software/S0395) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [LoudMiner](/software/S0451) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Mafalda](/software/S1060) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Melcoz](/software/S0530) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Metamorfo](/software/S0455) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Micropsia](/software/S0339) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Milan](/software/S1015) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Mimikatz](/software/S0002) <small style="color:#929393">(v1.8&#8594;v1.9)</small>
* [More_eggs](/software/S0284) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [Mosquito](/software/S0256) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [NanHaiShu](/software/S0228) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Net](/software/S0039) <small style="color:#929393">(v2.5&#8594;v2.6)</small>
* [OSX_OCEANLOTUS.D](/software/S0352) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [PS1](/software/S0613) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [PcShare](/software/S1050) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Penquin](/software/S0587) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [PipeMon](/software/S0501) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [PoisonIvy](/software/S0012) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Prikormka](/software/S0113) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [PsExec](/software/S0029) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
* [PyDCrypt](/software/S1032) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [QakBot](/software/S0650) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [RCSession](/software/S0662) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [REvil](/software/S0496) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Raindrop](/software/S0565) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [RainyDay](/software/S0629) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Rclone](/software/S1040) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Reaver](/software/S0172) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [RedLeaves](/software/S0153) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Remexi](/software/S0375) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Remsec](/software/S0125) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Rifdoor](/software/S0433) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Rising Sun](/software/S0448) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [STARWHALE](/software/S1037) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [SUNBURST](/software/S0559) <small style="color:#929393">(v2.4&#8594;v2.5)</small>
* [SUPERNOVA](/software/S0578) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Sakula](/software/S0074) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [SamSam](/software/S0370) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Seasalt](/software/S0345) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Shamoon](/software/S0140) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Shark](/software/S1019) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Skeleton Key](/software/S0007) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Skidmap](/software/S0468) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Sliver](/software/S0633) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Smoke Loader](/software/S0226) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [SpeakUp](/software/S0374) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Squirrelwaffle](/software/S1030) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [StoneDrill](/software/S0380) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [StrongPity](/software/S0491) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Stuxnet](/software/S0603) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [SysUpdate](/software/S0663) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [TINYTYPHON](/software/S0131) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [TYPEFRAME](/software/S0263) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Taidoor](/software/S0011) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Tasklist](/software/S0057) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [ThreatNeedle](/software/S0665) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Torisma](/software/S0678) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [TrickBot](/software/S0266) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [UBoatRAT](/software/S0333) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [USBStealer](/software/S0136) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Uroburos](/software/S0022) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Ursnif](/software/S0386) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [VERMIN](/software/S0257) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Volgmer](/software/S0180) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [WastedLocker](/software/S0612) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Waterbear](/software/S0579) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [WhisperGate](/software/S0689) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [WindTail](/software/S0466) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Winnti for Linux](/software/S0430) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Winnti for Windows](/software/S0141) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [Woody RAT](/software/S1065) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [YAHOYAH](/software/S0388) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [ZeroT](/software/S0230) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Zeus Panda](/software/S0330) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Zox](/software/S0672) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [ZxxZ](/software/S1013) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [gh0st RAT](/software/S0032) <small style="color:#929393">(v3.1&#8594;v3.2)</small>
* [metaMain](/software/S1059) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [netstat](/software/S0104) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [njRAT](/software/S0385) <small style="color:#929393">(v1.5&#8594;v1.6)</small>

#### Patches

* [Industroyer](/software/S0604) <small style="color:#929393">(v1.1)</small>
* [Keydnap](/software/S0276) <small style="color:#929393">(v1.2)</small>
* [WEBC2](/software/S0109) <small style="color:#929393">(v2.0)</small>

### Mobile

#### New Software

* [AhRat](/software/S1095) <small style="color:#929393">(v1.0)</small>
* [BRATA](/software/S1094) <small style="color:#929393">(v1.0)</small>
* [FlixOnline](/software/S1103) <small style="color:#929393">(v1.0)</small>
* [HilalRAT](/software/S1128) <small style="color:#929393">(v1.0)</small>
* [Phenakite](/software/S1126) <small style="color:#929393">(v1.0)</small>

#### Minor Version Changes

* [AndroRAT](/software/S0292) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Pegasus for iOS](/software/S0289) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [eSurv](/software/S0507) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

### ICS

#### Minor Version Changes

* [REvil](/software/S0496) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Stuxnet](/software/S0603) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Triton](/software/S1009) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [VPNFilter](/software/S1010) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Patches

* [Industroyer](/software/S0604) <small style="color:#929393">(v1.1)</small>

## Groups

### Enterprise

#### New Groups

* [APT-C-23](/groups/G1028) <small style="color:#929393">(v1.0)</small>
* [APT5](/groups/G1023) <small style="color:#929393">(v1.0)</small>
* [Akira](/groups/G1024) <small style="color:#929393">(v1.0)</small>
* [Cinnamon Tempest](/groups/G1021) <small style="color:#929393">(v1.0)</small>
* [Malteiro](/groups/G1026) <small style="color:#929393">(v1.0)</small>
* [Mustard Tempest](/groups/G1020) <small style="color:#929393">(v1.0)</small>
* [ToddyCat](/groups/G1022) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [APT28](/groups/G0007) <small style="color:#929393">(v4.0&#8594;v5.0)</small>
* [APT29](/groups/G0016) <small style="color:#929393">(v5.0&#8594;v6.0)</small>
* [APT32](/groups/G0050) <small style="color:#929393">(v2.7&#8594;v3.0)</small>
* [APT33](/groups/G0064) <small style="color:#929393">(v1.4&#8594;v2.0)</small>
* [APT38](/groups/G0082) <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* [APT41](/groups/G0096) <small style="color:#929393">(v3.1&#8594;v4.0)</small>
* [Andariel](/groups/G0138) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [CURIUM](/groups/G1012) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Darkhotel](/groups/G0012) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* [Dragonfly](/groups/G0035) <small style="color:#929393">(v3.2&#8594;v4.0)</small>
* [Earth Lusca](/groups/G1006) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [FIN6](/groups/G0037) <small style="color:#929393">(v3.3&#8594;v4.0)</small>
* [FIN7](/groups/G0046) <small style="color:#929393">(v3.0&#8594;v4.0)</small>
* [Fox Kitten](/groups/G0117) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [GALLIUM](/groups/G0093) <small style="color:#929393">(v3.0&#8594;v4.0)</small>
* [Gamaredon Group](/groups/G0047) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* [HAFNIUM](/groups/G0125) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* [Indrik Spider](/groups/G0119) <small style="color:#929393">(v3.0&#8594;v4.0)</small>
* [Ke3chang](/groups/G0004) <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* [Kimsuky](/groups/G0094) <small style="color:#929393">(v3.1&#8594;v4.0)</small>
* [LAPSUS$](/groups/G1004) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [Lazarus Group](/groups/G0032) <small style="color:#929393">(v3.2&#8594;v4.0)</small>
* [Leviathan](/groups/G0065) <small style="color:#929393">(v3.0&#8594;v4.0)</small>
* [Lotus Blossom](/groups/G0030) <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* [Magic Hound](/groups/G0059) <small style="color:#929393">(v5.2&#8594;v6.0)</small>
* [Moses Staff](/groups/G1009) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [MuddyWater](/groups/G0069) <small style="color:#929393">(v4.1&#8594;v5.0)</small>
* [OilRig](/groups/G0049) <small style="color:#929393">(v3.1&#8594;v4.0)</small>
* [Orangeworm](/groups/G0071) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [POLONIUM](/groups/G1005) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Sandworm Team](/groups/G0034) <small style="color:#929393">(v3.1&#8594;v4.0)</small>
* [Scattered Spider](/groups/G1015) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [TA505](/groups/G0092) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* [Turla](/groups/G0010) <small style="color:#929393">(v4.0&#8594;v5.0)</small>
* [Wizard Spider](/groups/G0102) <small style="color:#929393">(v3.0&#8594;v4.0)</small>
* [ZIRCONIUM](/groups/G0128) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [menuPass](/groups/G0045) <small style="color:#929393">(v2.1&#8594;v3.0)</small>

#### Minor Version Changes

* [APT18](/groups/G0026) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [APT19](/groups/G0073) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
* [APT39](/groups/G0087) <small style="color:#929393">(v3.1&#8594;v3.2)</small>
* [BITTER](/groups/G1002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Blue Mockingbird](/groups/G0108) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Dark Caracal](/groups/G0070) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Elderwood](/groups/G0066) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Group5](/groups/G0043) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [HEXANE](/groups/G1001) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Higaisa](/groups/G0126) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Inception](/groups/G0100) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Metador](/groups/G1013) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Mofang](/groups/G0103) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Molerats](/groups/G0021) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [PROMETHIUM](/groups/G0056) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Putter Panda](/groups/G0024) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Rancor](/groups/G0075) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Sidewinder](/groups/G0121) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [TA2541](/groups/G1018) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [TEMP.Veles](/groups/G0088) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [TeamTNT](/groups/G0139) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Threat Group-3390](/groups/G0027) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Transparent Tribe](/groups/G0134) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Tropic Trooper](/groups/G0081) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Volt Typhoon](/groups/G1017) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Whitefly](/groups/G0107) <small style="color:#929393">(v1.1&#8594;v1.2)</small>

#### Patches

* [APT3](/groups/G0022) <small style="color:#929393">(v1.4)</small>

### Mobile

#### New Groups

* [APT-C-23](/groups/G1028) <small style="color:#929393">(v1.0)</small>
* [BITTER](/groups/G1002) <small style="color:#eb6635">(v1.1)</small>
* [PROMETHIUM](/groups/G0056) <small style="color:#eb6635">(v2.1)</small>
* [Scattered Spider](/groups/G1015) <small style="color:#eb6635">(v2.0)</small>
* [UNC788](/groups/G1029) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [APT28](/groups/G0007) <small style="color:#929393">(v4.0&#8594;v5.0)</small>
* [Earth Lusca](/groups/G1006) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Sandworm Team](/groups/G0034) <small style="color:#929393">(v3.1&#8594;v4.0)</small>

#### Minor Version Changes

* [Dark Caracal](/groups/G0070) <small style="color:#929393">(v1.3&#8594;v1.4)</small>

### ICS

#### New Groups

* [CyberAv3ngers](/groups/G1027) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [APT33](/groups/G0064) <small style="color:#929393">(v1.4&#8594;v2.0)</small>
* [APT38](/groups/G0082) <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* [Dragonfly](/groups/G0035) <small style="color:#929393">(v3.2&#8594;v4.0)</small>
* [FIN6](/groups/G0037) <small style="color:#929393">(v3.3&#8594;v4.0)</small>
* [FIN7](/groups/G0046) <small style="color:#929393">(v3.0&#8594;v4.0)</small>
* [Lazarus Group](/groups/G0032) <small style="color:#929393">(v3.2&#8594;v4.0)</small>
* [OilRig](/groups/G0049) <small style="color:#929393">(v3.1&#8594;v4.0)</small>
* [Sandworm Team](/groups/G0034) <small style="color:#929393">(v3.1&#8594;v4.0)</small>
* [Wizard Spider](/groups/G0102) <small style="color:#929393">(v3.0&#8594;v4.0)</small>

#### Minor Version Changes

* [HEXANE](/groups/G1001) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [TEMP.Veles](/groups/G0088) <small style="color:#929393">(v1.3&#8594;v1.4)</small>

## Campaigns

### Enterprise

#### New Campaigns

* [2022 Ukraine Electric Power Attack](/campaigns/C0034) <small style="color:#929393">(v1.0)</small>
* [C0032](/campaigns/C0032) <small style="color:#929393">(v1.0)</small>
* [C0033](/campaigns/C0033) <small style="color:#929393">(v1.0)</small>
* [Cutting Edge](/campaigns/C0029) <small style="color:#929393">(v1.0)</small>
* [Triton Safety Instrumented System Attack](/campaigns/C0030) <small style="color:#929393">(v1.0)</small>

#### Minor Version Changes

* [Night Dragon](/campaigns/C0002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Operation Dream Job](/campaigns/C0022) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Operation Dust Storm](/campaigns/C0016) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Operation Honeybee](/campaigns/C0006) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Operation Spalax](/campaigns/C0005) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

### Mobile

#### New Campaigns

* [C0033](/campaigns/C0033) <small style="color:#929393">(v1.0)</small>

#### Minor Version Changes

* [Operation Dust Storm](/campaigns/C0016) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

### ICS

#### New Campaigns

* [2022 Ukraine Electric Power Attack](/campaigns/C0034) <small style="color:#929393">(v1.0)</small>
* [Triton Safety Instrumented System Attack](/campaigns/C0030) <small style="color:#929393">(v1.0)</small>
* [Unitronics Defacement Campaign](/campaigns/C0031) <small style="color:#929393">(v1.0)</small>

## Mitigations

### Enterprise

#### Minor Version Changes

* [Software Configuration](/mitigations/M1054) <small style="color:#929393">(v1.1&#8594;v1.2)</small>

### Mobile

#### New Mitigations

* [Do Not Mitigate](/mitigations/M1059) <small style="color:#929393">(v1.0)</small>

## Data Components

### Mobile

#### New Data Components

* [Application Assets](/datasources/DS0041/#Application%20Assets) <small style="color:#929393">(v1.0)</small>

## Contributors to this release

* @_montysecurity
* Alexander Rodchenko
* Ami Holeston
* Andrew Northern, @ex_raritas
* Blake Strom, Microsoft Threat Intelligence
* BT Security
* Daniel Fernando Soriano Espinosa
* David Galazin @themalwareman1
* Debabrata Sharma
* Denise Tan
* Diyar Saadi Ali
* Dragos Threat Intelligence
* Dray Agha, @Purp1eW0lf, Huntress Labs
* Eduardo Chavarro Ovalle
* Edward Stevens
* Eliav Livneh
* Eliraz Levi, Hunters
* Gabriel Currie
* Gavin Knapp
* Goldstein Menachem
* Harjot Shah Singh
* Harun Küßner
* Hen Porcilan
* Hiroki Nagahama, NEC Corporation
* Ivy Bostock
* Jai Minton, @Cyberraiju
* Jeremy Hedges
* Jiraput Thamsongkrah
* Joas Antonio dos Santos, @C0d3Cr4zy
* Joe Wise
* Joshua Penny
* Kostya Vasilkov
* Liran Ravich, CardinalOps
* Manikantan Srinivasan, NEC Corporation India
* Marina Liang
* Mark Tsipershtein
* Matt Mullins
* Monty
* Nikita Rostovcev, Group-IB
* Nikola Kovac
* Obsidian Security
* Pooja Natarajan, NEC Corporation India
* Rahmat Nurfauzi, @infosecn1nja, PT Xynexis International
* Sam Seabrook, Duke Energy
* SCILabs
* Selena Larson, @selenalarson
* Serhii Melnyk, Trustwave SpiderLabs
* Shankar Raman, Amrita University, Gen Digital, Traboda
* Shaul Vilkomir-Preisman
* Sittikorn Sangrattanapitak
* Takahashi Wataru, NEC Corporation
* Tamir Yehuda
* Thomas B
* Tim (Wadhwa-)Brown
* Tristan Madani
* TruKno
* Vectra AI
* Viren Chaudhari, Qualys
* Will Alexander
* Wirapong Petshagun
* Yves Yonan
