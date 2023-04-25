Title: Updates - April 2022
Date: April 2022
Category: Cyber Threat Intelligence
Authors: Adam Pennington
Template: resources/update-post
url: /resources/updates/updates-april-2022
save_as: resources/updates/updates-april-2022/index.html

| Version | Start Date | End Date | Data | Changelogs |
|:--------|:-----------|:---------|:-----|:-----------|
| [ATT&CK v11](/versions/v11) | April 25, 2022 | October 24, 2022 | [v11.0 on MITRE/CTI](https://github.com/mitre/cti/releases/tag/ATT%26CK-v11.0)<br />[v11.1 on MITRE/CTI](https://github.com/mitre/cti/releases/tag/ATT%26CK-v11.1)<br />[v11.2 on MITRE/CTI](https://github.com/mitre/cti/releases/tag/ATT%26CK-v11.2)<br />[v11.3 on MITRE/CTI](https://github.com/mitre/cti/releases/tag/ATT%26CK-v11.3) | v10.1 - v11.0 [Details](/docs/changelogs/v10.1-v11.0/changelog-detailed.html) ([JSON](/docs/changelogs/v10.1-v11.0/changelog.json))<br />v11.0 - v11.1 [Details](/docs/changelogs/v11.0-v11.1/changelog-detailed.html) ([JSON](/docs/changelogs/v11.0-v11.1/changelog.json))<br />v11.1 - v11.2 [Details](/docs/changelogs/v11.1-v11.2/changelog-detailed.html) ([JSON](/docs/changelogs/v11.1-v11.2/changelog.json))<br />v11.2 - v11.3 [Details](/docs/changelogs/v11.2-v11.3/changelog-detailed.html) ([JSON](/docs/changelogs/v11.2-v11.3/changelog.json)) |

The April 2022 (v11) ATT&CK release updates Techniques, Groups, and Software for Enterprise, Mobile, and ICS. The biggest changes are the restructuring of Detections, now tied to [Data Source](/datasources/) and Data Component objects in Enterprise ATT&CK, a beta release of ATT&CK for Mobile leveraging sub-techniques, and [ATT&CK for ICS now on attack.mitre.org](/matrices/ics/) An [accompanying blog post](https://medium.com/mitre-attack/attack-goes-to-v11-599a9112a025) describes these changes as well as improvements across ATT&CK's various domains and platforms.

This release contains a beta version of [ATT&CK for Mobile](/matrices/mobile/) represented using sub-techniques. The current stable version of ATT&CK for Mobile can still be found at [https://attack.mitre.org/versions/v10/matrices/mobile/](https://attack.mitre.org/versions/v10/matrices/mobile/). Information on how to make the transition to this new version of ATT&CK for Mobile can be found in an [accompanying blog post](https://medium.com/mitre-attack/attack-goes-to-v11-599a9112a025). A version of this beta content rendered in STIX can be found in our [GitHub repo](https://github.com/mitre/cti/releases/tag/ATT%26CK-v11.0-mobile-beta).

In this release we have replaced the Enterprise Sub-Techniques [Boot or Logon Autostart Execution: Plist Modification (T1547.011)](https://attack.mitre.org/versions/v10/techniques/T1547/011/) with [Plist File Modification (T1647)](/techniques/T1647/) and [Scheduled Task/Job: At (Linux)(T1053.001)](https://attack.mitre.org/versions/v10/techniques/T1053/001/) was incorporated into [Scheduled Task/Job: At (T1053.002)](/techniques/T1053/002/) in to better reflect adversary behavior.

This version of ATT&CK for Enterprise contains 14 Tactics, 191 Techniques, 386 Sub-techniques, 134 Groups, and 680 Pieces of Software.

## Techniques

### Enterprise

#### New Techniques

* Account Manipulation: [Device Registration](/techniques/T1098/005)
* Active Scanning: [Wordlist Scanning](/techniques/T1595/003)
* Adversary-in-the-Middle: [DHCP Spoofing](/techniques/T1557/003)
* [Debugger Evasion](/techniques/T1622)
* Hide Artifacts: [Process Argument Spoofing](/techniques/T1564/010)
* Hijack Execution Flow: [KernelCallbackTable](/techniques/T1574/013)
* Inter-Process Communication: [XPC Services](/techniques/T1559/003)
* Modify Authentication Process: [Reversible Encryption](/techniques/T1556/005)
* [Multi-Factor Authentication Request Generation](/techniques/T1621)
* [Plist File Modification](/techniques/T1647)
* Process Injection: [ListPlanting](/techniques/T1055/015)
* Server Software Component: [Terminal Services DLL](/techniques/T1505/005)

#### Technique changes

* Abuse Elevation Control Mechanism: [Setuid and Setgid](/techniques/T1548/001)
* [Account Access Removal](/techniques/T1531)
* [Account Manipulation](/techniques/T1098)
  * [Additional Cloud Credentials](/techniques/T1098/001)
  * [Additional Cloud Roles](/techniques/T1098/003)
  * [Additional Email Delegate Permissions](/techniques/T1098/002)
  * [SSH Authorized Keys](/techniques/T1098/004)
* [Adversary-in-the-Middle](/techniques/T1557)
* [Application Window Discovery](/techniques/T1010)
* Archive Collected Data: [Archive via Utility](/techniques/T1560/001)
* [Automated Collection](/techniques/T1119)
* Boot or Logon Autostart Execution: [Kernel Modules and Extensions](/techniques/T1547/006)
* Boot or Logon Autostart Execution: [Port Monitors](/techniques/T1547/010)
* Boot or Logon Autostart Execution: [Re-opened Applications](/techniques/T1547/007)
* Boot or Logon Initialization Scripts: [Login Hook](/techniques/T1037/002)
* [Brute Force](/techniques/T1110)
  * [Password Cracking](/techniques/T1110/002)
  * [Password Guessing](/techniques/T1110/001)
* [Build Image on Host](/techniques/T1612)
* [Cloud Infrastructure Discovery](/techniques/T1580)
* [Command and Scripting Interpreter](/techniques/T1059)
  * [PowerShell](/techniques/T1059/001)
  * [Visual Basic](/techniques/T1059/005)
* [Compromise Infrastructure](/techniques/T1584)
  * [DNS Server](/techniques/T1584/002)
  * [Domains](/techniques/T1584/001)
* [Container Administration Command](/techniques/T1609)
* Create Account: [Cloud Account](/techniques/T1136/003)
* [Create or Modify System Process](/techniques/T1543)
  * [Launch Agent](/techniques/T1543/001)
  * [Windows Service](/techniques/T1543/003)
* Credentials from Password Stores: [Keychain](/techniques/T1555/001)
* Credentials from Password Stores: [Securityd Memory](/techniques/T1555/002)
* [Data Encrypted for Impact](/techniques/T1486)
* [Data Manipulation](/techniques/T1565)
  * [Runtime Data Manipulation](/techniques/T1565/003)
  * [Stored Data Manipulation](/techniques/T1565/001)
  * [Transmitted Data Manipulation](/techniques/T1565/002)
* [Data Staged](/techniques/T1074)
  * [Local Data Staging](/techniques/T1074/001)
* [Data from Local System](/techniques/T1005)
* [Defacement](/techniques/T1491)
  * [External Defacement](/techniques/T1491/002)
  * [Internal Defacement](/techniques/T1491/001)
* [Deploy Container](/techniques/T1610)
* [Drive-by Compromise](/techniques/T1189)
* Endpoint Denial of Service: [Application Exhaustion Flood](/techniques/T1499/003)
* Endpoint Denial of Service: [Application or System Exploitation](/techniques/T1499/004)
* Endpoint Denial of Service: [OS Exhaustion Flood](/techniques/T1499/001)
* Endpoint Denial of Service: [Service Exhaustion Flood](/techniques/T1499/002)
* [Escape to Host](/techniques/T1611)
* Event Triggered Execution: [PowerShell Profile](/techniques/T1546/013)
* Exfiltration Over Alternative Protocol: [Exfiltration Over Unencrypted Non-C2 Protocol](/techniques/T1048/003)
* Exfiltration Over Other Network Medium: [Exfiltration Over Bluetooth](/techniques/T1011/001)
* [Exploitation for Client Execution](/techniques/T1203)
* [File and Directory Discovery](/techniques/T1083)
* [Firmware Corruption](/techniques/T1495)
* [Gather Victim Identity Information](/techniques/T1589)
  * [Email Addresses](/techniques/T1589/002)
* [Hardware Additions](/techniques/T1200)
* Hide Artifacts: [Email Hiding Rules](/techniques/T1564/008)
* Hide Artifacts: [Hidden Users](/techniques/T1564/002)
* Hide Artifacts: [Hidden Window](/techniques/T1564/003)
* [Hijack Execution Flow](/techniques/T1574)
* Impair Defenses: [Disable Cloud Logs](/techniques/T1562/008)
* Impair Defenses: [Downgrade Attack](/techniques/T1562/010)
* Impair Defenses: [Impair Command History Logging](/techniques/T1562/003)
* [Implant Internal Image](/techniques/T1525)
* [Indicator Removal on Host](/techniques/T1070)
  * [Clear Command History](/techniques/T1070/003)
  * [Clear Windows Event Logs](/techniques/T1070/001)
  * [File Deletion](/techniques/T1070/004)
* [Ingress Tool Transfer](/techniques/T1105)
* [Inhibit System Recovery](/techniques/T1490)
* Input Capture: [GUI Input Capture](/techniques/T1056/002)
* [Inter-Process Communication](/techniques/T1559)
  * [Dynamic Data Exchange](/techniques/T1559/002)
* [Internal Spearphishing](/techniques/T1534)
* [Lateral Tool Transfer](/techniques/T1570)
* [Modify Authentication Process](/techniques/T1556)
* [Multi-Factor Authentication Interception](/techniques/T1111)
* [Network Boundary Bridging](/techniques/T1599)
* Network Denial of Service: [Direct Network Flood](/techniques/T1498/001)
* Network Denial of Service: [Reflection Amplification](/techniques/T1498/002)
* [Network Service Discovery](/techniques/T1046)
* [Network Sniffing](/techniques/T1040)
* OS Credential Dumping: [NTDS](/techniques/T1003/003)
* Obfuscated Files or Information: [Software Packing](/techniques/T1027/002)
* [Password Policy Discovery](/techniques/T1201)
* [Peripheral Device Discovery](/techniques/T1120)
* Phishing: [Spearphishing Link](/techniques/T1566/002)
* Phishing for Information: [Spearphishing Link](/techniques/T1598/003)
* Pre-OS Boot: [Component Firmware](/techniques/T1542/002)
* Process Injection: [Process Hollowing](/techniques/T1055/012)
* [Remote Access Software](/techniques/T1219)
* Remote Services: [Remote Desktop Protocol](/techniques/T1021/001)
* [Remote System Discovery](/techniques/T1018)
* [Resource Hijacking](/techniques/T1496)
* [Rogue Domain Controller](/techniques/T1207)
* [Scheduled Task/Job](/techniques/T1053)
  * [At](/techniques/T1053/002)
  * [Container Orchestration Job](/techniques/T1053/007)
  * [Scheduled Task](/techniques/T1053/005)
* [Server Software Component](/techniques/T1505)
* Software Discovery: [Security Software Discovery](/techniques/T1518/001)
* Stage Capabilities: [Drive-by Target](/techniques/T1608/004)
* [Steal Application Access Token](/techniques/T1528)
* [Steal or Forge Kerberos Tickets](/techniques/T1558)
  * [Kerberoasting](/techniques/T1558/003)
* Subvert Trust Controls: [Mark-of-the-Web Bypass](/techniques/T1553/005)
* [Supply Chain Compromise](/techniques/T1195)
* [System Binary Proxy Execution](/techniques/T1218)
  * [CMSTP](/techniques/T1218/003)
  * [Compiled HTML File](/techniques/T1218/001)
  * [Control Panel](/techniques/T1218/002)
  * [InstallUtil](/techniques/T1218/004)
  * [MMC](/techniques/T1218/014)
  * [Mavinject](/techniques/T1218/013)
  * [Mshta](/techniques/T1218/005)
  * [Msiexec](/techniques/T1218/007)
  * [Odbcconf](/techniques/T1218/008)
  * [Regsvcs/Regasm](/techniques/T1218/009)
  * [Regsvr32](/techniques/T1218/010)
  * [Rundll32](/techniques/T1218/011)
  * [Verclsid](/techniques/T1218/012)
* [System Information Discovery](/techniques/T1082)
* [System Network Configuration Discovery](/techniques/T1016)
* [System Network Connections Discovery](/techniques/T1049)
* [System Script Proxy Execution](/techniques/T1216)
  * [PubPrn](/techniques/T1216/001)
* [System Service Discovery](/techniques/T1007)
* [System Services](/techniques/T1569)
* [System Shutdown/Reboot](/techniques/T1529)
* [Template Injection](/techniques/T1221)
* [Traffic Signaling](/techniques/T1205)
* [Transfer Data to Cloud Account](/techniques/T1537)
* Unsecured Credentials: [Bash History](/techniques/T1552/003)
* Unsecured Credentials: [Cloud Instance Metadata API](/techniques/T1552/005)
* Unsecured Credentials: [Container API](/techniques/T1552/007)
* Use Alternate Authentication Material: [Application Access Token](/techniques/T1550/001)
* [User Execution](/techniques/T1204)
  * [Malicious File](/techniques/T1204/002)
* [Valid Accounts](/techniques/T1078)
  * [Cloud Accounts](/techniques/T1078/004)
* [Video Capture](/techniques/T1125)

#### Minor Technique changes

* [Abuse Elevation Control Mechanism](/techniques/T1548)
  * [Bypass User Account Control](/techniques/T1548/002)
  * [Sudo and Sudo Caching](/techniques/T1548/003)
* [Active Scanning](/techniques/T1595)
* [Archive Collected Data](/techniques/T1560)
* [Automated Exfiltration](/techniques/T1020)
  * [Traffic Duplication](/techniques/T1020/001)
* [Boot or Logon Autostart Execution](/techniques/T1547)
  * [Authentication Package](/techniques/T1547/002)
  * [LSASS Driver](/techniques/T1547/008)
  * [Registry Run Keys / Startup Folder](/techniques/T1547/001)
  * [Time Providers](/techniques/T1547/003)
  * [Winlogon Helper DLL](/techniques/T1547/004)
* [Boot or Logon Initialization Scripts](/techniques/T1037)
  * [Startup Items](/techniques/T1037/005)
* [Browser Extensions](/techniques/T1176)
* [Browser Session Hijacking](/techniques/T1185)
* [Cloud Storage Object Discovery](/techniques/T1619)
* Command and Scripting Interpreter: [AppleScript](/techniques/T1059/002)
* Command and Scripting Interpreter: [Network Device CLI](/techniques/T1059/008)
* Compromise Infrastructure: [Botnet](/techniques/T1584/005)
* [Credentials from Password Stores](/techniques/T1555)
  * [Credentials from Web Browsers](/techniques/T1555/003)
  * [Password Managers](/techniques/T1555/005)
* [Data from Configuration Repository](/techniques/T1602)
  * [Network Device Configuration Dump](/techniques/T1602/002)
* [Data from Information Repositories](/techniques/T1213)
* Develop Capabilities: [Malware](/techniques/T1587/001)
* [Domain Trust Discovery](/techniques/T1482)
* [Dynamic Resolution](/techniques/T1568)
  * [Domain Generation Algorithms](/techniques/T1568/002)
* [Endpoint Denial of Service](/techniques/T1499)
* [Event Triggered Execution](/techniques/T1546)
  * [Change Default File Association](/techniques/T1546/001)
  * [Emond](/techniques/T1546/014)
  * [LC_LOAD_DYLIB Addition](/techniques/T1546/006)
  * [Netsh Helper DLL](/techniques/T1546/007)
  * [Screensaver](/techniques/T1546/002)
  * [Windows Management Instrumentation Event Subscription](/techniques/T1546/003)
* [Exfiltration Over Other Network Medium](/techniques/T1011)
* [Exploit Public-Facing Application](/techniques/T1190)
* [Exploitation of Remote Services](/techniques/T1210)
* [Hide Artifacts](/techniques/T1564)
* [Impair Defenses](/techniques/T1562)
* [Input Capture](/techniques/T1056)
* Modify Authentication Process: [Network Device Authentication](/techniques/T1556/004)
* [Native API](/techniques/T1106)
* [Network Denial of Service](/techniques/T1498)
* [Non-Application Layer Protocol](/techniques/T1095)
* [OS Credential Dumping](/techniques/T1003)
* [Obfuscated Files or Information](/techniques/T1027)
* Permission Groups Discovery: [Cloud Groups](/techniques/T1069/003)
* [Phishing](/techniques/T1566)
* [Phishing for Information](/techniques/T1598)
* [Pre-OS Boot](/techniques/T1542)
* [Process Injection](/techniques/T1055)
  * [VDSO Hijacking](/techniques/T1055/014)
* [Reflective Code Loading](/techniques/T1620)
* [Remote Services](/techniques/T1021)
* Scheduled Task/Job: [Cron](/techniques/T1053/003)
* [Shared Modules](/techniques/T1129)
* [Software Discovery](/techniques/T1518)
* [Stage Capabilities](/techniques/T1608)
* [Subvert Trust Controls](/techniques/T1553)
* Supply Chain Compromise: [Compromise Software Dependencies and Development Tools](/techniques/T1195/001)
* Supply Chain Compromise: [Compromise Software Supply Chain](/techniques/T1195/002)
* [System Owner/User Discovery](/techniques/T1033)
* Traffic Signaling: [Port Knocking](/techniques/T1205/001)
* [Unsecured Credentials](/techniques/T1552)
* [Use Alternate Authentication Material](/techniques/T1550)
* Valid Accounts: [Domain Accounts](/techniques/T1078/002)
* [Windows Management Instrumentation](/techniques/T1047)

#### Technique revocations

* Boot or Logon Autostart Execution: Plist Modification (revoked by [Plist File Modification (T1647)](/techniques/T1647/))
* Scheduled Task/Job: At (Linux) (revoked by Scheduled Task/Job: [At (T1053.002)](/techniques/T1053/002/))

#### Technique deprecations

* No changes

### Mobile v11.0-beta

The below changes represent the Mobile v11.0-beta release. The current production release at [https://attack.mitre.org/versions/v10/matrices/mobile/](https://attack.mitre.org/versions/v10/matrices/mobile/) remains unchanged.

#### New Techniques

* [Abuse Elevation Control Mechanism](/techniques/T1626)
  * [Device Administrator Permissions](/techniques/T1626/001)
* [Account Access Removal](/techniques/T1640)
* [Adversary-in-the-Middle](/techniques/T1638)
* Application Layer Protocol: [Web Protocols](/techniques/T1437/001)
* [Command and Scripting Interpreter](/techniques/T1623)
  * [Unix Shell](/techniques/T1623/001)
* [Compromise Client Software Binary](/techniques/T1645)
* [Credentials from Password Store](/techniques/T1634)
  * [Keychain](/techniques/T1634/001)
* [Data Manipulation](/techniques/T1641)
  * [Transmitted Data Manipulation](/techniques/T1641/001)
* [Dynamic Resolution](/techniques/T1637)
  * [Domain Generation Algorithms](/techniques/T1637/001)
* Encrypted Channel: [Asymmetric Cryptography](/techniques/T1521/002)
* Encrypted Channel: [Symmetric Cryptography](/techniques/T1521/001)
* [Endpoint Denial of Service](/techniques/T1642)
* [Event Triggered Execution](/techniques/T1624)
  * [Broadcast Receivers](/techniques/T1624/001)
* [Execution Guardrails](/techniques/T1627)
  * [Geofencing](/techniques/T1627/001)
* [Exfiltration Over Alternative Protocol](/techniques/T1639)
  * [Exfiltration Over Unencrypted Non-C2 Protocol](/techniques/T1639/001)
* [Exfiltration Over C2 Channel](/techniques/T1646)
* [Generate Traffic from Victim](/techniques/T1643)
* [Hide Artifacts](/techniques/T1628)
  * [Suppress Application Icon](/techniques/T1628/001)
  * [User Evasion](/techniques/T1628/002)
* [Hijack Execution Flow](/techniques/T1625)
  * [System Runtime API Hijacking](/techniques/T1625/001)
* [Impair Defenses](/techniques/T1629)
  * [Device Lockout](/techniques/T1629/002)
  * [Disable or Modify Tools](/techniques/T1629/003)
  * [Prevent Application Removal](/techniques/T1629/001)
* [Indicator Removal on Host](/techniques/T1630)
  * [Disguise Root/Jailbreak Indicators](/techniques/T1630/003)
  * [File Deletion](/techniques/T1630/002)
  * [Uninstall Malicious Application](/techniques/T1630/001)
* Input Capture: [GUI Input Capture](/techniques/T1417/002)
* Input Capture: [Keylogging](/techniques/T1417/001)
* Location Tracking: [Impersonate SS7 Nodes](/techniques/T1430/002)
* Location Tracking: [Remote Device Management Services](/techniques/T1430/001)
* Obfuscated Files or Information: [Software Packing](/techniques/T1406/002)
* Obfuscated Files or Information: [Steganography](/techniques/T1406/001)
* [Out of Band Data](/techniques/T1644)
* [Process Injection](/techniques/T1631)
  * [Ptrace System Calls](/techniques/T1631/001)
* [Protected User Data](/techniques/T1636)
  * [Calendar Entries](/techniques/T1636/001)
  * [Call Log](/techniques/T1636/002)
  * [Contact List](/techniques/T1636/003)
  * [SMS Messages](/techniques/T1636/004)
* Software Discovery: [Security Software Discovery](/techniques/T1418/001)
* [Steal Application Access Token](/techniques/T1635)
  * [URI Hijacking](/techniques/T1635/001)
* [Subvert Trust Controls](/techniques/T1632)
  * [Code Signing Policy Modification](/techniques/T1632/001)
* Supply Chain Compromise: [Compromise Hardware Supply Chain](/techniques/T1474/002)
* Supply Chain Compromise: [Compromise Software Dependencies and Development Tools](/techniques/T1474/001)
* Supply Chain Compromise: [Compromise Software Supply Chain](/techniques/T1474/003)
* [Virtualization/Sandbox Evasion](/techniques/T1633)
  * [System Checks](/techniques/T1633/001)
* Web Service: [Bidirectional Communication](/techniques/T1481/002)
* Web Service: [Dead Drop Resolver](/techniques/T1481/001)
* Web Service: [One-Way Communication](/techniques/T1481/003)

#### Technique changes

* [Access Notifications](/techniques/T1517)
* [Application Layer Protocol](/techniques/T1437)
* [Archive Collected Data](/techniques/T1532)
* [Audio Capture](/techniques/T1429)
* [Boot or Logon Initialization Scripts](/techniques/T1398)
* [Clipboard Data](/techniques/T1414)
* [Data Encrypted for Impact](/techniques/T1471)
* [Data from Local System](/techniques/T1533)
* [Download New Code at Runtime](/techniques/T1407)
* [Drive-By Compromise](/techniques/T1456)
* [Encrypted Channel](/techniques/T1521)
* [Exploitation for Privilege Escalation](/techniques/T1404)
* [Exploitation of Remote Services](/techniques/T1428)
* [File and Directory Discovery](/techniques/T1420)
* [Foreground Persistence](/techniques/T1541)
* [Ingress Tool Transfer](/techniques/T1544)
* [Input Capture](/techniques/T1417)
* [Location Tracking](/techniques/T1430)
* [Lockscreen Bypass](/techniques/T1461)
* [Native API](/techniques/T1575)
* [Network Denial of Service](/techniques/T1464)
* [Network Service Scanning](/techniques/T1423)
* [Non-Standard Port](/techniques/T1509)
* [Obfuscated Files or Information](/techniques/T1406)
* [Process Discovery](/techniques/T1424)
* [Replication Through Removable Media](/techniques/T1458)
* [Screen Capture](/techniques/T1513)
* [Software Discovery](/techniques/T1418)
* [Stored Application Data](/techniques/T1409)
* [Supply Chain Compromise](/techniques/T1474)
* [System Information Discovery](/techniques/T1426)
* [System Network Configuration Discovery](/techniques/T1422)
* [System Network Connections Discovery](/techniques/T1421)
* [Video Capture](/techniques/T1512)
* [Web Service](/techniques/T1481)

#### Minor Technique changes

* No changes

#### Technique revocations

* Access Calendar Entries (revoked by Protected User Data: [Calendar Entries](/techniques/T1636/001))
* Access Call Log (revoked by Protected User Data: [Call Log](/techniques/T1636/002))
* Access Contact List (revoked by Protected User Data: [Contact List](/techniques/T1636/003))
* Broadcast Receivers (revoked by Event Triggered Execution : [Broadcast Receivers](/techniques/T1624/001))
* Capture SMS Messages (revoked by Protected User Data: [SMS Messages](/techniques/T1636/004))
* Carrier Billing Fraud (revoked by [Generate Traffic from Victim](/techniques/T1643))
* Clipboard Modification (revoked by Data Manipulation: [Transmitted Data Manipulation](/techniques/T1641/001))
* Code Injection (revoked by Process Injection: [Ptrace System Calls](/techniques/T1631/001))
* Command-Line Interface (revoked by Command and Scripting Interpreter: [Unix Shell](/techniques/T1623/001))
* Delete Device Data (revoked by Indicator Removal on Host: [File Deletion](/techniques/T1630/002))
* Device Administrator Permissions (revoked by Abuse Elevation Control Mechanism: [Device Administrator Permissions](/techniques/T1626/001))
* Device Lockout (revoked by Impair Defenses: [Device Lockout](/techniques/T1629/002))
* Disguise Root/Jailbreak Indicators (revoked by Indicator Removal on Host: [Disguise Root/Jailbreak Indicators](/techniques/T1630/003))
* Domain Generation Algorithms (revoked by Dynamic Resolution: [Domain Generation Algorithms](/techniques/T1637/001))
* Downgrade to Insecure Protocols (revoked by [Adversary-in-the-Middle](/techniques/T1638))
* Eavesdrop on Insecure Network Communication (revoked by [Adversary-in-the-Middle](/techniques/T1638))
* Evade Analysis Environment (revoked by Virtualization/Sandbox Evasion: [System Checks](/techniques/T1633/001))
* Exfiltration Over Other Network Medium (revoked by [Out of Band Data](/techniques/T1644))
* Exploit SS7 to Track Device Location (revoked by Location Tracking: [Impersonate SS7 Nodes](/techniques/T1430/002))
* Generate Fraudulent Advertising Revenue (revoked by [Generate Traffic from Victim](/techniques/T1643))
* Geofencing (revoked by Execution Guardrails: [Geofencing](/techniques/T1627/001))
* Input Prompt (revoked by Input Capture: [GUI Input Capture](/techniques/T1417/002))
* Install Insecure or Malicious Configuration (revoked by Subvert Trust Controls: [Code Signing Policy Modification](/techniques/T1632/001))
* Keychain (revoked by Credentials from Password Store: [Keychain](/techniques/T1634/001))
* Manipulate App Store Rankings or Ratings (revoked by [Generate Traffic from Victim](/techniques/T1643))
* Manipulate Device Communication (revoked by [Adversary-in-the-Middle](/techniques/T1638))
* Modify System Partition (revoked by Hijack Execution Flow: [System Runtime API Hijacking](/techniques/T1625/001))
* Network Information Discovery (revoked by [System Network Connections Discovery](/techniques/T1421))
* Network Traffic Capture or Redirection (revoked by [Adversary-in-the-Middle](/techniques/T1638))
* Remotely Track Device Without Authorization (revoked by Location Tracking: [Remote Device Management Services](/techniques/T1430/001))
* Rogue Cellular Base Station (revoked by [Adversary-in-the-Middle](/techniques/T1638))
* Rogue Wi-Fi Access Points (revoked by [Adversary-in-the-Middle](/techniques/T1638))
* Suppress Application Icon (revoked by Hide Artifacts: [Suppress Application Icon](/techniques/T1628/001))
* URI Hijacking (revoked by Steal Application Access Token: [URI Hijacking](/techniques/T1635/001))
* Uninstall Malicious Application (revoked by Indicator Removal on Host: [Uninstall Malicious Application](/techniques/T1630/001))
* User Evasion (revoked by Hide Artifacts: [User Evasion](/techniques/T1628/002))

#### Technique deprecations

* [Access Sensitive Data in Device Logs](/techniques/T1413)
* [Attack PC via USB Connection](/techniques/T1427)
* [Commonly Used Port](/techniques/T1436)
* [Deliver Malicious App via Authorized App Store](/techniques/T1475)
* [Deliver Malicious App via Other Means](/techniques/T1476)
* [Exploit SS7 to Redirect Phone Calls/SMS](/techniques/T1449)
* [Exploit TEE Vulnerability](/techniques/T1405)
* [Exploit via Radio Interfaces](/techniques/T1477)
* [Masquerade as Legitimate Application](/techniques/T1444)
* [Modify Cached Executable Code](/techniques/T1403)
* [Modify Trusted Execution Environment](/techniques/T1399)
* [Obtain Device Cloud Backups](/techniques/T1470)
* [Remotely Wipe Data Without Authorization](/techniques/T1469)
* [SIM Card Swap](/techniques/T1451)

## Software

### Enterprise

#### New Software

* [AADInternals](/software/S0677)
* [CaddyWiper](/software/S0693)
* [CharmPower](/software/S0674)
* [Chrommme](/software/S0667)
* [Clambling](/software/S0660)
* [Cyclops Blink](/software/S0687)
* [DRATzarus](/software/S0694)
* [DarkWatchman](/software/S0673)
* [Diavol](/software/S0659)
* [Donut](/software/S0695)
* [Ferocious](/software/S0679)
* [Flagpro](/software/S0696)
* [FoggyWeb](/software/S0661)
* [Gelsemium](/software/S0666)
* [Green Lambert](/software/S0690)
* [HermeticWiper](/software/S0697)
* [HermeticWizard](/software/S0698)
* [KOCTOPUS](/software/S0669)
* [LitePower](/software/S0680)
* [Lizar](/software/S0681)
* [Meteor](/software/S0688)
* [Mythic](/software/S0699)
* [Neoichor](/software/S0691)
* [Pandora](/software/S0664)
* [Peirates](/software/S0683)
* [PowerPunch](/software/S0685)
* [QuietSieve](/software/S0686)
* [RCSession](/software/S0662)
* [ROADTools](/software/S0684)
* [SILENTTRINITY](/software/S0692)
* [SysUpdate](/software/S0663)
* [ThreatNeedle](/software/S0665)
* [TinyTurla](/software/S0668)
* [Tomiris](/software/S0671)
* [Torisma](/software/S0678)
* [TrailBlazer](/software/S0682)
* [WarzoneRAT](/software/S0670)
* [WhisperGate](/software/S0689)
* [Zox](/software/S0672)

#### Software changes

* [AppleSeed](/software/S0622)
* [Arp](/software/S0099)
* [Backdoor.Oldrea](/software/S0093)
* [Bisonal](/software/S0268)
* [BloodHound](/software/S0521)
* [Brave Prince](/software/S0252)
* [CHOPSTICK](/software/S0023)
* [Cobalt Strike](/software/S0154)
* [Conti](/software/S0575)
* [Derusbi](/software/S0021)
* [EKANS](/software/S0605)
* [Empire](/software/S0363)
* [FinFisher](/software/S0182)
* [Gold Dragon](/software/S0249)
* [GoldMax](/software/S0588)
* [Hikit](/software/S0009)
* [Hydraq](/software/S0203)
* [HyperBro](/software/S0398)
* [InvisiMole](/software/S0260)
* [KONNI](/software/S0356)
* [KillDisk](/software/S0607)
* [Koadic](/software/S0250)
* [LockerGoga](/software/S0372)
* [Mimikatz](/software/S0002)
* [Ngrok](/software/S0508)
* [OSX_OCEANLOTUS.D](/software/S0352)
* [Orz](/software/S0229)
* [PLEAD](/software/S0435)
* [Ping](/software/S0097)
* [PlugX](/software/S0013)
* [PoetRAT](/software/S0428)
* [PoisonIvy](/software/S0012)
* [Prikormka](/software/S0113)
* [Pteranodon](/software/S0147)
* [QuasarRAT](/software/S0262)
* [REvil](/software/S0496)
* [ROKRAT](/software/S0240)
* [Remcos](/software/S0332)
* [Responder](/software/S0174)
* [Ryuk](/software/S0446)
* [SUNBURST](/software/S0559)
* [SombRAT](/software/S0615)
* [Stuxnet](/software/S0603)
* [ThiefQuest](/software/S0595)
* [Trojan.Karagany](/software/S0094)
* [USBStealer](/software/S0136)
* [Waterbear](/software/S0579)
* [Winnti for Windows](/software/S0141)
* [XCSSET](/software/S0658)
* [ZxShell](/software/S0412)
* [at](/software/S0110)
* [ftp](/software/S0095)
* [gh0st RAT](/software/S0032)
* [njRAT](/software/S0385)
* [route](/software/S0103)
* [schtasks](/software/S0111)

#### Minor Software changes

* [Anchor](/software/S0504)
* [BoomBox](/software/S0635)
* [Bundlore](/software/S0482)
* [China Chopper](/software/S0020)
* [EVILNUM](/software/S0568)
* [Industroyer](/software/S0604)
* [Maze](/software/S0449)
* [Mis-Type](/software/S0084)
* [Misdat](/software/S0083)
* [Nidiran](/software/S0118)
* [Octopus](/software/S0340)
* [S-Type](/software/S0085)
* [SYNful Knock](/software/S0519)
* [TSCookie](/software/S0436)
* [WindTail](/software/S0466)
* [ZLib](/software/S0086)

#### Software revocations

* No changes

#### Software deprecations

* No changes

### Mobile

#### New Software

* No changes

#### Software changes

* [FinFisher](/software/S0182)
* [XLoader for iOS](/software/S0490)

#### Minor Software changes

* [BrainTest](/software/S0293)

#### Software revocations

* No changes

#### Software deprecations

* No changes

## Groups

### Enterprise

#### New Groups

* [Aquatic Panda](/groups/G0143)
* [Confucius](/groups/G0142)
* [Gelsemium](/groups/G0141)
* [LazyScripter](/groups/G0140)

#### Group changes

* [APT28](/groups/G0007)
* [APT29](/groups/G0016)
* [Axiom](/groups/G0001)
* [BlackTech](/groups/G0098)
* [Dragonfly](/groups/G0035)
* [FIN7](/groups/G0046)
* [Gamaredon Group](/groups/G0047)
* [HAFNIUM](/groups/G0125)
* [Indrik Spider](/groups/G0119)
* [Ke3chang](/groups/G0004)
* [Kimsuky](/groups/G0094)
* [Lazarus Group](/groups/G0032)
* [Magic Hound](/groups/G0059)
* [Mustang Panda](/groups/G0129)
* [Sandworm Team](/groups/G0034)
* [TeamTNT](/groups/G0139)
* [Threat Group-3390](/groups/G0027)
* [Tonto Team](/groups/G0131)
* [Turla](/groups/G0010)
* [Volatile Cedar](/groups/G0123)
* [WIRTE](/groups/G0090)
* [Winnti Group](/groups/G0044)

#### Minor Group changes

* [APT38](/groups/G0082)
* [Ajax Security Team](/groups/G0130)
* [Chimera](/groups/G0114)
* [Dust Storm](/groups/G0031)
* [Leviathan](/groups/G0065)
* [OilRig](/groups/G0049)
* [Operation Wocao](/groups/G0116)
* [Suckfly](/groups/G0039)
* [TA505](/groups/G0092)

#### Group revocations

* Dragonfly 2.0 (revoked by [Dragonfly](/groups/G0035))

#### Group deprecations

* No changes

### Mobile

#### New Groups

* No changes

#### Group changes

* [APT28](/groups/G0007)
* [Sandworm Team](/groups/G0034)

#### Minor Group changes

* No changes

#### Group revocations

* No changes

#### Group deprecations

* No changes

## Mitigations

### Enterprise

#### New Mitigations

* No changes

#### Mitigation  changes

* [Execution Prevention](/mitigations/M1038)

#### Minor Mitigation changes

* No changes

#### Mitigation revocations

* No changes

#### Mitigation deprecations

* No changes

### Mobile

#### New Mitigations

* No changes

#### Mitigation changes

* No changes

#### Minor Mitigation changes

* No changes

#### Mitigation revocations

* No changes

#### Mitigation deprecations

* [Application Vetting](/mitigations/M1005)
* [Caution with Device Administrator Access](/mitigations/M1007)

## Data Sources and/or Components

### Enterprise

#### New Data Sources and/or Components

* No changes

Data Source and/or Component changes:

* No changes

#### Minor Data Source and/or Component changes

* [Active Directory](/datasources/DS0026)
* [Application Log](/datasources/DS0015)
* [Cloud Service](/datasources/DS0025)
* [Command](/datasources/DS0017)
* Domain Name: [Active DNS](/datasources/DS0038/#Active%20DNS)
* [Drive](/datasources/DS0016)
* [Driver](/datasources/DS0027)
* [File](/datasources/DS0022)
  * [File Deletion](/datasources/DS0022/#File%20Deletion)
* [Firewall](/datasources/DS0018)
* [Firmware](/datasources/DS0001)
* [Group](/datasources/DS0036)
* [Logon Session](/datasources/DS0028)
* Malware Repository: [Malware Content](/datasources/DS0004/#Malware%20Content)
* Malware Repository: [Malware Metadata](/datasources/DS0004/#Malware%20Metadata)
* [Module](/datasources/DS0011)
* [Named Pipe](/datasources/DS0023)
* [Network Share](/datasources/DS0033)
* [Network Traffic](/datasources/DS0029)
  * [Network Connection Creation](/datasources/DS0029/#Network%20Connection%20Creation)
* [Process](/datasources/DS0009)
  * [OS API Execution](/datasources/DS0009/#OS%20API%20Execution)
* [Scheduled Job](/datasources/DS0003)
* [Sensor Health](/datasources/DS0013)
  * [Host Status](/datasources/DS0013/#Host%20Status)
* [Service](/datasources/DS0019)
* [User Account](/datasources/DS0002)
* [Volume](/datasources/DS0034)
* [Web Credential](/datasources/DS0006)

#### Data Source and/or Component revocations

* No changes

#### Data Source and/or Component deprecations

* No changes

### Mobile

ATT&CK for Mobile does not support data sources

## Contributors to this release

* Abhijit Mohanta, @abhijit_mohanta, Uptycs
* Akshat Pradhan, Qualys
* Alex Hinchliffe, Palo Alto Networks
* Alex Parsons, Crowdstrike
* Alex Spivakovsky, Pentera
* Andrew Northern, @ex_raritas
* Antonio Piazza, @antman1p
* Austin Clark, @c2defense
* Bryan Campbell, @bry_campbell
* Chris Romano, Crowdstrike
* Clément Notin, Tenable
* Cody Thomas, SpecterOps
* Craig Smith, BT Security
* Csaba Fitzl @theevilbit of Offensive Security
* Daniel Acevedo, Blackbot
* Daniel Feichter, @VirtualAllocEx, Infosec Tirol
* Daniyal Naeem, BT Security
* Darin Smith, Cisco
* Dror Alon, Palo Alto Networks
* Edward Millington
* Elvis Veliz, Citi
* Emily Ratliff, IBM
* Eric Kaiser @ideologysec
* ESET
* Hannah Simes, BT Security
* Harshal Tupsamudre, Qualys
* Hiroki Nagahama, NEC Corporation
* Isif Ibrahima, Mandiant
* James_inthe_box, Me
* Jan Petrov, Citi
* Jannie Li, Microsoft Threat Intelligence Center (MSTIC)
* Jen Burns, HubSpot
* Jeremy Galloway
* Joas Antonio dos Santos, @C0d3Cr4zy, Inmetrics
* John Page (aka hyp3rlinx), ApparitionSec
* Jon Sternstein, Stern Security
* Kobi Haimovich, CardinalOps
* Krishnan Subramanian, @krish203
* Kyaw Pyiyt Htet, @KyawPyiytHtet
* Leo Zhang, Trend Micro
* Manikantan Srinivasan, NEC Corporation India
* Massimiliano Romano, BT Security
* Matthew Green
* Mayan Arora aka Mayan Mohan
* Mayuresh Dani, Qualys
* Michael Raggi @aRtAGGI
* Mohamed Kmal
* NEC
* NST Assure Research Team, NetSentries Technologies
* Oleg Kolesnikov, Securonix
* Or Kliger, Palo Alto Networks
* Pawel Partyka, Microsoft 365 Defender
* Phil Taylor, BT Security
* Pià Consigny, Tenable
* Pooja Natarajan, NEC Corporation India
* Praetorian
* Prasad Somasamudram, McAfee
* Ram Pliskin, Microsoft Azure Security Center
* Richard Julian, Citi
* Runa Sandvik
* Sekhar Sarukkai, McAfee 
* Selena Larson, @selenalarson
* Shilpesh Trivedi, Uptycs
* Sittikorn Sangrattanapitak
* Steven Du, Trend Micro
* Suzy Schapperle - Microsoft Azure Red Team
* Syed Ummar Farooqh, McAfee
* Taewoo Lee, KISA
* The Wover, @TheRealWover
* Tiago Faria, 3CORESec
* Tony Lee
* Travis Smith, Qualys
* TruKno
* Tsubasa Matsuda, NEC Corporation
* Vinay Pidathala
* Wes Hurd
* Wietze Beukema, @wietze
* Wojciech Lesicki
* Zachary Abzug, @ZackDoesML
* Zachary Stanford, @svch0st
