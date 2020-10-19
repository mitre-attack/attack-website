Title: Updates - April 2019
Date: April 2019
Category: Cyber Threat Intelligence
Authors: Blake Strom
Template: resources/update-post
url: /resources/updates/updates-april-2019
save_as: resources/updates/updates-april-2019/index.html

| Version | Start Date | End Date | Data |
|:--------|:-----------|:---------|:-----|
| [ATT&CK v4](/versions/v4) | April 30, 2019 | July 30, 2019 | [v4.0 on MITRE/CTI](https://github.com/mitre/cti/releases/tag/ATT%26CK-v4.0) |

### Previous Versions
Previous versions of the ATT&CK website are now being saved and displayed [here](/resources/versions) to give a historical reference for prior content releases.

### Tactics and Techniques

**Enterprise**

Impact Tactic:

The [Impact](/tactics/TA0040) Tactic was added to cover integrity and availability attacks against enterprise systems. Each technique will include an Impact Type label of 'Integrity' or 'Availability'.

The tactic covers 14 techniques that were added in this update:

* [Data Destruction](/techniques/T1485)
* [Data Encrypted for Impact](/techniques/T1486)
* [Defacement](/techniques/T1491)
* [Disk Content Wipe](/techniques/T1488)
* [Disk Structure Wipe](/techniques/T1487)
* [Endpoint Denial of Service](/techniques/T1499)
* [Firmware Corruption](/techniques/T1495)
* [Inhibit System Recovery](/techniques/T1490)
* [Network Denial of Service](/techniques/T1498)
* [Resource Hijacking](/techniques/T1496)
* [Runtime Data Manipulation](/techniques/T1494)
* [Service Stop](/techniques/T1489)
* [Stored Data Manipulation](/techniques/T1492)
* [Transmitted Data Manipulation](/techniques/T1493)

Seven additional techniques were added:

* [Compile After Delivery](/techniques/T1500) (Defense Evasion)
* [Domain Generation Algorithms](/techniques/T1483) (Command and Control)
* [Domain Trust Discovery](/techniques/T1482) (Discovery)
* [Execution Guardrails](/techniques/T1480) (Defense Evasion)
* [Group Policy Modification](/techniques/T1484) (Defense Evasion)
* [Systemd Service](/techniques/T1501) (Persistence)
* [Virtualization/Sandbox Evasion](/techniques/T1497) (Defense Evasion, Discovery)

The following techniques were updated:

* [External Remote Services](/techniques/T1133) - Added to Initial Access Tactic
* [Input Prompt](/techniques/T1141) - Added Windows and examples
* [LLMNR/NBT-NS Poisoning and Relay](/techniques/T1171) - Broadened scope to include hash relay
* [Masquerading](/techniques/T1036) - Broadened scope to include right-to-left override, added adversary examples of moving and renaming system utilities to avoid detection
* [Office Application Startup](/techniques/T1137) - Broadened scope to include Outlook Rules, Forms, Home Page, and Add-in persistence variations
* [PowerShell](/techniques/T1086) - Updated description to include use of System.Management.Automation
* [Remote System Discovery](/techniques/T1018) - Updated description to include accessing local hosts file
* [Security Software Discovery](/techniques/T1063) - Removed virtualization
* [Signed Binary Proxy Execution](/techniques/T1218) - Added msiexec.exe and odbcconf.exe variations
* [Supply Chain Compromise](/techniques/T1195) - Added compromise of open source dependencies
* [Valid Accounts](/techniques/T1078) - Broke out specific account types in description to include default accounts local accounts, and domain accounts

Added Digital Certificate Validation as a defense bypassed:

* [Compiled HTML File](/techniques/T1223)
* [InstallUtil](/techniques/T1118)
* [Mshta](/techniques/T1170)
* [Regsvcs/Regasm](/techniques/T1121)
* [Regsvr32](/techniques/T1117)
* [Rundll32](/techniques/T1085)

Miscellaneous minor changes:

* [Brute Force](/techniques/T1110) - Minor description update
* [Dynamic Data Exchange](/techniques/T1173) - Minor description update
* [Exploit Public-Facing Application](/techniques/T1190) - Minor description update
* [Screensaver](/techniques/T1180) - Minor description update
* [Template Injection](/techniques/T1221) - Reference added

*You can view the new and changed enterprise techniques in the ATT&CK Navigator by checking out the layer file we made available [here](https://mitre-attack.github.io/attack-navigator/enterprise/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2Fmitre-attack%2Fattack-navigator%2Fmaster%2Flayers%2Fdata%2Fupdate_layers%2FApril_2019_Updates_Enterprise.json). You can also check out a preview of the changes below! New techniques are green, and changed techniques are yellow.*

![ATT&CK Navigator - April 2019 Updates](/theme/images/April2019NavigatorLayer.png){ width=85% }

**PRE-ATT&CK**

Technique deprecations:

* Domain Generation Algorithms (DGA)- Moved under Enterprise with a new definition

**Mobile**

New Techniques:

* [Web Service](/techniques/T1481)

### Groups

On both Group and Software pages, we have changed the term “Aliases” to “Associated Groups” and “Associated Software” respectively to better reflect what these terms represent. Analysts track clusters of activities using various analytic methodologies and terms such as threat groups, activity groups, threat actors, intrusion sets, and campaigns. Some groups have multiple names associated with similar activities due to various organizations tracking similar activities by different names. Malware/software faces the same challenge with different organizations assigning different names to the same or similar samples. Organizations' group and software names may partially overlap with names designated by other organizations and may disagree on specific activity.

The MITRE ATT&CK team believes that tracking overlaps in activity for both groups and malware/software is useful to analysts, which is why we began tracking the “Aliases” field many years ago. While we always recognized that these were not true, complete “aliases,” we have realized that calling these “Aliases” only furthers the confusion over group naming. Thus, we have decided to change the field “Aliases” to “Associated Groups” and “Associated Software” to more accurately represent what we are trying to express. We make a best effort to track overlapping groups and software, but we do not represent these names as exact overlaps and encourage analysts to do additional research. If you have input on associated groups or software, please [contact us](/contact).

**Enterprise**

New Groups:

* [APT38](/groups/G0082)
* [APT39](/groups/G0087)
* [FIN4](/groups/G0085)
* [Gallmaker](/groups/G0084)
* [SilverTerrier](/groups/G0083)
* [Stolen Pencil](/groups/G0086)
* [TEMP.Veles](/groups/G0088)
* [Tropic Trooper](/groups/G0081)

Group changes:

* [APT18](/groups/G0026)
* [APT19](/groups/G0073)
* [APT1](/groups/G0006)
* [APT28](/groups/G0007)
* [APT29](/groups/G0016)
* [APT32](/groups/G0050)
* [APT33](/groups/G0064)
* [APT37](/groups/G0067)
* [APT3](/groups/G0022)
* [Cobalt Group](/groups/G0080)
* [CopyKittens](/groups/G0052)
* [Darkhotel](/groups/G0012)
* [Dragonfly 2.0](/groups/G0074)
* [Equation](/groups/G0020)
* [FIN10](/groups/G0051)
* [FIN6](/groups/G0037)
* [FIN7](/groups/G0046)
* [Gorgon Group](/groups/G0078)
* [Ke3chang](/groups/G0004)
* [Lazarus Group](/groups/G0032)
* [Leafminer](/groups/G0077)
* [Leviathan](/groups/G0065)
* [Lotus Blossom](/groups/G0030)
* [MuddyWater](/groups/G0069)
* [Night Dragon](/groups/G0014)
* [OilRig](/groups/G0049)
* [PLATINUM](/groups/G0068)
* [Rancor](/groups/G0075)
* [Scarlet Mimic](/groups/G0029)
* [Turla](/groups/G0010)
* [menuPass](/groups/G0045)

**PRE-ATT&CK**

New Groups:

* [TEMP.Veles](/groups/G0088)

Group changes:

* [APT1](/groups/G0006)
* [APT28](/groups/G0007)
* [Night Dragon](/groups/G0014)

**Mobile**

Group changes:

* [APT28](/groups/G0007)

### Software

**Enterprise**

New Software:

* [Agent Tesla](/software/S0331)
* [Astaroth](/software/S0373)
* [AuditCred](/software/S0347)
* [Azorult](/software/S0344)
* [BONDUPDATER](/software/S0360)
* [BadPatch](/software/S0337)
* [Cannon](/software/S0351)
* [Carbon](/software/S0335)
* [Cardinal RAT](/software/S0348)
* [Cobian RAT](/software/S0338)
* [CoinTicker](/software/S0369)
* [DarkComet](/software/S0334)
* [Denis](/software/S0354)
* [Ebury](/software/S0377)
* [Emotet](/software/S0367)
* [Empire](/software/S0363)
* [Exaramel](/software/S0343)
* [Expand](/software/S0361)
* [Final1stspy](/software/S0355)
* [GreyEnergy](/software/S0342)
* [HOPLIGHT](/software/S0376)
* [Impacket](/software/S0357)
* [KONNI](/software/S0356)
* [LaZagne](/software/S0349)
* [Linux Rabbit](/software/S0362)
* [LockerGoga ](/software/S0372)
* [Micropsia](/software/S0339)
* [NOKKI](/software/S0353)
* [NanoCore](/software/S0336)
* [Nltest](/software/S0359)
* [NotPetya](/software/S0368)
* [OSX_OCEANLOTUS.D](/software/S0352)
* [OceanSalt](/software/S0346)
* [Octopus](/software/S0340)
* [Olympic Destroyer](/software/S0365)
* [POWERTON](/software/S0371)
* [PoshC2](/software/S0378)
* [RawDisk](/software/S0364)
* [Remcos](/software/S0332)
* [Remexi](/software/S0375)
* [Ruler](/software/S0358)
* [SamSam](/software/S0370)
* [Seasalt](/software/S0345)
* [SpeakUp](/software/S0374)
* [Twitoor](/software/S0302)
* [UBoatRAT](/software/S0333)
* [WannaCry](/software/S0366)
* [Xbash](/software/S0341)
* [Zeus Panda](/software/S0330)
* [zwShell](/software/S0350)

Software changes:

* [BBSRAT](/software/S0127)
* [BISCUIT](/software/S0017)
* [BlackEnergy](/software/S0089)
* [CALENDAR](/software/S0025)
* [CCBkdr](/software/S0222)
* [CHOPSTICK](/software/S0023)
* [CORESHELL](/software/S0137)
* [China Chopper](/software/S0020)
* [Cobalt Strike](/software/S0154)
* [CozyCar](/software/S0046)
* [DOGCALL](/software/S0213)
* [Duqu](/software/S0038)
* [Dyre](/software/S0024)
* [Elise](/software/S0081)
* [Epic](/software/S0091)
* [FELIXROOT](/software/S0267)
* [FinFisher](/software/S0182)
* [GravityRAT](/software/S0237)
* [H1N1](/software/S0132)
* [HTRAN](/software/S0040)
* [JHUHUGIT](/software/S0044)
* [Kazuar](/software/S0265)
* [Mimikatz](/software/S0002)
* [Net](/software/S0039)
* [OopsIE](/software/S0264)
* [POSHSPY](/software/S0150)
* [POWERSTATS](/software/S0223)
* [PlugX](/software/S0013)
* [PowerDuke](/software/S0139)
* [PowerSploit](/software/S0194)
* [Proxysvc](/software/S0238)
* [Pupy](/software/S0192)
* [ROKRAT](/software/S0240)
* [RogueRobin](/software/S0270)
* [SDelete](/software/S0195)
* [Shamoon](/software/S0140)
* [Smoke Loader](/software/S0226)
* [TrickBot](/software/S0266)
* [WEBC2](/software/S0109)
* [XAgentOSX](/software/S0161)
* [XTunnel](/software/S0117)
* [Zebrocy](/software/S0251)
* [dsquery](/software/S0105)
* [gh0st RAT](/software/S0032)
* [jRAT](/software/S0283)
* [yty](/software/S0248)

**Mobile**

Software changes:

* [ANDROIDOS_ANSERVER.A](/software/S0310)