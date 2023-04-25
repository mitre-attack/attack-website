Title: Updates - October 2021
Date: October 2021
Category: Cyber Threat Intelligence
Authors: Adam Pennington
Template: resources/update-post
url: /resources/updates/updates-october-2021
save_as: resources/updates/updates-october-2021/index.html

| Version | Start Date | End Date | Data | Changelogs |
|:--------|:-----------|:---------|:-----|:-----------|
| [ATT&CK v10](/versions/v10) | October 21, 2021 | April 24, 2022 | [v10.0 on MITRE/CTI](https://github.com/mitre/cti/releases/tag/ATT%26CK-v10.0)<br />[v10.1 on MITRE/CTI](https://github.com/mitre/cti/releases/tag/ATT%26CK-v10.1) | v9.0 - v10.0 [Details](/docs/changelogs/v9.0-v10.0/changelog-detailed.html) ([JSON](/docs/changelogs/v9.0-v10.0/changelog.json))<br />v10.0 - v10.1 [Details](/docs/changelogs/v10.0-v10.1/changelog-detailed.html) ([JSON](/docs/changelogs/v10.0-v10.1/changelog.json)) |

The October 2021 (v10) ATT&CK release updates Techniques, Groups, and Software for Enterprise, Mobile, and ICS. The biggest change is the addition of a new set of [Data Source](/datasources/) and Data Component objects in Enterprise ATT&CK, complementing the ATT&CK Data Source name changes released in ATT&CK v9. An [accompanying blog post](https://medium.com/mitre-attack/introducing-attack-v10-7743870b37e3) describes these changes as well as improvements across ATT&CK's various domains and platforms.

In this release we have renamed [T1185](/techniques/T1185/) and [T1557](/techniques/T1557/) to be more inclusive, and deprecated [T1053.004](https://attack.mitre.org/versions/v9/techniques/T1053/004/) to better reflect adversary behavior.

This version of ATT&CK for Enterprise contains 14 Tactics, 188 Techniques, 379 Sub-techniques, 129 Groups, and 637 Pieces of Software.

### New Data Sources and/or Components in Enterprise ATT&CK:

* [Active Directory](/datasources/DS0026)
	* [Active Directory Credential Request](/datasources/DS0026/#Active%20Directory%20Credential%20Request)
	* [Active Directory Object Access](/datasources/DS0026/#Active%20Directory%20Object%20Access)
	* [Active Directory Object Creation](/datasources/DS0026/#Active%20Directory%20Object%20Creation)
	* [Active Directory Object Deletion](/datasources/DS0026/#Active%20Directory%20Object%20Deletion)
	* [Active Directory Object Modification](/datasources/DS0026/#Active%20Directory%20Object%20Modification)
* [Application Log](/datasources/DS0015)
	* [Application Log Content](/datasources/DS0015/#Application%20Log%20Content)
* [Certificate](/datasources/DS0037)
	* [Certificate Registration](/datasources/DS0037/#Certificate%20Registration)
* [Cloud Service](/datasources/DS0025)
	* [Cloud Service Disable](/datasources/DS0025/#Cloud%20Service%20Disable)
	* [Cloud Service Enumeration](/datasources/DS0025/#Cloud%20Service%20Enumeration)
	* [Cloud Service Metadata](/datasources/DS0025/#Cloud%20Service%20Metadata)
	* [Cloud Service Modification](/datasources/DS0025/#Cloud%20Service%20Modification)
* [Cloud Storage](/datasources/DS0010)
	* [Cloud Storage Access](/datasources/DS0010/#Cloud%20Storage%20Access)
	* [Cloud Storage Creation](/datasources/DS0010/#Cloud%20Storage%20Creation)
	* [Cloud Storage Deletion](/datasources/DS0010/#Cloud%20Storage%20Deletion)
	* [Cloud Storage Enumeration](/datasources/DS0010/#Cloud%20Storage%20Enumeration)
	* [Cloud Storage Metadata](/datasources/DS0010/#Cloud%20Storage%20Metadata)
	* [Cloud Storage Modification](/datasources/DS0010/#Cloud%20Storage%20Modification)
* [Cluster](/datasources/DS0031)
	* [Cluster Metadata](/datasources/DS0031/#Cluster%20Metadata)
* [Command](/datasources/DS0017)
	* [Command Execution](/datasources/DS0017/#Command%20Execution)
* [Container](/datasources/DS0032)
	* [Container Creation](/datasources/DS0032/#Container%20Creation)
	* [Container Enumeration](/datasources/DS0032/#Container%20Enumeration)
	* [Container Metadata](/datasources/DS0032/#Container%20Metadata)
	* [Container Start](/datasources/DS0032/#Container%20Start)
* [Domain Name](/datasources/DS0038)
	* [Active DNS](/datasources/DS0038/#Active%20DNS)
	* [Domain Registration](/datasources/DS0038/#Domain%20Registration)
	* [Passive DNS](/datasources/DS0038/#Passive%20DNS)
* [Drive](/datasources/DS0016)
	* [Drive Access](/datasources/DS0016/#Drive%20Access)
	* [Drive Creation](/datasources/DS0016/#Drive%20Creation)
	* [Drive Modification](/datasources/DS0016/#Drive%20Modification)
* [Driver](/datasources/DS0027)
	* [Driver Load](/datasources/DS0027/#Driver%20Load)
	* [Driver Metadata](/datasources/DS0027/#Driver%20Metadata)
* [File](/datasources/DS0022)
	* [File Access](/datasources/DS0022/#File%20Access)
	* [File Creation](/datasources/DS0022/#File%20Creation)
	* [File Deletion](/datasources/DS0022/#File%20Deletion)
	* [File Metadata](/datasources/DS0022/#File%20Metadata)
	* [File Modification](/datasources/DS0022/#File%20Modification)
* [Firewall](/datasources/DS0018)
	* [Firewall Disable](/datasources/DS0018/#Firewall%20Disable)
	* [Firewall Enumeration](/datasources/DS0018/#Firewall%20Enumeration)
	* [Firewall Metadata](/datasources/DS0018/#Firewall%20Metadata)
	* [Firewall Rule Modification](/datasources/DS0018/#Firewall%20Rule%20Modification)
* [Firmware](/datasources/DS0001)
	* [Firmware Modification](/datasources/DS0001/#Firmware%20Modification)
* [Group](/datasources/DS0036)
	* [Group Enumeration](/datasources/DS0036/#Group%20Enumeration)
	* [Group Metadata](/datasources/DS0036/#Group%20Metadata)
	* [Group Modification](/datasources/DS0036/#Group%20Modification)
* [Image](/datasources/DS0007)
	* [Image Creation](/datasources/DS0007/#Image%20Creation)
	* [Image Deletion](/datasources/DS0007/#Image%20Deletion)
	* [Image Metadata](/datasources/DS0007/#Image%20Metadata)
	* [Image Modification](/datasources/DS0007/#Image%20Modification)
* [Instance](/datasources/DS0030)
	* [Instance Creation](/datasources/DS0030/#Instance%20Creation)
	* [Instance Deletion](/datasources/DS0030/#Instance%20Deletion)
	* [Instance Enumeration](/datasources/DS0030/#Instance%20Enumeration)
	* [Instance Metadata](/datasources/DS0030/#Instance%20Metadata)
	* [Instance Modification](/datasources/DS0030/#Instance%20Modification)
	* [Instance Start](/datasources/DS0030/#Instance%20Start)
	* [Instance Stop](/datasources/DS0030/#Instance%20Stop)
* [Internet Scan](/datasources/DS0035)
	* [Response Content](/datasources/DS0035/#Response%20Content)
	* [Response Metadata](/datasources/DS0035/#Response%20Metadata)
* [Kernel](/datasources/DS0008)
	* [Kernel Module Load](/datasources/DS0008/#Kernel%20Module%20Load)
* [Logon Session](/datasources/DS0028)
	* [Logon Session Creation](/datasources/DS0028/#Logon%20Session%20Creation)
	* [Logon Session Metadata](/datasources/DS0028/#Logon%20Session%20Metadata)
* [Malware Repository](/datasources/DS0004)
	* [Malware Content](/datasources/DS0004/#Malware%20Content)
	* [Malware Metadata](/datasources/DS0004/#Malware%20Metadata)
* [Module](/datasources/DS0011)
	* [Module Load](/datasources/DS0011/#Module%20Load)
* [Named Pipe](/datasources/DS0023)
	* [Named Pipe Metadata](/datasources/DS0023/#Named%20Pipe%20Metadata)
* [Network Share](/datasources/DS0033)
	* [Network Share Access](/datasources/DS0033/#Network%20Share%20Access)
* [Network Traffic](/datasources/DS0029)
	* [Network Connection Creation](/datasources/DS0029/#Network%20Connection%20Creation)
	* [Network Traffic Content](/datasources/DS0029/#Network%20Traffic%20Content)
	* [Network Traffic Flow](/datasources/DS0029/#Network%20Traffic%20Flow)
* [Persona](/datasources/DS0021)
	* [Social Media](/datasources/DS0021/#Social%20Media)
* [Pod](/datasources/DS0014)
	* [Pod Creation](/datasources/DS0014/#Pod%20Creation)
	* [Pod Enumeration](/datasources/DS0014/#Pod%20Enumeration)
	* [Pod Metadata](/datasources/DS0014/#Pod%20Metadata)
	* [Pod Modification](/datasources/DS0014/#Pod%20Modification)
* [Process](/datasources/DS0009)
	* [OS API Execution](/datasources/DS0009/#OS%20API%20Execution)
	* [Process Access](/datasources/DS0009/#Process%20Access)
	* [Process Creation](/datasources/DS0009/#Process%20Creation)
	* [Process Metadata](/datasources/DS0009/#Process%20Metadata)
	* [Process Modification](/datasources/DS0009/#Process%20Modification)
	* [Process Termination](/datasources/DS0009/#Process%20Termination)
* [Scheduled Job](/datasources/DS0003)
	* [Scheduled Job Creation](/datasources/DS0003/#Scheduled%20Job%20Creation)
	* [Scheduled Job Metadata](/datasources/DS0003/#Scheduled%20Job%20Metadata)
	* [Scheduled Job Modification](/datasources/DS0003/#Scheduled%20Job%20Modification)
* [Script](/datasources/DS0012)
	* [Script Execution](/datasources/DS0012/#Script%20Execution)
* [Sensor Health](/datasources/DS0013)
	* [Host Status](/datasources/DS0013/#Host%20Status)
* [Service](/datasources/DS0019)
	* [Service Creation](/datasources/DS0019/#Service%20Creation)
	* [Service Metadata](/datasources/DS0019/#Service%20Metadata)
	* [Service Modification](/datasources/DS0019/#Service%20Modification)
* [Snapshot](/datasources/DS0020)
	* [Snapshot Creation](/datasources/DS0020/#Snapshot%20Creation)
	* [Snapshot Deletion](/datasources/DS0020/#Snapshot%20Deletion)
	* [Snapshot Enumeration](/datasources/DS0020/#Snapshot%20Enumeration)
	* [Snapshot Metadata](/datasources/DS0020/#Snapshot%20Metadata)
	* [Snapshot Modification](/datasources/DS0020/#Snapshot%20Modification)
* [User Account](/datasources/DS0002)
	* [User Account Authentication](/datasources/DS0002/#User%20Account%20Authentication)
	* [User Account Creation](/datasources/DS0002/#User%20Account%20Creation)
	* [User Account Deletion](/datasources/DS0002/#User%20Account%20Deletion)
	* [User Account Metadata](/datasources/DS0002/#User%20Account%20Metadata)
	* [User Account Modification](/datasources/DS0002/#User%20Account%20Modification)
* [Volume](/datasources/DS0034)
	* [Volume Creation](/datasources/DS0034/#Volume%20Creation)
	* [Volume Deletion](/datasources/DS0034/#Volume%20Deletion)
	* [Volume Enumeration](/datasources/DS0034/#Volume%20Enumeration)
	* [Volume Metadata](/datasources/DS0034/#Volume%20Metadata)
	* [Volume Modification](/datasources/DS0034/#Volume%20Modification)
* [WMI](/datasources/DS0005)
	* [WMI Creation](/datasources/DS0005/#WMI%20Creation)
* [Web Credential](/datasources/DS0006)
	* [Web Credential Creation](/datasources/DS0006/#Web%20Credential%20Creation)
	* [Web Credential Usage](/datasources/DS0006/#Web%20Credential%20Usage)
* [Windows Registry](/datasources/DS0024)
	* [Windows Registry Key Access](/datasources/DS0024/#Windows%20Registry%20Key%20Access)
	* [Windows Registry Key Creation](/datasources/DS0024/#Windows%20Registry%20Key%20Creation)
	* [Windows Registry Key Deletion](/datasources/DS0024/#Windows%20Registry%20Key%20Deletion)
	* [Windows Registry Key Modification](/datasources/DS0024/#Windows%20Registry%20Key%20Modification)

### Techniques

**Enterprise**

New Techniques:

* Boot or Logon Autostart Execution: [Login Items](/techniques/T1547/015)
* [Cloud Storage Object Discovery](/techniques/T1619)
* Data from Information Repositories: [Code Repositories](/techniques/T1213/003)
* [Group Policy Discovery](/techniques/T1615)
* Hide Artifacts: [Email Hiding Rules](/techniques/T1564/008)
* Hide Artifacts: [Resource Forking](/techniques/T1564/009)
* Impair Defenses: [Downgrade Attack](/techniques/T1562/010)
* Impair Defenses: [Safe Mode Boot](/techniques/T1562/009)
* Masquerading: [Double File Extension](/techniques/T1036/007)
* Obfuscated Files or Information: [HTML Smuggling](/techniques/T1027/006)
* [Reflective Code Loading](/techniques/T1620)
* Server Software Component: [IIS Components](/techniques/T1505/004)
* Signed Binary Proxy Execution: [MMC](/techniques/T1218/014)
* Signed Binary Proxy Execution: [Mavinject](/techniques/T1218/013)
* System Location Discovery: [System Language Discovery](/techniques/T1614/001)


Technique changes:

* Access Token Manipulation: [Create Process with Token](/techniques/T1134/002)
* Account Discovery: [Local Account](/techniques/T1087/001)
* Account Manipulation: [Exchange Email Delegate Permissions](/techniques/T1098/002)
* [Acquire Infrastructure](/techniques/T1583)
	* [Domains](/techniques/T1583/001)
	* [Server](/techniques/T1583/004)
	* [Virtual Private Server](/techniques/T1583/003)
	* [Web Services](/techniques/T1583/006)
* [Adversary-in-the-Middle](/techniques/T1557)
	* [ARP Cache Poisoning](/techniques/T1557/002)
	* [LLMNR/NBT-NS Poisoning and SMB Relay](/techniques/T1557/001)
* Automated Exfiltration: [Traffic Duplication](/techniques/T1020/001)
* Boot or Logon Autostart Execution: [Kernel Modules and Extensions](/techniques/T1547/006)
* Boot or Logon Autostart Execution: [Plist Modification](/techniques/T1547/011)
* [Browser Session Hijacking](/techniques/T1185)
* [Brute Force](/techniques/T1110)
* [Build Image on Host](/techniques/T1612)
* [Cloud Infrastructure Discovery](/techniques/T1580)
* [Command and Scripting Interpreter](/techniques/T1059)
	* [JavaScript](/techniques/T1059/007)
	* [Network Device CLI](/techniques/T1059/008)
	* [PowerShell](/techniques/T1059/001)
	* [Unix Shell](/techniques/T1059/004)
	* [Visual Basic](/techniques/T1059/005)
	* [Windows Command Shell](/techniques/T1059/003)
* [Compromise Accounts](/techniques/T1586)
	* [Social Media Accounts](/techniques/T1586/001)
* [Compromise Infrastructure](/techniques/T1584)
	* [DNS Server](/techniques/T1584/002)
	* [Domains](/techniques/T1584/001)
	* [Server](/techniques/T1584/004)
	* [Virtual Private Server](/techniques/T1584/003)
	* [Web Services](/techniques/T1584/006)
* Create Account: [Local Account](/techniques/T1136/001)
* Create or Modify System Process: [Launch Agent](/techniques/T1543/001)
* Create or Modify System Process: [Launch Daemon](/techniques/T1543/004)
* [Data Encrypted for Impact](/techniques/T1486)
* [Data from Information Repositories](/techniques/T1213)
* [Data from Local System](/techniques/T1005)
* [Data from Removable Media](/techniques/T1025)
* [Develop Capabilities](/techniques/T1587)
	* [Code Signing Certificates](/techniques/T1587/002)
	* [Digital Certificates](/techniques/T1587/003)
	* [Malware](/techniques/T1587/001)
* [Drive-by Compromise](/techniques/T1189)
* [Email Collection](/techniques/T1114)
	* [Email Forwarding Rule](/techniques/T1114/003)
* [Escape to Host](/techniques/T1611)
* [Establish Accounts](/techniques/T1585)
	* [Social Media Accounts](/techniques/T1585/001)
* Event Triggered Execution: [Unix Shell Configuration Modification](/techniques/T1546/004)
* Event Triggered Execution: [Windows Management Instrumentation Event Subscription](/techniques/T1546/003)
* [Exfiltration Over Alternative Protocol](/techniques/T1048)
	* [Exfiltration Over Asymmetric Encrypted Non-C2 Protocol](/techniques/T1048/002)
	* [Exfiltration Over Unencrypted/Obfuscated Non-C2 Protocol](/techniques/T1048/003)
* [Exfiltration Over C2 Channel](/techniques/T1041)
* [Exfiltration Over Physical Medium](/techniques/T1052)
	* [Exfiltration over USB](/techniques/T1052/001)
* [Exfiltration Over Web Service](/techniques/T1567)
* [Exploitation for Client Execution](/techniques/T1203)
* [External Remote Services](/techniques/T1133)
* File and Directory Permissions Modification: [Linux and Mac File and Directory Permissions Modification](/techniques/T1222/002)
* [Forge Web Credentials](/techniques/T1606)
	* [SAML Tokens](/techniques/T1606/002)
	* [Web Cookies](/techniques/T1606/001)
* [Gather Victim Host Information](/techniques/T1592)
	* [Client Configurations](/techniques/T1592/004)
	* [Hardware](/techniques/T1592/001)
	* [Software](/techniques/T1592/002)
* [Gather Victim Org Information](/techniques/T1591)
	* [Determine Physical Locations](/techniques/T1591/001)
* [Hardware Additions](/techniques/T1200)
* [Hide Artifacts](/techniques/T1564)
	* [Hidden Users](/techniques/T1564/002)
	* [Run Virtual Instance](/techniques/T1564/006)
	* [VBA Stomping](/techniques/T1564/007)
* Hijack Execution Flow: [Services Registry Permissions Weakness](/techniques/T1574/011)
* [Impair Defenses](/techniques/T1562)
	* [Disable Windows Event Logging](/techniques/T1562/002)
	* [Disable or Modify Tools](/techniques/T1562/001)
* Input Capture: [GUI Input Capture](/techniques/T1056/002)
* [Inter-Process Communication](/techniques/T1559)
	* [Component Object Model](/techniques/T1559/001)
	* [Dynamic Data Exchange](/techniques/T1559/002)
* [Lateral Tool Transfer](/techniques/T1570)
* Masquerading: [Masquerade Task or Service](/techniques/T1036/004)
* Masquerading: [Right-to-Left Override](/techniques/T1036/002)
* [Native API](/techniques/T1106)
* [Network Share Discovery](/techniques/T1135)
* [OS Credential Dumping](/techniques/T1003)
	* [LSASS Memory](/techniques/T1003/001)
* [Obfuscated Files or Information](/techniques/T1027)
	* [Binary Padding](/techniques/T1027/001)
	* [Software Packing](/techniques/T1027/002)
	* [Steganography](/techniques/T1027/003)
* [Obtain Capabilities](/techniques/T1588)
	* [Code Signing Certificates](/techniques/T1588/003)
	* [Digital Certificates](/techniques/T1588/004)
	* [Malware](/techniques/T1588/001)
	* [Tool](/techniques/T1588/002)
* [Office Application Startup](/techniques/T1137)
	* [Add-ins](/techniques/T1137/006)
	* [Office Template Macros](/techniques/T1137/001)
	* [Office Test](/techniques/T1137/002)
	* [Outlook Forms](/techniques/T1137/003)
	* [Outlook Home Page](/techniques/T1137/004)
	* [Outlook Rules](/techniques/T1137/005)
* [Password Policy Discovery](/techniques/T1201)
* [Permission Groups Discovery](/techniques/T1069)
	* [Cloud Groups](/techniques/T1069/003)
* [Phishing](/techniques/T1566)
	* [Spearphishing Attachment](/techniques/T1566/001)
* [Process Injection](/techniques/T1055)
	* [Asynchronous Procedure Call](/techniques/T1055/004)
	* [Dynamic-link Library Injection](/techniques/T1055/001)
	* [Portable Executable Injection](/techniques/T1055/002)
	* [Process Hollowing](/techniques/T1055/012)
	* [Ptrace System Calls](/techniques/T1055/008)
	* [Thread Execution Hijacking](/techniques/T1055/003)
	* [Thread Local Storage](/techniques/T1055/005)
* [Remote Services](/techniques/T1021)
	* [Distributed Component Object Model](/techniques/T1021/003)
	* [SSH](/techniques/T1021/004)
	* [VNC](/techniques/T1021/005)
	* [Windows Remote Management](/techniques/T1021/006)
* [Remote System Discovery](/techniques/T1018)
* [Replication Through Removable Media](/techniques/T1091)
* Scheduled Task/Job: [At (Linux)](/techniques/T1053/001)
* Scheduled Task/Job: [Container Orchestration Job](/techniques/T1053/007)
* Scheduled Task/Job: [Cron](/techniques/T1053/003)
* Scheduled Task/Job: [Systemd Timers](/techniques/T1053/006)
* [Server Software Component](/techniques/T1505)
	* [Web Shell](/techniques/T1505/003)
* [Shared Modules](/techniques/T1129)
* Signed Binary Proxy Execution: [Mshta](/techniques/T1218/005)
* Signed Binary Proxy Execution: [Rundll32](/techniques/T1218/011)
* Signed Script Proxy Execution: [PubPrn](/techniques/T1216/001)
* [Stage Capabilities](/techniques/T1608)
	* [Drive-by Target](/techniques/T1608/004)
	* [Install Digital Certificate](/techniques/T1608/003)
	* [Link Target](/techniques/T1608/005)
	* [Upload Malware](/techniques/T1608/001)
	* [Upload Tool](/techniques/T1608/002)
* [Steal Web Session Cookie](/techniques/T1539)
* [Steal or Forge Kerberos Tickets](/techniques/T1558)
* [Subvert Trust Controls](/techniques/T1553)
	* [Gatekeeper Bypass](/techniques/T1553/001)
	* [Install Root Certificate](/techniques/T1553/004)
* [System Information Discovery](/techniques/T1082)
* [System Network Configuration Discovery](/techniques/T1016)
* [System Owner/User Discovery](/techniques/T1033)
* [System Service Discovery](/techniques/T1007)
* [System Services](/techniques/T1569)
	* [Launchctl](/techniques/T1569/001)
	* [Service Execution](/techniques/T1569/002)
* [Taint Shared Content](/techniques/T1080)
* Trusted Developer Utilities Proxy Execution: [MSBuild](/techniques/T1127/001)
* [Use Alternate Authentication Material](/techniques/T1550)
	* [Web Session Cookie](/techniques/T1550/004)
* [User Execution](/techniques/T1204)
	* [Malicious File](/techniques/T1204/002)
	* [Malicious Image](/techniques/T1204/003)
* [Valid Accounts](/techniques/T1078)
	* [Cloud Accounts](/techniques/T1078/004)
	* [Domain Accounts](/techniques/T1078/002)
	* [Local Accounts](/techniques/T1078/003)
* [Virtualization/Sandbox Evasion](/techniques/T1497)
	* [System Checks](/techniques/T1497/001)
	* [Time Based Evasion](/techniques/T1497/003)
	* [User Activity Based Checks](/techniques/T1497/002)
* [Windows Management Instrumentation](/techniques/T1047)


Minor Technique changes:

* [Access Token Manipulation](/techniques/T1134)
* [Account Discovery](/techniques/T1087)
	* [Domain Account](/techniques/T1087/002)
* [Account Manipulation](/techniques/T1098)
* [Automated Exfiltration](/techniques/T1020)
* [Boot or Logon Autostart Execution](/techniques/T1547)
* Command and Scripting Interpreter: [Python](/techniques/T1059/006)
* [Compromise Client Software Binary](/techniques/T1554)
* [Create Account](/techniques/T1136)
* [Create or Modify System Process](/techniques/T1543)
* [Credentials from Password Stores](/techniques/T1555)
	* [Password Managers](/techniques/T1555/005)
* Data from Information Repositories: [Confluence](/techniques/T1213/001)
* Data from Information Repositories: [Sharepoint](/techniques/T1213/002)
* [Event Triggered Execution](/techniques/T1546)
* [Execution Guardrails](/techniques/T1480)
	* [Environmental Keying](/techniques/T1480/001)
* [Exploit Public-Facing Application](/techniques/T1190)
* [File and Directory Discovery](/techniques/T1083)
* [File and Directory Permissions Modification](/techniques/T1222)
* [Hijack Execution Flow](/techniques/T1574)
	* [COR_PROFILER](/techniques/T1574/012)
* [Indicator Removal on Host](/techniques/T1070)
* [Input Capture](/techniques/T1056)
* [Masquerading](/techniques/T1036)
* [Modify Authentication Process](/techniques/T1556)
	* [Pluggable Authentication Modules](/techniques/T1556/003)
* [Proxy](/techniques/T1090)
* [Scheduled Task/Job](/techniques/T1053)
* Server Software Component: [Transport Agent](/techniques/T1505/002)
* [Signed Binary Proxy Execution](/techniques/T1218)
	* [Msiexec](/techniques/T1218/007)
* [Signed Script Proxy Execution](/techniques/T1216)
* Steal or Forge Kerberos Tickets: [AS-REP Roasting](/techniques/T1558/004)
* [System Location Discovery](/techniques/T1614)
* [Trusted Developer Utilities Proxy Execution](/techniques/T1127)
* Use Alternate Authentication Material: [Application Access Token](/techniques/T1550/001)
* Use Alternate Authentication Material: [Pass the Hash](/techniques/T1550/002)
* Use Alternate Authentication Material: [Pass the Ticket](/techniques/T1550/003)


Technique revocations:
No changes

Technique deprecations:

* Scheduled Task/Job: [Launchd](/techniques/T1053/004)


**Mobile**

New Techniques:

* [Call Control](/techniques/T1616)
* [Hooking](/techniques/T1617)
* [User Evasion](/techniques/T1618)


Technique changes:

* [Exploit SS7 to Redirect Phone Calls/SMS](/techniques/T1449)
* [Manipulate Device Communication](/techniques/T1463)
* [SIM Card Swap](/techniques/T1451)


Minor Technique changes:
No changes

Technique revocations:
No changes

Technique deprecations:
No changes

### Software

**Enterprise**

New Software:

* [AppleSeed](/software/S0622)
* [Avaddon](/software/S0640)
* [BADFLICK](/software/S0642)
* [BLUELIGHT](/software/S0657)
* [Babuk](/software/S0638)
* [Bad Rabbit](/software/S0606)
* [BoomBox](/software/S0635)
* [BoxCaon](/software/S0651)
* [Chaes](/software/S0631)
* [Clop](/software/S0611)
* [Conficker](/software/S0608)
* [CostaBricks](/software/S0614)
* [Cuba](/software/S0625)
* [DEATHRANSOM](/software/S0616)
* [EKANS](/software/S0605)
* [Ecipekac](/software/S0624)
* [EnvyScout](/software/S0634)
* [FIVEHANDS](/software/S0618)
* [FYAnti](/software/S0628)
* [GrimAgent](/software/S0632)
* [HELLOKITTY](/software/S0617)
* [Industroyer](/software/S0604)
* [JSS Loader](/software/S0648)
* [KillDisk](/software/S0607)
* [Kobalos](/software/S0641)
* [LiteDuke](/software/S0513)
* [MarkiRAT](/software/S0652)
* [NativeZone](/software/S0637)
* [Nebulae](/software/S0630)
* [ObliqueRAT](/software/S0644)
* [P8RAT](/software/S0626)
* [PS1](/software/S0613)
* [Peppy](/software/S0643)
* [ProLock](/software/S0654)
* [QakBot](/software/S0650)
* [RainyDay](/software/S0629)
* [SMOKEDHAM](/software/S0649)
* [Seth-Locker](/software/S0639)
* [SideTwist](/software/S0610)
* [Siloscape](/software/S0623)
* [Sliver](/software/S0633)
* [SodaMaster](/software/S0627)
* [SombRAT](/software/S0615)
* [SpicyOmelette](/software/S0646)
* [Stuxnet](/software/S0603)
* [Turian](/software/S0647)
* [VaporRage](/software/S0636)
* [WastedLocker](/software/S0612)
* [Wevtutil](/software/S0645)
* [XCSSET](/software/S0658)
* [xCaon](/software/S0653)


Software changes:

* [Aria-body](/software/S0456)
* [Bandook](/software/S0234)
* [Bazar](/software/S0534)
* [Bisonal](/software/S0268)
* [BloodHound](/software/S0521)
* [Bundlore](/software/S0482)
* [Carberp](/software/S0484)
* [China Chopper](/software/S0020)
* [Cobalt Strike](/software/S0154)
* [Conti](/software/S0575)
* [Crimson](/software/S0115)
* [Dok](/software/S0281)
* [Dridex](/software/S0384)
* [DropBook](/software/S0547)
* [Emissary](/software/S0082)
* [Empire](/software/S0363)
* [FatDuke](/software/S0512)
* [GuLoader](/software/S0561)
* [Hildegard](/software/S0601)
* [Impacket](/software/S0357)
* [Kerrdown](/software/S0585)
* [Keydnap](/software/S0276)
* [Kinsing](/software/S0599)
* [LaZagne](/software/S0349)
* [Lokibot](/software/S0447)
* [LoudMiner](/software/S0451)
* [Lucifer](/software/S0532)
* [Maze](/software/S0449)
* [Metamorfo](/software/S0455)
* [MimiPenguin](/software/S0179)
* [Mimikatz](/software/S0002)
* [MiniDuke](/software/S0051)
* [NETWIRE](/software/S0198)
* [Net](/software/S0039)
* [Nltest](/software/S0359)
* [OSX/Shlayer](/software/S0402)
* [OSX_OCEANLOTUS.D](/software/S0352)
* [Octopus](/software/S0340)
* [OwaAuth](/software/S0072)
* [PoisonIvy](/software/S0012)
* [PowerSploit](/software/S0194)
* [PsExec](/software/S0029)
* [QuasarRAT](/software/S0262)
* [REvil](/software/S0496)
* [RGDoor](/software/S0258)
* [Ryuk](/software/S0446)
* [SUNBURST](/software/S0559)
* [SharpStage](/software/S0546)
* [Spark](/software/S0543)
* [SynAck](/software/S0242)
* [Taidoor](/software/S0011)
* [ThiefQuest](/software/S0595)
* [TrickBot](/software/S0266)
* [Zeus Panda](/software/S0330)
* [certutil](/software/S0160)
* [esentutl](/software/S0404)


Minor Software changes:

* [BADNEWS](/software/S0128)
* [BOOTRASH](/software/S0114)
* [ECCENTRICBANDWAGON](/software/S0593)
* [Egregor](/software/S0554)
* [Hikit](/software/S0009)
* [HyperBro](/software/S0398)
* [Reg](/software/S0075)
* [WindTail](/software/S0466)
* [zwShell](/software/S0350)


Software revocations:
No changes

Software deprecations:
No changes

**Mobile**

New Software:

* [BusyGasper](/software/S0655)


Software changes:

* [Anubis](/software/S0422)
* [CarbonSteal](/software/S0529)
* [Monokle](/software/S0407)


Minor Software changes:
No changes

Software revocations:
No changes

Software deprecations:
No changes

### Groups

**Enterprise**

New Groups:

* [Andariel](/groups/G0138)
* [BackdoorDiplomacy](/groups/G0135)
* [CostaRicto](/groups/G0132)
* [Ferocious Kitten](/groups/G0137)
* [IndigoZebra](/groups/G0136)
* [Nomadic Octopus](/groups/G0133)
* [TeamTNT](/groups/G0139)
* [Tonto Team](/groups/G0131)
* [Transparent Tribe](/groups/G0134)


Group changes:

* [APT-C-36](/groups/G0099)
* [APT1](/groups/G0006)
* [APT19](/groups/G0073)
* [APT28](/groups/G0007)
* [APT29](/groups/G0016)
* [APT3](/groups/G0022)
* [APT32](/groups/G0050)
* [APT33](/groups/G0064)
* [APT37](/groups/G0067)
* [APT38](/groups/G0082)
* [APT39](/groups/G0087)
* [APT41](/groups/G0096)
* [BRONZE BUTLER](/groups/G0060)
* [Blue Mockingbird](/groups/G0108)
* [Carbanak](/groups/G0008)
* [Chimera](/groups/G0114)
* [Cleaver](/groups/G0003)
* [Cobalt Group](/groups/G0080)
* [CopyKittens](/groups/G0052)
* [Dark Caracal](/groups/G0070)
* [DarkHydrus](/groups/G0079)
* [DarkVishnya](/groups/G0105)
* [Dragonfly](/groups/G0035)
* [Dragonfly 2.0](/groups/G0074)
* [FIN10](/groups/G0051)
* [FIN4](/groups/G0085)
* [FIN5](/groups/G0053)
* [FIN6](/groups/G0037)
* [FIN7](/groups/G0046)
* [FIN8](/groups/G0061)
* [Frankenstein](/groups/G0101)
* [Gorgon Group](/groups/G0078)
* [Inception](/groups/G0100)
* [Indrik Spider](/groups/G0119)
* [Ke3chang](/groups/G0004)
* [Kimsuky](/groups/G0094)
* [Lazarus Group](/groups/G0032)
* [Leafminer](/groups/G0077)
* [Leviathan](/groups/G0065)
* [Magic Hound](/groups/G0059)
* [Mustang Panda](/groups/G0129)
* [Naikon](/groups/G0019)
* [Night Dragon](/groups/G0014)
* [OilRig](/groups/G0049)
* [Patchwork](/groups/G0040)
* [PittyTiger](/groups/G0011)
* [Sandworm Team](/groups/G0034)
* [Silence](/groups/G0091)
* [TA505](/groups/G0092)
* [TA551](/groups/G0127)
* [TEMP.Veles](/groups/G0088)
* [Threat Group-3390](/groups/G0027)
* [Thrip](/groups/G0076)
* [Turla](/groups/G0010)
* [WIRTE](/groups/G0090)
* [Whitefly](/groups/G0107)
* [Wizard Spider](/groups/G0102)
* [menuPass](/groups/G0045)


Minor Group changes:

* [Machete](/groups/G0095)


Group revocations:

* Stolen Pencil (revoked by [Kimsuky](/groups/G0094))


Group deprecations:

* [Taidoor](/groups/G0015)


**Mobile**

New Groups:
No changes

Group changes:

* [APT28](/groups/G0007)
* [Dark Caracal](/groups/G0070)
* [Sandworm Team](/groups/G0034)


Minor Group changes:
No changes

Group revocations:
No changes

Group deprecations:
No changes

### Mitigations

**Enterprise**

New Mitigations:

* [Data Loss Prevention](/mitigations/M1057)


Mitigation changes:
No changes

Minor Mitigation changes:
No changes

Mitigation revocations:
No changes

Mitigation deprecations:
No changes

**Mobile**

New Mitigations:
No changes

Mitigation changes:
No changes

Minor Mitigation changes:
No changes

Mitigation revocations:
No changes

Mitigation deprecations:
No changes

### Contributors to this release

* @ionstorm
* Achute Sharma, Keysight
* Arnim Rupp, Deutsche Lufthansa AG
* Atul Nair, Qualys
* Austin Clark
* Ayan Saha, Keysight
* Center for Threat-Informed Defense (CTID)
* Christoffer Strömblad
* Christopher Glyer, Mandiant, @cglyer
* Cody Thomas, SpecterOps
* Dan Borges, @1njection
* Daniel Prizmant, Palo Alto Networks
* Daniyal Naeem, BT Security
* Dor Edry, Microsoft
* Edward Millington
* Eli Salem, @elisalem9
* ExtraHop
* Gaetan van Diemen, ThreatFabric
* Gareth Phillips, Seek Ltd.
* Gordon Long, Box, Inc., @ethicalhax
* Harshal Tupsamudre, Qualys
* Hiroki Nagahama, NEC Corporation
* Isif Ibrahima
* Itamar Mizrahi, Cymptom
* Ivan Sinyakov
* Janantha Marasinghe
* Jaron Bradley @jbradley89
* Jeff Felling, Red Canary
* Jen Burns, HubSpot
* Joas Antonio dos Santos, @C0d3Cr4zy
* Johann Rehberger
* Jon Sheedy
* Jon Sternstein, Stern Security
* Jonathan Boucher, @crash_wave, Bank of Canada
* Jonhnathan Ribeiro, 3CORESec, @_w0rk3r
* Jorell Magtibay, National Australia Bank Limited
* Jorge Orchilles, SCYTHE
* Jose Luis Sánchez Martinez
* Josh Liburdi, @jshlbrd
* João Paulo de A. Filho, @Hug1nN__
* Jörg Abraham, EclecticIQ
* Karim Hasanen, @_karimhasanen
* Kiyohito Yamamoto, RedLark, NTT Communications
* Kyaw Pyiyt Htet, @KyawPyiytHtet
* Kyoung-ju Kwak (S2W)
* Lior Ribak, SentinelOne
* Manikantan Srinivasan, NEC Corporation India
* Maril Vernon, @shewhohacks
* Matt Brenton, Zurich Global Information Security
* Microsoft Detection and Response Team (DART)
* Microsoft Security
* Mike Burns, Mandiant
* Mnemonic AS
* Nagahama Hiroki, NEC Corporation
* Naveen Vijayaraghavan, Nilesh Dherange (Gurucul)
* Nick Carr, Mandiant
* Omkar Gudhate
* Patrick Sungbahadoor
* Pooja Natarajan, NEC Corporation India
* Prasanth Sadanala, Cigna Information Protection (CIP) - Threat Response Engineering Team
* Regina Elwell
* Rex Guo, @Xiaofei_REX, Confluera
* Rick Cole, Mandiant
* Ruben Dodge, @shotgunner101
* Shlomi Salem, SentinelOne
* SOCCRATES
* Stan Hegt, Outflank
* Ted Samuels, Rapid7
* Tim (Wadhwa-)Brown
* Toby Kohlenberg
* Vadim Khrykov
* Viren Chaudhari, Qualys
* Wes Hurd
* Will Thomas, Cyjax
* William Cain
* Yoshihiro Kori, NEC Corporation
* Yossi Nisani, Cymptom
* Yusuke Kubo, RedLark, NTT Communications
* Yuval Avrahami, Palo Alto Networks
* Zaw Min Htun, @Z3TAE
* Ziv Kaspersky, Cymptom
