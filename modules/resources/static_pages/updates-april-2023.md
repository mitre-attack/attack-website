Title: Updates - April 2023
Date: April 2023
Category: Cyber Threat Intelligence
Authors: Adam Pennington
Template: resources/update-post
url: /resources/updates/updates-april-2023
save_as: resources/updates/updates-april-2023/index.html

| Version | Start Date | End Date | Data | Changelogs |
|:--------|:-----------|:---------|:-----|:-----------|
| [ATT&CK v13](/versions/v13) | April 25, 2023 | This is the current version of ATT&CK | [v13.0 on MITRE/CTI](https://github.com/mitre/cti/releases/tag/ATT%26CK-v13.0)<br />[v13.1 on MITRE/CTI](https://github.com/mitre/cti/releases/tag/ATT%26CK-v13.1) | v12.1 - v13.0 [Details](/docs/changelogs/v12.1-v13.0/changelog-detailed.html) ([JSON](/docs/changelogs/v12.1-v13.0/changelog.json))<br />v13.0 - v13.1 [Details](/docs/changelogs/v13.0-v13.1/changelog-detailed.html) ([JSON](/docs/changelogs/v13.0-v13.1/changelog.json)) |

The April 2023 (v13) ATT&CK release updates Techniques, Groups, Campaigns and Software for Enterprise, Mobile, and ICS. The biggest changes in ATT&CK v13 are the addition of detailed detection guidance to some Techniques in ATT&CK for Enterprise, Mobile Data Sources, and two new types of changelogs to help identify more precisely what has changed in ATT&CK. An [accompanying blog post](https://medium.com/mitre-attack/attack-v13-enters-the-room-5cef174c32ff) describes these changes as well as improvements across ATT&CK's various domains and platforms.

This release includes a new [human-readable detailed changelog](/docs/changelogs/v12.1-v13.0/changelog-detailed.html) showing more specifically what changed in updated ATT&CK objects, and a new [machine-readable JSON changelog](/docs/changelogs/v12.1-v13.0/changelog.json), whose format is described in [ATT&CK's Github](https://github.com/mitre-attack/mitreattack-python/blob/master/mitreattack/diffStix/README.md). The terminology used in these release notes has also been updated to better describe the changes to various ATT&CK objects:

* New objects: ATT&CK objects which are only present in the new release.
* Major version changes: ATT&CK objects that have a major version change. (e.g., 1.0 → 2.0)
* Minor version changes: ATT&CK objects that have a minor version change. (e.g., 1.0 → 1.1)
* Patches: ATT&CK objects that have been patched while keeping the version the same. (e.g., 1.0 → 1.0 but something like a typo, a URL, or some metadata was fixed)
* Object revocations: ATT&CK objects which are revoked by a different object.
* Object deprecations: ATT&CK objects which are deprecated and no longer in use, and not replaced.
* Object deletions: ATT&CK objects which are no longer found in the STIX data.

This version of ATT&CK for Enterprise contains 14 Tactics, 196 Techniques, 411 Sub-techniques, 138 Groups, 22 Campaigns, and 740 Pieces of Software.

## Techniques

### Enterprise

#### New Techniques

* [Acquire Access](/techniques/T1650) <small style="color:#929393">(v1.0)</small>
* Acquire Infrastructure: [Malvertising](/techniques/T1583/008) <small style="color:#929393">(v1.0)</small>
* [Cloud Administration Command](/techniques/T1651) <small style="color:#929393">(v1.0)</small>
* Command and Scripting Interpreter: [Cloud API](/techniques/T1059/009) <small style="color:#929393">(v1.0)</small>
* [Device Driver Discovery](/techniques/T1652) <small style="color:#929393">(v1.0)</small>
* Exfiltration Over Web Service: [Exfiltration to Text Storage Sites](/techniques/T1567/003) <small style="color:#929393">(v1.0)</small>
* Impair Defenses: [Spoof Security Alerting](/techniques/T1562/011) <small style="color:#929393">(v1.0)</small>
* Masquerading: [Masquerade File Type](/techniques/T1036/008) <small style="color:#929393">(v1.0)</small>
* Modify Authentication Process: [Network Provider DLL](/techniques/T1556/008) <small style="color:#929393">(v1.0)</small>
* Obfuscated Files or Information: [Command Obfuscation](/techniques/T1027/010) <small style="color:#929393">(v1.0)</small>
* Obfuscated Files or Information: [Fileless Storage](/techniques/T1027/011) <small style="color:#929393">(v1.0)</small>
* Remote Services: [Cloud Services](/techniques/T1021/007) <small style="color:#929393">(v1.0)</small>
* Unsecured Credentials: [Chat Messages](/techniques/T1552/008) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [Browser Information Discovery](/techniques/T1217) <small style="color:#929393">(v1.0&#8594;v2.0)</small>

#### Minor Version Changes

* [Abuse Elevation Control Mechanism](/techniques/T1548) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Bypass User Account Control](/techniques/T1548/002) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Access Token Manipulation: [Create Process with Token](/techniques/T1134/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Access Token Manipulation: [Make and Impersonate Token](/techniques/T1134/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Access Token Manipulation: [Token Impersonation/Theft](/techniques/T1134/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Account Access Removal](/techniques/T1531) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Account Discovery](/techniques/T1087) <small style="color:#929393">(v2.3&#8594;v2.4)</small>
  * [Domain Account](/techniques/T1087/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
  * [Local Account](/techniques/T1087/001) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Account Manipulation](/techniques/T1098) <small style="color:#929393">(v2.4&#8594;v2.5)</small>
  * [Additional Cloud Credentials](/techniques/T1098/001) <small style="color:#929393">(v2.4&#8594;v2.5)</small>
  * [Additional Cloud Roles](/techniques/T1098/003) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
  * [Device Registration](/techniques/T1098/005) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [SSH Authorized Keys](/techniques/T1098/004) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Acquire Infrastructure](/techniques/T1583) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
  * [Server](/techniques/T1583/004) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
  * [Web Services](/techniques/T1583/006) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Application Layer Protocol](/techniques/T1071) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
  * [Web Protocols](/techniques/T1071/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Application Window Discovery](/techniques/T1010) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Archive Collected Data: [Archive via Utility](/techniques/T1560/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Automated Exfiltration: [Traffic Duplication](/techniques/T1020/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [BITS Jobs](/techniques/T1197) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Brute Force](/techniques/T1110) <small style="color:#929393">(v2.4&#8594;v2.5)</small>
  * [Credential Stuffing](/techniques/T1110/004) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
  * [Password Guessing](/techniques/T1110/001) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
  * [Password Spraying](/techniques/T1110/003) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Build Image on Host](/techniques/T1612) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Clipboard Data](/techniques/T1115) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Cloud Service Discovery](/techniques/T1526) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Command and Scripting Interpreter](/techniques/T1059) <small style="color:#929393">(v2.3&#8594;v2.4)</small>
  * [PowerShell](/techniques/T1059/001) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
  * [Visual Basic](/techniques/T1059/005) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Compromise Accounts](/techniques/T1586) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
  * [Email Accounts](/techniques/T1586/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Compromise Infrastructure](/techniques/T1584) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
  * [Domains](/techniques/T1584/001) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
  * [Server](/techniques/T1584/004) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
  * [Web Services](/techniques/T1584/006) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Container Administration Command](/techniques/T1609) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Container and Resource Discovery](/techniques/T1613) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Create Account](/techniques/T1136) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
  * [Cloud Account](/techniques/T1136/003) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
  * [Local Account](/techniques/T1136/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Create or Modify System Process: [Systemd Service](/techniques/T1543/002) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Create or Modify System Process: [Windows Service](/techniques/T1543/003) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Data Encoding](/techniques/T1132) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Data from Local System](/techniques/T1005) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
* [Deobfuscate/Decode Files or Information](/techniques/T1140) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Deploy Container](/techniques/T1610) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Disk Wipe](/techniques/T1561) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Disk Structure Wipe](/techniques/T1561/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Drive-by Compromise](/techniques/T1189) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Email Collection](/techniques/T1114) <small style="color:#929393">(v2.3&#8594;v2.4)</small>
  * [Email Forwarding Rule](/techniques/T1114/003) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Escape to Host](/techniques/T1611) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* Event Triggered Execution: [Accessibility Features](/techniques/T1546/008) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Event Triggered Execution: [AppInit DLLs](/techniques/T1546/010) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Event Triggered Execution: [Component Object Model Hijacking](/techniques/T1546/015) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Event Triggered Execution: [Screensaver](/techniques/T1546/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Event Triggered Execution: [Windows Management Instrumentation Event Subscription](/techniques/T1546/003) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Exfiltration Over Alternative Protocol](/techniques/T1048) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
  * [Exfiltration Over Unencrypted Non-C2 Protocol](/techniques/T1048/003) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Exfiltration Over C2 Channel](/techniques/T1041) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Exploit Public-Facing Application](/techniques/T1190) <small style="color:#929393">(v2.3&#8594;v2.4)</small>
* [Exploitation for Privilege Escalation](/techniques/T1068) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* File and Directory Permissions Modification: [Windows File and Directory Permissions Modification](/techniques/T1222/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Forge Web Credentials](/techniques/T1606) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Gather Victim Identity Information: [Credentials](/techniques/T1589/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Group Policy Discovery](/techniques/T1615) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Hide Artifacts: [Email Hiding Rules](/techniques/T1564/008) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Impair Defenses](/techniques/T1562) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
  * [Disable Cloud Logs](/techniques/T1562/008) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
  * [Disable Windows Event Logging](/techniques/T1562/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
  * [Disable or Modify Cloud Firewall](/techniques/T1562/007) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
  * [Disable or Modify System Firewall](/techniques/T1562/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Disable or Modify Tools](/techniques/T1562/001) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
  * [Indicator Blocking](/techniques/T1562/006) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Indicator Removal](/techniques/T1070) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
  * [Clear Command History](/techniques/T1070/003) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
  * [Clear Mailbox Data](/techniques/T1070/008) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Clear Persistence](/techniques/T1070/009) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Clear Windows Event Logs](/techniques/T1070/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
  * [Network Share Connection Removal](/techniques/T1070/005) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Ingress Tool Transfer](/techniques/T1105) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Inhibit System Recovery](/techniques/T1490) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Masquerading](/techniques/T1036) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
  * [Rename System Utilities](/techniques/T1036/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Modify Authentication Process](/techniques/T1556) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* [Modify Registry](/techniques/T1112) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Multi-Factor Authentication Interception](/techniques/T1111) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Network Sniffing](/techniques/T1040) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Non-Application Layer Protocol](/techniques/T1095) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Non-Standard Port](/techniques/T1571) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* OS Credential Dumping: [LSASS Memory](/techniques/T1003/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* OS Credential Dumping: [Proc Filesystem](/techniques/T1003/007) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Obfuscated Files or Information](/techniques/T1027) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Permission Groups Discovery](/techniques/T1069) <small style="color:#929393">(v2.4&#8594;v2.5)</small>
  * [Cloud Groups](/techniques/T1069/003) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
  * [Domain Groups](/techniques/T1069/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
  * [Local Groups](/techniques/T1069/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Phishing](/techniques/T1566) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
  * [Spearphishing Link](/techniques/T1566/002) <small style="color:#929393">(v2.3&#8594;v2.4)</small>
* [Phishing for Information](/techniques/T1598) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
  * [Spearphishing Link](/techniques/T1598/003) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Process Discovery](/techniques/T1057) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Query Registry](/techniques/T1012) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Remote Services](/techniques/T1021) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
  * [Distributed Component Object Model](/techniques/T1021/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
  * [SMB/Windows Admin Shares](/techniques/T1021/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Scheduled Task/Job: [Container Orchestration Job](/techniques/T1053/007) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Scheduled Task/Job: [Scheduled Task](/techniques/T1053/005) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Software Discovery: [Security Software Discovery](/techniques/T1518/001) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* Stage Capabilities: [Drive-by Target](/techniques/T1608/004) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Stage Capabilities: [Link Target](/techniques/T1608/005) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Stage Capabilities: [Upload Malware](/techniques/T1608/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Steal or Forge Authentication Certificates](/techniques/T1649) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* System Binary Proxy Execution: [CMSTP](/techniques/T1218/003) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* System Binary Proxy Execution: [Compiled HTML File](/techniques/T1218/001) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* System Binary Proxy Execution: [Regsvr32](/techniques/T1218/010) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* System Binary Proxy Execution: [Rundll32](/techniques/T1218/011) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [System Owner/User Discovery](/techniques/T1033) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [System Service Discovery](/techniques/T1007) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [System Shutdown/Reboot](/techniques/T1529) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [System Time Discovery](/techniques/T1124) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Unsecured Credentials](/techniques/T1552) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
  * [Cloud Instance Metadata API](/techniques/T1552/005) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
  * [Container API](/techniques/T1552/007) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
  * [Private Keys](/techniques/T1552/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Use Alternate Authentication Material: [Application Access Token](/techniques/T1550/001) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* User Execution: [Malicious File](/techniques/T1204/002) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Valid Accounts](/techniques/T1078) <small style="color:#929393">(v2.5&#8594;v2.6)</small>
  * [Cloud Accounts](/techniques/T1078/004) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
  * [Domain Accounts](/techniques/T1078/002) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
  * [Local Accounts](/techniques/T1078/003) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Windows Management Instrumentation](/techniques/T1047) <small style="color:#929393">(v1.2&#8594;v1.3)</small>

#### Patches

* Abuse Elevation Control Mechanism: [Setuid and Setgid](/techniques/T1548/001) <small style="color:#929393">(v1.1)</small>
* [Access Token Manipulation](/techniques/T1134) <small style="color:#929393">(v2.0)</small>
* Acquire Infrastructure: [Domains](/techniques/T1583/001) <small style="color:#929393">(v1.2)</small>
* Active Scanning: [Vulnerability Scanning](/techniques/T1595/002) <small style="color:#929393">(v1.0)</small>
* [Adversary-in-the-Middle](/techniques/T1557) <small style="color:#929393">(v2.2)</small>
* [Audio Capture](/techniques/T1123) <small style="color:#929393">(v1.0)</small>
* [Boot or Logon Autostart Execution](/techniques/T1547) <small style="color:#929393">(v1.1)</small>
  * [Active Setup](/techniques/T1547/014) <small style="color:#929393">(v1.0)</small>
  * [Registry Run Keys / Startup Folder](/techniques/T1547/001) <small style="color:#929393">(v1.2)</small>
  * [Shortcut Modification](/techniques/T1547/009) <small style="color:#929393">(v1.2)</small>
  * [Winlogon Helper DLL](/techniques/T1547/004) <small style="color:#929393">(v1.0)</small>
* [Boot or Logon Initialization Scripts](/techniques/T1037) <small style="color:#929393">(v2.1)</small>
* Brute Force: [Password Cracking](/techniques/T1110/002) <small style="color:#929393">(v1.2)</small>
* Create or Modify System Process: [Launch Daemon](/techniques/T1543/004) <small style="color:#929393">(v1.2)</small>
* Data Encoding: [Standard Encoding](/techniques/T1132/001) <small style="color:#929393">(v1.0)</small>
* [Data from Network Shared Drive](/techniques/T1039) <small style="color:#929393">(v1.3)</small>
* Disk Wipe: [Disk Content Wipe](/techniques/T1561/001) <small style="color:#929393">(v1.0)</small>
* Domain Policy Modification: [Group Policy Modification](/techniques/T1484/001) <small style="color:#929393">(v1.0)</small>
* [Endpoint Denial of Service](/techniques/T1499) <small style="color:#929393">(v1.1)</small>
  * [OS Exhaustion Flood](/techniques/T1499/001) <small style="color:#929393">(v1.2)</small>
  * [Service Exhaustion Flood](/techniques/T1499/002) <small style="color:#929393">(v1.3)</small>
* Event Triggered Execution: [Change Default File Association](/techniques/T1546/001) <small style="color:#929393">(v1.0)</small>
* [External Remote Services](/techniques/T1133) <small style="color:#929393">(v2.4)</small>
* [File and Directory Discovery](/techniques/T1083) <small style="color:#929393">(v1.5)</small>
* [Hardware Additions](/techniques/T1200) <small style="color:#929393">(v1.6)</small>
* Hijack Execution Flow: [DLL Search Order Hijacking](/techniques/T1574/001) <small style="color:#929393">(v1.1)</small>
* Hijack Execution Flow: [DLL Side-Loading](/techniques/T1574/002) <small style="color:#929393">(v2.0)</small>
* Hijack Execution Flow: [Dylib Hijacking](/techniques/T1574/004) <small style="color:#929393">(v2.0)</small>
* Hijack Execution Flow: [Dynamic Linker Hijacking](/techniques/T1574/006) <small style="color:#929393">(v2.0)</small>
* Hijack Execution Flow: [Path Interception by PATH Environment Variable](/techniques/T1574/007) <small style="color:#929393">(v1.0)</small>
* Hijack Execution Flow: [Path Interception by Search Order Hijacking](/techniques/T1574/008) <small style="color:#929393">(v1.0)</small>
* Hijack Execution Flow: [Path Interception by Unquoted Path](/techniques/T1574/009) <small style="color:#929393">(v1.1)</small>
* Hijack Execution Flow: [Services File Permissions Weakness](/techniques/T1574/010) <small style="color:#929393">(v1.0)</small>
* Hijack Execution Flow: [Services Registry Permissions Weakness](/techniques/T1574/011) <small style="color:#929393">(v1.1)</small>
* Impair Defenses: [Impair Command History Logging](/techniques/T1562/003) <small style="color:#929393">(v2.2)</small>
* [Input Capture](/techniques/T1056) <small style="color:#929393">(v1.2)</small>
  * [GUI Input Capture](/techniques/T1056/002) <small style="color:#929393">(v1.2)</small>
  * [Keylogging](/techniques/T1056/001) <small style="color:#929393">(v1.1)</small>
  * [Web Portal Capture](/techniques/T1056/003) <small style="color:#929393">(v1.0)</small>
* Masquerading: [Match Legitimate Name or Location](/techniques/T1036/005) <small style="color:#929393">(v1.1)</small>
* Masquerading: [Space after Filename](/techniques/T1036/006) <small style="color:#929393">(v1.0)</small>
* Modify Authentication Process: [Multi-Factor Authentication](/techniques/T1556/006) <small style="color:#929393">(v1.0)</small>
* [Multi-Factor Authentication Request Generation](/techniques/T1621) <small style="color:#929393">(v1.0)</small>
* Network Denial of Service: [Direct Network Flood](/techniques/T1498/001) <small style="color:#929393">(v1.3)</small>
* Network Denial of Service: [Reflection Amplification](/techniques/T1498/002) <small style="color:#929393">(v1.3)</small>
* [Network Service Discovery](/techniques/T1046) <small style="color:#929393">(v3.0)</small>
* [Network Share Discovery](/techniques/T1135) <small style="color:#929393">(v3.1)</small>
* Obfuscated Files or Information: [Binary Padding](/techniques/T1027/001) <small style="color:#929393">(v1.2)</small>
* Obfuscated Files or Information: [Software Packing](/techniques/T1027/002) <small style="color:#929393">(v1.2)</small>
* Obfuscated Files or Information: [Steganography](/techniques/T1027/003) <small style="color:#929393">(v1.2)</small>
* [Peripheral Device Discovery](/techniques/T1120) <small style="color:#929393">(v1.3)</small>
* Phishing: [Spearphishing Attachment](/techniques/T1566/001) <small style="color:#929393">(v2.2)</small>
* Phishing: [Spearphishing via Service](/techniques/T1566/003) <small style="color:#929393">(v2.0)</small>
* Pre-OS Boot: [Bootkit](/techniques/T1542/003) <small style="color:#929393">(v1.1)</small>
* Pre-OS Boot: [System Firmware](/techniques/T1542/001) <small style="color:#929393">(v1.0)</small>
* [Process Injection](/techniques/T1055) <small style="color:#929393">(v1.3)</small>
* Proxy: [Domain Fronting](/techniques/T1090/004) <small style="color:#929393">(v1.1)</small>
* Remote Services: [Remote Desktop Protocol](/techniques/T1021/001) <small style="color:#929393">(v1.1)</small>
* Remote Services: [SSH](/techniques/T1021/004) <small style="color:#929393">(v1.1)</small>
* Remote Services: [VNC](/techniques/T1021/005) <small style="color:#929393">(v1.1)</small>
* [Remote System Discovery](/techniques/T1018) <small style="color:#929393">(v3.4)</small>
* [Rootkit](/techniques/T1014) <small style="color:#929393">(v1.1)</small>
* [Scheduled Task/Job](/techniques/T1053) <small style="color:#929393">(v2.2)</small>
* [Screen Capture](/techniques/T1113) <small style="color:#929393">(v1.1)</small>
* Server Software Component: [Web Shell](/techniques/T1505/003) <small style="color:#929393">(v1.3)</small>
* [Software Deployment Tools](/techniques/T1072) <small style="color:#929393">(v2.1)</small>
* [Software Discovery](/techniques/T1518) <small style="color:#929393">(v1.3)</small>
* Stage Capabilities: [SEO Poisoning](/techniques/T1608/006) <small style="color:#929393">(v1.0)</small>
* [Steal or Forge Kerberos Tickets](/techniques/T1558) <small style="color:#929393">(v1.4)</small>
  * [Kerberoasting](/techniques/T1558/003) <small style="color:#929393">(v1.2)</small>
* Subvert Trust Controls: [Install Root Certificate](/techniques/T1553/004) <small style="color:#929393">(v1.1)</small>
* Subvert Trust Controls: [Mark-of-the-Web Bypass](/techniques/T1553/005) <small style="color:#929393">(v1.1)</small>
* [Supply Chain Compromise](/techniques/T1195) <small style="color:#929393">(v1.5)</small>
* [System Information Discovery](/techniques/T1082) <small style="color:#929393">(v2.5)</small>
* [System Network Configuration Discovery](/techniques/T1016) <small style="color:#929393">(v1.5)</small>
* [Taint Shared Content](/techniques/T1080) <small style="color:#929393">(v1.3)</small>
* Unsecured Credentials: [Credentials In Files](/techniques/T1552/001) <small style="color:#929393">(v1.1)</small>
* Use Alternate Authentication Material: [Pass the Hash](/techniques/T1550/002) <small style="color:#929393">(v1.1)</small>
* Use Alternate Authentication Material: [Pass the Ticket](/techniques/T1550/003) <small style="color:#929393">(v1.1)</small>
* Use Alternate Authentication Material: [Web Session Cookie](/techniques/T1550/004) <small style="color:#929393">(v1.3)</small>
* Valid Accounts: [Default Accounts](/techniques/T1078/001) <small style="color:#929393">(v1.2)</small>
* [Video Capture](/techniques/T1125) <small style="color:#929393">(v1.1)</small>

### Mobile

#### Minor Version Changes

* [Abuse Elevation Control Mechanism](/techniques/T1626) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Device Administrator Permissions](/techniques/T1626/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Access Notifications](/techniques/T1517) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Account Access Removal](/techniques/T1640) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Adversary-in-the-Middle](/techniques/T1638) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Audio Capture](/techniques/T1429) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [Boot or Logon Initialization Scripts](/techniques/T1398) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Call Control](/techniques/T1616) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Clipboard Data](/techniques/T1414) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [Command and Scripting Interpreter](/techniques/T1623) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Unix Shell](/techniques/T1623/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Compromise Client Software Binary](/techniques/T1645) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Credentials from Password Store](/techniques/T1634) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Keychain](/techniques/T1634/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Data Encrypted for Impact](/techniques/T1471) <small style="color:#929393">(v3.1&#8594;v3.2)</small>
* [Data Manipulation](/techniques/T1641) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Transmitted Data Manipulation](/techniques/T1641/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Download New Code at Runtime](/techniques/T1407) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Drive-By Compromise](/techniques/T1456) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Endpoint Denial of Service](/techniques/T1642) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Event Triggered Execution](/techniques/T1624) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Broadcast Receivers](/techniques/T1624/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Execution Guardrails](/techniques/T1627) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Geofencing](/techniques/T1627/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Exploitation for Privilege Escalation](/techniques/T1404) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Exploitation of Remote Services](/techniques/T1428) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [File and Directory Discovery](/techniques/T1420) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Foreground Persistence](/techniques/T1541) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Generate Traffic from Victim](/techniques/T1643) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Hide Artifacts](/techniques/T1628) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Suppress Application Icon](/techniques/T1628/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Hijack Execution Flow](/techniques/T1625) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [System Runtime API Hijacking](/techniques/T1625/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Impair Defenses](/techniques/T1629) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Device Lockout](/techniques/T1629/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Disable or Modify Tools](/techniques/T1629/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Prevent Application Removal](/techniques/T1629/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Indicator Removal on Host](/techniques/T1630) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Disguise Root/Jailbreak Indicators](/techniques/T1630/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [File Deletion](/techniques/T1630/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Uninstall Malicious Application](/techniques/T1630/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Ingress Tool Transfer](/techniques/T1544) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Input Capture](/techniques/T1417) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
  * [GUI Input Capture](/techniques/T1417/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Keylogging](/techniques/T1417/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Location Tracking](/techniques/T1430) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
  * [Impersonate SS7 Nodes](/techniques/T1430/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Remote Device Management Services](/techniques/T1430/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Network Denial of Service](/techniques/T1464) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Non-Standard Port](/techniques/T1509) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Obfuscated Files or Information: [Software Packing](/techniques/T1406/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Out of Band Data](/techniques/T1644) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Process Discovery](/techniques/T1424) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Process Injection](/techniques/T1631) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Ptrace System Calls](/techniques/T1631/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Protected User Data](/techniques/T1636) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Calendar Entries](/techniques/T1636/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Call Log](/techniques/T1636/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Contact List](/techniques/T1636/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [SMS Messages](/techniques/T1636/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Proxy Through Victim](/techniques/T1604) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [SMS Control](/techniques/T1582) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Screen Capture](/techniques/T1513) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Software Discovery](/techniques/T1418) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
  * [Security Software Discovery](/techniques/T1418/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Steal Application Access Token](/techniques/T1635) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [URI Hijacking](/techniques/T1635/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Stored Application Data](/techniques/T1409) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [Subvert Trust Controls](/techniques/T1632) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Code Signing Policy Modification](/techniques/T1632/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Supply Chain Compromise](/techniques/T1474) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
  * [Compromise Hardware Supply Chain](/techniques/T1474/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Compromise Software Dependencies and Development Tools](/techniques/T1474/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Compromise Software Supply Chain](/techniques/T1474/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [System Network Configuration Discovery](/techniques/T1422) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* [Video Capture](/techniques/T1512) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Virtualization/Sandbox Evasion](/techniques/T1633) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [System Checks](/techniques/T1633/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Web Service](/techniques/T1481) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
  * [Bidirectional Communication](/techniques/T1481/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [Dead Drop Resolver](/techniques/T1481/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
  * [One-Way Communication](/techniques/T1481/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

### ICS

#### New Techniques

* [Change Credential](/techniques/T0892) <small style="color:#929393">(v1.0)</small>
* [Data from Local System](/techniques/T0893) <small style="color:#929393">(v1.0)</small>

#### Minor Version Changes

* [Alarm Suppression](/techniques/T0878) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Brute Force I/O](/techniques/T0806) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Damage to Property](/techniques/T0879) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Data from Information Repositories](/techniques/T0811) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Denial of Control](/techniques/T0813) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Denial of Service](/techniques/T0814) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Denial of View](/techniques/T0815) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [External Remote Services](/techniques/T0822) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Hooking](/techniques/T0874) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Modify Alarm Settings](/techniques/T0838) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Modify Parameter](/techniques/T0836) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Rogue Master](/techniques/T0848) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Spoof Reporting Message](/techniques/T0856) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Transient Cyber Asset](/techniques/T0864) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Unauthorized Command Message](/techniques/T0855) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Wireless Compromise](/techniques/T0860) <small style="color:#929393">(v1.1&#8594;v1.2)</small>

#### Patches

* [Adversary-in-the-Middle](/techniques/T0830) <small style="color:#929393">(v2.0)</small>
* [Automated Collection](/techniques/T0802) <small style="color:#929393">(v1.0)</small>
* [Change Operating Mode](/techniques/T0858) <small style="color:#929393">(v1.0)</small>
* [Command-Line Interface](/techniques/T0807) <small style="color:#929393">(v1.1)</small>
* [Commonly Used Port](/techniques/T0885) <small style="color:#929393">(v1.1)</small>
* [Connection Proxy](/techniques/T0884) <small style="color:#929393">(v1.1)</small>
* [Default Credentials](/techniques/T0812) <small style="color:#929393">(v1.0)</small>
* [Detect Operating Mode](/techniques/T0868) <small style="color:#929393">(v1.0)</small>
* [Drive-by Compromise](/techniques/T0817) <small style="color:#929393">(v1.0)</small>
* [Execution through API](/techniques/T0871) <small style="color:#929393">(v1.1)</small>
* [Exploit Public-Facing Application](/techniques/T0819) <small style="color:#929393">(v1.0)</small>
* [Exploitation for Evasion](/techniques/T0820) <small style="color:#929393">(v1.1)</small>
* [Exploitation of Remote Services](/techniques/T0866) <small style="color:#929393">(v1.0)</small>
* [Graphical User Interface](/techniques/T0823) <small style="color:#929393">(v1.1)</small>
* [Hardcoded Credentials](/techniques/T0891) <small style="color:#929393">(v1.0)</small>
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
* [Manipulation of Control](/techniques/T0831) <small style="color:#929393">(v1.0)</small>
* [Manipulation of View](/techniques/T0832) <small style="color:#929393">(v1.0)</small>
* [Masquerading](/techniques/T0849) <small style="color:#929393">(v1.1)</small>
* [Modify Controller Tasking](/techniques/T0821) <small style="color:#929393">(v1.1)</small>
* [Modify Program](/techniques/T0889) <small style="color:#929393">(v1.1)</small>
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
* [Rootkit](/techniques/T0851) <small style="color:#929393">(v1.1)</small>
* [Screen Capture](/techniques/T0852) <small style="color:#929393">(v1.0)</small>
* [Scripting](/techniques/T0853) <small style="color:#929393">(v1.0)</small>
* [Spearphishing Attachment](/techniques/T0865) <small style="color:#929393">(v1.1)</small>
* [Standard Application Layer Protocol](/techniques/T0869) <small style="color:#929393">(v1.0)</small>
* [Supply Chain Compromise](/techniques/T0862) <small style="color:#929393">(v1.1)</small>
* [System Firmware](/techniques/T0857) <small style="color:#929393">(v1.1)</small>
* [Theft of Operational Information](/techniques/T0882) <small style="color:#929393">(v1.0)</small>
* [User Execution](/techniques/T0863) <small style="color:#929393">(v1.1)</small>
* [Valid Accounts](/techniques/T0859) <small style="color:#929393">(v1.1)</small>
* [Wireless Sniffing](/techniques/T0887) <small style="color:#929393">(v1.1)</small>

## Software

### Enterprise

#### New Software

* [AvosLocker](/software/S1053) <small style="color:#929393">(v1.0)</small>
* [Black Basta](/software/S1070) <small style="color:#929393">(v1.0)</small>
* [BlackCat](/software/S1068) <small style="color:#929393">(v1.0)</small>
* [Brute Ratel C4](/software/S1063) <small style="color:#929393">(v1.0)</small>
* [DEADEYE](/software/S1052) <small style="color:#929393">(v1.0)</small>
* [DarkTortilla](/software/S1066) <small style="color:#929393">(v1.0)</small>
* [Industroyer2](/software/S1072) <small style="color:#929393">(v1.0)</small>
* [KEYPLUG](/software/S1051) <small style="color:#929393">(v1.0)</small>
* [Mafalda](/software/S1060) <small style="color:#929393">(v1.0)</small>
* [Prestige](/software/S1058) <small style="color:#929393">(v1.0)</small>
* [Royal](/software/S1073) <small style="color:#929393">(v1.0)</small>
* [Rubeus](/software/S1071) <small style="color:#929393">(v1.0)</small>
* [SVCReady](/software/S1064) <small style="color:#929393">(v1.0)</small>
* [Woody RAT](/software/S1065) <small style="color:#929393">(v1.0)</small>
* [metaMain](/software/S1059) <small style="color:#929393">(v1.0)</small>

#### Minor Version Changes

* [AADInternals](/software/S0677) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [AdFind](/software/S0552) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Astaroth](/software/S0373) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [BackConfig](/software/S0475) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [BloodHound](/software/S0521) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [CARROTBAT](/software/S0462) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [CHOPSTICK](/software/S0023) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* [Chaes](/software/S0631) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [China Chopper](/software/S0020) <small style="color:#929393">(v2.3&#8594;v2.4)</small>
* [Cobalt Strike](/software/S0154) <small style="color:#929393">(v1.9&#8594;v1.10)</small>
* [ComRAT](/software/S0126) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [CookieMiner](/software/S0492) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [DRATzarus](/software/S0694) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [DarkWatchman](/software/S0673) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Denis](/software/S0354) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Emotet](/software/S0367) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Empire](/software/S0363) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
* [Exaramel for Windows](/software/S0343) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [FruitFly](/software/S0277) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Gelsemium](/software/S0666) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [GoldFinder](/software/S0597) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [GoldMax](/software/S0588) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Grandoreiro](/software/S0531) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [HOPLIGHT](/software/S0376) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [IceApple](/software/S1022) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Impacket](/software/S0357) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [KOCTOPUS](/software/S0669) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [LaZagne](/software/S0349) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [LoudMiner](/software/S0451) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Machete](/software/S0409) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Mimikatz](/software/S0002) <small style="color:#929393">(v1.6&#8594;v1.7)</small>
* [Mosquito](/software/S0256) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [NETWIRE](/software/S0198) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Net](/software/S0039) <small style="color:#929393">(v2.3&#8594;v2.4)</small>
* [Netwalker](/software/S0457) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [POWERSTATS](/software/S0223) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* [Pillowmint](/software/S0517) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Ping](/software/S0097) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [PipeMon](/software/S0501) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [PlugX](/software/S0013) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [PoetRAT](/software/S0428) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [PolyglotDuke](/software/S0518) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [PowerLess](/software/S1012) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [PowerPunch](/software/S0685) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [PowerSploit](/software/S0194) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
* [PsExec](/software/S0029) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [QUADAGENT](/software/S0269) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [QakBot](/software/S0650) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [RCSession](/software/S0662) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [REvil](/software/S0496) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Raindrop](/software/S0565) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [RegDuke](/software/S0511) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Remsec](/software/S0125) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Responder](/software/S0174) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [RogueRobin](/software/S0270) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [S-Type](/software/S0085) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [SHARPSTATS](/software/S0450) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [SMOKEDHAM](/software/S0649) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [SQLRat](/software/S0390) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [SUNBURST](/software/S0559) <small style="color:#929393">(v2.3&#8594;v2.4)</small>
* [SUNSPOT](/software/S0562) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [ServHelper](/software/S0382) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [ShadowPad](/software/S0596) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Sibot](/software/S0589) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Sliver](/software/S0633) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Stuxnet](/software/S0603) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [SysUpdate](/software/S0663) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Systeminfo](/software/S0096) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [TEARDROP](/software/S0560) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [TYPEFRAME](/software/S0263) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [ThreatNeedle](/software/S0665) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [TinyTurla](/software/S0668) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Torisma](/software/S0678) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [TrailBlazer](/software/S0682) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Ursnif](/software/S0386) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Valak](/software/S0476) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Volgmer](/software/S0180) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [WhisperGate](/software/S0689) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Zeus Panda](/software/S0330) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [certutil](/software/S0160) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [dsquery](/software/S0105) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [netsh](/software/S0108) <small style="color:#929393">(v1.1&#8594;v1.2)</small>

#### Patches

* [CORESHELL](/software/S0137) <small style="color:#929393">(v2.1)</small>
* [ChChes](/software/S0144) <small style="color:#929393">(v1.1)</small>
* [Conficker](/software/S0608) <small style="color:#929393">(v1.0)</small>
* [ConnectWise](/software/S0591) <small style="color:#929393">(v1.0)</small>
* [Crimson](/software/S0115) <small style="color:#929393">(v1.3)</small>
* [Derusbi](/software/S0021) <small style="color:#929393">(v1.2)</small>
* [Duqu](/software/S0038) <small style="color:#929393">(v1.2)</small>
* [EKANS](/software/S0605) <small style="color:#929393">(v2.0)</small>
* [EvilGrab](/software/S0152) <small style="color:#929393">(v1.1)</small>
* [HDoor](/software/S0061) <small style="color:#929393">(v1.0)</small>
* [Hikit](/software/S0009) <small style="color:#929393">(v1.3)</small>
* [Hydraq](/software/S0203) <small style="color:#929393">(v2.0)</small>
* [KeyBoy](/software/S0387) <small style="color:#929393">(v1.2)</small>
* [KillDisk](/software/S0607) <small style="color:#929393">(v1.1)</small>
* [LockerGoga](/software/S0372) <small style="color:#929393">(v2.0)</small>
* [Ngrok](/software/S0508) <small style="color:#929393">(v1.1)</small>
* [NotPetya](/software/S0368) <small style="color:#929393">(v2.0)</small>
* [OLDBAIT](/software/S0138) <small style="color:#929393">(v1.1)</small>
* [PoisonIvy](/software/S0012) <small style="color:#929393">(v2.1)</small>
* [Rclone](/software/S1040) <small style="color:#929393">(v1.0)</small>
* [RedLeaves](/software/S0153) <small style="color:#929393">(v1.1)</small>
* [Remcos](/software/S0332) <small style="color:#929393">(v1.3)</small>
* [SILENTTRINITY](/software/S0692) <small style="color:#929393">(v1.0)</small>
* [TrickBot](/software/S0266) <small style="color:#929393">(v2.0)</small>
* [WannaCry](/software/S0366) <small style="color:#929393">(v1.1)</small>
* [Winnti for Windows](/software/S0141) <small style="color:#929393">(v3.0)</small>
* [YAHOYAH](/software/S0388) <small style="color:#929393">(v1.1)</small>
* [Zox](/software/S0672) <small style="color:#929393">(v1.0)</small>
* [ZxShell](/software/S0412) <small style="color:#929393">(v1.2)</small>
* [gh0st RAT](/software/S0032) <small style="color:#929393">(v3.1)</small>

### Mobile

#### New Software

* [AbstractEmu](/software/S1061) <small style="color:#929393">(v1.0)</small>
* [Drinik](/software/S1054) <small style="color:#929393">(v1.0)</small>
* [FluBot](/software/S1067) <small style="color:#929393">(v1.0)</small>
* [S.O.V.A.](/software/S1062) <small style="color:#929393">(v1.0)</small>
* [SharkBot](/software/S1055) <small style="color:#929393">(v1.0)</small>
* [TangleBot](/software/S1069) <small style="color:#929393">(v1.0)</small>
* [TianySpy](/software/S1056) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [YiSpecter](/software/S0311) <small style="color:#929393">(v1.0&#8594;v2.0)</small>

#### Minor Version Changes

* [Bread](/software/S0432) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [HummingBad](/software/S0322) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Patches

* [BusyGasper](/software/S0655) <small style="color:#929393">(v1.0)</small>

### ICS

#### New Software

* [Industroyer2](/software/S1072) <small style="color:#929393">(v1.0)</small>

#### Minor Version Changes

* [REvil](/software/S0496) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Stuxnet](/software/S0603) <small style="color:#929393">(v1.2&#8594;v1.3)</small>

#### Patches

* [Conficker](/software/S0608) <small style="color:#929393">(v1.0)</small>
* [Duqu](/software/S0038) <small style="color:#929393">(v1.2)</small>
* [EKANS](/software/S0605) <small style="color:#929393">(v2.0)</small>
* [INCONTROLLER](/software/S1045) <small style="color:#929393">(v1.0)</small>
* [KillDisk](/software/S0607) <small style="color:#929393">(v1.1)</small>
* [LockerGoga](/software/S0372) <small style="color:#929393">(v2.0)</small>
* [NotPetya](/software/S0368) <small style="color:#929393">(v2.0)</small>
* [Triton](/software/S1009) <small style="color:#929393">(v1.0)</small>
* [WannaCry](/software/S0366) <small style="color:#929393">(v1.1)</small>

## Groups

### Enterprise

#### New Groups

* [CURIUM](/groups/G1012) <small style="color:#929393">(v1.0)</small>
* [LuminousMoth](/groups/G1014) <small style="color:#929393">(v1.0)</small>
* [Metador](/groups/G1013) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [APT29](/groups/G0016) <small style="color:#929393">(v3.1&#8594;v4.0)</small>
* [GOLD SOUTHFIELD](/groups/G0115) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Sandworm Team](/groups/G0034) <small style="color:#929393">(v2.2&#8594;v3.0)</small>

#### Minor Version Changes

* [APT19](/groups/G0073) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [APT32](/groups/G0050) <small style="color:#929393">(v2.5&#8594;v2.6)</small>
* [APT41](/groups/G0096) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [Aquatic Panda](/groups/G0143) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Chimera](/groups/G0114) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Cobalt Group](/groups/G0080) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Ember Bear](/groups/G1003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [FIN6](/groups/G0037) <small style="color:#929393">(v3.2&#8594;v3.3)</small>
* [FIN7](/groups/G0046) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [FIN8](/groups/G0061) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Fox Kitten](/groups/G0117) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Gamaredon Group](/groups/G0047) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [HAFNIUM](/groups/G0125) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [HEXANE](/groups/G1001) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [LAPSUS$](/groups/G1004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Lazarus Group](/groups/G0032) <small style="color:#929393">(v3.1&#8594;v3.2)</small>
* [LazyScripter](/groups/G0140) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Leafminer](/groups/G0077) <small style="color:#929393">(v2.3&#8594;v2.4)</small>
* [Magic Hound](/groups/G0059) <small style="color:#929393">(v5.0&#8594;v5.1)</small>
* [MuddyWater](/groups/G0069) <small style="color:#929393">(v4.0&#8594;v4.1)</small>
* [Mustang Panda](/groups/G0129) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [OilRig](/groups/G0049) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [Patchwork](/groups/G0040) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Sidewinder](/groups/G0121) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Silence](/groups/G0091) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [TA505](/groups/G0092) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [TA551](/groups/G0127) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Threat Group-3390](/groups/G0027) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Turla](/groups/G0010) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [Wizard Spider](/groups/G0102) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [ZIRCONIUM](/groups/G0128) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Patches

* [APT28](/groups/G0007) <small style="color:#929393">(v4.0)</small>
* [APT33](/groups/G0064) <small style="color:#929393">(v1.4)</small>
* [Andariel](/groups/G0138) <small style="color:#929393">(v1.0)</small>
* [Axiom](/groups/G0001) <small style="color:#929393">(v2.0)</small>
* [Dragonfly](/groups/G0035) <small style="color:#929393">(v3.1)</small>
* [FIN4](/groups/G0085) <small style="color:#929393">(v1.2)</small>
* [Kimsuky](/groups/G0094) <small style="color:#929393">(v3.1)</small>
* [TEMP.Veles](/groups/G0088) <small style="color:#929393">(v1.3)</small>
* [Winnti Group](/groups/G0044) <small style="color:#929393">(v1.2)</small>
* [menuPass](/groups/G0045) <small style="color:#929393">(v2.1)</small>

### Mobile

#### Major Version Changes

* [Sandworm Team](/groups/G0034) <small style="color:#929393">(v2.2&#8594;v3.0)</small>

#### Patches

* [APT28](/groups/G0007) <small style="color:#929393">(v4.0)</small>

### ICS

#### Major Version Changes

* [GOLD SOUTHFIELD](/groups/G0115) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Sandworm Team](/groups/G0034) <small style="color:#929393">(v2.2&#8594;v3.0)</small>

#### Minor Version Changes

* [FIN6](/groups/G0037) <small style="color:#929393">(v3.2&#8594;v3.3)</small>
* [FIN7](/groups/G0046) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [HEXANE](/groups/G1001) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Lazarus Group](/groups/G0032) <small style="color:#929393">(v3.1&#8594;v3.2)</small>
* [OilRig](/groups/G0049) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [Wizard Spider](/groups/G0102) <small style="color:#929393">(v2.0&#8594;v2.1)</small>

#### Patches

* [APT33](/groups/G0064) <small style="color:#929393">(v1.4)</small>
* [Dragonfly](/groups/G0035) <small style="color:#929393">(v3.1)</small>
* [TEMP.Veles](/groups/G0088) <small style="color:#929393">(v1.3)</small>

## Campaigns

### Enterprise

#### New Campaigns

* [2016 Ukraine Electric Power Attack](/campaigns/C0025) <small style="color:#929393">(v1.0)</small>
* [C0017](/campaigns/C0017) <small style="color:#929393">(v1.0)</small>
* [C0018](/campaigns/C0018) <small style="color:#929393">(v1.0)</small>
* [C0021](/campaigns/C0021) <small style="color:#929393">(v1.0)</small>
* [Operation Dream Job](/campaigns/C0022) <small style="color:#929393">(v1.0)</small>
* [Operation Ghost](/campaigns/C0023) <small style="color:#929393">(v1.0)</small>
* [SolarWinds Compromise](/campaigns/C0024) <small style="color:#929393">(v1.0)</small>

#### Minor Version Changes

* [Frankenstein](/campaigns/C0001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Operation CuckooBees](/campaigns/C0012) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Operation Wocao](/campaigns/C0014) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

### Mobile

### ICS

#### New Campaigns

* [2016 Ukraine Electric Power Attack](/campaigns/C0025) <small style="color:#929393">(v1.0)</small>
* [Maroochy Water Breach](/campaigns/C0020) <small style="color:#929393">(v1.0)</small>

## Mitigations

### Enterprise

#### Minor Version Changes

* [Audit](/mitigations/M1047) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Operating System Configuration](/mitigations/M1028) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Restrict Registry Permissions](/mitigations/M1024) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

### Mobile

### ICS

#### New Mitigations

* [Validate Program Inputs](/mitigations/M0818) <small style="color:#929393">(v1.0)</small>

#### Minor Version Changes

* [Static Network Configuration](/mitigations/M0814) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Patches

* [Access Management](/mitigations/M0801) <small style="color:#929393">(v1.0)</small>
* [Account Use Policies](/mitigations/M0936) <small style="color:#929393">(v1.0)</small>
* [Antivirus/Antimalware](/mitigations/M0949) <small style="color:#929393">(v1.0)</small>
* [Application Developer Guidance](/mitigations/M0913) <small style="color:#929393">(v1.0)</small>
* [Application Isolation and Sandboxing](/mitigations/M0948) <small style="color:#929393">(v1.0)</small>
* [Audit](/mitigations/M0947) <small style="color:#929393">(v1.0)</small>
* [Authorization Enforcement](/mitigations/M0800) <small style="color:#929393">(v1.0)</small>
* [Boot Integrity](/mitigations/M0946) <small style="color:#929393">(v1.0)</small>
* [Code Signing](/mitigations/M0945) <small style="color:#929393">(v1.0)</small>
* [Communication Authenticity](/mitigations/M0802) <small style="color:#929393">(v1.0)</small>
* [Data Backup](/mitigations/M0953) <small style="color:#929393">(v1.0)</small>
* [Data Loss Prevention](/mitigations/M0803) <small style="color:#929393">(v1.0)</small>
* [Disable or Remove Feature or Program](/mitigations/M0942) <small style="color:#929393">(v1.0)</small>
* [Encrypt Network Traffic](/mitigations/M0808) <small style="color:#929393">(v1.0)</small>
* [Encrypt Sensitive Information](/mitigations/M0941) <small style="color:#929393">(v1.0)</small>
* [Execution Prevention](/mitigations/M0938) <small style="color:#929393">(v1.0)</small>
* [Exploit Protection](/mitigations/M0950) <small style="color:#929393">(v1.0)</small>
* [Filter Network Traffic](/mitigations/M0937) <small style="color:#929393">(v1.0)</small>
* [Human User Authentication](/mitigations/M0804) <small style="color:#929393">(v1.0)</small>
* [Limit Access to Resource Over Network](/mitigations/M0935) <small style="color:#929393">(v1.0)</small>
* [Limit Hardware Installation](/mitigations/M0934) <small style="color:#929393">(v1.0)</small>
* [Minimize Wireless Signal Propagation](/mitigations/M0806) <small style="color:#929393">(v1.0)</small>
* [Multi-factor Authentication](/mitigations/M0932) <small style="color:#929393">(v1.0)</small>
* [Network Allowlists](/mitigations/M0807) <small style="color:#929393">(v1.0)</small>
* [Network Intrusion Prevention](/mitigations/M0931) <small style="color:#929393">(v1.0)</small>
* [Network Segmentation](/mitigations/M0930) <small style="color:#929393">(v1.0)</small>
* [Operating System Configuration](/mitigations/M0928) <small style="color:#929393">(v1.0)</small>
* [Operational Information Confidentiality](/mitigations/M0809) <small style="color:#929393">(v1.0)</small>
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
* [Supply Chain Management](/mitigations/M0817) <small style="color:#929393">(v1.0)</small>
* [Update Software](/mitigations/M0951) <small style="color:#929393">(v1.0)</small>
* [User Account Management](/mitigations/M0918) <small style="color:#929393">(v1.0)</small>
* [User Training](/mitigations/M0917) <small style="color:#929393">(v1.0)</small>
* [Vulnerability Scanning](/mitigations/M0916) <small style="color:#929393">(v1.0)</small>
* [Watchdog Timers](/mitigations/M0815) <small style="color:#929393">(v1.0)</small>

## Data Sources

### Enterprise

#### Patches

* [Command](/datasources/DS0017) <small style="color:#929393">(v1.1)</small>
* [File](/datasources/DS0022) <small style="color:#929393">(v1.0)</small>
* [Logon Session](/datasources/DS0028) <small style="color:#929393">(v1.1)</small>
* [Malware Repository](/datasources/DS0004) <small style="color:#929393">(v1.1)</small>
* [Network Traffic](/datasources/DS0029) <small style="color:#929393">(v1.1)</small>
* [Process](/datasources/DS0009) <small style="color:#929393">(v1.1)</small>
* [Script](/datasources/DS0012) <small style="color:#929393">(v1.1)</small>
* [Sensor Health](/datasources/DS0013) <small style="color:#929393">(v1.1)</small>
* [User Account](/datasources/DS0002) <small style="color:#929393">(v1.1)</small>

### Mobile

#### New Data Sources

* [Application Vetting](/datasources/DS0041) <small style="color:#929393">(v1.0)</small>
* [Command](/datasources/DS0017) <small style="color:#eb6635">(v1.1)</small>
* [Network Traffic](/datasources/DS0029) <small style="color:#eb6635">(v1.1)</small>
* [Process](/datasources/DS0009) <small style="color:#eb6635">(v1.1)</small>
* [Sensor Health](/datasources/DS0013) <small style="color:#eb6635">(v1.1)</small>
* [User Interface](/datasources/DS0042) <small style="color:#929393">(v1.0)</small>

### ICS

#### Patches

* [Asset](/datasources/DS0039) <small style="color:#929393">(v1.0)</small>
* [Command](/datasources/DS0017) <small style="color:#929393">(v1.1)</small>
* [File](/datasources/DS0022) <small style="color:#929393">(v1.0)</small>
* [Logon Session](/datasources/DS0028) <small style="color:#929393">(v1.1)</small>
* [Network Traffic](/datasources/DS0029) <small style="color:#929393">(v1.1)</small>
* [Operational Databases](/datasources/DS0040) <small style="color:#929393">(v1.0)</small>
* [Process](/datasources/DS0009) <small style="color:#929393">(v1.1)</small>
* [Script](/datasources/DS0012) <small style="color:#929393">(v1.1)</small>
* [User Account](/datasources/DS0002) <small style="color:#929393">(v1.1)</small>

## Data Components

### Enterprise

#### Patches

* [OS API Execution](/datasources/DS0009/#OS%20API%20Execution) <small style="color:#929393">(v1.0)</small>

### Mobile

#### New Data Components

* [API Calls](/datasources/DS0041/#API%20Calls) <small style="color:#929393">(v1.0)</small>
* [Command Execution](/datasources/DS0017/#Command%20Execution) <small style="color:#eb6635">(v1.1)</small>
* [Host Status](/datasources/DS0013/#Host%20Status) <small style="color:#eb6635">(v1.1)</small>
* [Network Communication](/datasources/DS0041/#Network%20Communication) <small style="color:#929393">(v1.0)</small>
* [Network Connection Creation](/datasources/DS0029/#Network%20Connection%20Creation) <small style="color:#eb6635">(v1.1)</small>
* [Network Traffic Content](/datasources/DS0029/#Network%20Traffic%20Content) <small style="color:#929393">(v1.0)</small>
* [Network Traffic Flow](/datasources/DS0029/#Network%20Traffic%20Flow) <small style="color:#929393">(v1.0)</small>
* [Permissions Request](/datasources/DS0042/#Permissions%20Request) <small style="color:#929393">(v1.0)</small>
* [Permissions Requests](/datasources/DS0041/#Permissions%20Requests) <small style="color:#929393">(v1.0)</small>
* [Process Creation](/datasources/DS0009/#Process%20Creation) <small style="color:#eb6635">(v1.1)</small>
* [Process Metadata](/datasources/DS0009/#Process%20Metadata) <small style="color:#929393">(v1.0)</small>
* [Process Termination](/datasources/DS0009/#Process%20Termination) <small style="color:#929393">(v1.0)</small>
* [Protected Configuration](/datasources/DS0041/#Protected%20Configuration) <small style="color:#929393">(v1.0)</small>
* [System Notifications](/datasources/DS0042/#System%20Notifications) <small style="color:#929393">(v1.0)</small>
* [System Settings](/datasources/DS0042/#System%20Settings) <small style="color:#929393">(v1.0)</small>

### ICS

#### Patches

* [OS API Execution](/datasources/DS0009/#OS%20API%20Execution) <small style="color:#929393">(v1.0)</small>

## Contributors to this release

* Adam Lichters
* Adrien Bataille
* Akiko To, NEC Corporation
* Akshat Pradhan, Qualys
* Anders Vejlby
* Austin Clark, @c2defense
* Ben Smith
* Bryan Onel
* Caio Silva
* Center for Threat-Informed Defense (CTID)
* Christopher Peacock
* Cisco
* CrowdStrike Falcon OverWatch
* Daniel Acevedo, @darmad0, ARMADO
* Daniyal Naeem, BT Security
* Denise Tan
* Dor Edry, Microsoft
* Douglas Weir
* Duane Michael
* Dylan
* Elpidoforos Maragkos, @emaragkos
* Emad Al-Mousa, Saudi Aramco
* ExtraHop
* Felix Eberstaller
* Filip Kafka, ESET
* Flavio Costa, Cisco
* Gavin Knapp
* George Thomas
* Goldstein Menachem
* Hiroki Nagahama, NEC Corporation
* Hubert Mank
* Inna Danilevich, U.S Bank
* Jared Wilson
* Jason Sevilla
* Jeffrey Barto
* Jeremy Kennelly
* Jimmy Wylie, Dragos, Inc.
* Joas Antonio dos Santos, @C0d3Cr4zy
* Joe Gumke, U.S. Bank
* Jonny Johnson
* Josh Arenas, Trustwave Spiderlabs
* Juan Carlos Campuzano - Mnemo-CERT
* Kuessner Consulting
* Kyaw Pyiyt Htet, @KyawPyiytHtet
* Liora Itkin
* Liran Ravich, CardinalOps
* Lucas Heiligenstein
* Manikantan Srinivasan, NEC Corporation India
* Marcus Weeks
* Mark Wee
* Massimiliano Romano, BT Security
* Mathieu Hinse
* Matt Brenton, Zurich Global Information Security
* Mayuresh Dani, Qualys
* Mindaugas Gudzis, BT Security
* Miroslav Babiš, ESET
* Muhammad Moiz Arshad, @5T34L7H
* Nader Zaveri
* Nichols Jasper
* Ohad Zaidenberg, @ohad_mz
* Ozan Olali
* Pallavi Sivakumaran
* Pooja Natarajan, NEC Corporation India
* Ross Brittain
* Scott Cook, Capital One
* Shailesh Tiwary (Indian Army)
* Simona David
* Sittikorn Sangrattanapitak
* Thanabodi
* Tim (Wadhwa-)Brown
* Tim Peck
* Tom Hegel
* Tristan Bennett, Seamless Intelligence
* TruKno
* Vinayak Wadhwa, SAFE Security
* Wataru Takahashi, NEC Corporation
* Yinon Engelsman, Talon Cyber Security
* Yonatan Gotlib, Talon Cyber Security
* Yoshihiro Kori, NEC Corporation
* Zaw Min Htun, @Z3TAE
* Zuzana Legáthová, ESET
