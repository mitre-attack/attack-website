Title: Updates - October 2019
Date: October 2019
Category: Cyber Threat Intelligence
Authors: Blake Strom
Template: resources/update-post
url: /resources/updates/updates-october-2019
save_as: resources/updates/updates-october-2019/index.html

| Version | Start Date | End Date | Data |
|:--------|:-----------|:---------|:-----|
| [ATT&CK v6](/versions/v6) | October 24, 2019 | July 7, 2020 | [v6.3 on MITRE/CTI](https://github.com/mitre/cti/releases/tag/ATT%26CK-v6.3) |

The October 2019 ATT&CK release updates techniques, Groups, and Software for both Enterprise and Mobile. The biggest change is the addition of cloud-focused techniques.

#### ATT&CK for Cloud

36 techniques have been added or updated to cover adversary behavior against cloud-based platforms. We’ve added three infrastructure as a service (IaaS) platforms, [Amazon Web Services (AWS)](/matrices/enterprise/cloud/aws/), [Microsoft Azure (Azure)](/matrices/enterprise/cloud/azure/), and [Google Cloud Platform (GCP)](/matrices/enterprise/cloud/gcp/). The [Software as a service (SaaS)](/matrices/enterprise/cloud/saas/) platform will cover techniques against general cloud-based software platforms. Separately from IaaS and SaaS, we've also added two cloud software platforms, [Azure Active Directory (Azure AD)](/matrices/enterprise/cloud/azuread/) and [Office 365](/matrices/enterprise/cloud/office365/), to cover techniques against those specific platforms.

#### New techniques and updates for cloud:

* [Application Access Token](/techniques/T1527)
* [Cloud Instance Metadata API](/techniques/T1522)
* [Cloud Service Dashboard](/techniques/T1538)
* [Cloud Service Discovery](/techniques/T1526)
* [Data from Cloud Storage Object](/techniques/T1530)
* [Implant Container Image](/techniques/T1525)
* [Internal Spearphishing](/techniques/T1534)
* [Revert Cloud Instance](/techniques/T1536)
* [Steal Application Access Token](/techniques/T1528)
* [Steal Web Session Cookie](/techniques/T1539)
* [Transfer Data to Cloud Account](/techniques/T1537)
* [Unused Cloud Regions](/techniques/T1535)
* [Web Session Cookie](/techniques/T1506)
* [Account Discovery](/techniques/T1087)
* [Account Manipulation](/techniques/T1098)
* [Brute Force](/techniques/T1110)
* [Create Account](/techniques/T1136)
* [Credentials in Files](/techniques/T1081)
* [Data from Information Repositories](/techniques/T1213)
* [Data from Local System](/techniques/T1005)
* [Data Staged](/techniques/T1074)
* [Drive-by Compromise](/techniques/T1189)
* [Email Collection](/techniques/T1114)
* [Exploit Public-Facing Application](/techniques/T1190)
* [Network Service Scanning](/techniques/T1046)
* [Network Share Discovery](/techniques/T1135)
* [Office Application Startup](/techniques/T1137)
* [Permission Groups Discovery](/techniques/T1069)
* [Redundant Access](/techniques/T1108)
* [Remote System Discovery](/techniques/T1018)
* [Resource Hijacking](/techniques/T1496)
* [Spearphishing Link](/techniques/T1192)
* [System Information Discovery](/techniques/T1082)
* [System Network Connections Discovery](/techniques/T1049)
* [Trusted Relationship](/techniques/T1199)
* [Valid Accounts](/techniques/T1078)

The majority of the people and organizations we talked to while defining what ATT&CK means in a cloud environment said that they consider it an extension of an enterprise network, so we made it part of ATT&CK for Enterprise instead of creating a separate model. The ATT&CK for Cloud matrix along with the individual platforms can still be viewed separately from the rest of the Enterprise matrix. Due to web applications being thought of as the new perimeter with cloud, we've had to expand the definition of Lateral Movement a bit to cover access and interaction with cloud-based systems and services. Common credentialing material such as web browser cookies and application access tokens like OAuth are commonplace and are targeted for access to cloud-based software.

The current list of cloud platforms was selected based on input from contributors and what has been reported in incidents. We plan on re-evaluating them as needed to expand or refine them based on the threat landscape.

We shifted priorities a bit this year to this effort because of the overwhelming demand for cloud coverage in ATT&CK. The lack of public incident reporting made it difficult to do, but we were able to use a lot of the community's expertise and knowledge in building it. ATT&CK for Cloud is the first new technology domain that has been created based on almost 100% community contributions for technique ideas! Cloud is by no means finished. We will continue to build out additional cloud-based techniques for another release next year.

### Techniques

**Enterprise**

View enterprise technique updates in the ATT&CK Navigator [here](https://mitre-attack.github.io/attack-navigator/enterprise/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2Fmitre-attack%2Fattack-navigator%2Fmaster%2Flayers%2Fdata%2Fupdate_layers%2FOctober_2019_Updates_Enterprise.json).

New Techniques:

* [Account Access Removal](/techniques/T1531)
* [Application Access Token](/techniques/T1527)
* [Cloud Instance Metadata API](/techniques/T1522)
* [Cloud Service Dashboard](/techniques/T1538)
* [Cloud Service Discovery](/techniques/T1526)
* [Credentials from Web Browsers](/techniques/T1503)
* [Data from Cloud Storage Object](/techniques/T1530)
* [Elevated Execution with Prompt](/techniques/T1514)
* [Emond](/techniques/T1519)
* [Implant Container Image](/techniques/T1525)
* [Internal Spearphishing](/techniques/T1534)
* [Parent PID Spoofing](/techniques/T1502)
* [PowerShell Profile](/techniques/T1504)
* [Revert Cloud Instance](/techniques/T1536)
* [Server Software Component](/techniques/T1505)
* [Software Discovery](/techniques/T1518)
* [Steal Application Access Token](/techniques/T1528)
* [Steal Web Session Cookie](/techniques/T1539)
* [System Shutdown/Reboot](/techniques/T1529)
* [Transfer Data to Cloud Account](/techniques/T1537)
* [Unused/Unsupported Cloud Regions](/techniques/T1535)
* [Web Session Cookie](/techniques/T1506)

Technique deletions:
No changes

Technique changes:

* [.bash_profile and .bashrc](/techniques/T1156)
* [Account Discovery](/techniques/T1087)
* [Account Manipulation](/techniques/T1098)
* [Binary Padding](/techniques/T1009)
* [Brute Force](/techniques/T1110)
* [Component Object Model and Distributed COM](/techniques/T1175)
* [Connection Proxy](/techniques/T1090)
* [Create Account](/techniques/T1136)
* [Credential Dumping](/techniques/T1003)
* [Credentials in Files](/techniques/T1081)
* [Data Staged](/techniques/T1074)
* [Data from Information Repositories](/techniques/T1213)
* [Data from Local System](/techniques/T1005)
* [Drive-by Compromise](/techniques/T1189)
* [Email Collection](/techniques/T1114)
* [Exfiltration Over Alternative Protocol](/techniques/T1048)
* [Exploit Public-Facing Application](/techniques/T1190)
* [Exploitation for Privilege Escalation](/techniques/T1068)
* [File and Directory Discovery](/techniques/T1083)
* [File and Directory Permissions Modification](/techniques/T1222)
* [Forced Authentication](/techniques/T1187)
* [Gatekeeper Bypass](/techniques/T1144)
* [Hidden Window](/techniques/T1143)
* [Indicator Blocking](/techniques/T1054)
* [InstallUtil](/techniques/T1118)
* [Masquerading](/techniques/T1036)
* [Mshta](/techniques/T1170)
* [Network Service Scanning](/techniques/T1046)
* [Network Share Discovery](/techniques/T1135)
* [Office Application Startup](/techniques/T1137)
* [Peripheral Device Discovery](/techniques/T1120)
* [Permission Groups Discovery](/techniques/T1069)
* [Port Knocking](/techniques/T1205)
* [Process Discovery](/techniques/T1057)
* [Query Registry](/techniques/T1012)
* [Re-opened Applications](/techniques/T1164)
* [Redundant Access](/techniques/T1108)
* [Regsvcs/Regasm](/techniques/T1121)
* [Regsvr32](/techniques/T1117)
* [Remote System Discovery](/techniques/T1018)
* [Resource Hijacking](/techniques/T1496)
* [Scheduled Task](/techniques/T1053)
* [Security Software Discovery](/techniques/T1063)
* [Service Registry Permissions Weakness](/techniques/T1058)
* [Software Packing](/techniques/T1045)
* [Source](/techniques/T1153)
* [Spearphishing Link](/techniques/T1192)
* [System Information Discovery](/techniques/T1082)
* [System Network Configuration Discovery](/techniques/T1016)
* [System Network Connections Discovery](/techniques/T1049)
* [System Owner/User Discovery](/techniques/T1033)
* [System Service Discovery](/techniques/T1007)
* [Taint Shared Content](/techniques/T1080)
* [Third-party Software](/techniques/T1072)
* [Timestomp](/techniques/T1099)
* [Trap](/techniques/T1154)
* [Trusted Developer Utilities](/techniques/T1127)
* [Trusted Relationship](/techniques/T1199)
* [User Execution](/techniques/T1204)
* [Valid Accounts](/techniques/T1078)
* [Virtualization/Sandbox Evasion](/techniques/T1497)
* [Windows Admin Shares](/techniques/T1077)
* [Windows Management Instrumentation Event Subscription](/techniques/T1084)
* [Windows Remote Management](/techniques/T1028)
* [XSL Script Processing](/techniques/T1220)

Technique revocations:
No changes

Technique deprecations:
No changes

Minor Technique changes:

* [Access Token Manipulation](/techniques/T1134)
* [Accessibility Features](/techniques/T1015)
* [AppCert DLLs](/techniques/T1182)
* [AppInit DLLs](/techniques/T1103)
* [AppleScript](/techniques/T1155)
* [Application Deployment Software](/techniques/T1017)
* [Application Shimming](/techniques/T1138)
* [Audio Capture](/techniques/T1123)
* [Authentication Package](/techniques/T1131)
* [Automated Collection](/techniques/T1119)
* [BITS Jobs](/techniques/T1197)
* [Bash History](/techniques/T1139)
* [Bootkit](/techniques/T1067)
* [Browser Extensions](/techniques/T1176)
* [Bypass User Account Control](/techniques/T1088)
* [CMSTP](/techniques/T1191)
* [Clear Command History](/techniques/T1146)
* [Clipboard Data](/techniques/T1115)
* [Command-Line Interface](/techniques/T1059)
* [Commonly Used Port](/techniques/T1043)
* [Communication Through Removable Media](/techniques/T1092)
* [Compiled HTML File](/techniques/T1223)
* [Component Firmware](/techniques/T1109)
* [Control Panel Items](/techniques/T1196)
* [Credentials in Registry](/techniques/T1214)
* [Custom Command and Control Protocol](/techniques/T1094)
* [Custom Cryptographic Protocol](/techniques/T1024)
* [DLL Search Order Hijacking](/techniques/T1038)
* [DLL Side-Loading](/techniques/T1073)
* [Data Compressed](/techniques/T1002)
* [Data Destruction](/techniques/T1485)
* [Data Encoding](/techniques/T1132)
* [Data Encrypted for Impact](/techniques/T1486)
* [Data Obfuscation](/techniques/T1001)
* [Data Transfer Size Limits](/techniques/T1030)
* [Defacement](/techniques/T1491)
* [Disabling Security Tools](/techniques/T1089)
* [Disk Content Wipe](/techniques/T1488)
* [Disk Structure Wipe](/techniques/T1487)
* [Domain Fronting](/techniques/T1172)
* [Domain Generation Algorithms](/techniques/T1483)
* [Domain Trust Discovery](/techniques/T1482)
* [Dylib Hijacking](/techniques/T1157)
* [Dynamic Data Exchange](/techniques/T1173)
* [Endpoint Denial of Service](/techniques/T1499)
* [Execution Guardrails](/techniques/T1480)
* [Execution through API](/techniques/T1106)
* [Execution through Module Load](/techniques/T1129)
* [Exfiltration Over Command and Control Channel](/techniques/T1041)
* [Exfiltration Over Other Network Medium](/techniques/T1011)
* [Exfiltration Over Physical Medium](/techniques/T1052)
* [Exploitation for Client Execution](/techniques/T1203)
* [Exploitation for Credential Access](/techniques/T1212)
* [Exploitation for Defense Evasion](/techniques/T1211)
* [Exploitation of Remote Services](/techniques/T1210)
* [External Remote Services](/techniques/T1133)
* [Fallback Channels](/techniques/T1008)
* [File Deletion](/techniques/T1107)
* [File System Permissions Weakness](/techniques/T1044)
* [Firmware Corruption](/techniques/T1495)
* [Graphical User Interface](/techniques/T1061)
* [Group Policy Modification](/techniques/T1484)
* [HISTCONTROL](/techniques/T1148)
* [Hardware Additions](/techniques/T1200)
* [Hidden Users](/techniques/T1147)
* Indicator Removal on Host
* [Inhibit System Recovery](/techniques/T1490)
* [Input Capture](/techniques/T1056)
* [Input Prompt](/techniques/T1141)
* [Install Root Certificate](/techniques/T1130)
* [Kerberoasting](/techniques/T1208)
* [Kernel Modules and Extensions](/techniques/T1215)
* [Keychain](/techniques/T1142)
* [LC_LOAD_DYLIB Addition](/techniques/T1161)
* [LC_MAIN Hijacking](/techniques/T1149)
* [LLMNR/NBT-NS Poisoning and Relay](/techniques/T1171)
* [LSASS Driver](/techniques/T1177)
* [Launch Agent](/techniques/T1159)
* [Launch Daemon](/techniques/T1160)
* [Launchctl](/techniques/T1152)
* [Local Job Scheduling](/techniques/T1168)
* [Login Item](/techniques/T1162)
* [Logon Scripts](/techniques/T1037)
* [Man in the Browser](/techniques/T1185)
* [Modify Existing Service](/techniques/T1031)
* [Modify Registry](/techniques/T1112)
* [Multi-Stage Channels](/techniques/T1104)
* [Multi-hop Proxy](/techniques/T1188)
* [Multiband Communication](/techniques/T1026)
* [Multilayer Encryption](/techniques/T1079)
* [NTFS File Attributes](/techniques/T1096)
* [Network Denial of Service](/techniques/T1498)
* [Network Sniffing](/techniques/T1040)
* [New Service](/techniques/T1050)
* [Obfuscated Files or Information](/techniques/T1027)
* [Pass the Hash](/techniques/T1075)
* [Pass the Ticket](/techniques/T1097)
* [Password Filter DLL](/techniques/T1174)
* [Password Policy Discovery](/techniques/T1201)
* [Path Interception](/techniques/T1034)
* [Plist Modification](/techniques/T1150)
* [PowerShell](/techniques/T1086)
* [Private Keys](/techniques/T1145)
* [Process Doppelgänging](/techniques/T1186)
* [Process Injection](/techniques/T1055)
* [Rc.common](/techniques/T1163)
* [Registry Run Keys / Startup Folder](/techniques/T1060)
* [Remote Access Tools](/techniques/T1219)
* [Remote Desktop Protocol](/techniques/T1076)
* [Remote File Copy](/techniques/T1105)
* [Remote Services](/techniques/T1021)
* [Replication Through Removable Media](/techniques/T1091)
* [Rootkit](/techniques/T1014)
* [Rundll32](/techniques/T1085)
* [Runtime Data Manipulation](/techniques/T1494)
* [SID-History Injection](/techniques/T1178)
* [SIP and Trust Provider Hijacking](/techniques/T1198)
* [SSH Hijacking](/techniques/T1184)
* [Scheduled Transfer](/techniques/T1029)
* [Screen Capture](/techniques/T1113)
* [Screensaver](/techniques/T1180)
* [Scripting](/techniques/T1064)
* [Security Support Provider](/techniques/T1101)
* [Service Execution](/techniques/T1035)
* [Service Stop](/techniques/T1489)
* [Setuid and Setgid](/techniques/T1166)
* [Shared Webroot](/techniques/T1051)
* [Shortcut Modification](/techniques/T1023)
* [Signed Binary Proxy Execution](/techniques/T1218)
* [Signed Script Proxy Execution](/techniques/T1216)
* [Space after Filename](/techniques/T1151)
* [Spearphishing Attachment](/techniques/T1193)
* [Spearphishing via Service](/techniques/T1194)
* [Standard Application Layer Protocol](/techniques/T1071)
* [Standard Cryptographic Protocol](/techniques/T1032)
* [Standard Non-Application Layer Protocol](/techniques/T1095)
* [Startup Items](/techniques/T1165)
* [Stored Data Manipulation](/techniques/T1492)
* [Sudo Caching](/techniques/T1206)
* [Sudo](/techniques/T1169)
* [Supply Chain Compromise](/techniques/T1195)
* [System Firmware](/techniques/T1019)
* [System Time Discovery](/techniques/T1124)
* [Systemd Service](/techniques/T1501)
* [Template Injection](/techniques/T1221)
* [Time Providers](/techniques/T1209)
* [Transmitted Data Manipulation](/techniques/T1493)
* [Two-Factor Authentication Interception](/techniques/T1111)
* [Uncommonly Used Port](/techniques/T1065)
* [Video Capture](/techniques/T1125)
* [Web Service](/techniques/T1102)
* [Web Shell](/techniques/T1100)
* [Windows Management Instrumentation](/techniques/T1047)
* [Winlogon Helper DLL](/techniques/T1004)

**PRE-ATT&CK**

New Techniques:
No changes

Technique deletions:
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

View mobile technique updates in the ATT&CK Navigator [here](https://mitre-attack.github.io/attack-navigator/mobile/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2Fmitre-attack%2Fattack-navigator%2Fmaster%2Flayers%2Fdata%2Fupdate_layers%2FOctober_2019_Updates_Mobile.json).

New Techniques:

* [Access Notifications](/techniques/T1517)
* [Capture Camera](/techniques/T1512)
* [Clipboard Modification](/techniques/T1510)
* [Data Encrypted](/techniques/T1532)
* [Data from Local System](/techniques/T1533)
* [Domain Generation Algorithms](/techniques/T1520)
* [Evade Analysis Environment](/techniques/T1523)
* [Input Injection](/techniques/T1516)
* [Network Information Discovery](/techniques/T1507)
* [Screen Capture](/techniques/T1513)
* [Standard Cryptographic Protocol](/techniques/T1521)
* [Suppress Application Icon](/techniques/T1508)
* [Uncommonly Used Port](/techniques/T1509)

Technique deletions:
No changes

Technique changes:

* [Access Call Log](/techniques/T1433)
* [Access Stored Application Data](/techniques/T1409)
* [Capture Audio](/techniques/T1429)
* [Capture Clipboard Data](/techniques/T1414)
* [Capture SMS Messages](/techniques/T1412)
* [Data Encrypted for Impact](/techniques/T1471)
* [Delete Device Data](/techniques/T1447)
* [Deliver Malicious App via Authorized App Store](/techniques/T1475)
* [Deliver Malicious App via Other Means](/techniques/T1476)
* [Device Lockout](/techniques/T1446)
* [Download New Code at Runtime](/techniques/T1407)
* [Input Capture](/techniques/T1417)
* [Input Prompt](/techniques/T1411)
* [Masquerade as Legitimate Application](/techniques/T1444)
* [Modify Cached Executable Code](/techniques/T1403)
* [Modify System Partition](/techniques/T1400)

Technique revocations:

* Device Type Discovery (revoked by [System Information Discovery](/techniques/T1426))

Technique deprecations:

* [Abuse Accessibility Features](/techniques/T1453)

Minor Technique changes:

* [App Auto-Start at Device Boot](/techniques/T1402)
* [Commonly Used Port](/techniques/T1436)
* [Generate Fraudulent Advertising Revenue](/techniques/T1472)
* [Location Tracking](/techniques/T1430)
* [Manipulate App Store Rankings or Ratings](/techniques/T1452)
* [Obfuscated Files or Information](/techniques/T1406)
* [Premium SMS Toll Fraud](/techniques/T1448)
* [System Information Discovery](/techniques/T1426)

### Software

**Enterprise**

Exaramel changed to [Exaramel for Windows](/software/S0343/), and [Exaramel for Linux](/software/S0401/) was added separately.

New Software:

* [BOOSTWRITE](/software/S0415)
* [BabyShark](/software/S0414)
* [Exaramel for Linux](/software/S0401)
* [Fysbis](/software/S0410)
* [GRIFFON](/software/S0417)
* [Machete](/software/S0409)
* [MailSniper](/software/S0413)
* [OSX/Shlayer](/software/S0402)
* [RDFSNIFFER](/software/S0416)
* [RobbinHood](/software/S0400)
* [ZxShell](/software/S0412)
* [esentutl](/software/S0404)

Software deletions:
No changes

Software changes:

* [Astaroth](/software/S0373)
* [BITSAdmin](/software/S0190)
* [BONDUPDATER](/software/S0360)
* [Downdelph](/software/S0134)
* [Exaramel for Windows](/software/S0343)
* [HAMMERTOSS](/software/S0037)
* [KeyBoy](/software/S0387)
* [LockerGoga](/software/S0372)
* [More_eggs](/software/S0284)
* [NotPetya](/software/S0368)
* [OSX_OCEANLOTUS.D](/software/S0352)
* [Olympic Destroyer](/software/S0365)
* [Orz](/software/S0229)
* [PoshC2](/software/S0378)
* [Ursnif](/software/S0386)
* [certutil](/software/S0160)

Software revocations:
No changes

Software deprecations:
No changes

Minor Software changes:

* [Derusbi](/software/S0021)
* [FinFisher](/software/S0182)
* [HyperBro](/software/S0398)
* [Revenge RAT](/software/S0379)
* [UBoatRAT](/software/S0333)
* [Volgmer](/software/S0180)

**PRE-ATT&CK**

New Software:
No changes

Software deletions:
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

* [Exodus](/software/S0405)
* [FlexiSpy](/software/S0408)
* [Gustuff](/software/S0406)
* [Monokle](/software/S0407)
* [Riltok](/software/S0403)
* [Rotexy](/software/S0411)

Software deletions:

* Android Overlay Malware (removed due to the determination that the name did not identify a specific malware family)

Software changes:

* [ANDROIDOS_ANSERVER.A](/software/S0310)
* [Android/Chuli.A](/software/S0304)
* [Dendroid](/software/S0301)
* [DroidJack](/software/S0320)
* [Gooligan](/software/S0290)
* [Pallas](/software/S0399)
* [Pegasus for Android](/software/S0316)
* [RCSAndroid](/software/S0295)
* [RedDrop](/software/S0326)
* [Skygofree](/software/S0327)
* [SpyDealer](/software/S0324)
* [SpyNote RAT](/software/S0305)
* [Stealth Mango](/software/S0328)
* [Tangelo](/software/S0329)

Software revocations:
No changes

Software deprecations:
No changes

Minor Software changes:

* [Charger](/software/S0323)
* [FinFisher](/software/S0182)

### Groups

**Enterprise**

New Groups:

* [APT41](/groups/G0096)
* [Kimsuky](/groups/G0094)
* [Machete](/groups/G0095)

Group deletions:
No changes

Group changes:

* [APT19](/groups/G0073)
* [APT28](/groups/G0007)
* [APT32](/groups/G0050)
* [APT37](/groups/G0067)
* [APT38](/groups/G0082)
* [APT3](/groups/G0022)
* [Axiom](/groups/G0001)
* [CopyKittens](/groups/G0052)
* [DarkHydrus](/groups/G0079)
* [Deep Panda](/groups/G0009)
* [FIN6](/groups/G0037)
* [FIN7](/groups/G0046)
* [Gorgon Group](/groups/G0078)
* [Lazarus Group](/groups/G0032)
* [Leafminer](/groups/G0077)
* [Magic Hound](/groups/G0059)
* [OilRig](/groups/G0049)
* [Threat Group-3390](/groups/G0027)
* [Tropic Trooper](/groups/G0081)
* [admin@338](/groups/G0018)
* [menuPass](/groups/G0045)

Group revocations:
No changes

Group deprecations:
No changes

Minor Group changes:

* [APT1](/groups/G0006)
* [FIN8](/groups/G0061)
* [Leviathan](/groups/G0065)

**PRE-ATT&CK**

New Groups:
No changes

Group deletions:
No changes

Group changes: 
No changes

Group revocations:
No changes

Group deprecations:
No changes

Minor Group changes:
No changes

**Mobile**

New Groups:
No changes

Group deletions:
No changes

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

* [Application Developer Guidance](/mitigations/M1013)

Mitigation deletions:
No changes

Mitigation changes:

* [Filter Network Traffic](/mitigations/M1037)

Mitigation revocations:
No changes

Mitigation deprecations:
No changes

Minor Mitigation changes:
No changes

**PRE-ATT&CK**

New Mitigations:
No changes

Mitigation deletions:
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

Mitigation deletions:

* Use Device-Provided Credential Storage (this removal is temporary; the mitigation will be re-added in a future update)

Mitigation changes:
No changes

Mitigation revocations:
No changes

Mitigation deprecations:
No changes

Minor Mitigation changes:

* [Application Vetting](/mitigations/M1005)
* [Attestation](/mitigations/M1002)
* [Security Updates](/mitigations/M1001)
* [User Guidance](/mitigations/M1011)

