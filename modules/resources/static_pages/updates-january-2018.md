Title: Updates - January 2018
Date: January 2018
Category: Cyber Threat Intelligence
Authors: Blake Strom
Template: resources/update-post
url: /resources/updates/updates-january-2018
save_as: resources/updates/updates-january-2018/index.html

| Version | Start Date | End Date | Data |
|:--------|:-----------|:---------|:-----|
| ATT&CK v1 | January 6, 2018 | April 12, 2018 | [v1.0 on MITRE/CTI](https://github.com/mitre/cti/releases/tag/ATT%26CK-v1.0) | 

#### Techniques

**19 new techniques** - Up to 188 from 169:

* [Mshta](/techniques/T1170)
* [LLMNR/NBT-NS Poisoning](/techniques/T1171)
* [Domain Fronting](/techniques/T1172)
* [Dynamic Data Exchange](/techniques/T1173)
* [Password Filter DLL](/techniques/T1174)
* [Distributed Component Object Model](/techniques/T1175)
* [Browser Extensions](/techniques/T1176)
* [LSASS Driver](/techniques/T1177)
* [SID-History Injection](/techniques/T1178)
* [Hooking](/techniques/T1179)
* [Screensaver](/techniques/T1180)
* [Extra Window Memory Injection](/techniques/T1181)
* [AppCert DLLs](/techniques/T1182)
* [Image File Execution Options Injection](/techniques/T1183)
* [SSH Hijacking](/techniques/T1184)
* [Man in the Browser](/techniques/T1185)
* [Process Doppelgänging](/techniques/T1186)
* [Forced Authentication](/techniques/T1187)
* [Multi-hop Proxy](/techniques/T1188)

**Three techniques renamed**

DLL Injection -> [Process Injection](/techniques/T1055)
Cron -> [Local Job Scheduling](/techniques/T1168)
Local Port Monitor -> [Port Monitors](/techniques/T1013)

**Many techniques updated**

Changes include adding new technical description information, detection and mitigation details, references, and adversary use examples. These range from major revisions, like with [Process Injection](/techniques/T1055) and [Access Token Manipulation](/techniques/T1134) to add substantially new information in the technical descriptions, to minor revisions, like [InstallUtil](/techniques/T1118) to add some additional details.

#### Groups and Software

In addition to the new pages below, we updated many Group and Software pages, including [OilRig](/groups/G0049) and [Dragonfly](/groups/G0035). We also added additional Associated Groups in an attempt to track overlapping activity from multiple vendors as a single Group.

**Nine new groups:**

* [CopyKittens](/groups/G0052)
* [FIN5](/groups/G0053)
* [Sowbug](/groups/G0054)
* [NEODYMIUM](/groups/G0055)
* [PROMETHIUM](/groups/G0056)
* [APT34](/groups/G0057)
* [Charming Kitten](/groups/G0058)
* [Magic Hound](/groups/G0059)
* [BRONZE BUTLER](/groups/G0060)

**26 new software entries:**

* [TDTESS](/software/S0164)
* [OSInfo](/software/S0165)
* [RemoteCMD](/software/S0166)
* [Matroyshka](/software/S0167)
* [Gazer](/software/S0168)
* [RawPOS](/software/S0169)
* [Helminth](/software/S0170)
* [Felismus](/software/S0171)
* [Reaver](/software/S0172)
* [FLIPSIDE](/software/S0173)
* [Responder](/software/S0174)
* [meek](/software/S0175)
* [Wingbird](/software/S0176)
* [Power Loader](/software/S0177)
* [Truvasys](/software/S0178)
* [MimiPenguin](/software/S0179)
* [Volgmer](/software/S0180)
* [FALLCHILL](/software/S0181)
* [FinFisher](/software/S0182)
* [Tor](/software/S0183)
* [POWRUNER](/software/S0184)
* [SEASHARPEE](/software/S0185)
* [DownPaper](/software/S0186)
* [Daserf](/software/S0187)
* [Starloader](/software/S0188)
* [ISMInjector](/software/S0189)

#### Other Changes

**Consolidated platforms parameters** - It was becoming cumbersome to track individual OS platform versions and releases. Since many of the techniques described work across most versions of a platform, we decided to consolidate them to down to one tag. Any version requirements will be captured in the technical description and requirements sections of a technique

* All Windows versions -> Windows
* MacOS/OS X -> macOS
* Linux - no change