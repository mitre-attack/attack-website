Title: Updates - October 2018
Date: October 2018
Category: Cyber Threat Intelligence
Authors: Blake Strom
Template: resources/update-post
url: /resources/updates/updates-october-2018
save_as: resources/updates/updates-october-2018/index.html

| Version | Start Date | End Date | Data |
|:--------|:-----------|:---------|:-----|
| [ATT&CK v3](/versions/v3) | October 23, 2018 | April 29, 2019 | [v3.0 on MITRE/CTI](https://github.com/mitre/cti/releases/tag/ATT%26CK-v3.0) |

#### Transition from MediaWiki
The MediaWiki version of ATT&CK was moved to [attack-old.mitre.org](https://attack-old.mitre.org) and will remain up until the end of January 2019. The old website will not be receiving content updates during this timeframe, so you will need to use the new website and [STIX/TAXII](/resources/working-with-attack) to get the most up-to-date ATT&CK information.

#### Consolidated Technique and Software IDs
 
As of the October 2018 update all techniques across Enterprise ATT&CK, PRE-ATT&CK, and Mobile will have the same T#### numbering scheme. Existing PRE-ATT&CK and Mobile technique IDs have been converted over to the Enterprise IDs. Links to specific pages on the old wiki or to the new site with the old IDs will hit pages that redirect to the appropriate technique page.
 
Mobile software IDs were converted to the Enterprise format of S####.

*NOTE: If you have created layers for the [ATT&CK Navigator](https://github.com/mitre/attack-navigator) that include PRE-ATT&CK or Mobile ATT&CK techniques, you will need to update your layer files to use the new ATT&CK technique IDs.*
 
#### Tactic IDs
 
Tactics have been given ID numbers formatted as TA####.

#### Mobile Mitigation IDs

Mobile migitations have been given ID numbers formatted as M####.
 
#### Versioning
 
We've implemented a versioning system to all ATT&CK objects (techniques, groups, software, Mobile mitigations) to enable better tracking of incremental changes to existing ATT&CK content. The system will consist of a MAJOR.MINOR number. All objects will start at version 1.0 with the October release.
 
**Techniques**

Major version changes

* Name change
* Technique scope change - Change in definition resulting in broadening or focusing the scope of the technique

Minor version changes

* Minor descriptive information - technical information, examples, detection, mitigation, references
* Metadata change - platform, permissions, data sources, defense bypassed, etc.
 
**Groups**

Major version changes

* Adding or changing associated group or software
* Big changes to description and scope of a group

Minor version changes

* Relationship to new techniques or software
* New references
 
**Software**

Major version changes

* Adding or changing an associated group or software
* High level description or information changes
* Metadata change (type)

Minor version changes

* Relationship to new techniques or software
* New references
 
**Mobile Mitigations**

Major version changes

* Name change
* Scope, description, or information changes

Minor version changes

* Metadata change
* Relationship to new techniques
* New references
 
In addition, the ATT&CK Matrix view of techniques within an ATT&CK domain will be timestamped with the last change that impacts its structure and organization which will act as a version number for it.
 
#### Techniques

**Enterprise**
 
New techniques:

* [XSL Script Processing](/techniques/T1220)
* [Template Injection](/techniques/T1221)
* [File Permissions Modification](/techniques/T1222)
* [Compiled HTML File](/techniques/T1223)
 
Technique Changes:

* [Port Knocking](/techniques/T1205)
* [Modify Registry](/techniques/T1112)
* [SID-History Injection](/techniques/T1178)
* [Graphical User Interface](/techniques/T1061)
* [Image File Execution Options Injection](/techniques/T1183)
* [Registry Run Keys / Startup Folder](/techniques/T1060)
* [NTFS File Attributes](/techniques/T1096)
* Indicator Removal on Host
* [Indicator Blocking](/techniques/T1054)
* [Component Firmware](/techniques/T1109)
* [Binary Padding](/techniques/T1009)
* [Shared Webroot](/techniques/T1051)
* [Two-Factor Authentication Interception](/techniques/T1111)
* [Change Default File Association](/techniques/T1042)
* [Path Interception](/techniques/T1034)
* [Extra Window Memory Injection](/techniques/T1181)
* [Process Injection](/techniques/T1055)

*You can view the new and changed enterprise techniques in the ATT&CK Navigator by checking out the layer file we made available [here](https://mitre-attack.github.io/attack-navigator/enterprise/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2Fmitre-attack%2Fattack-navigator%2Fmaster%2Flayers%2Fdata%2Fupdate_layers%2FOctober_2018_Updates_Enterprise.json). You can also check out a preview of the changes below! New techniques are green, and changed techniques are yellow.*

![ATT&CK Navigator - October 2018 Updates](/theme/images/October2018NavigatorLayer.png){ width=85% }

<br>
**PRE-ATT&CK**
 
No changes
 
**Mobile**
 
The Obtain Device Access Matrix was collapsed into an [Initial Access](/tactics/TA0027) tactic to match the formatting of Enterprise.
 
The Network-Based Effects Matrix was consolidated into two tactic categories: [Network Effects](/tactics/TA0038) and [Remote Service Effects](/tactics/TA0039).
 
Technique Additions and Changes:

* [Deliver Malicious App via Authorized App Store](/techniques/T1475) created to consolidate several techniques in the old tactic 
* [Deliver Malicious App via Other Means](/techniques/T1476) created
* [Drive-by Compromise](/techniques/T1456) renamed from Malicious Web Content 
* [Exploit via Radio Interfaces](/techniques/T1477) created to consolidate Exploit Baseband Vulnerability and Malicious SMS Message 
* [Install Insecure or Malicious Configuration](/techniques/T1478) created
* [Supply Chain Compromise](/techniques/T1474) created to consolidate several techniques in the old tactic
 
Updated Content:
 
[User interface spoofing](/techniques/T1411)

*You can view the new and changed mobile techniques in the ATT&CK Navigator by checking out the layer file we made available [here](https://mitre.github.io/attack-navigator/mobile/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2Fmitre%2Fattack-navigator%2Fmaster%2Flayers%2Fdata%2Fupdate_layers%2FOctober_2018_Updates_Mobile.json).*
 
#### Groups
 
APT34 and OilRig were [combined](/groups/G0049) due to additional reporting increasing confidence in the overlap 
 
* [Dark Caracal](/groups/G0070)
* [Orangeworm](/groups/G0071)
* [Honeybee](/groups/G0072)
* [APT19](/groups/G0073)
* [Dragonfly 2.0](/groups/G0074) (split from Dragonfly due to reexamination of sources leading to assessment that these are better tracked as two groups)
* [Rancor](/groups/G0075)
* [Thrip](/groups/G0076)
* [Leafminer](/groups/G0077)
* [Gorgon Group](/groups/G0078)
* [DarkHydrus](/groups/G0079)
* [Cobalt Group](/groups/G0080)
 
#### Software
 
**Enterprise**
 
Poison Ivy and Darkmoon pages were combined into [Poison Ivy](/software/S0012)
 
[51 new software entries added](/software)
 
**Mobile**
 
* [Charger](/software/S0323)
* [SpyDealer](/software/S0324)
* [Judy](/software/S0325)
* [RedDrop](/software/S0326)
* [Skygofree](/software/S0327)
* [Stealth Mango](/software/S0328)
* [Tangelo](/software/S0329)