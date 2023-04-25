Title: Updates - October 2020
Date: October 2020
Category: Cyber Threat Intelligence
Authors: Adam Pennington
Template: resources/update-post
url: /resources/updates/updates-october-2020
save_as: resources/updates/updates-october-2020/index.html

| Version | Start Date | End Date | Data | Changelogs |
|:--------|:-----------|:---------|:-----|:-----------|
| [ATT&CK v8](/versions/v8) | October 27, 2020 | April 28, 2021 | [v8.0 on MITRE/CTI](https://github.com/mitre/cti/releases/tag/ATT%26CK-v8.0)<br />[v8.1 on MITRE/CTI](https://github.com/mitre/cti/releases/tag/ATT%26CK-v8.1)<br />[v8.2 on MITRE/CTI](https://github.com/mitre/cti/releases/tag/ATT%26CK-v8.2) | v7.2 - v8.0 [Details](/docs/changelogs/v7.2-v8.0/changelog-detailed.html) ([JSON](/docs/changelogs/v7.2-v8.0/changelog.json))<br />v8.0 - v8.1 [Details](/docs/changelogs/v8.0-v8.1/changelog-detailed.html) ([JSON](/docs/changelogs/v8.0-v8.1/changelog.json))<br />v8.1 - v8.2 [Details](/docs/changelogs/v8.1-v8.2/changelog-detailed.html) ([JSON](/docs/changelogs/v8.1-v8.2/changelog.json)) |

The October 2020 (v8) ATT&CK release updates Techniques, Groups, and Software for both Enterprise and Mobile. The biggest changes are the deprecation of the PRE-ATT&CK domain, the addition of two new Tactics to replace [PRE-ATT&CK](/versions/v7/matrices/pre/), and the addition of the Network platform to Enterprise ATT&CK. 

This version of ATT&CK for Enterprise contains 14 Tactics, 177 Techniques, and 348 Sub-techniques.

#### Retirement of PRE-ATT&CK
This release deprecates and removes the PRE-ATT&CK domain from ATT&CK, replacing its scope with two new Tactics in Enterprise ATT&CK [Reconnaissance](/tactics/TA0043/) and [Resource Development](/tactics/TA0042/). A new platform has also been added to ATT&CK to represent the environment these techniques occur in, [PRE](/matrices/enterprise/pre/). The previous contents of PRE-ATT&CK have been preserved [here](/versions/v7/matrices/pre/). See [the accompanying blog post](https://medium.com/mitre-attack/the-retirement-of-pre-attack-4b73ffecd3d3) for more details.

#### New techniques in Reconnaissance:

* [Active Scanning](/techniques/T1595)
	* [Scanning IP Blocks](/techniques/T1595/001)
	* [Vulnerability Scanning](/techniques/T1595/002)
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
* [Phishing for Information](/techniques/T1598)
	* [Spearphishing Attachment](/techniques/T1598/002)
	* [Spearphishing Link](/techniques/T1598/003)
	* [Spearphishing Service](/techniques/T1598/001)
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

#### New techniques in Resource Development:

* [Acquire Infrastructure](/techniques/T1583)
	* [Botnet](/techniques/T1583/005)
	* [DNS Server](/techniques/T1583/002)
	* [Domains](/techniques/T1583/001)
	* [Server](/techniques/T1583/004)
	* [Virtual Private Server](/techniques/T1583/003)
	* [Web Services](/techniques/T1583/006)
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
* [Develop Capabilities](/techniques/T1587)
	* [Code Signing Certificates](/techniques/T1587/002)
	* [Digital Certificates](/techniques/T1587/003)
	* [Exploits](/techniques/T1587/004)
	* [Malware](/techniques/T1587/001)
* [Establish Accounts](/techniques/T1585)
	* [Email Accounts](/techniques/T1585/002)
	* [Social Media Accounts](/techniques/T1585/001)
* [Obtain Capabilities](/techniques/T1588)
	* [Code Signing Certificates](/techniques/T1588/003)
	* [Digital Certificates](/techniques/T1588/004)
	* [Exploits](/techniques/T1588/005)
	* [Malware](/techniques/T1588/001)
	* [Tool](/techniques/T1588/002)
	* [Vulnerabilities](/techniques/T1588/006)


#### ATT&CK for Network Infrastructure Devices

13 techniques and 15 sub-techniques have been added or modified to cover adversary behavior against network infrastructure devices that constitute the fabric of enterprises' networks such as switches and routers. These techniques are represented by a new platform in ATT&CK for Enterprise, [Network](/matrices/enterprise/network/).

#### New and updated techniques for Network:
* [Exploit Public-Facing Application](/techniques/T1190)
* [Command and Scripting Interpreter](/techniques/T1059)
	* [Network Device CLI](/techniques/T1059/008)
* [Pre-OS Boot](/techniques/T1542)
	* [ROMMONkit](/techniques/T1542/004)
	* [TFTP Boot](/techniques/T1542/005)
* [Traffic Signaling](/techniques/T1205)
	* [Port Knocking](/techniques/T1205/001)
* [Modify Authentication Process](/techniques/T1556)
	* [Network Device Authentication](/techniques/T1556/004)
* [Modify System Image](/techniques/T1601)
	* [Downgrade System Image](/techniques/T1601/002)
	* [Patch System Image](/techniques/T1601/001)
* [Network Boundary Bridging](/techniques/T1599)
	* [Network Address Translation Traversal](/techniques/T1599/001)
* [Weaken Encryption](/techniques/T1600)
	* [Disable Crypto Hardware](/techniques/T1600/002)
	* [Reduce Key Space](/techniques/T1600/001)
* [Data from Configuration Repository](/techniques/T1602)
	* [Network Device Configuration Dump](/techniques/T1602/002)
	* [SNMP (MIB Dump)](/techniques/T1602/001)
* [Input Capture](/techniques/T1056)
	* [Keylogging](/techniques/T1056/001)
* [Non-Application Layer Protocol](/techniques/T1095)
* [Proxy](/techniques/T1090)
	* [Multi-hop Proxy](/techniques/T1090/003)	
* [Automated Exfiltration](/techniques/T1020)
	* [Traffic Duplication](/techniques/T1020/001)


Many of the new Network techniques and sub-techniques focus on embedded network devices running closed source proprietary operating systems. This is largely driven by behaviors present in reported in the wild intrusions. Many newer devices leverage commodity embedded operating systems such as Linux or BSD variants, but accounts of adversary activity against these have been more sparse. However, network infrastructure devices running proprietary operating systems are still widely deployed on the Internet and within enterprises.

We will continue to build out additional Network techniques and sub-techniques as they become known. We welcome contributions and feedback from the community and look to improve this representation of behaviors in the network infrastructure devices space.

### Techniques

**Enterprise**

We also added 1 additional new technique and 7 sub-techniques to Enterprise in this ATT&CK release beyond the scope of the above updates: 

* Boot or Logon Autostart Execution: [Print Processors](/techniques/T1547/012)
* [Cloud Infrastructure Discovery](/techniques/T1580)
* Hide Artifacts: [VBA Stomping](/techniques/T1564/007)
* Impair Defenses: [Disable Cloud Logs](/techniques/T1562/008)
* Man-in-the-Middle: [ARP Cache Poisoning](/techniques/T1557/002)
* Scheduled Task/Job: [Systemd Timers](/techniques/T1053/006)
* Signed Binary Proxy Execution: [Verclsid](/techniques/T1218/012)
* Steal or Forge Kerberos Tickets: [AS-REP Roasting](/techniques/T1558/004)

All Enterprise technique changes are documented below.

New Techniques:

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
* Automated Exfiltration: [Traffic Duplication](/techniques/T1020/001)
* Boot or Logon Autostart Execution: [Print Processors](/techniques/T1547/012)
* [Cloud Infrastructure Discovery](/techniques/T1580)
* Command and Scripting Interpreter: [Network Device CLI](/techniques/T1059/008)
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
* [Data from Configuration Repository](/techniques/T1602)
	* [Network Device Configuration Dump](/techniques/T1602/002)
	* [SNMP (MIB Dump)](/techniques/T1602/001)
* [Develop Capabilities](/techniques/T1587)
	* [Code Signing Certificates](/techniques/T1587/002)
	* [Digital Certificates](/techniques/T1587/003)
	* [Exploits](/techniques/T1587/004)
	* [Malware](/techniques/T1587/001)
* [Establish Accounts](/techniques/T1585)
	* [Email Accounts](/techniques/T1585/002)
	* [Social Media Accounts](/techniques/T1585/001)
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
* Hide Artifacts: [VBA Stomping](/techniques/T1564/007)
* Impair Defenses: [Disable Cloud Logs](/techniques/T1562/008)
* Man-in-the-Middle: [ARP Cache Poisoning](/techniques/T1557/002)
* Modify Authentication Process: [Network Device Authentication](/techniques/T1556/004)
* [Modify System Image](/techniques/T1601)
	* [Downgrade System Image](/techniques/T1601/002)
	* [Patch System Image](/techniques/T1601/001)
* [Network Boundary Bridging](/techniques/T1599)
	* [Network Address Translation Traversal](/techniques/T1599/001)
* [Obtain Capabilities](/techniques/T1588)
	* [Code Signing Certificates](/techniques/T1588/003)
	* [Digital Certificates](/techniques/T1588/004)
	* [Exploits](/techniques/T1588/005)
	* [Malware](/techniques/T1588/001)
	* [Tool](/techniques/T1588/002)
	* [Vulnerabilities](/techniques/T1588/006)
* [Phishing for Information](/techniques/T1598)
	* [Spearphishing Attachment](/techniques/T1598/002)
	* [Spearphishing Link](/techniques/T1598/003)
	* [Spearphishing Service](/techniques/T1598/001)
* Pre-OS Boot: [ROMMONkit](/techniques/T1542/004)
* Pre-OS Boot: [TFTP Boot](/techniques/T1542/005)
* Scheduled Task/Job: [Systemd Timers](/techniques/T1053/006)
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
* Signed Binary Proxy Execution: [Verclsid](/techniques/T1218/012)
* Steal or Forge Kerberos Tickets: [AS-REP Roasting](/techniques/T1558/004)
* [Weaken Encryption](/techniques/T1600)
	* [Disable Crypto Hardware](/techniques/T1600/002)
	* [Reduce Key Space](/techniques/T1600/001)


Technique changes:

* Abuse Elevation Control Mechanism: [Bypass User Account Control](/techniques/T1548/002)
* [Account Discovery](/techniques/T1087)
	* [Cloud Account](/techniques/T1087/004)
* Account Manipulation: [Additional Cloud Credentials](/techniques/T1098/001)
* [Automated Exfiltration](/techniques/T1020)
* [Boot or Logon Autostart Execution](/techniques/T1547)
	* [Registry Run Keys / Startup Folder](/techniques/T1547/001)
* [Boot or Logon Initialization Scripts](/techniques/T1037)
* Brute Force: [Credential Stuffing](/techniques/T1110/004)
* Brute Force: [Password Cracking](/techniques/T1110/002)
* Brute Force: [Password Guessing](/techniques/T1110/001)
* Brute Force: [Password Spraying](/techniques/T1110/003)
* [Command and Scripting Interpreter](/techniques/T1059)
	* [AppleScript](/techniques/T1059/002)
	* [Visual Basic](/techniques/T1059/005)
* Create or Modify System Process: [Launch Daemon](/techniques/T1543/004)
* Create or Modify System Process: [Systemd Service](/techniques/T1543/002)
* Create or Modify System Process: [Windows Service](/techniques/T1543/003)
* [Data from Information Repositories](/techniques/T1213)
* Endpoint Denial of Service: [OS Exhaustion Flood](/techniques/T1499/001)
* Endpoint Denial of Service: [Service Exhaustion Flood](/techniques/T1499/002)
* [Event Triggered Execution](/techniques/T1546)
	* [Image File Execution Options Injection](/techniques/T1546/012)
* [Exploit Public-Facing Application](/techniques/T1190)
* [File and Directory Discovery](/techniques/T1083)
* File and Directory Permissions Modification: [Windows File and Directory Permissions Modification](/techniques/T1222/001)
* [Hardware Additions](/techniques/T1200)
* Hijack Execution Flow: [LD_PRELOAD](/techniques/T1574/006)
* Hijack Execution Flow: [Path Interception by Unquoted Path](/techniques/T1574/009)
* Impair Defenses: [Impair Command History Logging](/techniques/T1562/003)
* Indicator Removal on Host: [Clear Command History](/techniques/T1070/003)
* [Input Capture](/techniques/T1056)
	* [Keylogging](/techniques/T1056/001)
* [Man-in-the-Middle](/techniques/T1557)
* [Modify Authentication Process](/techniques/T1556)
* [Modify Registry](/techniques/T1112)
* Network Denial of Service: [Direct Network Flood](/techniques/T1498/001)
* Network Denial of Service: [Reflection Amplification](/techniques/T1498/002)
* [Network Share Discovery](/techniques/T1135)
* [Non-Application Layer Protocol](/techniques/T1095)
* Obfuscated Files or Information: [Binary Padding](/techniques/T1027/001)
* Obfuscated Files or Information: [Steganography](/techniques/T1027/003)
* [Password Policy Discovery](/techniques/T1201)
* [Permission Groups Discovery](/techniques/T1069)
	* [Cloud Groups](/techniques/T1069/003)
* [Phishing](/techniques/T1566)
	* [Spearphishing Attachment](/techniques/T1566/001)
	* [Spearphishing Link](/techniques/T1566/002)
	* [Spearphishing via Service](/techniques/T1566/003)
* [Pre-OS Boot](/techniques/T1542)
	* [Bootkit](/techniques/T1542/003)
* [Proxy](/techniques/T1090)
	* [Domain Fronting](/techniques/T1090/004)
	* [Multi-hop Proxy](/techniques/T1090/003)
* [Remote System Discovery](/techniques/T1018)
* Server Software Component: [Web Shell](/techniques/T1505/003)
* [Service Stop](/techniques/T1489)
* Signed Binary Proxy Execution: [Control Panel](/techniques/T1218/002)
* [Software Deployment Tools](/techniques/T1072)
* [Software Discovery](/techniques/T1518)
	* [Security Software Discovery](/techniques/T1518/001)
* [Steal or Forge Kerberos Tickets](/techniques/T1558)
	* [Kerberoasting](/techniques/T1558/003)
* [Traffic Signaling](/techniques/T1205)
	* [Port Knocking](/techniques/T1205/001)
* [Unsecured Credentials](/techniques/T1552)
	* [Cloud Instance Metadata API](/techniques/T1552/005)
* Use Alternate Authentication Material: [Application Access Token](/techniques/T1550/001)
* Use Alternate Authentication Material: [Web Session Cookie](/techniques/T1550/004)
* Valid Accounts: [Cloud Accounts](/techniques/T1078/004)
* Valid Accounts: [Default Accounts](/techniques/T1078/001)
* Valid Accounts: [Domain Accounts](/techniques/T1078/002)


Minor Technique changes:

* [Abuse Elevation Control Mechanism](/techniques/T1548)
* [Account Manipulation](/techniques/T1098)
* [Application Layer Protocol](/techniques/T1071)
	* [DNS](/techniques/T1071/004)
	* [File Transfer Protocols](/techniques/T1071/002)
	* [Mail Protocols](/techniques/T1071/003)
* [Archive Collected Data](/techniques/T1560)
* [Brute Force](/techniques/T1110)
* [Create or Modify System Process](/techniques/T1543)
* [Data Encrypted for Impact](/techniques/T1486)
* [Data Staged](/techniques/T1074)
	* [Remote Data Staging](/techniques/T1074/002)
* [Domain Trust Discovery](/techniques/T1482)
* [Dynamic Resolution](/techniques/T1568)
	* [Domain Generation Algorithms](/techniques/T1568/002)
* Email Collection: [Email Forwarding Rule](/techniques/T1114/003)
* [Endpoint Denial of Service](/techniques/T1499)
* [File and Directory Permissions Modification](/techniques/T1222)
* [Hide Artifacts](/techniques/T1564)
	* [Hidden Users](/techniques/T1564/002)
* [Hijack Execution Flow](/techniques/T1574)
	* [DLL Side-Loading](/techniques/T1574/002)
	* [Dylib Hijacking](/techniques/T1574/004)
	* [Path Interception by PATH Environment Variable](/techniques/T1574/007)
	* [Path Interception by Search Order Hijacking](/techniques/T1574/008)
	* [Services File Permissions Weakness](/techniques/T1574/010)
	* [Services Registry Permissions Weakness](/techniques/T1574/011)
* [Impair Defenses](/techniques/T1562)
	* [Disable or Modify Cloud Firewall](/techniques/T1562/007)
* [Indicator Removal on Host](/techniques/T1070)
* [Internal Spearphishing](/techniques/T1534)
* Modify Authentication Process: [Domain Controller Authentication](/techniques/T1556/001)
* [Modify Cloud Compute Infrastructure](/techniques/T1578)
	* [Create Cloud Instance](/techniques/T1578/002)
	* [Create Snapshot](/techniques/T1578/001)
	* [Delete Cloud Instance](/techniques/T1578/003)
* [Network Denial of Service](/techniques/T1498)
* [Obfuscated Files or Information](/techniques/T1027)
* [Scheduled Task/Job](/techniques/T1053)
* [Server Software Component](/techniques/T1505)
* [Signed Binary Proxy Execution](/techniques/T1218)
* [Supply Chain Compromise](/techniques/T1195)
* [Use Alternate Authentication Material](/techniques/T1550)
* [Valid Accounts](/techniques/T1078)


Technique revocations:
No changes

Technique deprecations:
No changes

**Mobile**

New Techniques:

* [Geofencing](/techniques/T1581)
* [SMS Control](/techniques/T1582)


Technique changes:

* [Delete Device Data](/techniques/T1447)
* [Supply Chain Compromise](/techniques/T1474)
* [URI Hijacking](/techniques/T1416)


Minor Technique changes:
No changes

Technique revocations:

* URL Scheme Hijacking (revoked by [URI Hijacking](/techniques/T1416))


Technique deprecations:
No changes

### Software

**Enterprise**

New Software:

* [Anchor](/software/S0504)
* [Bonadan](/software/S0486)
* [Carberp](/software/S0484)
* [CookieMiner](/software/S0492)
* [CrackMapExec](/software/S0488)
* [Cryptoistic](/software/S0498)
* [Dacls](/software/S0497)
* [Drovorub](/software/S0502)
* [FatDuke](/software/S0512)
* [FrameworkPOS](/software/S0503)
* [GoldenSpy](/software/S0493)
* [Hancitor](/software/S0499)
* [IcedID](/software/S0483)
* [Kessel](/software/S0487)
* [MCMD](/software/S0500)
* [Ngrok](/software/S0508)
* [Pillowmint](/software/S0517)
* [PipeMon](/software/S0501)
* [PolyglotDuke](/software/S0518)
* [RDAT](/software/S0495)
* [REvil](/software/S0496)
* [RegDuke](/software/S0511)
* [SYNful Knock](/software/S0519)
* [SoreFang](/software/S0516)
* [StrongPity](/software/S0491)
* [WellMail](/software/S0515)
* [WellMess](/software/S0514)


Software changes:

* [BADNEWS](/software/S0128)
* [Cobalt Strike](/software/S0154)
* [Ebury](/software/S0377)
* [Emotet](/software/S0367)
* [InvisiMole](/software/S0260)
* [KONNI](/software/S0356)
* [LoudMiner](/software/S0451)
* [Machete](/software/S0409)
* [Maze](/software/S0449)
* [Metamorfo](/software/S0455)
* [MiniDuke](/software/S0051)
* [NETWIRE](/software/S0198)
* [OnionDuke](/software/S0052)
* [SDelete](/software/S0195)
* [TrickBot](/software/S0266)
* [Trojan.Karagany](/software/S0094)
* [Valak](/software/S0476)
* [WEBC2](/software/S0109)
* [gh0st RAT](/software/S0032)
* [njRAT](/software/S0385)


Minor Software changes:

* [HiddenWasp](/software/S0394)
* [JPIN](/software/S0201)
* [OSX/Shlayer](/software/S0402)
* [RATANKBA](/software/S0241)
* [pwdump](/software/S0006)


Software revocations:
No changes

Software deprecations:
No changes

Software deletions:

* Twitoor


**Mobile**

New Software:

* [Desert Scorpion](/software/S0505)
* [FakeSpy](/software/S0509)
* [Mandrake](/software/S0485)
* [Twitoor](/software/S0302)
* [ViperRAT](/software/S0506)
* [WolfRAT](/software/S0489)
* [XLoader for iOS](/software/S0490)
* [Zen](/software/S0494)
* [eSurv](/software/S0507)


Software changes:

* [Anubis](/software/S0422)
* [Bread](/software/S0432)
* [Cerberus](/software/S0480)
* [Corona Updates](/software/S0425)
* [Dendroid](/software/S0301)
* [Ginp](/software/S0423)
* [Rotexy](/software/S0411)
* [Stealth Mango](/software/S0328)
* [TrickMo](/software/S0427)
* [XLoader for Android](/software/S0318)


Minor Software changes:
No changes

Software revocations:
No changes

Software deprecations:
No changes

### Groups

**Enterprise**

New Groups:

* [Bouncing Golf](/groups/G0097)
* [Chimera](/groups/G0114)
* [GOLD SOUTHFIELD](/groups/G0115)


Group changes:

* [APT1](/groups/G0006)
* [APT16](/groups/G0023)
* [APT17](/groups/G0025)
* [APT28](/groups/G0007)
* [APT29](/groups/G0016)
* [APT30](/groups/G0013)
* [APT37](/groups/G0067)
* [APT39](/groups/G0087)
* [Cleaver](/groups/G0003)
* [Dragonfly](/groups/G0035)
* [Dragonfly 2.0](/groups/G0074)
* [FIN6](/groups/G0037)
* [FIN7](/groups/G0046)
* [Gamaredon Group](/groups/G0047)
* [Lazarus Group](/groups/G0032)
* [Machete](/groups/G0095)
* [MuddyWater](/groups/G0069)
* [Night Dragon](/groups/G0014)
* [OilRig](/groups/G0049)
* [PROMETHIUM](/groups/G0056)
* [Patchwork](/groups/G0040)
* [TEMP.Veles](/groups/G0088)
* [Turla](/groups/G0010)
* [Winnti Group](/groups/G0044)
* [Wizard Spider](/groups/G0102)
* [menuPass](/groups/G0045)


Minor Group changes:

* [APT-C-36](/groups/G0099)
* [Honeybee](/groups/G0072)


Group revocations:
No changes

Group deprecations:
No changes

**Mobile**

New Groups:
No changes

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

* [Pre-compromise](/mitigations/M1056)


Mitigation changes:

* [User Training](/mitigations/M1017)


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

