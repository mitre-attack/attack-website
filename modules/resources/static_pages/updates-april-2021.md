Title: Updates - April 2021
Date: April 2021
Category: Cyber Threat Intelligence
Authors: Adam Pennington
Template: resources/update-post
url: /resources/updates/updates-april-2021
save_as: resources/updates/updates-april-2021/index.html

| Version | Start Date | End Date | Data | Changelogs |
|:--------|:-----------|:---------|:-----|:-----------|
| [ATT&CK v9](/versions/v9) | April 29, 2021 | October 20, 2021 | [v9.0 on MITRE/CTI](https://github.com/mitre/cti/releases/tag/ATT%26CK-v9.0) | v8.2 - v9.0 [Details](/docs/changelogs/v8.2-v9.0/changelog-detailed.html) ([JSON](/docs/changelogs/v8.2-v9.0/changelog.json))

The April 2021 (v9) ATT&CK release updates Techniques, Groups, and Software for Enterprise, Mobile, and ICS. The biggest changes are a change in how we describe data sources, the addition of the [Containers](/matrices/enterprise/containers/) and [Google Workspace](/matrices/enterprise/cloud/googleworkspace/) platforms, and the replacement of the AWS, GCP, and Azure platforms with a single [IaaS](/matrices/enterprise/cloud/iaas/) (Infrastructure as a Service) platform. An [accompanying blog post](https://medium.com/mitre-attack/attack-april-2021-release-39accaf23c81) describes these changes and additions in more detail, with a focus on the new structure of data sources.

This version of ATT&CK for Enterprise contains 14 Tactics, 185 Techniques, and 367 Sub-techniques.
### Techniques

**Enterprise**

New Techniques:

* Boot or Logon Autostart Execution: [Active Setup](/techniques/T1547/014)
* Boot or Logon Autostart Execution: [XDG Autostart Entries](/techniques/T1547/013)
* [Build Image on Host](/techniques/T1612)
* [Container Administration Command](/techniques/T1609)
* [Container and Resource Discovery](/techniques/T1613)
* Credentials from Password Stores: [Password Managers](/techniques/T1555/005)
* Credentials from Password Stores: [Windows Credential Manager](/techniques/T1555/004)
* [Deploy Container](/techniques/T1610)
* [Escape to Host](/techniques/T1611)
* Scheduled Task/Job: [Container Orchestration Job](/techniques/T1053/007)
* [Stage Capabilities](/techniques/T1608)
	* [Drive-by Target](/techniques/T1608/004)
	* [Install Digital Certificate](/techniques/T1608/003)
	* [Link Target](/techniques/T1608/005)
	* [Upload Malware](/techniques/T1608/001)
	* [Upload Tool](/techniques/T1608/002)
* Subvert Trust Controls: [Code Signing Policy Modification](/techniques/T1553/006)
* Subvert Trust Controls: [Mark-of-the-Web Bypass](/techniques/T1553/005)
* [System Location Discovery](/techniques/T1614)
* System Network Configuration Discovery: [Internet Connection Discovery](/techniques/T1016/001)
* Unsecured Credentials: [Container API](/techniques/T1552/007)
* User Execution: [Malicious Image](/techniques/T1204/003)


Technique changes:

* [Account Discovery](/techniques/T1087)
	* [Cloud Account](/techniques/T1087/004)
	* [Email Account](/techniques/T1087/003)
	* [Local Account](/techniques/T1087/001)
* [Account Manipulation](/techniques/T1098)
	* [Additional Cloud Credentials](/techniques/T1098/001)
* [BITS Jobs](/techniques/T1197)
* Boot or Logon Autostart Execution: [Kernel Modules and Extensions](/techniques/T1547/006)
* Boot or Logon Autostart Execution: [Shortcut Modification](/techniques/T1547/009)
* Boot or Logon Initialization Scripts: [RC Scripts](/techniques/T1037/004)
* [Browser Extensions](/techniques/T1176)
* [Brute Force](/techniques/T1110)
	* [Credential Stuffing](/techniques/T1110/004)
	* [Password Guessing](/techniques/T1110/001)
	* [Password Spraying](/techniques/T1110/003)
* [Cloud Infrastructure Discovery](/techniques/T1580)
* [Cloud Service Dashboard](/techniques/T1538)
* [Cloud Service Discovery](/techniques/T1526)
* Command and Scripting Interpreter: [JavaScript](/techniques/T1059/007)
* Command and Scripting Interpreter: [Windows Command Shell](/techniques/T1059/003)
* [Create Account](/techniques/T1136)
	* [Cloud Account](/techniques/T1136/003)
* Credentials from Password Stores: [Credentials from Web Browsers](/techniques/T1555/003)
* [Data Destruction](/techniques/T1485)
* [Data Encrypted for Impact](/techniques/T1486)
* [Data Staged](/techniques/T1074)
	* [Remote Data Staging](/techniques/T1074/002)
* [Data from Cloud Storage Object](/techniques/T1530)
* [Data from Information Repositories](/techniques/T1213)
* [Defacement](/techniques/T1491)
	* [External Defacement](/techniques/T1491/002)
* Develop Capabilities: [Digital Certificates](/techniques/T1587/003)
* Develop Capabilities: [Malware](/techniques/T1587/001)
* [Email Collection](/techniques/T1114)
	* [Email Forwarding Rule](/techniques/T1114/003)
	* [Remote Email Collection](/techniques/T1114/002)
* [Endpoint Denial of Service](/techniques/T1499)
	* [Application Exhaustion Flood](/techniques/T1499/003)
	* [Application or System Exploitation](/techniques/T1499/004)
	* [Service Exhaustion Flood](/techniques/T1499/002)
* [Establish Accounts](/techniques/T1585)
* Event Triggered Execution: [Unix Shell Configuration Modification](/techniques/T1546/004)
* Event Triggered Execution: [Windows Management Instrumentation Event Subscription](/techniques/T1546/003)
* [Exploit Public-Facing Application](/techniques/T1190)
* [Exploitation for Privilege Escalation](/techniques/T1068)
* [External Remote Services](/techniques/T1133)
* [Forge Web Credentials](/techniques/T1606)
	* [SAML Tokens](/techniques/T1606/002)
* [Hijack Execution Flow](/techniques/T1574)
	* [DLL Search Order Hijacking](/techniques/T1574/001)
	* [DLL Side-Loading](/techniques/T1574/002)
	* [Dylib Hijacking](/techniques/T1574/004)
	* [Dynamic Linker Hijacking](/techniques/T1574/006)
* [Impair Defenses](/techniques/T1562)
	* [Disable Cloud Logs](/techniques/T1562/008)
	* [Disable or Modify Cloud Firewall](/techniques/T1562/007)
	* [Disable or Modify Tools](/techniques/T1562/001)
* [Implant Internal Image](/techniques/T1525)
* [Indicator Removal on Host](/techniques/T1070)
* [Internal Spearphishing](/techniques/T1534)
* [Masquerading](/techniques/T1036)
	* [Match Legitimate Name or Location](/techniques/T1036/005)
* [Modify Authentication Process](/techniques/T1556)
	* [Domain Controller Authentication](/techniques/T1556/001)
	* [Network Device Authentication](/techniques/T1556/004)
	* [Password Filter DLL](/techniques/T1556/002)
	* [Pluggable Authentication Modules](/techniques/T1556/003)
* [Modify Cloud Compute Infrastructure](/techniques/T1578)
	* [Create Cloud Instance](/techniques/T1578/002)
	* [Create Snapshot](/techniques/T1578/001)
	* [Delete Cloud Instance](/techniques/T1578/003)
	* [Revert Cloud Instance](/techniques/T1578/004)
* [Network Denial of Service](/techniques/T1498)
	* [Direct Network Flood](/techniques/T1498/001)
	* [Reflection Amplification](/techniques/T1498/002)
* [Network Service Scanning](/techniques/T1046)
* [Network Sniffing](/techniques/T1040)
* Obtain Capabilities: [Digital Certificates](/techniques/T1588/004)
* [Permission Groups Discovery](/techniques/T1069)
	* [Cloud Groups](/techniques/T1069/003)
* [Phishing](/techniques/T1566)
	* [Spearphishing Attachment](/techniques/T1566/001)
	* [Spearphishing Link](/techniques/T1566/002)
* [Phishing for Information](/techniques/T1598)
	* [Spearphishing Attachment](/techniques/T1598/002)
	* [Spearphishing Link](/techniques/T1598/003)
* [Remote System Discovery](/techniques/T1018)
* [Resource Hijacking](/techniques/T1496)
* [Scheduled Task/Job](/techniques/T1053)
* [Service Stop](/techniques/T1489)
* Signed Binary Proxy Execution: [Msiexec](/techniques/T1218/007)
* [Software Discovery](/techniques/T1518)
	* [Security Software Discovery](/techniques/T1518/001)
* [Steal Application Access Token](/techniques/T1528)
* [Steal Web Session Cookie](/techniques/T1539)
* [Steal or Forge Kerberos Tickets](/techniques/T1558)
	* [Golden Ticket](/techniques/T1558/001)
* [System Information Discovery](/techniques/T1082)
* [System Network Connections Discovery](/techniques/T1049)
* [System Time Discovery](/techniques/T1124)
* [Traffic Signaling](/techniques/T1205)
* [Transfer Data to Cloud Account](/techniques/T1537)
* Trusted Developer Utilities Proxy Execution: [MSBuild](/techniques/T1127/001)
* [Trusted Relationship](/techniques/T1199)
* [Unsecured Credentials](/techniques/T1552)
	* [Cloud Instance Metadata API](/techniques/T1552/005)
	* [Credentials In Files](/techniques/T1552/001)
* [Unused/Unsupported Cloud Regions](/techniques/T1535)
* [Use Alternate Authentication Material](/techniques/T1550)
	* [Application Access Token](/techniques/T1550/001)
	* [Pass the Hash](/techniques/T1550/002)
	* [Pass the Ticket](/techniques/T1550/003)
	* [Web Session Cookie](/techniques/T1550/004)
* [User Execution](/techniques/T1204)
* [Valid Accounts](/techniques/T1078)
	* [Cloud Accounts](/techniques/T1078/004)
	* [Default Accounts](/techniques/T1078/001)
	* [Local Accounts](/techniques/T1078/003)
* Virtualization/Sandbox Evasion: [System Checks](/techniques/T1497/001)
* Virtualization/Sandbox Evasion: [Time Based Evasion](/techniques/T1497/003)


Minor Technique changes:

* [Access Token Manipulation](/techniques/T1134)
	* [Parent PID Spoofing](/techniques/T1134/004)
	* [SID-History Injection](/techniques/T1134/005)
* [Acquire Infrastructure](/techniques/T1583)
	* [Botnet](/techniques/T1583/005)
	* [DNS Server](/techniques/T1583/002)
	* [Domains](/techniques/T1583/001)
	* [Server](/techniques/T1583/004)
	* [Virtual Private Server](/techniques/T1583/003)
	* [Web Services](/techniques/T1583/006)
* [Active Scanning](/techniques/T1595)
	* [Scanning IP Blocks](/techniques/T1595/001)
	* [Vulnerability Scanning](/techniques/T1595/002)
* [Automated Exfiltration](/techniques/T1020)
* [Boot or Logon Autostart Execution](/techniques/T1547)
	* [Plist Modification](/techniques/T1547/011)
	* [Registry Run Keys / Startup Folder](/techniques/T1547/001)
* [Boot or Logon Initialization Scripts](/techniques/T1037)
* [Command and Scripting Interpreter](/techniques/T1059)
* [Compromise Accounts](/techniques/T1586)
	* [Email Accounts](/techniques/T1586/002)
	* [Social Media Accounts](/techniques/T1586/001)
* [Compromise Infrastructure](/techniques/T1584)
	* [Botnet](/techniques/T1584/005)
	* [DNS Server](/techniques/T1584/002)
	* [Domains](/techniques/T1584/001)
	* [Server](/techniques/T1584/004)
	* [Virtual Private Server](/techniques/T1584/003)
	* [Web Services](/techniques/T1584/006)
* [Credentials from Password Stores](/techniques/T1555)
* [Data Manipulation](/techniques/T1565)
* [Develop Capabilities](/techniques/T1587)
	* [Code Signing Certificates](/techniques/T1587/002)
	* [Exploits](/techniques/T1587/004)
* [Direct Volume Access](/techniques/T1006)
* [Domain Policy Modification](/techniques/T1484)
	* [Group Policy Modification](/techniques/T1484/001)
* Dynamic Resolution: [Domain Generation Algorithms](/techniques/T1568/002)
* [Encrypted Channel](/techniques/T1573)
	* [Asymmetric Cryptography](/techniques/T1573/002)
* Establish Accounts: [Email Accounts](/techniques/T1585/002)
* Establish Accounts: [Social Media Accounts](/techniques/T1585/001)
* [Event Triggered Execution](/techniques/T1546)
	* [AppCert DLLs](/techniques/T1546/009)
	* [AppInit DLLs](/techniques/T1546/010)
	* [Application Shimming](/techniques/T1546/011)
	* [Component Object Model Hijacking](/techniques/T1546/015)
	* [Image File Execution Options Injection](/techniques/T1546/012)
	* [LC_LOAD_DYLIB Addition](/techniques/T1546/006)
* Execution Guardrails: [Environmental Keying](/techniques/T1480/001)
* [Exploitation of Remote Services](/techniques/T1210)
* [Gather Victim Host Information](/techniques/T1592)
	* [Client Configurations](/techniques/T1592/004)
	* [Firmware](/techniques/T1592/003)
	* [Hardware](/techniques/T1592/001)
	* [Software](/techniques/T1592/002)
* [Gather Victim Identity Information](/techniques/T1589)
	* [Credentials](/techniques/T1589/001)
	* [Email Addresses](/techniques/T1589/002)
	* [Employee Names](/techniques/T1589/003)
* [Gather Victim Network Information](/techniques/T1590)
	* [DNS](/techniques/T1590/002)
	* [Domain Properties](/techniques/T1590/001)
	* [IP Addresses](/techniques/T1590/005)
	* [Network Security Appliances](/techniques/T1590/006)
	* [Network Topology](/techniques/T1590/004)
	* [Network Trust Dependencies](/techniques/T1590/003)
* [Gather Victim Org Information](/techniques/T1591)
	* [Business Relationships](/techniques/T1591/002)
	* [Determine Physical Locations](/techniques/T1591/001)
	* [Identify Business Tempo](/techniques/T1591/003)
	* [Identify Roles](/techniques/T1591/004)
* [Hardware Additions](/techniques/T1200)
* Impair Defenses: [Impair Command History Logging](/techniques/T1562/003)
* Impair Defenses: [Indicator Blocking](/techniques/T1562/006)
* Indicator Removal on Host: [Network Share Connection Removal](/techniques/T1070/005)
* Input Capture: [Credential API Hooking](/techniques/T1056/004)
* [Man in the Browser](/techniques/T1185)
* Man-in-the-Middle: [ARP Cache Poisoning](/techniques/T1557/002)
* Masquerading: [Masquerade Task or Service](/techniques/T1036/004)
* Masquerading: [Rename System Utilities](/techniques/T1036/003)
* [Network Share Discovery](/techniques/T1135)
* [OS Credential Dumping](/techniques/T1003)
	* [DCSync](/techniques/T1003/006)
	* [LSA Secrets](/techniques/T1003/004)
	* [NTDS](/techniques/T1003/003)
* [Obfuscated Files or Information](/techniques/T1027)
* [Obtain Capabilities](/techniques/T1588)
	* [Code Signing Certificates](/techniques/T1588/003)
	* [Exploits](/techniques/T1588/005)
	* [Malware](/techniques/T1588/001)
	* [Tool](/techniques/T1588/002)
	* [Vulnerabilities](/techniques/T1588/006)
* Phishing for Information: [Spearphishing Service](/techniques/T1598/001)
* [Process Injection](/techniques/T1055)
	* [Asynchronous Procedure Call](/techniques/T1055/004)
	* [Dynamic-link Library Injection](/techniques/T1055/001)
	* [Extra Window Memory Injection](/techniques/T1055/011)
	* [Portable Executable Injection](/techniques/T1055/002)
	* [Process DoppelgÃ€nging](/techniques/T1055/013)
	* [Process Hollowing](/techniques/T1055/012)
	* [Thread Execution Hijacking](/techniques/T1055/003)
	* [Thread Local Storage](/techniques/T1055/005)
* [Rogue Domain Controller](/techniques/T1207)
* Scheduled Task/Job: [Scheduled Task](/techniques/T1053/005)
* [Search Closed Sources](/techniques/T1597)
	* [Purchase Technical Data](/techniques/T1597/002)
	* [Threat Intel Vendors](/techniques/T1597/001)
* [Search Open Technical Databases](/techniques/T1596)
	* [CDNs](/techniques/T1596/004)
	* [DNS/Passive DNS](/techniques/T1596/001)
	* [Digital Certificates](/techniques/T1596/003)
	* [Scan Databases](/techniques/T1596/005)
	* [WHOIS](/techniques/T1596/002)
* [Search Open Websites/Domains](/techniques/T1593)
	* [Search Engines](/techniques/T1593/002)
	* [Social Media](/techniques/T1593/001)
* [Search Victim-Owned Websites](/techniques/T1594)
* [Signed Binary Proxy Execution](/techniques/T1218)
	* [Mshta](/techniques/T1218/005)
	* [Rundll32](/techniques/T1218/011)
* [Software Deployment Tools](/techniques/T1072)
* [Subvert Trust Controls](/techniques/T1553)
	* [SIP and Trust Provider Hijacking](/techniques/T1553/003)
* [Supply Chain Compromise](/techniques/T1195)
* [System Network Configuration Discovery](/techniques/T1016)
* [Trusted Developer Utilities Proxy Execution](/techniques/T1127)
* [Virtualization/Sandbox Evasion](/techniques/T1497)
* [XSL Script Processing](/techniques/T1220)


Technique revocations:
No changes

Technique deprecations:
No changes

**Mobile**

New Techniques:

* [Command-Line Interface](/techniques/T1605)
* [Proxy Through Victim](/techniques/T1604)
* [Scheduled Task/Job](/techniques/T1603)


Technique changes:

* [Device Administrator Permissions](/techniques/T1401)


Minor Technique changes:

* [Deliver Malicious App via Other Means](/techniques/T1476)
* [Supply Chain Compromise](/techniques/T1474)

Technique revocations:
No changes

Technique deprecations:
No changes

### Software

**Enterprise**

New Software:

* [AppleJeus](/software/S0584)
* [BLINDINGCAN](/software/S0520)
* [Bazar](/software/S0534)
* [BendyBear](/software/S0574)
* [BitPaymer](/software/S0570)
* [BlackMould](/software/S0564)
* [CSPY Downloader](/software/S0527)
* [Caterpillar WebShell](/software/S0572)
* [ConnectWise](/software/S0591)
* [Conti](/software/S0575)
* [Crutch](/software/S0538)
* [Doki](/software/S0600)
* [DropBook](/software/S0547)
* [Dtrack](/software/S0567)
* [ECCENTRICBANDWAGON](/software/S0593)
* [EVILNUM](/software/S0568)
* [Egregor](/software/S0554)
* [Explosive](/software/S0569)
* [GoldFinder](/software/S0597)
* [GoldMax](/software/S0588)
* [Grandoreiro](/software/S0531)
* [GuLoader](/software/S0561)
* [Hildegard](/software/S0601)
* [HyperStack](/software/S0537)
* [IronNetInjector](/software/S0581)
* [Javali](/software/S0528)
* [KGH_SPY](/software/S0526)
* [Kerrdown](/software/S0585)
* [Kinsing](/software/S0599)
* [LookBack](/software/S0582)
* [Lucifer](/software/S0532)
* [MegaCortex](/software/S0576)
* [Melcoz](/software/S0530)
* [MoleNet](/software/S0553)
* [NBTscan](/software/S0590)
* [Out1](/software/S0594)
* [P.A.S. Webshell](/software/S0598)
* [Pay2Key](/software/S0556)
* [Penquin](/software/S0587)
* [Pysa](/software/S0583)
* [RemoteUtilities](/software/S0592)
* [SLOTHFULMEDIA](/software/S0533)
* [SUPERNOVA](/software/S0578)
* [ShadowPad](/software/S0596)
* [SharpStage](/software/S0546)
* [Sibot](/software/S0589)
* [Spark](/software/S0543)
* [TAINTEDSCRIBE](/software/S0586)
* [ThiefQuest](/software/S0595)
* [Waterbear](/software/S0579)


Software changes:

* [Agent Tesla](/software/S0331)
* [Astaroth](/software/S0373)
* [BabyShark](/software/S0414)
* [BlackEnergy](/software/S0089)
* [Carbon](/software/S0335)
* [China Chopper](/software/S0020)
* [Cobalt Strike](/software/S0154)
* [ComRAT](/software/S0126)
* [Ebury](/software/S0377)
* [Empire](/software/S0363)
* [EvilBunny](/software/S0396)
* [Exaramel for Linux](/software/S0401)
* [FALLCHILL](/software/S0181)
* [Fysbis](/software/S0410)
* [Gazer](/software/S0168)
* [HTRAN](/software/S0040)
* [HiddenWasp](/software/S0394)
* [Hikit](/software/S0009)
* [Kazuar](/software/S0265)
* [LaZagne](/software/S0349)
* [Machete](/software/S0409)
* [Matryoshka](/software/S0167)
* [Mimikatz](/software/S0002)
* [More_eggs](/software/S0284)
* [NETWIRE](/software/S0198)
* [Net](/software/S0039)
* [NotPetya](/software/S0368)
* [OSX_OCEANLOTUS.D](/software/S0352)
* [Olympic Destroyer](/software/S0365)
* [PoetRAT](/software/S0428)
* [PoisonIvy](/software/S0012)
* [PowerSploit](/software/S0194)
* [Proton](/software/S0279)
* [REvil](/software/S0496)
* [ROKRAT](/software/S0240)
* [Ragnar Locker](/software/S0481)
* [Raindrop](/software/S0565)
* [Ramsay](/software/S0458)
* [Ryuk](/software/S0446)
* [SDBbot](/software/S0461)
* [SEASHARPEE](/software/S0185)
* [SUNBURST](/software/S0559)
* [SUNSPOT](/software/S0562)
* [TEARDROP](/software/S0560)
* [TrickBot](/software/S0266)
* [Ursnif](/software/S0386)
* [Valak](/software/S0476)
* [Zebrocy](/software/S0251)
* [gh0st RAT](/software/S0032)


Minor Software changes:

* [BONDUPDATER](/software/S0360)
* [BOOTRASH](/software/S0114)
* [Briba](/software/S0204)
* [Carbanak](/software/S0030)
* [Catchamas](/software/S0261)
* [DustySky](/software/S0062)
* [Emotet](/software/S0367)
* [HAMMERTOSS](/software/S0037)
* [Hi-Zor](/software/S0087)
* [Hydraq](/software/S0203)
* [KeyBoy](/software/S0387)
* [Linfo](/software/S0211)
* [Linux Rabbit](/software/S0362)
* [Naid](/software/S0205)
* [Nerex](/software/S0210)
* [Net Crawler](/software/S0056)
* [Orz](/software/S0229)
* [PUNCHBUGGY](/software/S0196)
* [Pasam](/software/S0208)
* [PoshC2](/software/S0378)
* [PowerStallion](/software/S0393)
* [ROCKBOOT](/software/S0112)
* [Reaver](/software/S0172)
* [SeaDuke](/software/S0053)
* [Shamoon](/software/S0140)
* [TURNEDUP](/software/S0199)
* [TinyZBot](/software/S0004)
* [Vasport](/software/S0207)
* [WellMess](/software/S0514)
* [Wiarp](/software/S0206)
* [jRAT](/software/S0283)
* [meek](/software/S0175)
* [spwebmember](/software/S0227)


Software revocations:
No changes

Software deprecations:
No changes

**Mobile**

New Software:

* [Android/AdDisplay.Ashas](/software/S0525)
* [AndroidOS/MalLocker.B](/software/S0524)
* [Asacub](/software/S0540)
* [CHEMISTGAMES](/software/S0555)
* [CarbonSteal](/software/S0529)
* [Circles](/software/S0602)
* [DoubleAgent](/software/S0550)
* [Exobot](/software/S0522)
* [FrozenCell](/software/S0577)
* [GPlayed](/software/S0536)
* [Golden Cup](/software/S0535)
* [GoldenEagle](/software/S0551)
* [HenBox](/software/S0544)
* [Red Alert 2.0](/software/S0539)
* [SilkBean](/software/S0549)
* [TERRACOTTA](/software/S0545)
* [Tiktok Pro](/software/S0558)


Software changes:

* [Anubis](/software/S0422)
* [Desert Scorpion](/software/S0505)


Minor Software changes:
No changes

Software revocations:
No changes

Software deprecations:
No changes

### Groups

**Enterprise**

New Groups:

* [Ajax Security Team](/groups/G0130)
* [Bouncing Golf](/groups/G0097)
* [Evilnum](/groups/G0120)
* [Fox Kitten](/groups/G0117)
* [HAFNIUM](/groups/G0125)
* [Higaisa](/groups/G0126)
* [Indrik Spider](/groups/G0119)
* [Mustang Panda](/groups/G0129)
* [Operation Wocao](/groups/G0116)
* [Sidewinder](/groups/G0121)
* [Silent Librarian](/groups/G0122)
* [TA551](/groups/G0127)
* [Volatile Cedar](/groups/G0123)
* [Windigo](/groups/G0124)
* [ZIRCONIUM](/groups/G0128)


Group changes:

* [APT28](/groups/G0007)
* [APT29](/groups/G0016)
* [APT32](/groups/G0050)
* [APT39](/groups/G0087)
* [APT41](/groups/G0096)
* [BRONZE BUTLER](/groups/G0060)
* [BlackTech](/groups/G0098)
* [Carbanak](/groups/G0008)
* [Chimera](/groups/G0114)
* [Cobalt Group](/groups/G0080)
* [CopyKittens](/groups/G0052)
* [Darkhotel](/groups/G0012)
* [Dragonfly 2.0](/groups/G0074)
* [Elderwood](/groups/G0066)
* [FIN6](/groups/G0037)
* [GALLIUM](/groups/G0093)
* [GOLD SOUTHFIELD](/groups/G0115)
* [Kimsuky](/groups/G0094)
* [Lazarus Group](/groups/G0032)
* [Machete](/groups/G0095)
* [Magic Hound](/groups/G0059)
* [Molerats](/groups/G0021)
* [MuddyWater](/groups/G0069)
* [OilRig](/groups/G0049)
* [PLATINUM](/groups/G0068)
* [Sandworm Team](/groups/G0034)
* [Silence](/groups/G0091)
* [Stealth Falcon](/groups/G0038)
* [TA505](/groups/G0092)
* [Threat Group-3390](/groups/G0027)
* [Tropic Trooper](/groups/G0081)
* [Turla](/groups/G0010)
* [Windshift](/groups/G0112)
* [Wizard Spider](/groups/G0102)
* [menuPass](/groups/G0045)


Minor Group changes:

* [APT19](/groups/G0073)
* [APT3](/groups/G0022)
* [Cleaver](/groups/G0003)
* [DarkHydrus](/groups/G0079)
* [Deep Panda](/groups/G0009)
* [Dragonfly](/groups/G0035)
* [FIN8](/groups/G0061)
* [Gamaredon Group](/groups/G0047)
* [Gorgon Group](/groups/G0078)
* [Ke3chang](/groups/G0004)
* [TEMP.Veles](/groups/G0088)


Group revocations:

* UNC2452 (revoked by [APT29](/groups/G0016))


Group deprecations:
No changes

Group deletions:

* Charming Kitten


**Mobile**

New Groups:

* [Windshift](/groups/G0112)


Group changes:

* [APT28](/groups/G0007)


Minor Group changes:
No changes

Group revocations:
No changes

Group deprecations:
No changes

### Mitigations

**Enterprise**

New Mitigations:
No changes

Mitigation changes:
No changes

Minor Mitigation changes:

* [Audit](/mitigations/M1047)

Mitigation revocations:
No changes

Mitigation deprecations:
No changes

Mitigation deletions:

* Group Policy Modification Mitigation


**Mobile**

New Mitigations:
No changes

Mitigation changes:
No changes

Minor Mitigation changes:

* [Application Vetting](/mitigations/M1005)

Mitigation revocations:
No changes

Mitigation deprecations:
No changes

