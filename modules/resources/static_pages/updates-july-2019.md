Title: Updates - July 2019
Date: July 2019
Category: Cyber Threat Intelligence
Authors: Blake Strom
Template: resources/update-post
url: /resources/updates/updates-july-2019
save_as: resources/updates/updates-july-2019/index.html

| Version | Start Date | End Date | Data |
|:--------|:-----------|:---------|:-----|
| [ATT&CK v5](/versions/v5) | July 31, 2019 | October 23, 2019 |  [v5.2 on MITRE/CTI](https://github.com/mitre/cti/releases/tag/ATT%26CK-v5.2) |

The July 2019 release focuses on changes to how Mitigations in ATT&CK for Enterprise are represented and updates the Groups and Software entries. It does not contain updates to techniques- a larger technique update is planned for later this year. We're happy to check off another box on our [planned changes this year](https://medium.com/mitre-attack/attacking-2019-c05bccefed2d), which was to modify how we represent mitigations in Enterprise so that the information is organized similar to how mitigations are handled in ATT&CK for Mobile.
 
Mitigations in Enterprise are now treated like categories and are represented by objects similar to Groups and Software- one example being "[Multi-factor Authentication](/mitigations/M1032/)". In the previous free-text mitigation fields, several techniques may reference multi-factor authentication as a potential way to mitigate a technique, but it was difficult to see which techniques a particular mitigation applies to without scouring the text fields across the techniques. Now each technique that a mitigation applies to will be associated to that mitigation category and the details of how each mitigation applies to a technique will appear in a table under the mitigations section. Each mitigation category has a page that lists all the techniques associated with it to give an at-a-glance view of coverage. In all, [40 new mitigation categories](/mitigations/enterprise/) were created based on a text analysis of each technique where we pulled apart the definitions and binned them into like categories to consolidate the mitigation information in Enterprise.
 
During the process of applying the new mitigation categories, we also did a bit of house cleaning on what mitigations are appropriate for certain techniques. We generally took the stance that if a mitigation does not directly apply to that specific behavior, then we removed it. For example, there were quite a few techniques that we removed application whitelisting (Execution Prevention) from because it was previously treated as a mitigation of last resort.
 
Mitigations are represented as courses of action in STIX and will have the same ID numbering as Mobile mitigations (M####). The old mitigation text for techniques were placed into temporary mitigations objects with the full text field and will be included as deprecated mitigation objects. They are listed in STIX objects for historical purposes, but will not be present in the website. Those mitigation objects are labeled with the same technique ID (T####) as the technique they were associated to.
 
The Effects tactic in ATT&CK for Mobile was renamed to Impact for consistency with the Enterprise Impact tactic.
 
We've also updated the [Enterprise tactic descriptions](/tactics/enterprise/) based on a contribution from Elly Searle at CrowdStrike to make them more straightforward, uniform, and easier to understand.

### Techniques

**Enterprise**

New Techniques:
No changes

Technique changes:
No changes

Technique revocations:
No changes

Technique deprecations:
No changes

Minor Technique changes:
No changes

**PRE-ATT&CK**

New Techniques:
No changes

Technique changes:
No changes

Technique revocations:
No changes

Technique deprecations:
No changes

Minor Technique changes:
No changes

**Mobile**

New Techniques:
No changes

Technique changes:
No changes

Technique revocations:
No changes

Technique deprecations:
No changes

Minor Technique changes:
No changes

### Software

**Enterprise**

New Software:

* [Dridex](/software/S0384)
* [EvilBunny](/software/S0396)
* [FlawedAmmyy](/software/S0381)
* [FlawedGrace](/software/S0383)
* [HAWKBALL](/software/S0391)
* [HiddenWasp](/software/S0394)
* [HyperBro ](/software/S0398)
* [JCry](/software/S0389)
* [KeyBoy](/software/S0387)
* [LightNeuron](/software/S0395)
* [LoJax](/software/S0397)
* [PowerStallion](/software/S0393)
* [Revenge RAT](/software/S0379)
* [SQLRat](/software/S0390)
* [ServHelper](/software/S0382)
* [StoneDrill](/software/S0380)
* [Ursnif ](/software/S0386)
* [Yahoyah](/software/S0388)
* [njRAT](/software/S0385)

Software changes:

* [Azorult](/software/S0344)
* [Cobalt Strike](/software/S0154)
* [Emotet](/software/S0367)
* [Epic](/software/S0091)
* [FinFisher](/software/S0182)
* [Ixeshe](/software/S0015)
* [KONNI](/software/S0356)
* [Linux Rabbit](/software/S0362)
* [LockerGoga ](/software/S0372)
* [PUNCHBUGGY](/software/S0196)
* [Prikormka](/software/S0113)
* [ROKRAT](/software/S0240)
* [SynAck](/software/S0242)
* [XAgentOSX](/software/S0161)
* [Xbash](/software/S0341)
* [Zebrocy](/software/S0251)

Software revocations:
No changes

Software deprecations:
No changes

Minor Software changes:

* [BlackEnergy](/software/S0089)
* [CHOPSTICK](/software/S0023)
* [Cardinal RAT](/software/S0348)
* [Chaos](/software/S0220)
* [DarkComet](/software/S0334)
* [Empire](/software/S0363)
* [Flame](/software/S0143)
* [HOMEFRY](/software/S0232)
* [LaZagne](/software/S0349)
* [Olympic Destroyer](/software/S0365)
* [Proton](/software/S0279)
* [QuasarRAT](/software/S0262)
* [Smoke Loader](/software/S0226)
* [TURNEDUP](/software/S0199)
* [TrickBot](/software/S0266)
* [jRAT](/software/S0283)

**PRE-ATT&CK**

New Software:
No changes

Software changes:
No changes

Software revocations:
No changes

Software deprecations:
No changes

Minor Software changes:
No changes

**Mobile**

New Software:

* [FinFisher](/software/S0182)
* [Pallas](/software/S0399)

Software changes:
No changes

Software revocations:
No changes

Software deprecations:
No changes

Minor Software changes:
No changes

### Groups

**Enterprise**

New Groups:

* [Silence](/groups/G0091)
* [Soft Cell](/groups/G0093)
* [TA505](/groups/G0092)
* [The White Company](/groups/G0089)
* [WIRTE](/groups/G0090)

Group changes:

* [APT12](/groups/G0005)
* [APT28](/groups/G0007)
* [APT29](/groups/G0016)
* [APT33](/groups/G0064)
* [APT37](/groups/G0067)
* [Dark Caracal](/groups/G0070)
* [FIN7](/groups/G0046)
* [Gorgon Group](/groups/G0078)
* [Group5](/groups/G0043)
* [MuddyWater](/groups/G0069)
* [Patchwork](/groups/G0040)
* [Threat Group-3390](/groups/G0027)
* [Tropic Trooper](/groups/G0081)
* [Turla](/groups/G0010)
* [menuPass](/groups/G0045)

Group revocations:
No changes

Group deprecations:
No changes

Minor Group changes:

* [APT18](/groups/G0026)
* [APT32](/groups/G0050)
* [Cobalt Group](/groups/G0080)
* [FIN6](/groups/G0037)
* [OilRig](/groups/G0049)
* [PLATINUM](/groups/G0068)
* [Stolen Pencil](/groups/G0086)

**PRE-ATT&CK**

New Groups:
No changes

Group changes:

* [APT28](/groups/G0007)

Group revocations:
No changes

Group deprecations:
No changes

Minor Group changes:
No changes

**Mobile**

New Groups:

* [Dark Caracal](/groups/G0070)

Group changes:

* [APT28](/groups/G0007)

Group revocations:
No changes

Group deprecations:
No changes

Minor Group changes:
No changes

### Mitigations

**Enterprise**

New Mitigations:

* [Account Use Policies](/mitigations/M1036)
* [Active Directory Configuration](/mitigations/M1015)
* [Antivirus/Antimalware](/mitigations/M1049)
* [Application Isolation and Sandboxing](/mitigations/M1048)
* [Audit](/mitigations/M1047)
* [Behavior Prevention on Endpoint](/mitigations/M1040)
* [Boot Integrity](/mitigations/M1046)
* [Code Signing](/mitigations/M1045)
* [Credential Access Protection](/mitigations/M1043)
* [Data Backup](/mitigations/M1053)
* [Disable or Remove Feature or Program](/mitigations/M1042)
* [Do Not Mitigate](/mitigations/M1055)
* [Encrypt Sensitive Information](/mitigations/M1041)
* [Environment Variable Permissions](/mitigations/M1039)
* [Execution Prevention](/mitigations/M1038)
* [Exploit Protection](/mitigations/M1050)
* [Filter Network Traffic](/mitigations/M1037)
* [Limit Access to Resource Over Network](/mitigations/M1035)
* [Limit Hardware Installation](/mitigations/M1034)
* [Limit Software Installation](/mitigations/M1033)
* [Multi-factor Authentication](/mitigations/M1032)
* [Network Intrusion Prevention](/mitigations/M1031)
* [Network Segmentation](/mitigations/M1030)
* [Operating System Configuration](/mitigations/M1028)
* [Password Policies](/mitigations/M1027)
* [Privileged Account Management](/mitigations/M1026)
* [Privileged Process Integrity](/mitigations/M1025)
* [Remote Data Storage](/mitigations/M1029)
* [Restrict File and Directory Permissions](/mitigations/M1022)
* [Restrict Library Loading](/mitigations/M1044)
* [Restrict Registry Permissions](/mitigations/M1024)
* [Restrict Web-Based Content](/mitigations/M1021)
* [SSL/TLS Inspection](/mitigations/M1020)
* [Software Configuration](/mitigations/M1054)
* [Threat Intelligence Program](/mitigations/M1019)
* [Update Software](/mitigations/M1051)
* [User Account Control](/mitigations/M1052)
* [User Account Management](/mitigations/M1018)
* [User Training](/mitigations/M1017)
* [Vulnerability Scanning](/mitigations/M1016)

Mitigation changes:
No changes

Mitigation revocations:
No changes

Mitigation deprecations:

* .bash_profile and .bashrc Mitigation
* Access Token Manipulation Mitigation
* Accessibility Features Mitigation
* Account Discovery Mitigation
* Account Manipulation Mitigation
* AppCert DLLs Mitigation
* AppInit DLLs Mitigation
* AppleScript Mitigation
* Application Deployment Software Mitigation
* Application Shimming Mitigation
* Application Window Discovery Mitigation
* Audio Capture Mitigation
* Authentication Package Mitigation
* Automated Collection Mitigation
* Automated Exfiltration Mitigation
* BITS Jobs Mitigation
* Bash History Mitigation
* Binary Padding Mitigation
* Bootkit Mitigation
* Browser Bookmark Discovery Mitigation
* Browser Extensions Mitigation
* Brute Force Mitigation
* Bypass User Account Control Mitigation
* CMSTP Mitigation
* Change Default File Association Mitigation
* Clear Command History Mitigation
* Clipboard Data Mitigation
* Code Signing Mitigation
* Command-Line Interface Mitigation
* Commonly Used Port Mitigation
* Communication Through Removable Media Mitigation
* Compile After Delivery Mitigation
* Compiled HTML File Mitigation
* Component Firmware Mitigation
* Component Object Model Hijacking Mitigation
* Connection Proxy Mitigation
* Control Panel Items Mitigation
* Create Account Mitigation
* Credential Dumping Mitigation
* Credentials in Files Mitigation
* Credentials in Registry Mitigation
* Custom Command and Control Protocol Mitigation
* Custom Cryptographic Protocol Mitigation
* DCShadow Mitigation
* DLL Search Order Hijacking Mitigation
* DLL Side-Loading Mitigation
* Data Compressed Mitigation
* Data Destruction Mitigation
* Data Encoding Mitigation
* Data Encrypted Mitigation
* Data Encrypted for Impact Mitigation
* Data Obfuscation Mitigation
* Data Staged Mitigation
* Data Transfer Size Limits Mitigation
* Data from Information Repositories Mitigation
* Data from Local System Mitigation
* Data from Network Shared Drive Mitigation
* Data from Removable Media Mitigation
* Defacement Mitigation 
* Deobfuscate/Decode Files or Information Mitigation
* Disabling Security Tools Mitigation
* Distributed Component Object Model Mitigation
* Domain Fronting Mitigation
* Domain Generation Algorithms Mitigation
* Domain Trust Discovery Mitigation
* Drive-by Compromise Mitigation
* Dylib Hijacking Mitigation
* Dynamic Data Exchange Mitigation
* Email Collection Mitigation
* Endpoint Denial of Service Mitigation
* Environmental Keying Mitigation
* Execution through API Mitigation
* Execution through Module Load Mitigation
* Exfiltration Over Alternative Protocol Mitigation
* Exfiltration Over Command and Control Channel Mitigation
* Exfiltration Over Other Network Medium Mitigation
* Exfiltration Over Physical Medium Mitigation
* Exploit Public-Facing Application Mitigation
* Exploitation for Client Execution Mitigation
* Exploitation for Credential Access Mitigation
* Exploitation for Defense Evasion Mitigation
* Exploitation for Privilege Escalation Mitigation
* Exploitation of Remote Services Mitigation
* External Remote Services Mitigation
* Extra Window Memory Injection Mitigation
* Fallback Channels Mitigation
* File Deletion Mitigation
* File Permissions Modification Mitigation
* File System Logical Offsets Mitigation
* File System Permissions Weakness Mitigation
* File and Directory Discovery Mitigation
* Firmware Corruption Mitigation
* Forced Authentication Mitigation
* Gatekeeper Bypass Mitigation
* Graphical User Interface Mitigation
* Group Policy Modification Mitigation
* HISTCONTROL Mitigation
* Hardware Additions Mitigation
* Hidden Files and Directories Mitigation
* Hidden Users Mitigation
* Hidden Window Mitigation
* Hooking Mitigation
* Hypervisor Mitigation
* Image File Execution Options Injection Mitigation
* Indicator Blocking Mitigation
* Indicator Removal from Tools Mitigation
* Indicator Removal on Host Mitigation
* Indirect Command Execution Mitigation
* Inhibit System Recovery Mitigation
* Input Capture Mitigation
* Input Prompt Mitigation
* Install Root Certificate Mitigation
* InstallUtil Mitigation
* Kerberoasting Mitigation
* Kernel Modules and Extensions Mitigation
* Keychain Mitigation
* LC_LOAD_DYLIB Addition Mitigation
* LC_MAIN Hijacking Mitigation
* LLMNR/NBT-NS Poisoning Mitigation
* LSASS Driver Mitigation
* Launch Agent Mitigation
* Launch Daemon Mitigation
* Launchctl Mitigation
* Login Item Mitigation
* Logon Scripts Mitigation
* Man in the Browser Mitigation
* Masquerading Mitigation
* Modify Existing Service Mitigation
* Modify Registry Mitigation
* Mshta Mitigation
* Multi-Stage Channels Mitigation
* Multi-hop Proxy Mitigation
* Multiband Communication Mitigation
* Multilayer Encryption Mitigation
* NTFS File Attributes Mitigation
* Netsh Helper DLL Mitigation
* Network Denial of Service Mitigation
* Network Service Scanning Mitigation
* Network Share Connection Removal Mitigation
* Network Share Discovery Mitigation
* Network Sniffing Mitigation
* New Service Mitigation
* Obfuscated Files or Information Mitigation
* Office Application Startup Mitigation
* Pass the Hash Mitigation
* Pass the Ticket Mitigation
* Password Filter DLL Mitigation
* Password Policy Discovery Mitigation
* Path Interception Mitigation
* Peripheral Device Discovery Mitigation
* Permission Groups Discovery Mitigation
* Plist Modification Mitigation
* Port Knocking Mitigation
* Port Monitors Mitigation
* PowerShell Mitigation
* Private Keys Mitigation
* Process Discovery Mitigation
* Process Doppelgänging Mitigation
* Process Hollowing Mitigation
* Process Injection Mitigation
* Query Registry Mitigation
* Rc.common Mitigation
* Re-opened Applications Mitigation
* Redundant Access Mitigation
* Registry Run Keys / Startup Folder Mitigation
* Regsvcs/Regasm Mitigation
* Regsvr32 Mitigation
* Remote Access Tools Mitigation
* Remote Desktop Protocol Mitigation
* Remote File Copy Mitigation
* Remote Services Mitigation
* Remote System Discovery Mitigation
* Replication Through Removable Media Mitigation
* Resource Hijacking Mitigation
* Rootkit Mitigation
* Rundll32 Mitigation
* Runtime Data Manipulation Mitigation
* SID-History Injection Mitigation
* SIP and Trust Provider Hijacking Mitigation
* SSH Hijacking Mitigation
* Scheduled Task Mitigation
* Scheduled Transfer Mitigation
* Screen Capture Mitigation
* Screensaver Mitigation
* Scripting Mitigation
* Security Software Discovery Mitigation
* Security Support Provider Mitigation
* Service Execution Mitigation
* Service Registry Permissions Weakness Mitigation
* Service Stop Mitigation
* Setuid and Setgid Mitigation
* Shared Webroot Mitigation
* Shortcut Modification Mitigation
* Signed Binary Proxy Execution Mitigation
* Signed Script Proxy Execution Mitigation
* Software Packing Mitigation
* Source Mitigation
* Space after Filename Mitigation
* Spearphishing Attachment Mitigation
* Spearphishing Link Mitigation
* Spearphishing via Service Mitigation
* Standard Application Layer Protocol Mitigation
* Standard Cryptographic Protocol Mitigation
* Standard Non-Application Layer Protocol Mitigation
* Startup Items Mitigation
* Stored Data Manipulation Mitigation
* Sudo Caching Mitigation
* Sudo Mitigation
* Supply Chain Compromise Mitigation
* System Firmware Mitigation
* System Information Discovery Mitigation
* System Network Configuration Discovery Mitigation
* System Network Connections Discovery Mitigation
* System Owner/User Discovery Mitigation
* System Service Discovery Mitigation
* System Time Discovery Mitigation
* Systemd Service Mitigation
* Taint Shared Content Mitigation
* Template Injection Mitigation
* Third-party Software Mitigation
* Time Providers Mitigation
* Timestomp Mitigation
* Transmitted Data Manipulation Mitigation
* Trap Mitigation
* Trusted Developer Utilities Mitigation
* Trusted Relationship Mitigation
* Two-Factor Authentication Interception Mitigation
* Uncommonly Used Port Mitigation
* User Execution Mitigation
* Valid Accounts Mitigation
* Video Capture Mitigation
* Virtualization/Sandbox Evasion Mitigation
* Web Service Mitigation
* Web Shell Mitigation
* Windows Admin Shares Mitigation
* Windows Management Instrumentation Event Subscription Mitigation
* Windows Management Instrumentation Mitigation
* Windows Remote Management Mitigation
* Winlogon Helper DLL Mitigation
* XSL Script Processing Mitigation

Minor Mitigation changes:
No changes

**PRE-ATT&CK**

New Mitigations:
No changes

Mitigation changes:
No changes

Mitigation revocations:
No changes

Mitigation deprecations:
No changes

Minor Mitigation changes:
No changes

**Mobile**

New Mitigations:
No changes

Mitigation changes:
No changes

Mitigation revocations:
No changes

Mitigation deprecations:
No changes

Minor Mitigation changes:
No changes


