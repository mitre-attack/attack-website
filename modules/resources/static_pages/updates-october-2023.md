Title: Updates - October 2023
Date: October 2023
Category: Cyber Threat Intelligence
Authors: Adam Pennington
Template: resources/update-post
url: /resources/updates/updates-october-2023
save_as: resources/updates/updates-october-2023/index.html

| Version | Start Date | End Date | Data | Changelogs |
|:--------|:-----------|:---------|:-----|:-----------|
| [ATT&CK v14](/versions/v14) | October 31, 2023 | April 22, 2024 | [v14.0 on MITRE/CTI](https://github.com/mitre/cti/releases/tag/ATT%26CK-v14.0)<br />[v14.1 on MITRE/CTI](https://github.com/mitre/cti/releases/tag/ATT%26CK-v14.1) | 13.1 - 14.0 [Details](/docs/changelogs/v13.1-v14.0/changelog-detailed.html) ([JSON](/docs/changelogs/v13.1-v14.0/changelog.json))<br />14.0 - 14.1 [Details](/docs/changelogs/v14.0-v14.1/changelog-detailed.html) ([JSON](/docs/changelogs/v14.0-v14.1/changelog.json)) |

The October 2023 (v14) ATT&CK release updates Techniques, Groups, Campaigns and Software for Enterprise, Mobile, and ICS. The biggest changes in ATT&CK v14 are a large expansion of detection notes and analytics to Techniques in Enterprise, a minor scoping change to Enterprise resulting in coverage of [Financial Theft](/techniques/T1657) and [Voice](/techniques/T1566/004) [Phishing](/techniques/T1598/004), structured Detections in Mobile, and the (re-)addition of [Assets](/assets) to ICS. An [accompanying blog post](https://medium.com/mitre-attack/attack-v14-fa473603f86b
) describes these changes as well as improvements across ATT&CK's various domains and platforms.

This release also includes a [human-readable detailed changelog](/docs/changelogs/v13.1-v14.0/changelog-detailed.html) showing more specifically what changed in updated ATT&CK objects, and a [machine-readable JSON changelog](/docs/changelogs/v13.1-v14.0/changelog.json), whose format is described in [ATT&CK's Github](https://github.com/mitre-attack/mitreattack-python/blob/master/mitreattack/diffStix/README.md).

This version of ATT&CK contains 760 Pieces of Software, 143 Groups, and 24 Campaigns. Broken out by domain:

* Enterprise: 201 Techniques, 424 Sub-Techniques, 141 Groups, 648 Pieces of Software, 23 Campaigns, 43 Mitigations, and 109 Data Sources
* Mobile: 72 Techniques, 42 Sub-Techniques, 8 Groups, 108 Pieces of Software, 1 Campaign, 12 Mitigations, and 15 Data Sources
* ICS: 81 Techniques, 13 Groups, 21 Pieces of Software, 52 Mitigations, 3 Campaigns, 14 Assets, and 34 Data Sources

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

* Abuse Elevation Control Mechanism: [Temporary Elevated Cloud Access](/techniques/T1548/005) <small style="color:#929393">(v1.0)</small>
* Account Manipulation: [Additional Container Cluster Roles](/techniques/T1098/006) <small style="color:#929393">(v1.0)</small>
* [Content Injection](/techniques/T1659) <small style="color:#929393">(v1.0)</small>
* Credentials from Password Stores: [Cloud Secrets Management Stores](/techniques/T1555/006) <small style="color:#929393">(v1.0)</small>
* Exfiltration Over Web Service: [Exfiltration Over Webhook](/techniques/T1567/004) <small style="color:#929393">(v1.0)</small>
* [Financial Theft](/techniques/T1657) <small style="color:#929393">(v1.0)</small>
* Hide Artifacts: [Ignore Process Interrupts](/techniques/T1564/011) <small style="color:#929393">(v1.0)</small>
* Impair Defenses: [Disable or Modify Linux Audit System](/techniques/T1562/012) <small style="color:#929393">(v1.0)</small>
* [Impersonation](/techniques/T1656) <small style="color:#929393">(v1.0)</small>
* [Log Enumeration](/techniques/T1654) <small style="color:#929393">(v1.0)</small>
* Masquerading: [Break Process Trees](/techniques/T1036/009) <small style="color:#929393">(v1.0)</small>
* Modify Cloud Compute Infrastructure: [Modify Cloud Compute Configurations](/techniques/T1578/005) <small style="color:#929393">(v1.0)</small>
* Obfuscated Files or Information: [LNK Icon Smuggling](/techniques/T1027/012) <small style="color:#929393">(v1.0)</small>
* Phishing: [Spearphishing Voice](/techniques/T1566/004) <small style="color:#929393">(v1.0)</small>
* Phishing for Information: [Spearphishing Voice](/techniques/T1598/004) <small style="color:#929393">(v1.0)</small>
* [Power Settings](/techniques/T1653) <small style="color:#929393">(v1.0)</small>
* Remote Services: [Direct Cloud VM Connections](/techniques/T1021/008) <small style="color:#929393">(v1.0)</small>
* System Network Configuration Discovery: [Wi-Fi Discovery](/techniques/T1016/002) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* Boot or Logon Autostart Execution: [Registry Run Keys / Startup Folder](/techniques/T1547/001) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Impair Defenses: [Disable or Modify Cloud Logs](/techniques/T1562/008) <small style="color:#929393">(v1.3&#8594;v2.0)</small>

#### Minor Version Changes

* [Abuse Elevation Control Mechanism](/techniques/T1548) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Access Token Manipulation: [Token Impersonation/Theft](/techniques/T1134/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Account Manipulation](/techniques/T1098) <small style="color:#929393">(v2.5&#8594;v2.6)</small>
  * [Additional Cloud Credentials](/techniques/T1098/001) <small style="color:#929393">(v2.5&#8594;v2.6)</small>
  * [Additional Cloud Roles](/techniques/T1098/003) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
  * [Additional Email Delegate Permissions](/techniques/T1098/002) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
  * [Device Registration](/techniques/T1098/005) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
  * [SSH Authorized Keys](/techniques/T1098/004) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Acquire Infrastructure](/techniques/T1583) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Adversary-in-the-Middle](/techniques/T1557) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* Application Layer Protocol: [File Transfer Protocols](/techniques/T1071/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Application Layer Protocol: [Web Protocols](/techniques/T1071/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Archive Collected Data: [Archive via Utility](/techniques/T1560/001) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Boot or Logon Autostart Execution: [Print Processors](/techniques/T1547/012) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Boot or Logon Autostart Execution: [Winlogon Helper DLL](/techniques/T1547/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Boot or Logon Autostart Execution: [XDG Autostart Entries](/techniques/T1547/013) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Boot or Logon Initialization Scripts](/techniques/T1037) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* Brute Force: [Credential Stuffing](/techniques/T1110/004) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* Brute Force: [Password Guessing](/techniques/T1110/001) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* Brute Force: [Password Spraying](/techniques/T1110/003) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Cloud Service Dashboard](/techniques/T1538) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Command and Scripting Interpreter: [Windows Command Shell](/techniques/T1059/003) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Compromise Client Software Binary](/techniques/T1554) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Compromise Infrastructure](/techniques/T1584) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Create Account](/techniques/T1136) <small style="color:#929393">(v2.3&#8594;v2.4)</small>
  * [Cloud Account](/techniques/T1136/003) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
  * [Domain Account](/techniques/T1136/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Local Account](/techniques/T1136/001) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Create or Modify System Process: [Systemd Service](/techniques/T1543/002) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* Create or Modify System Process: [Windows Service](/techniques/T1543/003) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Credentials from Password Stores](/techniques/T1555) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Data Destruction](/techniques/T1485) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Data from Cloud Storage](/techniques/T1530) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Data from Network Shared Drive](/techniques/T1039) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Deobfuscate/Decode Files or Information](/techniques/T1140) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Direct Volume Access](/techniques/T1006) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Email Collection](/techniques/T1114) <small style="color:#929393">(v2.4&#8594;v2.5)</small>
  * [Remote Email Collection](/techniques/T1114/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Event Triggered Execution: [Screensaver](/techniques/T1546/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Exfiltration Over Other Network Medium](/techniques/T1011) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Exfiltration Over Web Service](/techniques/T1567) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
  * [Exfiltration to Cloud Storage](/techniques/T1567/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
  * [Exfiltration to Code Repository](/techniques/T1567/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Exploitation for Credential Access](/techniques/T1212) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Exploitation for Defense Evasion](/techniques/T1211) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* File and Directory Permissions Modification: [Linux and Mac File and Directory Permissions Modification](/techniques/T1222/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Forced Authentication](/techniques/T1187) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Forge Web Credentials](/techniques/T1606) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* Hide Artifacts: [Email Hiding Rules](/techniques/T1564/008) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Hijack Execution Flow: [Path Interception by PATH Environment Variable](/techniques/T1574/007) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Impair Defenses](/techniques/T1562) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
  * [Disable Windows Event Logging](/techniques/T1562/002) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
  * [Disable or Modify Tools](/techniques/T1562/001) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
  * [Downgrade Attack](/techniques/T1562/010) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
  * [Indicator Blocking](/techniques/T1562/006) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Indicator Removal: [Clear Network Connection History and Configurations](/techniques/T1070/007) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Indicator Removal: [Clear Windows Event Logs](/techniques/T1070/001) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Ingress Tool Transfer](/techniques/T1105) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* [Inhibit System Recovery](/techniques/T1490) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Input Capture: [Keylogging](/techniques/T1056/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Inter-Process Communication: [Dynamic Data Exchange](/techniques/T1559/002) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Lateral Tool Transfer](/techniques/T1570) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Masquerading](/techniques/T1036) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
  * [Masquerade Task or Service](/techniques/T1036/004) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
  * [Match Legitimate Name or Location](/techniques/T1036/005) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Modify Authentication Process: [Multi-Factor Authentication](/techniques/T1556/006) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Modify Cloud Compute Infrastructure](/techniques/T1578) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Modify Registry](/techniques/T1112) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Native API](/techniques/T1106) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Network Service Discovery](/techniques/T1046) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [Network Share Discovery](/techniques/T1135) <small style="color:#929393">(v3.1&#8594;v3.2)</small>
* [Network Sniffing](/techniques/T1040) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Non-Application Layer Protocol](/techniques/T1095) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* OS Credential Dumping: [LSASS Memory](/techniques/T1003/001) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* OS Credential Dumping: [NTDS](/techniques/T1003/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* OS Credential Dumping: [Security Account Manager](/techniques/T1003/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Obfuscated Files or Information](/techniques/T1027) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
  * [Embedded Payloads](/techniques/T1027/009) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [HTML Smuggling](/techniques/T1027/006) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Phishing](/techniques/T1566) <small style="color:#929393">(v2.3&#8594;v2.4)</small>
  * [Spearphishing Link](/techniques/T1566/002) <small style="color:#929393">(v2.4&#8594;v2.5)</small>
* [Phishing for Information](/techniques/T1598) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
  * [Spearphishing Link](/techniques/T1598/003) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Process Discovery](/techniques/T1057) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* Process Injection: [Dynamic-link Library Injection](/techniques/T1055/001) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Process Injection: [Process Hollowing](/techniques/T1055/012) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Reflective Code Loading](/techniques/T1620) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Remote Access Software](/techniques/T1219) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* Remote Service Session Hijacking: [RDP Hijacking](/techniques/T1563/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Remote Services](/techniques/T1021) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
  * [Distributed Component Object Model](/techniques/T1021/003) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
  * [Remote Desktop Protocol](/techniques/T1021/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
  * [SMB/Windows Admin Shares](/techniques/T1021/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
  * [SSH](/techniques/T1021/004) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
  * [Windows Remote Management](/techniques/T1021/006) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Remote System Discovery](/techniques/T1018) <small style="color:#929393">(v3.4&#8594;v3.5)</small>
* [Resource Hijacking](/techniques/T1496) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* Scheduled Task/Job: [At](/techniques/T1053/002) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Scheduled Task/Job: [Scheduled Task](/techniques/T1053/005) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* Scheduled Task/Job: [Systemd Timers](/techniques/T1053/006) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Shared Modules](/techniques/T1129) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Software Deployment Tools](/techniques/T1072) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* Subvert Trust Controls: [Install Root Certificate](/techniques/T1553/004) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* System Binary Proxy Execution: [Rundll32](/techniques/T1218/011) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [System Network Configuration Discovery](/techniques/T1016) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
* [System Owner/User Discovery](/techniques/T1033) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* System Services: [Service Execution](/techniques/T1569/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Taint Shared Content](/techniques/T1080) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* Trusted Developer Utilities Proxy Execution: [MSBuild](/techniques/T1127/001) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Unsecured Credentials: [Credentials In Files](/techniques/T1552/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Unsecured Credentials: [Credentials in Registry](/techniques/T1552/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Use Alternate Authentication Material: [Pass the Hash](/techniques/T1550/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Valid Accounts: [Cloud Accounts](/techniques/T1078/004) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
* Valid Accounts: [Domain Accounts](/techniques/T1078/002) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* Valid Accounts: [Local Accounts](/techniques/T1078/003) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Windows Management Instrumentation](/techniques/T1047) <small style="color:#929393">(v1.3&#8594;v1.4)</small>

#### Patches

* [Cloud Service Discovery](/techniques/T1526) <small style="color:#929393">(v1.3)</small>
* Event Triggered Execution: [PowerShell Profile](/techniques/T1546/013) <small style="color:#929393">(v1.1)</small>
* Forge Web Credentials: [SAML Tokens](/techniques/T1606/002) <small style="color:#929393">(v1.2)</small>
* Forge Web Credentials: [Web Cookies](/techniques/T1606/001) <small style="color:#929393">(v1.1)</small>
* Masquerading: [Masquerade File Type](/techniques/T1036/008) <small style="color:#929393">(v1.0)</small>
* Masquerading: [Rename System Utilities](/techniques/T1036/003) <small style="color:#929393">(v1.1)</small>
* OS Credential Dumping: [Cached Domain Credentials](/techniques/T1003/005) <small style="color:#929393">(v1.0)</small>
* [Replication Through Removable Media](/techniques/T1091) <small style="color:#929393">(v1.2)</small>
* [Steal Application Access Token](/techniques/T1528) <small style="color:#929393">(v1.2)</small>
* [Steal Web Session Cookie](/techniques/T1539) <small style="color:#929393">(v1.2)</small>
* System Binary Proxy Execution: [Compiled HTML File](/techniques/T1218/001) <small style="color:#929393">(v2.1)</small>
* Use Alternate Authentication Material: [Application Access Token](/techniques/T1550/001) <small style="color:#929393">(v1.5)</small>
* Use Alternate Authentication Material: [Web Session Cookie](/techniques/T1550/004) <small style="color:#929393">(v1.3)</small>

### Mobile

#### New Techniques

* [Application Versioning](/techniques/T1661) <small style="color:#929393">(v1.0)</small>
* [Data Destruction](/techniques/T1662) <small style="color:#929393">(v1.0)</small>
* [Exploitation for Client Execution](/techniques/T1658) <small style="color:#929393">(v1.0)</small>
* [Masquerading](/techniques/T1655) <small style="color:#929393">(v1.0)</small>
  * [Match Legitimate Name or Location](/techniques/T1655/001) <small style="color:#929393">(v1.0)</small>
* [Phishing](/techniques/T1660) <small style="color:#929393">(v1.0)</small>
* [Remote Access Software](/techniques/T1663) <small style="color:#929393">(v1.0)</small>

#### Minor Version Changes

* [Call Control](/techniques/T1616) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Command and Scripting Interpreter](/techniques/T1623) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
  * [Unix Shell](/techniques/T1623/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Download New Code at Runtime](/techniques/T1407) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Drive-By Compromise](/techniques/T1456) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Dynamic Resolution](/techniques/T1637) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Domain Generation Algorithms](/techniques/T1637/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Exfiltration Over Alternative Protocol](/techniques/T1639) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Exfiltration Over Unencrypted Non-C2 Protocol](/techniques/T1639/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Exfiltration Over C2 Channel](/techniques/T1646) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Impair Defenses: [Prevent Application Removal](/techniques/T1629/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Ingress Tool Transfer](/techniques/T1544) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Input Injection](/techniques/T1516) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Lockscreen Bypass](/techniques/T1461) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Obfuscated Files or Information](/techniques/T1406) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [Replication Through Removable Media](/techniques/T1458) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Web Service](/techniques/T1481) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
  * [Bidirectional Communication](/techniques/T1481/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
  * [Dead Drop Resolver](/techniques/T1481/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
  * [One-Way Communication](/techniques/T1481/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>

#### Patches

* [Credentials from Password Store](/techniques/T1634) <small style="color:#929393">(v1.1)</small>
* [Exploitation for Privilege Escalation](/techniques/T1404) <small style="color:#929393">(v2.1)</small>
* Hijack Execution Flow: [System Runtime API Hijacking](/techniques/T1625/001) <small style="color:#929393">(v1.1)</small>
* Location Tracking: [Impersonate SS7 Nodes](/techniques/T1430/002) <small style="color:#929393">(v1.1)</small>
* [Non-Standard Port](/techniques/T1509) <small style="color:#929393">(v2.1)</small>

### ICS

#### Minor Version Changes

* [Block Command Message](/techniques/T0803) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Modify Controller Tasking](/techniques/T0821) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Modify Parameter](/techniques/T0836) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Modify Program](/techniques/T0889) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Service Stop](/techniques/T0881) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Patches

* [Activate Firmware Update Mode](/techniques/T0800) <small style="color:#929393">(v1.0)</small>
* [Adversary-in-the-Middle](/techniques/T0830) <small style="color:#929393">(v2.0)</small>
* [Alarm Suppression](/techniques/T0878) <small style="color:#929393">(v1.2)</small>
* [Automated Collection](/techniques/T0802) <small style="color:#929393">(v1.0)</small>
* [Block Reporting Message](/techniques/T0804) <small style="color:#929393">(v1.0)</small>
* [Block Serial COM](/techniques/T0805) <small style="color:#929393">(v1.1)</small>
* [Brute Force I/O](/techniques/T0806) <small style="color:#929393">(v1.1)</small>
* [Change Credential](/techniques/T0892) <small style="color:#929393">(v1.0)</small>
* [Change Operating Mode](/techniques/T0858) <small style="color:#929393">(v1.0)</small>
* [Command-Line Interface](/techniques/T0807) <small style="color:#929393">(v1.1)</small>
* [Commonly Used Port](/techniques/T0885) <small style="color:#929393">(v1.1)</small>
* [Connection Proxy](/techniques/T0884) <small style="color:#929393">(v1.1)</small>
* [Damage to Property](/techniques/T0879) <small style="color:#929393">(v1.1)</small>
* [Data Destruction](/techniques/T0809) <small style="color:#929393">(v1.0)</small>
* [Data from Information Repositories](/techniques/T0811) <small style="color:#929393">(v1.2)</small>
* [Data from Local System](/techniques/T0893) <small style="color:#929393">(v1.0)</small>
* [Default Credentials](/techniques/T0812) <small style="color:#929393">(v1.0)</small>
* [Denial of Control](/techniques/T0813) <small style="color:#929393">(v1.1)</small>
* [Denial of Service](/techniques/T0814) <small style="color:#929393">(v1.1)</small>
* [Denial of View](/techniques/T0815) <small style="color:#929393">(v1.1)</small>
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
* [Hardcoded Credentials](/techniques/T0891) <small style="color:#929393">(v1.0)</small>
* [Hooking](/techniques/T0874) <small style="color:#929393">(v1.2)</small>
* [I/O Image](/techniques/T0877) <small style="color:#929393">(v1.1)</small>
* [Indicator Removal on Host](/techniques/T0872) <small style="color:#929393">(v1.0)</small>
* [Internet Accessible Device](/techniques/T0883) <small style="color:#929393">(v1.0)</small>
* [Lateral Tool Transfer](/techniques/T0867) <small style="color:#929393">(v1.1)</small>
* [Loss of Availability](/techniques/T0826) <small style="color:#929393">(v1.0)</small>
* [Loss of Control](/techniques/T0827) <small style="color:#929393">(v1.0)</small>
* [Loss of Productivity and Revenue](/techniques/T0828) <small style="color:#929393">(v1.0)</small>
* [Loss of Protection](/techniques/T0837) <small style="color:#929393">(v1.0)</small>
* [Loss of Safety](/techniques/T0880) <small style="color:#929393">(v1.0)</small>
* [Loss of View](/techniques/T0829) <small style="color:#929393">(v1.0)</small>
* [Manipulate I/O Image](/techniques/T0835) <small style="color:#929393">(v1.1)</small>
* [Manipulation of Control](/techniques/T0831) <small style="color:#929393">(v1.0)</small>
* [Manipulation of View](/techniques/T0832) <small style="color:#929393">(v1.0)</small>
* [Masquerading](/techniques/T0849) <small style="color:#929393">(v1.1)</small>
* [Modify Alarm Settings](/techniques/T0838) <small style="color:#929393">(v1.2)</small>
* [Module Firmware](/techniques/T0839) <small style="color:#929393">(v1.1)</small>
* [Monitor Process State](/techniques/T0801) <small style="color:#929393">(v1.0)</small>
* [Native API](/techniques/T0834) <small style="color:#929393">(v1.0)</small>
* [Network Connection Enumeration](/techniques/T0840) <small style="color:#929393">(v1.1)</small>
* [Network Sniffing](/techniques/T0842) <small style="color:#929393">(v1.0)</small>
* [Point & Tag Identification](/techniques/T0861) <small style="color:#929393">(v1.1)</small>
* [Program Download](/techniques/T0843) <small style="color:#929393">(v1.1)</small>
* [Program Upload](/techniques/T0845) <small style="color:#929393">(v1.0)</small>
* [Project File Infection](/techniques/T0873) <small style="color:#929393">(v1.0)</small>
* [Remote Services](/techniques/T0886) <small style="color:#929393">(v1.1)</small>
* [Remote System Discovery](/techniques/T0846) <small style="color:#929393">(v1.1)</small>
* [Remote System Information Discovery](/techniques/T0888) <small style="color:#929393">(v1.1)</small>
* [Replication Through Removable Media](/techniques/T0847) <small style="color:#929393">(v1.0)</small>
* [Rogue Master](/techniques/T0848) <small style="color:#929393">(v1.2)</small>
* [Rootkit](/techniques/T0851) <small style="color:#929393">(v1.1)</small>
* [Screen Capture](/techniques/T0852) <small style="color:#929393">(v1.0)</small>
* [Scripting](/techniques/T0853) <small style="color:#929393">(v1.0)</small>
* [Spearphishing Attachment](/techniques/T0865) <small style="color:#929393">(v1.1)</small>
* [Spoof Reporting Message](/techniques/T0856) <small style="color:#929393">(v1.2)</small>
* [Standard Application Layer Protocol](/techniques/T0869) <small style="color:#929393">(v1.0)</small>
* [Supply Chain Compromise](/techniques/T0862) <small style="color:#929393">(v1.1)</small>
* [System Firmware](/techniques/T0857) <small style="color:#929393">(v1.1)</small>
* [Theft of Operational Information](/techniques/T0882) <small style="color:#929393">(v1.0)</small>
* [Transient Cyber Asset](/techniques/T0864) <small style="color:#929393">(v1.2)</small>
* [Unauthorized Command Message](/techniques/T0855) <small style="color:#929393">(v1.2)</small>
* [User Execution](/techniques/T0863) <small style="color:#929393">(v1.1)</small>
* [Valid Accounts](/techniques/T0859) <small style="color:#929393">(v1.1)</small>
* [Wireless Compromise](/techniques/T0860) <small style="color:#929393">(v1.2)</small>
* [Wireless Sniffing](/techniques/T0887) <small style="color:#929393">(v1.1)</small>

## Software

### Enterprise

#### New Software

* [ANDROMEDA](/software/S1074) <small style="color:#929393">(v1.0)</small>
* [AsyncRAT](/software/S1087) <small style="color:#929393">(v1.0)</small>
* [BADHATCH](/software/S1081) <small style="color:#929393">(v1.0)</small>
* [Disco](/software/S1088) <small style="color:#929393">(v1.0)</small>
* [KOPILUWAK](/software/S1075) <small style="color:#929393">(v1.0)</small>
* [NightClub](/software/S1090) <small style="color:#929393">(v1.0)</small>
* [Pacu](/software/S1091) <small style="color:#929393">(v1.0)</small>
* [QUIETCANARY](/software/S1076) <small style="color:#929393">(v1.0)</small>
* [QUIETEXIT](/software/S1084) <small style="color:#929393">(v1.0)</small>
* [RotaJakiro](/software/S1078) <small style="color:#929393">(v1.0)</small>
* [Sardonic](/software/S1085) <small style="color:#929393">(v1.0)</small>
* [SharpDisco](/software/S1089) <small style="color:#929393">(v1.0)</small>
* [Snip3](/software/S1086) <small style="color:#929393">(v1.0)</small>
* [ngrok](/software/S0508) <small style="color:#eb6635">(v1.2)</small>

#### Major Version Changes

* [OSX_OCEANLOTUS.D](/software/S0352) <small style="color:#929393">(v2.2&#8594;v3.0)</small>
* [Uroburos](/software/S0022) <small style="color:#929393">(v1.0&#8594;v2.0)</small>

#### Minor Version Changes

* [AdFind](/software/S0552) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Agent Tesla](/software/S0331) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Arp](/software/S0099) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [BITSAdmin](/software/S0190) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [BlackEnergy](/software/S0089) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [BloodHound](/software/S0521) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Cobalt Strike](/software/S0154) <small style="color:#929393">(v1.10&#8594;v1.11)</small>
* [Conti](/software/S0575) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [CrossRAT](/software/S0235) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Dridex](/software/S0384) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Emotet](/software/S0367) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Empire](/software/S0363) <small style="color:#929393">(v1.6&#8594;v1.7)</small>
* [Fysbis](/software/S0410) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [GoldMax](/software/S0588) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Imminent Monitor](/software/S0434) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Impacket](/software/S0357) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [KillDisk](/software/S0607) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [LaZagne](/software/S0349) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Mimikatz](/software/S0002) <small style="color:#929393">(v1.7&#8594;v1.8)</small>
* [NETWIRE](/software/S0198) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
* [Net](/software/S0039) <small style="color:#929393">(v2.4&#8594;v2.5)</small>
* [Nltest](/software/S0359) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [OSX/Shlayer](/software/S0402) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Ping](/software/S0097) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [PsExec](/software/S0029) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Pupy](/software/S0192) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Ragnar Locker](/software/S0481) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Regin](/software/S0019) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Revenge RAT](/software/S0379) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Rubeus](/software/S1071) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Ryuk](/software/S0446) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [TrickBot](/software/S0266) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [WarzoneRAT](/software/S0670) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [certutil](/software/S0160) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [esentutl](/software/S0404) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [jRAT](/software/S0283) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [netstat](/software/S0104) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [njRAT](/software/S0385) <small style="color:#929393">(v1.4&#8594;v1.5)</small>

#### Patches

* [BlackCat](/software/S1068) <small style="color:#929393">(v1.0)</small>
* [Calisto](/software/S0274) <small style="color:#929393">(v1.1)</small>
* [Carbanak](/software/S0030) <small style="color:#929393">(v1.1)</small>
* [Doki](/software/S0600) <small style="color:#929393">(v1.0)</small>
* [Industroyer](/software/S0604) <small style="color:#929393">(v1.1)</small>
* [LockerGoga](/software/S0372) <small style="color:#929393">(v2.0)</small>
* [PUNCHBUGGY](/software/S0196) <small style="color:#929393">(v2.1)</small>
* [PUNCHTRACK](/software/S0197) <small style="color:#929393">(v1.1)</small>
* [PowerSploit](/software/S0194) <small style="color:#929393">(v1.6)</small>

#### Revocations

* Ngrok (revoked by [ngrok](/software/S0508)) <small style="color:#929393">(v1.1)</small>

### Mobile

#### New Software

* [BOULDSPY](/software/S1079) <small style="color:#929393">(v1.0)</small>
* [Chameleon](/software/S1083) <small style="color:#929393">(v1.0)</small>
* [Escobar](/software/S1092) <small style="color:#929393">(v1.0)</small>
* [Fakecalls](/software/S1080) <small style="color:#929393">(v1.0)</small>
* [FlyTrap](/software/S1093) <small style="color:#929393">(v1.0)</small>
* [Hornbill](/software/S1077) <small style="color:#929393">(v1.0)</small>
* [Sunbird](/software/S1082) <small style="color:#929393">(v1.0)</small>

### ICS

#### Minor Version Changes

* [BlackEnergy](/software/S0089) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [KillDisk](/software/S0607) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Ryuk](/software/S0446) <small style="color:#929393">(v1.3&#8594;v1.4)</small>

#### Patches

* [Industroyer](/software/S0604) <small style="color:#929393">(v1.1)</small>
* [LockerGoga](/software/S0372) <small style="color:#929393">(v2.0)</small>

## Groups

### Enterprise

#### New Groups

* [FIN13](/groups/G1016) <small style="color:#929393">(v1.0)</small>
* [MoustachedBouncer](/groups/G1019) <small style="color:#929393">(v1.0)</small>
* [Scattered Spider](/groups/G1015) <small style="color:#929393">(v1.0)</small>
* [TA2541](/groups/G1018) <small style="color:#929393">(v1.0)</small>
* [Volt Typhoon](/groups/G1017) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [APT29](/groups/G0016) <small style="color:#929393">(v4.0&#8594;v5.0)</small>
* [FIN7](/groups/G0046) <small style="color:#929393">(v2.2&#8594;v3.0)</small>
* [FIN8](/groups/G0061) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* [Indrik Spider](/groups/G0119) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* [Turla](/groups/G0010) <small style="color:#929393">(v3.1&#8594;v4.0)</small>
* [Wizard Spider](/groups/G0102) <small style="color:#929393">(v2.1&#8594;v3.0)</small>

#### Minor Version Changes

* [APT32](/groups/G0050) <small style="color:#929393">(v2.6&#8594;v2.7)</small>
* [Confucius](/groups/G0142) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Dragonfly](/groups/G0035) <small style="color:#929393">(v3.1&#8594;v3.2)</small>
* [LAPSUS$](/groups/G1004) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Magic Hound](/groups/G0059) <small style="color:#929393">(v5.1&#8594;v5.2)</small>
* [Sandworm Team](/groups/G0034) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [SilverTerrier](/groups/G0083) <small style="color:#929393">(v1.1&#8594;v1.2)</small>

#### Patches

* [APT37](/groups/G0067) <small style="color:#929393">(v2.0)</small>
* [Ajax Security Team](/groups/G0130) <small style="color:#929393">(v1.0)</small>
* [Darkhotel](/groups/G0012) <small style="color:#929393">(v2.1)</small>
* [Kimsuky](/groups/G0094) <small style="color:#929393">(v3.1)</small>

### Mobile

#### New Groups

* [Confucius](/groups/G0142) <small style="color:#eb6635">(v1.1)</small>
* [MoustachedBouncer](/groups/G1019) <small style="color:#929393">(v1.0)</small>

#### Minor Version Changes

* [Sandworm Team](/groups/G0034) <small style="color:#929393">(v3.0&#8594;v3.1)</small>

### ICS

#### Major Version Changes

* [FIN7](/groups/G0046) <small style="color:#929393">(v2.2&#8594;v3.0)</small>
* [Wizard Spider](/groups/G0102) <small style="color:#929393">(v2.1&#8594;v3.0)</small>

#### Minor Version Changes

* [Dragonfly](/groups/G0035) <small style="color:#929393">(v3.1&#8594;v3.2)</small>
* [Sandworm Team](/groups/G0034) <small style="color:#929393">(v3.0&#8594;v3.1)</small>

## Campaigns

### Enterprise

#### New Campaigns

* [2015 Ukraine Electric Power Attack](/campaigns/C0028) <small style="color:#929393">(v1.0)</small>
* [C0026](/campaigns/C0026) <small style="color:#929393">(v1.0)</small>
* [C0027](/campaigns/C0027) <small style="color:#929393">(v1.0)</small>

#### Minor Version Changes

* [Operation Dream Job](/campaigns/C0022) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

### Mobile

### ICS

#### New Campaigns

* [2015 Ukraine Electric Power Attack](/campaigns/C0028) <small style="color:#929393">(v1.0)</small>

#### Deprecations

* [Oldsmar Treatment Plant Intrusion](/campaigns/C0009) <small style="color:#929393">(v1.0)</small>

## Assets

### ICS

#### New Assets

* [Application Server](/assets/A0008) <small style="color:#929393">(v1.0)</small>
* [Control Server](/assets/A0007) <small style="color:#929393">(v1.0)</small>
* [Data Gateway](/assets/A0009) <small style="color:#929393">(v1.0)</small>
* [Data Historian](/assets/A0006) <small style="color:#929393">(v1.0)</small>
* [Field I/O](/assets/A0013) <small style="color:#929393">(v1.0)</small>
* [Human-Machine Interface (HMI)](/assets/A0002) <small style="color:#929393">(v1.0)</small>
* [Intelligent Electronic Device (IED)](/assets/A0005) <small style="color:#929393">(v1.0)</small>
* [Jump Host](/assets/A0012) <small style="color:#929393">(v1.0)</small>
* [Programmable Logic Controller (PLC)](/assets/A0003) <small style="color:#929393">(v1.0)</small>
* [Remote Terminal Unit (RTU)](/assets/A0004) <small style="color:#929393">(v1.0)</small>
* [Routers](/assets/A0014) <small style="color:#929393">(v1.0)</small>
* [Safety Controller](/assets/A0010) <small style="color:#929393">(v1.0)</small>
* [Virtual Private Network (VPN) Server](/assets/A0011) <small style="color:#929393">(v1.0)</small>
* [Workstation](/assets/A0001) <small style="color:#929393">(v1.0)</small>

## Mitigations

### Enterprise

#### Minor Version Changes

* [Application Developer Guidance](/mitigations/M1013) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

### Mobile

#### New Mitigations

* [Antivirus/Antimalware](/mitigations/M1058) <small style="color:#929393">(v1.0)</small>

#### Minor Version Changes

* [Application Developer Guidance](/mitigations/M1013) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Patches

* [Interconnection Filtering](/mitigations/M1014) <small style="color:#929393">(v1.0)</small>

### ICS

#### Minor Version Changes

* [Authorization Enforcement](/mitigations/M0800) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Human User Authentication](/mitigations/M0804) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Patches

* [Access Management](/mitigations/M0801) <small style="color:#929393">(v1.0)</small>
* [Account Use Policies](/mitigations/M0936) <small style="color:#929393">(v1.0)</small>
* [Antivirus/Antimalware](/mitigations/M0949) <small style="color:#929393">(v1.0)</small>
* [Application Developer Guidance](/mitigations/M0913) <small style="color:#929393">(v1.0)</small>
* [Application Isolation and Sandboxing](/mitigations/M0948) <small style="color:#929393">(v1.0)</small>
* [Audit](/mitigations/M0947) <small style="color:#929393">(v1.0)</small>
* [Boot Integrity](/mitigations/M0946) <small style="color:#929393">(v1.0)</small>
* [Code Signing](/mitigations/M0945) <small style="color:#929393">(v1.0)</small>
* [Communication Authenticity](/mitigations/M0802) <small style="color:#929393">(v1.0)</small>
* [Data Backup](/mitigations/M0953) <small style="color:#929393">(v1.0)</small>
* [Disable or Remove Feature or Program](/mitigations/M0942) <small style="color:#929393">(v1.0)</small>
* [Encrypt Network Traffic](/mitigations/M0808) <small style="color:#929393">(v1.0)</small>
* [Encrypt Sensitive Information](/mitigations/M0941) <small style="color:#929393">(v1.0)</small>
* [Execution Prevention](/mitigations/M0938) <small style="color:#929393">(v1.0)</small>
* [Exploit Protection](/mitigations/M0950) <small style="color:#929393">(v1.0)</small>
* [Filter Network Traffic](/mitigations/M0937) <small style="color:#929393">(v1.0)</small>
* [Limit Access to Resource Over Network](/mitigations/M0935) <small style="color:#929393">(v1.0)</small>
* [Limit Hardware Installation](/mitigations/M0934) <small style="color:#929393">(v1.0)</small>
* [Minimize Wireless Signal Propagation](/mitigations/M0806) <small style="color:#929393">(v1.0)</small>
* [Multi-factor Authentication](/mitigations/M0932) <small style="color:#929393">(v1.0)</small>
* [Network Allowlists](/mitigations/M0807) <small style="color:#929393">(v1.0)</small>
* [Network Intrusion Prevention](/mitigations/M0931) <small style="color:#929393">(v1.0)</small>
* [Network Segmentation](/mitigations/M0930) <small style="color:#929393">(v1.0)</small>
* [Operating System Configuration](/mitigations/M0928) <small style="color:#929393">(v1.0)</small>
* [Out-of-Band Communications Channel](/mitigations/M0810) <small style="color:#929393">(v1.0)</small>
* [Password Policies](/mitigations/M0927) <small style="color:#929393">(v1.0)</small>
* [Privileged Account Management](/mitigations/M0926) <small style="color:#929393">(v1.0)</small>
* [Redundancy of Service](/mitigations/M0811) <small style="color:#929393">(v1.0)</small>
* [Restrict File and Directory Permissions](/mitigations/M0922) <small style="color:#929393">(v1.0)</small>
* [Restrict Library Loading](/mitigations/M0944) <small style="color:#929393">(v1.0)</small>
* [Restrict Registry Permissions](/mitigations/M0924) <small style="color:#929393">(v1.0)</small>
* [Restrict Web-Based Content](/mitigations/M0921) <small style="color:#929393">(v1.0)</small>
* [Software Configuration](/mitigations/M0954) <small style="color:#929393">(v1.0)</small>
* [Software Process and Device Authentication](/mitigations/M0813) <small style="color:#929393">(v1.0)</small>
* [Static Network Configuration](/mitigations/M0814) <small style="color:#929393">(v1.1)</small>
* [Supply Chain Management](/mitigations/M0817) <small style="color:#929393">(v1.0)</small>
* [Update Software](/mitigations/M0951) <small style="color:#929393">(v1.0)</small>
* [User Account Management](/mitigations/M0918) <small style="color:#929393">(v1.0)</small>
* [User Training](/mitigations/M0917) <small style="color:#929393">(v1.0)</small>
* [Validate Program Inputs](/mitigations/M0818) <small style="color:#929393">(v1.0)</small>
* [Vulnerability Scanning](/mitigations/M0916) <small style="color:#929393">(v1.0)</small>

## Contributors to this release

* Aaron Jornet
* Adam Lichters
* Adam Mashinchi
* Ai Kimura, NEC Corporation
* Alain Homewood
* Alex Spivakovsky, Pentera
* Amir Gharib, Microsoft Threat Intelligence
* Andrew Northern, @ex_raritas
* Arad Inbar, Fidelis Security
* Austin Herrin
* Ben Smith, @ezaspy
* Bilal Bahadır Yenici
* Blake Strom, Microsoft Threat Intelligence
* Brian Donohue
* Caio Silva
* Christopher Peacock
* Edward Stevens, BT Security
* Ford Qin, Trend Micro
* Giorgi Gurgenidze, ISAC
* Goldstein Menachem
* Gregory Lesnewich, @greglesnewich
* Gunji Satoshi, NEC Corporation
* Harry Kim, CODEMIZE
* Harun Küßner
* Hiroki Nagahama, NEC Corporation
* Itamar Mizrahi, Cymptom
* Jack Burns, HubSpot
* Janantha Marasinghe
* Jennifer Kim Roman, CrowdStrike
* Joas Antonio dos Santos, @C0d3Cr4zy
* Joe Gumke, U.S. Bank
* Joe Slowik - Dragos
* Joey Lei
* Juan Tapiador
* Liran Ravich, CardinalOps
* Manikantan Srinivasan, NEC Corporation India
* Martin McCloskey, Datadog
* Matt Green, @mgreen27
* Michael Raggi @aRtAGGI
* Mohit Rathore
* Naveen Devaraja, bolttech
* Noam Lifshitz, Sygnia
* Olaf Hartong, Falcon Force
* Oren Biderman, Sygnia
* Pawel Partyka, Microsoft Threat Intelligence
* Phyo Paing Htun (ChiLai), I-Secure Co.,Ltd
* Pooja Natarajan, NEC Corporation India
* Sam Seabrook, Duke Energy
* Serhii Melnyk, Trustwave SpiderLabs
* Shailesh Tiwary (Indian Army)
* Shankar Raman, Gen Digital and Abhinand, Amrita University
* Sunders Bruskin, Microsoft Threat Intelligence
* Tahseen Bin Taj
* Thanabodi Phrakhun, @naikordian
* The DFIR Report
* Tim (Wadhwa-)Brown
* Tom Simpson, CrowdStrike Falcon OverWatch
* Tristan Madani (Cybereason)
* TruKno
* Uriel Kosayev
* Vijay Lalwani
* Will Thomas, Equinix
* Yasuhito Kawanishi, NEC Corporation
* Yoshihiro Kori, NEC Corporation
* Yossi Weizman, Microsoft Threat Intelligence
