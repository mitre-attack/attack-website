Title: Updates - April 2018
Date: April 2018
Category: Cyber Threat Intelligence
Authors: Blake Strom
Template: resources/update-post
url: /resources/updates/updates-april-2018
save_as: resources/updates/updates-april-2018/index.html

| Version | Start Date | End Date | Data |
|:--------|:-----------|:---------|:-----|
| ATT&CK v2 | April 13, 2018 | October 22, 2018 | [v2.0 on MITRE/CTI](https://github.com/mitre/cti/releases/tag/ATT%26CK-v2.0) | 

#### Initial Access Tactic Addition

[Initial Access](/tactics/TA0001) was added to ATT&CK and some techniques were added to [Execution](/tactics/TA0002) to cover the Launch and Compromise techniques within PRE-ATT&CK. The techniques were refactored to fit the enterprise level of detail.

The following techniques were added under Initial Access:

* [Drive-by Compromise](/techniques/T1189)
* [Exploit Public-Facing Application](/techniques/T1190)
* [Hardware Additions](/techniques/T1200)
* [Spearphishing Attachment](/techniques/T1193)
* [Spearphishing Link](/techniques/T1192)
* [Spearphishing via Service](/techniques/T1194)
* [Supply Chain Compromise](/techniques/T1195)
* [Trusted Relationship](/techniques/T1199)


The following existing techniques were cross-referenced into Initial Access:

* [Replication Through Removable Media](/techniques/T1091)
* [Valid Accounts](/techniques/T1078)

The following techniques were added to Execution:

* [Exploitation for Client Execution](/techniques/T1203)
* [User Execution](/techniques/T1204)

#### Techniques

**Aside from those added from PRE-ATT&CK, 23 additional new techniques were added** - Up to 219 from 188:

* [CMSTP](/techniques/T1191)
* [Control Panel Items](/techniques/T1196)
* [BITS Jobs](/techniques/T1197)
* [SIP and Trust Provider Hijacking](/techniques/T1198)
* [Password Policy Discovery](/techniques/T1201)
* [Indirect Command Execution](/techniques/T1202)
* [Exploitation for Client Execution](/techniques/T1203)
* [User Execution](/techniques/T1204)
* [Port Knocking](/techniques/T1205)
* [Sudo Caching](/techniques/T1206)
* [DCShadow](/techniques/T1207)
* [Kerberoasting](/techniques/T1208)
* [Time Providers](/techniques/T1209)
* [Exploitation of Remote Services](/techniques/T1210)
* [Exploitation for Defense Evasion](/techniques/T1211)
* [Exploitation for Credential Access](/techniques/T1212)
* [Data from Information Repositories](/techniques/T1213)
* [Credentials in Registry](/techniques/T1214)
* [Kernel Modules and Extensions](/techniques/T1215)
* [Signed Script Proxy Execution](/techniques/T1216)
* [Browser Bookmark Discovery](/techniques/T1217)
* [Signed Binary Proxy Execution](/techniques/T1218)
* [Remote Access Tools](/techniques/T1219)

**One technique renamed**

NTFS Extended Attributes -> [NTFS File Attributes](/techniques/T1096)

**Moderate to major updates to scope and/or content**

* [Winlogon Helper DLL](/techniques/T1004)
* [Credential Dumping](/techniques/T1003)
* [NTFS File Attributes](/techniques/T1096)
* [Web Service](/techniques/T1102)
* [Taint Shared Content](/techniques/T1080)

#### Groups and Software

**Nine new groups:**

* [FIN8](/groups/G0061)
* [TA459](/groups/G0062)
* [BlackOasis](/groups/G0063)
* [APT33](/groups/G0064)
* [Leviathan](/groups/G0065)
* [Elderwood](/groups/G0066)
* [APT37](/groups/G0067)
* [PLATINUM](/groups/G0068)
* [MuddyWater](/groups/G0069)

**Group Updates** [Patchwork](/groups/G0040) combined with Monsoon, G0042 redirects to G0040

**Groups with New Techniques Added**

* [Axiom](/groups/G0001)
* [APT28](/groups/G0007)
* [APT29](/groups/G0016)
* [APT3](/groups/G0022)
* [Lazarus Group](/groups/G0032)
* [menuPass](/groups/G0045)
* [APT34](/groups/G0057)
* [Carbanak](/groups/G0008)
* [Night Dragon](/groups/G0014)
* [FIN7](/groups/G0046)
* [APT32](/groups/G0050)

**45 new software entries:**

* [ISMInjector](/software/S0189)
* [BITSAdmin](/software/S0190)
* [Winexe](/software/S0191)
* [Pupy](/software/S0192)
* [Forfiles](/software/S0193)
* [PowerSploit](/software/S0194)
* [SDelete](/software/S0195)
* [PUNCHBUGGY](/software/S0196)
* [PUNCHTRACK](/software/S0197)
* [NETWIRE](/software/S0198)
* [TURNEDUP](/software/S0199)
* [Dipsind](/software/S0200)
* [JPIN](/software/S0201)
* [adbupd](/software/S0202)
* [Hydraq](/software/S0203)
* [Briba](/software/S0204)
* [Naid](/software/S0205)
* [Wiarp](/software/S0206)
* [Vasport](/software/S0207)
* [Pasam](/software/S0208)
* [Darkmoon](/software/S0209)
* [Nerex](/software/S0210)
* [Linfo](/software/S0211)
* [CORALDECK](/software/S0212)
* [DOGCALL](/software/S0213)
* [HAPPYWORK](/software/S0214)
* [KARAE](/software/S0215)
* [POORAIM](/software/S0216)
* [SHUTTERSPEED](/software/S0217)
* [SLOWDRIFT](/software/S0218)
* [WINERACK](/software/S0219)
* [Chaos](/software/S0220)
* [Umbreon](/software/S0221)
* [CCBkdr](/software/S0222)
* [POWERSTATS](/software/S0223)
* [Havij](/software/S0224)
* [sqlmap](/software/S0225)
* [Smoke Loader](/software/S0226)
* [spwebmember](/software/S0227)
* [NanHaiShu](/software/S0228)
* [Orz](/software/S0229)
* [ZeroT](/software/S0230)
* [Invoke-PSImage](/software/S0231)
* [HOMEFRY](/software/S0232)
* [MURKYTOP](/software/S0233)

#### Other Changes

**Exploitation of Vulnerability Breakout** - With the addition of Initial Access, more clarity was needed to define software exploitation behavior. The original Exploitation of Vulnerability technique was broken out into six variations specifically for individual tactics.

* Initial Access - [Exploit Public-Facing Application](/techniques/T1190)
* Execution - [Exploitation for Client Execution](/techniques/T1203)
* Privilege Escalation - [Exploitation for Privilege Escalation](/techniques/T1068): maintains the original Exploitation of Vulnerability technique ID T1068
* Lateral Movement - [Exploitation of Remote Services](/techniques/T1210)
* Defense Evasion - [Exploitation for Defense Evasion](/techniques/T1211)
* Credential Access - [Exploitation for Credential Access](/techniques/T1212)

**Software Platforms** - Added Windows, Linux, and macOS tags for software objects.

#### What's New in PRE-ATT&CK?

This release deprecates the Launch and Compromise tactics and most of the techniques that belong to them. In the future, these TTPs will be covered by techniques in the [Initial Access](/tactics/TA0001) and [Execution](/tactics/TA0002) tactics on ATT&CK.

* 2 tactics deprecated: Launch and Compromise
* Disseminate removable media has been moved from Launch to Stage Capabilities
* A new technique, Spearphishing for Information, has been added to Technical Information Gathering
* 23 techniques have been deprecated in this release
* PRE-ATT&CK now comprises 15 tactics and 151 techniques