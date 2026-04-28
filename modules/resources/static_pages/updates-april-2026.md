Title: Updates - April 2026
Date: April 2026
Category: Cyber Threat Intelligence
Authors: Adam Pennington
Template: resources/update-post
url: /resources/updates/updates-april-2026
save_as: resources/updates/updates-april-2026/index.html

| Version | Start Date | End Date | Data | Changelogs |
|:--------|:-----------|:---------|:-----|:-----------|
| [ATT&CK v19](/versions/v19) | April 28, 2026 | Current version of ATT&CK | [v19.0 on MITRE/CTI](https://github.com/mitre/cti/releases/tag/ATT%26CK-v19.0) | 18.1 - 19.0 [Details](/docs/changelogs/v18.1-v19.0/changelog-detailed.html) ([JSON](/docs/changelogs/v18.1-v19.0/changelog.json)) |

The April 2026 (v19) ATT&CK release updates Techniques, Groups, Campaigns and Software for Enterprise, Mobile, and ICS.

The biggest changes in ATT&CK v19 are the split of the Defense Evasion Tactic in Enterprise ATT&CK into the [Stealth](https://attack.mitre.org/tactics/TA0005/) and [Defense Impairment](https://attack.mitre.org/tactics/TA0112/) Tactics, the addition of Sub-Techniques to ICS ATT&CK, and the beginnings of [Detection Strategies](https://medium.com/mitre-attack/smarter-detection-strategies-in-attack-7e6738fec31f) in Mobile ATT&CK. A post describing the rationale behind the Defense Evasion split was published to [ATT&CK's Blog](https://medium.com/mitre-attack/defense-evasion-split-5d533545fa32) in March, and an [accompanying blog post](https://medium.com/mitre-attack/attack-v19-ff329cb65d66) describes final details of the split, contains guidance for transitioning to the new Tactics, and details changes across the entire ATT&CK release.

This release also includes a [human-readable detailed changelog](/docs/changelogs/v18.1-v19.0/changelog-detailed.html) showing more specifically what changed in updated ATT&CK objects, and a [machine-readable JSON changelog](/docs/changelogs/v18.1-v19.0/changelog.json), whose format is described in [ATT&CK's Github](https://github.com/mitre-attack/mitreattack-python/blob/main/mitreattack/diffStix/README.md).

This version of ATT&CK contains 949 Pieces of Software, 178 Groups, and 59 Campaigns.

Broken out by domain:

* Enterprise: 15 Tactics, 222 Techniques, 475 Sub-Techniques, 174 Groups, 821 Pieces of Software, 56 Campaigns, 44 Mitigations, 697 Detection Strategies, 1758 Analytics, and 106 Data Components
* Mobile: 12 Tactics, 77 Techniques, 47 Sub-Techniques, 20 Groups, 126 Pieces of Software, 3 Campaigns, 13 Mitigations, 124 Detection Strategies, 211 Analytics, and 29 Data Components
* ICS: 12 Tactics, 79 Techniques, 18 Sub-Techniques, 14 Groups, 23 Pieces of Software, 8 Campaigns, 52 Mitigations, 18 Assets, 97 Detection Strategies, 96 Analytics, and 36 Data Components

## Release Notes Terminology

* New objects: ATT&CK objects which are only present in the new release.
* Major version changes: ATT&CK objects that have a major version change. (e.g. 1.0 → 2.0)
* Minor version changes: ATT&CK objects that have a minor version change. (e.g. 1.0 → 1.1)
* Other version changes: ATT&CK objects that have a version change of any other kind. (e.g. 1.0 → 1.2)
* Patches: ATT&CK objects that have been patched while keeping the version the same. (e.g., 1.0 → 1.0 but something like a typo, a URL, or some metadata was fixed)
* Object revocations: ATT&CK objects which are revoked by a different object.
* Object deprecations: ATT&CK objects which are deprecated and no longer in use, and not replaced.
* Object deletions: ATT&CK objects which are no longer found in the STIX data.

## Table of Contents

[TOC]

## Techniques

### Enterprise

#### New Techniques

* [Disable or Modify System Firewall](/techniques/T1686) <small style="color:#929393">(v1.0)</small>
* Disable or Modify System Firewall: [Cloud Firewall](/techniques/T1686/001) <small style="color:#929393">(v1.0)</small>
* Disable or Modify System Firewall: [Network Device Firewall](/techniques/T1686/002) <small style="color:#929393">(v1.0)</small>
* Disable or Modify System Firewall: [Windows Host Firewall](/techniques/T1686/003) <small style="color:#929393">(v1.0)</small>
* [Disable or Modify Tools](/techniques/T1685) <small style="color:#929393">(v1.0)</small>
* Disable or Modify Tools: [Clear Linux or Mac System Logs](/techniques/T1685/006) <small style="color:#929393">(v1.0)</small>
* Disable or Modify Tools: [Clear Windows Event Logs](/techniques/T1685/005) <small style="color:#929393">(v1.0)</small>
* Disable or Modify Tools: [Disable or Modify Cloud Log](/techniques/T1685/002) <small style="color:#929393">(v1.0)</small>
* Disable or Modify Tools: [Disable or Modify Linux Audit System Log](/techniques/T1685/004) <small style="color:#929393">(v1.0)</small>
* Disable or Modify Tools: [Disable or Modify Windows Event Log](/techniques/T1685/001) <small style="color:#929393">(v1.0)</small>
* Disable or Modify Tools: [Modify or Spoof Tool UI](/techniques/T1685/003) <small style="color:#929393">(v1.0)</small>
* [Downgrade Attack](/techniques/T1689) <small style="color:#929393">(v1.0)</small>
* [Exploitation for Defense Impairment](/techniques/T1687) <small style="color:#929393">(v1.0)</small>
* [Generate Content](/techniques/T1683) <small style="color:#929393">(v1.0)</small>
* Generate Content: [Audio-Visual Content](/techniques/T1683/002) <small style="color:#929393">(v1.0)</small>
* Generate Content: [Written Content](/techniques/T1683/001) <small style="color:#929393">(v1.0)</small>
* Obfuscated Files or Information: [Invisible Unicode](/techniques/T1027/018) <small style="color:#929393">(v1.0)</small>
* [Prevent Command History Logging](/techniques/T1690) <small style="color:#929393">(v1.0)</small>
* [Query Public AI Services](/techniques/T1682) <small style="color:#929393">(v1.0)</small>
* [Safe Mode Boot](/techniques/T1688) <small style="color:#929393">(v1.0)</small>
* [Social Engineering](/techniques/T1684) <small style="color:#929393">(v1.0)</small>
* Social Engineering: [Email Spoofing](/techniques/T1684/002) <small style="color:#929393">(v1.0)</small>
* Social Engineering: [Impersonation](/techniques/T1684/001) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [Abuse Elevation Control Mechanism](/techniques/T1548) <small style="color:#929393">(v1.5&#8594;v2.0)</small>
* Abuse Elevation Control Mechanism: [Bypass User Account Control](/techniques/T1548/002) <small style="color:#929393">(v2.2&#8594;v3.0)</small>
* Abuse Elevation Control Mechanism: [Elevated Execution with Prompt](/techniques/T1548/004) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Abuse Elevation Control Mechanism: [Setuid and Setgid](/techniques/T1548/001) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Abuse Elevation Control Mechanism: [Sudo and Sudo Caching](/techniques/T1548/003) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Abuse Elevation Control Mechanism: [TCC Manipulation](/techniques/T1548/006) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Abuse Elevation Control Mechanism: [Temporary Elevated Cloud Access](/techniques/T1548/005) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [Access Token Manipulation](/techniques/T1134) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* Access Token Manipulation: [Create Process with Token](/techniques/T1134/002) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* Access Token Manipulation: [Make and Impersonate Token](/techniques/T1134/003) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Access Token Manipulation: [Parent PID Spoofing](/techniques/T1134/004) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Access Token Manipulation: [SID-History Injection](/techniques/T1134/005) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Access Token Manipulation: [Token Impersonation/Theft](/techniques/T1134/001) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* Adversary-in-the-Middle: [Name Resolution Poisoning and SMB Relay](/techniques/T1557/001) <small style="color:#929393">(v1.4&#8594;v2.0)</small>
* [BITS Jobs](/techniques/T1197) <small style="color:#929393">(v1.5&#8594;v2.0)</small>
* [Build Image on Host](/techniques/T1612) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* [Debugger Evasion](/techniques/T1622) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Delay Execution](/techniques/T1678) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Deobfuscate/Decode Files or Information](/techniques/T1140) <small style="color:#929393">(v1.4&#8594;v2.0)</small>
* [Deploy Container](/techniques/T1610) <small style="color:#929393">(v1.4&#8594;v2.0)</small>
* [Direct Volume Access](/techniques/T1006) <small style="color:#929393">(v2.3&#8594;v3.0)</small>
* [Domain or Tenant Policy Modification](/techniques/T1484) <small style="color:#929393">(v3.2&#8594;v4.0)</small>
* Domain or Tenant Policy Modification: [Group Policy Modification](/techniques/T1484/001) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Domain or Tenant Policy Modification: [Trust Modification](/techniques/T1484/002) <small style="color:#929393">(v2.2&#8594;v3.0)</small>
* [Execution Guardrails](/techniques/T1480) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* Execution Guardrails: [Environmental Keying](/techniques/T1480/001) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Execution Guardrails: [Mutual Exclusion](/techniques/T1480/002) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Exploitation for Stealth](/techniques/T1211) <small style="color:#929393">(v1.5&#8594;v2.0)</small>
* [File and Directory Permissions Modification](/techniques/T1222) <small style="color:#929393">(v2.3&#8594;v3.0)</small>
* File and Directory Permissions Modification: [Linux and Mac Permissions](/techniques/T1222/002) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* File and Directory Permissions Modification: [Windows Permissions](/techniques/T1222/001) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [Hide Artifacts](/techniques/T1564) <small style="color:#929393">(v1.4&#8594;v2.0)</small>
* Hide Artifacts: [Bind Mounts](/techniques/T1564/013) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Hide Artifacts: [Email Hiding Rules](/techniques/T1564/008) <small style="color:#929393">(v1.4&#8594;v2.0)</small>
* Hide Artifacts: [Extended Attributes](/techniques/T1564/014) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Hide Artifacts: [File/Path Exclusions](/techniques/T1564/012) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Hide Artifacts: [Hidden File System](/techniques/T1564/005) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Hide Artifacts: [Hidden Files and Directories](/techniques/T1564/001) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Hide Artifacts: [Hidden Users](/techniques/T1564/002) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Hide Artifacts: [Hidden Window](/techniques/T1564/003) <small style="color:#929393">(v1.4&#8594;v2.0)</small>
* Hide Artifacts: [Ignore Process Interrupts](/techniques/T1564/011) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Hide Artifacts: [NTFS File Attributes](/techniques/T1564/004) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Hide Artifacts: [Process Argument Spoofing](/techniques/T1564/010) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Hide Artifacts: [Resource Forking](/techniques/T1564/009) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Hide Artifacts: [Run Virtual Instance](/techniques/T1564/006) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* Hide Artifacts: [VBA Stomping](/techniques/T1564/007) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [Hijack Execution Flow](/techniques/T1574) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* Hijack Execution Flow: [AppDomainManager](/techniques/T1574/014) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Hijack Execution Flow: [COR_PROFILER](/techniques/T1574/012) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Hijack Execution Flow: [DLL](/techniques/T1574/001) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* Hijack Execution Flow: [Dylib Hijacking](/techniques/T1574/004) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* Hijack Execution Flow: [Dynamic Linker Hijacking](/techniques/T1574/006) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* Hijack Execution Flow: [Executable Installer File Permissions Weakness](/techniques/T1574/005) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Hijack Execution Flow: [KernelCallbackTable](/techniques/T1574/013) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Hijack Execution Flow: [Path Interception by PATH Environment Variable](/techniques/T1574/007) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Hijack Execution Flow: [Path Interception by Search Order Hijacking](/techniques/T1574/008) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Hijack Execution Flow: [Path Interception by Unquoted Path](/techniques/T1574/009) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Hijack Execution Flow: [Services File Permissions Weakness](/techniques/T1574/010) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Hijack Execution Flow: [Services Registry Permissions Weakness](/techniques/T1574/011) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* [Indicator Removal](/techniques/T1070) <small style="color:#929393">(v2.4&#8594;v3.0)</small>
* Indicator Removal: [Clear Command History](/techniques/T1070/003) <small style="color:#929393">(v1.6&#8594;v2.0)</small>
* Indicator Removal: [Clear Mailbox Data](/techniques/T1070/008) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Indicator Removal: [Clear Network Connection History and Configurations](/techniques/T1070/007) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Indicator Removal: [Clear Persistence](/techniques/T1070/009) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Indicator Removal: [File Deletion](/techniques/T1070/004) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Indicator Removal: [Network Share Connection Removal](/techniques/T1070/005) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Indicator Removal: [Relocate Malware](/techniques/T1070/010) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Indicator Removal: [Timestomp](/techniques/T1070/006) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [Indirect Command Execution](/techniques/T1202) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* [Masquerading](/techniques/T1036) <small style="color:#929393">(v1.8&#8594;v2.0)</small>
* Masquerading: [Break Process Trees](/techniques/T1036/009) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Masquerading: [Browser Fingerprint](/techniques/T1036/012) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Masquerading: [Double File Extension](/techniques/T1036/007) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Masquerading: [Invalid Code Signature](/techniques/T1036/001) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Masquerading: [Masquerade Account Name](/techniques/T1036/010) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Masquerading: [Masquerade File Type](/techniques/T1036/008) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Masquerading: [Masquerade Task or Service](/techniques/T1036/004) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Masquerading: [Match Legitimate Resource Name or Location](/techniques/T1036/005) <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* Masquerading: [Overwrite Process Arguments](/techniques/T1036/011) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Masquerading: [Rename Legitimate Utilities](/techniques/T1036/003) <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* Masquerading: [Right-to-Left Override](/techniques/T1036/002) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Masquerading: [Space after Filename](/techniques/T1036/006) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Modify Authentication Process](/techniques/T1556) <small style="color:#929393">(v2.6&#8594;v3.0)</small>
* Modify Authentication Process: [Conditional Access Policies](/techniques/T1556/009) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Modify Authentication Process: [Domain Controller Authentication](/techniques/T1556/001) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* Modify Authentication Process: [Hybrid Identity](/techniques/T1556/007) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Modify Authentication Process: [Multi-Factor Authentication](/techniques/T1556/006) <small style="color:#929393">(v1.4&#8594;v2.0)</small>
* Modify Authentication Process: [Network Device Authentication](/techniques/T1556/004) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* Modify Authentication Process: [Network Provider DLL](/techniques/T1556/008) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Modify Authentication Process: [Password Filter DLL](/techniques/T1556/002) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* Modify Authentication Process: [Pluggable Authentication Modules](/techniques/T1556/003) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* Modify Authentication Process: [Reversible Encryption](/techniques/T1556/005) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Modify Cloud Compute Infrastructure](/techniques/T1578) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Modify Cloud Compute Infrastructure: [Create Cloud Instance](/techniques/T1578/002) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Modify Cloud Compute Infrastructure: [Create Snapshot](/techniques/T1578/001) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Modify Cloud Compute Infrastructure: [Delete Cloud Instance](/techniques/T1578/003) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Modify Cloud Compute Infrastructure: [Modify Cloud Compute Configurations](/techniques/T1578/005) <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* Modify Cloud Compute Infrastructure: [Revert Cloud Instance](/techniques/T1578/004) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [Modify Cloud Resource Hierarchy](/techniques/T1666) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Modify Registry](/techniques/T1112) <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* [Modify System Image](/techniques/T1601) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Modify System Image: [Downgrade System Image](/techniques/T1601/002) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Modify System Image: [Patch System Image](/techniques/T1601/001) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Network Boundary Bridging](/techniques/T1599) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Network Boundary Bridging: [Network Address Translation Traversal](/techniques/T1599/001) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [Obfuscated Files or Information](/techniques/T1027) <small style="color:#929393">(v1.7&#8594;v2.0)</small>
* Obfuscated Files or Information: [Binary Padding](/techniques/T1027/001) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* Obfuscated Files or Information: [Command Obfuscation](/techniques/T1027/010) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Obfuscated Files or Information: [Compile After Delivery](/techniques/T1027/004) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Obfuscated Files or Information: [Compression](/techniques/T1027/015) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Obfuscated Files or Information: [Dynamic API Resolution](/techniques/T1027/007) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Obfuscated Files or Information: [Embedded Payloads](/techniques/T1027/009) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Obfuscated Files or Information: [Encrypted/Encoded File](/techniques/T1027/013) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Obfuscated Files or Information: [Fileless Storage](/techniques/T1027/011) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* Obfuscated Files or Information: [HTML Smuggling](/techniques/T1027/006) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* Obfuscated Files or Information: [Indicator Removal from Tools](/techniques/T1027/005) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Obfuscated Files or Information: [Junk Code Insertion](/techniques/T1027/016) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Obfuscated Files or Information: [LNK Icon Smuggling](/techniques/T1027/012) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Obfuscated Files or Information: [Polymorphic Code](/techniques/T1027/014) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Obfuscated Files or Information: [SVG Smuggling](/techniques/T1027/017) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Obfuscated Files or Information: [Software Packing](/techniques/T1027/002) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* Obfuscated Files or Information: [Steganography](/techniques/T1027/003) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Obfuscated Files or Information: [Stripped Payloads](/techniques/T1027/008) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [Plist File Modification](/techniques/T1647) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Pre-OS Boot](/techniques/T1542) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* Pre-OS Boot: [Bootkit](/techniques/T1542/003) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Pre-OS Boot: [Component Firmware](/techniques/T1542/002) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Pre-OS Boot: [ROMMONkit](/techniques/T1542/004) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Pre-OS Boot: [System Firmware](/techniques/T1542/001) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Pre-OS Boot: [TFTP Boot](/techniques/T1542/005) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Process Injection](/techniques/T1055) <small style="color:#929393">(v1.4&#8594;v2.0)</small>
* Process Injection: [Asynchronous Procedure Call](/techniques/T1055/004) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Process Injection: [Dynamic-link Library Injection](/techniques/T1055/001) <small style="color:#929393">(v1.4&#8594;v2.0)</small>
* Process Injection: [Extra Window Memory Injection](/techniques/T1055/011) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Process Injection: [ListPlanting](/techniques/T1055/015) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Process Injection: [Portable Executable Injection](/techniques/T1055/002) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Process Injection: [Proc Memory](/techniques/T1055/009) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Process Injection: [Process Doppelgänging](/techniques/T1055/013) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Process Injection: [Process Hollowing](/techniques/T1055/012) <small style="color:#929393">(v1.4&#8594;v2.0)</small>
* Process Injection: [Ptrace System Calls](/techniques/T1055/008) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Process Injection: [Thread Execution Hijacking](/techniques/T1055/003) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Process Injection: [Thread Local Storage](/techniques/T1055/005) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Process Injection: [VDSO Hijacking](/techniques/T1055/014) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [Reflective Code Loading](/techniques/T1620) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* [Rogue Domain Controller](/techniques/T1207) <small style="color:#929393">(v2.2&#8594;v3.0)</small>
* [Rootkit](/techniques/T1014) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* [Selective Exclusion](/techniques/T1679) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Subvert Trust Controls](/techniques/T1553) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* Subvert Trust Controls: [Code Signing](/techniques/T1553/002) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Subvert Trust Controls: [Code Signing Policy Modification](/techniques/T1553/006) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Subvert Trust Controls: [Gatekeeper Bypass](/techniques/T1553/001) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* Subvert Trust Controls: [Install Root Certificate](/techniques/T1553/004) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* Subvert Trust Controls: [Mark-of-the-Web Bypass](/techniques/T1553/005) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Subvert Trust Controls: [SIP and Trust Provider Hijacking](/techniques/T1553/003) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [System Binary Proxy Execution](/techniques/T1218) <small style="color:#929393">(v3.2&#8594;v4.0)</small>
* System Binary Proxy Execution: [CMSTP](/techniques/T1218/003) <small style="color:#929393">(v2.2&#8594;v3.0)</small>
* System Binary Proxy Execution: [Compiled HTML File](/techniques/T1218/001) <small style="color:#929393">(v2.2&#8594;v3.0)</small>
* System Binary Proxy Execution: [Control Panel](/techniques/T1218/002) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* System Binary Proxy Execution: [Electron Applications](/techniques/T1218/015) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* System Binary Proxy Execution: [InstallUtil](/techniques/T1218/004) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* System Binary Proxy Execution: [MMC](/techniques/T1218/014) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* System Binary Proxy Execution: [Mavinject](/techniques/T1218/013) <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* System Binary Proxy Execution: [Mshta](/techniques/T1218/005) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* System Binary Proxy Execution: [Msiexec](/techniques/T1218/007) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* System Binary Proxy Execution: [Odbcconf](/techniques/T1218/008) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* System Binary Proxy Execution: [Regsvcs/Regasm](/techniques/T1218/009) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* System Binary Proxy Execution: [Regsvr32](/techniques/T1218/010) <small style="color:#929393">(v2.2&#8594;v3.0)</small>
* System Binary Proxy Execution: [Rundll32](/techniques/T1218/011) <small style="color:#929393">(v2.5&#8594;v3.0)</small>
* System Binary Proxy Execution: [Verclsid](/techniques/T1218/012) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* [System Script Proxy Execution](/techniques/T1216) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* System Script Proxy Execution: [PubPrn](/techniques/T1216/001) <small style="color:#929393">(v2.1&#8594;v3.0)</small>
* System Script Proxy Execution: [SyncAppvPublishingServer](/techniques/T1216/002) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Template Injection](/techniques/T1221) <small style="color:#929393">(v1.4&#8594;v2.0)</small>
* [Traffic Signaling](/techniques/T1205) <small style="color:#929393">(v2.5&#8594;v3.0)</small>
* Traffic Signaling: [Port Knocking](/techniques/T1205/001) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Traffic Signaling: [Socket Filters](/techniques/T1205/002) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Trusted Developer Utilities Proxy Execution](/techniques/T1127) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* Trusted Developer Utilities Proxy Execution: [ClickOnce](/techniques/T1127/002) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Trusted Developer Utilities Proxy Execution: [JamPlus](/techniques/T1127/003) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Trusted Developer Utilities Proxy Execution: [MSBuild](/techniques/T1127/001) <small style="color:#929393">(v1.4&#8594;v2.0)</small>
* [Unused/Unsupported Cloud Regions](/techniques/T1535) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Use Alternate Authentication Material](/techniques/T1550) <small style="color:#929393">(v1.5&#8594;v2.0)</small>
* Use Alternate Authentication Material: [Application Access Token](/techniques/T1550/001) <small style="color:#929393">(v1.8&#8594;v2.0)</small>
* Use Alternate Authentication Material: [Pass the Hash](/techniques/T1550/002) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* Use Alternate Authentication Material: [Pass the Ticket](/techniques/T1550/003) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* Use Alternate Authentication Material: [Web Session Cookie](/techniques/T1550/004) <small style="color:#929393">(v1.5&#8594;v2.0)</small>
* [Valid Accounts](/techniques/T1078) <small style="color:#929393">(v2.8&#8594;v3.0)</small>
* Valid Accounts: [Cloud Accounts](/techniques/T1078/004) <small style="color:#929393">(v1.9&#8594;v2.0)</small>
* Valid Accounts: [Default Accounts](/techniques/T1078/001) <small style="color:#929393">(v1.5&#8594;v2.0)</small>
* Valid Accounts: [Domain Accounts](/techniques/T1078/002) <small style="color:#929393">(v1.5&#8594;v2.0)</small>
* Valid Accounts: [Local Accounts](/techniques/T1078/003) <small style="color:#929393">(v1.5&#8594;v2.0)</small>
* [Virtualization/Sandbox Evasion](/techniques/T1497) <small style="color:#929393">(v1.4&#8594;v2.0)</small>
* Virtualization/Sandbox Evasion: [System Checks](/techniques/T1497/001) <small style="color:#929393">(v2.3&#8594;v3.0)</small>
* Virtualization/Sandbox Evasion: [Time Based Checks](/techniques/T1497/003) <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* Virtualization/Sandbox Evasion: [User Activity Based Checks](/techniques/T1497/002) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [Weaken Encryption](/techniques/T1600) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Weaken Encryption: [Disable Crypto Hardware](/techniques/T1600/002) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* Weaken Encryption: [Reduce Key Space](/techniques/T1600/001) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [XSL Script Processing](/techniques/T1220) <small style="color:#929393">(v1.3&#8594;v2.0)</small>

#### Minor Version Changes

* [Command and Scripting Interpreter](/techniques/T1059) <small style="color:#929393">(v2.6&#8594;v2.7)</small>
* [Scheduled Task/Job](/techniques/T1053) <small style="color:#929393">(v2.4&#8594;v2.5)</small>

#### Patches

* [Adversary-in-the-Middle](/techniques/T1557) <small style="color:#929393">(v2.5)</small>
* [Cloud Service Discovery](/techniques/T1526) <small style="color:#929393">(v1.4)</small>
* [Compromise Host Software Binary](/techniques/T1554) <small style="color:#929393">(v2.2)</small>
* Create or Modify System Process: [Windows Service](/techniques/T1543/003) <small style="color:#929393">(v1.6)</small>
* Data Encoding: [Non-Standard Encoding](/techniques/T1132/002) <small style="color:#929393">(v1.1)</small>
* [Data Manipulation](/techniques/T1565) <small style="color:#929393">(v1.1)</small>
* Data Manipulation: [Runtime Data Manipulation](/techniques/T1565/003) <small style="color:#929393">(v1.2)</small>
* Data Manipulation: [Stored Data Manipulation](/techniques/T1565/001) <small style="color:#929393">(v1.1)</small>
* Data Manipulation: [Transmitted Data Manipulation](/techniques/T1565/002) <small style="color:#929393">(v1.1)</small>
* Develop Capabilities: [Exploits](/techniques/T1587/004) <small style="color:#929393">(v1.0)</small>
* Event Triggered Execution: [Image File Execution Options Injection](/techniques/T1546/012) <small style="color:#929393">(v1.2)</small>
* [Exploit Public-Facing Application](/techniques/T1190) <small style="color:#929393">(v2.8)</small>
* [Financial Theft](/techniques/T1657) <small style="color:#929393">(v1.2)</small>
* [Internal Spearphishing](/techniques/T1534) <small style="color:#929393">(v1.4)</small>
* [Native API](/techniques/T1106) <small style="color:#929393">(v2.3)</small>
* [Network Sniffing](/techniques/T1040) <small style="color:#929393">(v1.7)</small>
* Obtain Capabilities: [Artificial Intelligence](/techniques/T1588/007) <small style="color:#929393">(v1.1)</small>
* Obtain Capabilities: [Exploits](/techniques/T1588/005) <small style="color:#929393">(v1.0)</small>
* [Phishing](/techniques/T1566) <small style="color:#929393">(v2.7)</small>
* Phishing: [Spearphishing Voice](/techniques/T1566/004) <small style="color:#929393">(v1.2)</small>
* [Phishing for Information](/techniques/T1598) <small style="color:#929393">(v1.4)</small>
* Phishing for Information: [Spearphishing Voice](/techniques/T1598/004) <small style="color:#929393">(v1.0)</small>
* Software Extensions: [Browser Extensions](/techniques/T1176/001) <small style="color:#929393">(v1.1)</small>
* Stage Capabilities: [Upload Malware](/techniques/T1608/001) <small style="color:#929393">(v1.3)</small>
* User Execution: [Malicious Copy and Paste](/techniques/T1204/004) <small style="color:#929393">(v1.1)</small>

#### Revocations

* Clear Linux or Mac System Logs (revoked by Disable or Modify Tools: [Clear Linux or Mac System Logs](/techniques/T1685/006)) <small style="color:#929393">(v1.0)</small>
* Clear Windows Event Logs (revoked by Disable or Modify Tools: [Clear Windows Event Logs](/techniques/T1685/005)) <small style="color:#929393">(v1.5)</small>
* Disable Windows Event Logging (revoked by Disable or Modify Tools: [Disable or Modify Windows Event Log](/techniques/T1685/001)) <small style="color:#929393">(v1.4)</small>
* Disable or Modify Cloud Firewall (revoked by Disable or Modify System Firewall: [Cloud Firewall](/techniques/T1686/001)) <small style="color:#929393">(v1.3)</small>
* Disable or Modify Cloud Logs (revoked by Disable or Modify Tools: [Disable or Modify Cloud Log](/techniques/T1685/002)) <small style="color:#929393">(v2.1)</small>
* Disable or Modify Linux Audit System (revoked by Disable or Modify Tools: [Disable or Modify Linux Audit System Log](/techniques/T1685/004)) <small style="color:#929393">(v1.0)</small>
* Disable or Modify Network Device Firewall (revoked by Disable or Modify System Firewall: [Network Device Firewall](/techniques/T1686/002)) <small style="color:#929393">(v1.0)</small>
* Disable or Modify System Firewall (revoked by [Disable or Modify System Firewall](/techniques/T1686)) <small style="color:#929393">(v1.3)</small>
* Disable or Modify Tools (revoked by [Disable or Modify Tools](/techniques/T1685)) <small style="color:#929393">(v1.7)</small>
* Downgrade Attack (revoked by [Downgrade Attack](/techniques/T1689)) <small style="color:#929393">(v1.3)</small>
* Email Spoofing (revoked by Social Engineering: [Email Spoofing](/techniques/T1684/002)) <small style="color:#929393">(v1.1)</small>
* Impair Command History Logging (revoked by [Prevent Command History Logging](/techniques/T1690)) <small style="color:#929393">(v2.3)</small>
* Impair Defenses (revoked by [Disable or Modify Tools](/techniques/T1685)) <small style="color:#929393">(v1.7)</small>
* Impersonation (revoked by Social Engineering: [Impersonation](/techniques/T1684/001)) <small style="color:#929393">(v1.1)</small>
* Indicator Blocking (revoked by [Disable or Modify Tools](/techniques/T1685)) <small style="color:#929393">(v1.5)</small>
* Safe Mode Boot (revoked by [Safe Mode Boot](/techniques/T1688)) <small style="color:#929393">(v1.1)</small>
* Spoof Security Alerting (revoked by Disable or Modify Tools: [Modify or Spoof Tool UI](/techniques/T1685/003)) <small style="color:#929393">(v1.0)</small>

### Mobile

#### Minor Version Changes

* [Phishing](/techniques/T1660) <small style="color:#929393">(v1.1&#8594;v1.2)</small>

### ICS

#### New Techniques

* [Block Communications](/techniques/T1695) <small style="color:#929393">(v1.0)</small>
* Block Communications: [Ethernet](/techniques/T1695/002) <small style="color:#929393">(v1.0)</small>
* Block Communications: [Serial COM](/techniques/T1695/001) <small style="color:#929393">(v1.0)</small>
* Block Communications: [Wi-Fi](/techniques/T1695/003) <small style="color:#929393">(v1.0)</small>
* [Block Operational Technology Message](/techniques/T1691) <small style="color:#929393">(v1.0)</small>
* Block Operational Technology Message: [Command Message](/techniques/T1691/001) <small style="color:#929393">(v1.0)</small>
* Block Operational Technology Message: [Reporting Message](/techniques/T1691/002) <small style="color:#929393">(v1.0)</small>
* [Insecure Credentials](/techniques/T1694) <small style="color:#929393">(v1.0)</small>
* Insecure Credentials: [Default Credentials](/techniques/T1694/001) <small style="color:#929393">(v1.0)</small>
* Insecure Credentials: [Hardcoded Credentials](/techniques/T1694/002) <small style="color:#929393">(v1.0)</small>
* [Modify Firmware](/techniques/T1693) <small style="color:#929393">(v1.0)</small>
* Modify Firmware: [Module Firmware](/techniques/T1693/002) <small style="color:#929393">(v1.0)</small>
* Modify Firmware: [System Firmware](/techniques/T1693/001) <small style="color:#929393">(v1.0)</small>
* Program Download: [Download All](/techniques/T0843/001) <small style="color:#929393">(v1.0)</small>
* Program Download: [Online Edit](/techniques/T0843/002) <small style="color:#929393">(v1.0)</small>
* Program Download: [Program Append](/techniques/T0843/003) <small style="color:#929393">(v1.0)</small>
* Project File Infection: [Siemens Project File Format](/techniques/T0873/001) <small style="color:#929393">(v1.0)</small>
* Remote System Discovery: [Broadcast Discovery](/techniques/T0846/002) <small style="color:#929393">(v1.0)</small>
* Remote System Discovery: [Multicast Discovery](/techniques/T0846/003) <small style="color:#929393">(v1.0)</small>
* Remote System Discovery: [Port Scan](/techniques/T0846/001) <small style="color:#929393">(v1.0)</small>
* [Unauthorized Message](/techniques/T1692) <small style="color:#929393">(v1.0)</small>
* Unauthorized Message: [Command Message](/techniques/T1692/001) <small style="color:#929393">(v1.0)</small>
* Unauthorized Message: [Reporting Message](/techniques/T1692/002) <small style="color:#929393">(v1.0)</small>

#### Minor Version Changes

* [Project File Infection](/techniques/T0873) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Patches

* [Remote System Discovery](/techniques/T0846) <small style="color:#929393">(v1.1)</small>

#### Revocations

* Block Command Message (revoked by Block Operational Technology Message: [Command Message](/techniques/T1691/001)) <small style="color:#929393">(v1.1)</small>
* Block Reporting Message (revoked by Block Operational Technology Message: [Reporting Message](/techniques/T1691/002)) <small style="color:#929393">(v1.0)</small>
* Block Serial COM (revoked by Block Communications: [Serial COM](/techniques/T1695/001)) <small style="color:#929393">(v1.1)</small>
* Default Credentials (revoked by Insecure Credentials: [Default Credentials](/techniques/T1694/001)) <small style="color:#929393">(v1.0)</small>
* Hardcoded Credentials (revoked by Insecure Credentials: [Hardcoded Credentials](/techniques/T1694/002)) <small style="color:#929393">(v1.0)</small>
* Module Firmware (revoked by Modify Firmware: [Module Firmware](/techniques/T1693/002)) <small style="color:#929393">(v1.1)</small>
* Spoof Reporting Message (revoked by Unauthorized Message: [Reporting Message](/techniques/T1692/002)) <small style="color:#929393">(v1.2)</small>
* System Firmware (revoked by Modify Firmware: [System Firmware](/techniques/T1693/001)) <small style="color:#929393">(v1.1)</small>
* Unauthorized Command Message (revoked by Unauthorized Message: [Command Message](/techniques/T1692/001)) <small style="color:#929393">(v1.2)</small>

## Software

### Enterprise

#### New Software

* [ANELLDR](/software/S9027) <small style="color:#929393">(v1.0)</small>
* [AshTag](/software/S9031) <small style="color:#929393">(v1.0)</small>
* [BRICKSTORM](/software/S9015) <small style="color:#929393">(v1.0)</small>
* [BRUSHFIRE](/software/S9011) <small style="color:#929393">(v1.0)</small>
* [Caminho](/software/S9016) <small style="color:#929393">(v1.0)</small>
* [Crocodilus](/software/S9004) <small style="color:#929393">(v1.0)</small>
* [DCRAT](/software/S9017) <small style="color:#929393">(v1.0)</small>
* [DOWNIISSA](/software/S9021) <small style="color:#929393">(v1.0)</small>
* [DRYHOOK](/software/S9013) <small style="color:#929393">(v1.0)</small>
* [Diskpart](/software/S9002) <small style="color:#929393">(v1.0)</small>
* [DynoWiper](/software/S9038) <small style="color:#929393">(v1.0)</small>
* [Fooder](/software/S9033) <small style="color:#929393">(v1.0)</small>
* [GlassWorm](/software/S9010) <small style="color:#929393">(v1.0)</small>
* [HTTPTroy](/software/S9007) <small style="color:#929393">(v1.0)</small>
* [HeartCrypt](/software/S9018) <small style="color:#929393">(v1.0)</small>
* [HiddenFace](/software/S9023) <small style="color:#929393">(v1.0)</small>
* [IronWind](/software/S9029) <small style="color:#929393">(v1.0)</small>
* [LAMEHUG](/software/S9035) <small style="color:#929393">(v1.0)</small>
* [LODEINFO](/software/S9020) <small style="color:#929393">(v1.0)</small>
* [LP-Notes](/software/S9036) <small style="color:#929393">(v1.0)</small>
* [LazyWiper](/software/S9039) <small style="color:#929393">(v1.0)</small>
* [MirrorStealer](/software/S9022) <small style="color:#929393">(v1.0)</small>
* [MuddyViper](/software/S9032) <small style="color:#929393">(v1.0)</small>
* [NOOPLDR](/software/S9025) <small style="color:#929393">(v1.0)</small>
* [PHASEJAM](/software/S9014) <small style="color:#929393">(v1.0)</small>
* [PHPsert](/software/S9028) <small style="color:#929393">(v1.0)</small>
* [PureCrypter](/software/S9019) <small style="color:#929393">(v1.0)</small>
* [ROAMINGHOUSE](/software/S9026) <small style="color:#929393">(v1.0)</small>
* [RustyWater](/software/S9037) <small style="color:#929393">(v1.0)</small>
* [SPAWNCHIMERA](/software/S9024) <small style="color:#929393">(v1.0)</small>
* [SameCoin](/software/S9030) <small style="color:#929393">(v1.0)</small>
* [Shai-Hulud](/software/S9008) <small style="color:#929393">(v1.0)</small>
* [SystemBC](/software/S9001) <small style="color:#929393">(v1.0)</small>
* [TRAILBLAZE](/software/S9012) <small style="color:#929393">(v1.0)</small>
* [TruffleHog](/software/S9009) <small style="color:#929393">(v1.0)</small>
* [Tsundere Botnet](/software/S9034) <small style="color:#929393">(v1.0)</small>
* [evilginx2](/software/S9003) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [Qilin](/software/S1242) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [UPPERCUT](/software/S0275) <small style="color:#929393">(v1.1&#8594;v2.0)</small>

#### Minor Version Changes

* [Arp](/software/S0099) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [BITSAdmin](/software/S0190) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Cobalt Strike](/software/S0154) <small style="color:#929393">(v1.13&#8594;v1.14)</small>
* [FRP](/software/S1144) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Havoc](/software/S1229) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Industroyer](/software/S0604) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [LockerGoga](/software/S0372) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Mimikatz](/software/S0002) <small style="color:#929393">(v1.10&#8594;v1.11)</small>
* [Net](/software/S0039) <small style="color:#929393">(v2.7&#8594;v2.8)</small>
* [Nltest](/software/S0359) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [PUBLOAD](/software/S1228) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Ping](/software/S0097) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [PlugX](/software/S0013) <small style="color:#929393">(v3.2&#8594;v3.3)</small>
* [QuasarRAT](/software/S0262) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Rclone](/software/S1040) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Remcos](/software/S0332) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Rubeus](/software/S1071) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [ShrinkLocker](/software/S1178) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Stuxnet](/software/S0603) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [TONESHELL](/software/S1239) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Tasklist](/software/S0057) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Tor](/software/S0183) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Wevtutil](/software/S0645) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [certutil](/software/S0160) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
* [ipconfig](/software/S0100) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [njRAT](/software/S0385) <small style="color:#929393">(v1.6&#8594;v1.7)</small>
* [sqlmap](/software/S0225) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Patches

* [HyperStack](/software/S0537) <small style="color:#929393">(v1.0)</small>
* [MCMD](/software/S0500) <small style="color:#929393">(v1.1)</small>
* [OSInfo](/software/S0165) <small style="color:#929393">(v1.1)</small>
* [RemoteCMD](/software/S0166) <small style="color:#929393">(v1.1)</small>
* [SDBbot](/software/S0461) <small style="color:#929393">(v2.1)</small>

### Mobile

#### New Software

* [Crocodilus](/software/S9004) <small style="color:#929393">(v1.0)</small>
* [DocSwap](/software/S9005) <small style="color:#929393">(v1.0)</small>
* [SameCoin](/software/S9030) <small style="color:#929393">(v1.0)</small>
* [VajraSpy](/software/S9006) <small style="color:#929393">(v1.0)</small>

### ICS

#### Minor Version Changes

* [INCONTROLLER](/software/S1045) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Industroyer](/software/S0604) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [LockerGoga](/software/S0372) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [PLC-Blaster](/software/S1006) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Stuxnet](/software/S0603) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Triton](/software/S1009) <small style="color:#929393">(v1.1&#8594;v1.2)</small>

## Groups

### Enterprise

#### New Groups

* [MirrorFace](/groups/G1054) <small style="color:#929393">(v1.0)</small>
* [VOID MANTICORE](/groups/G1055) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [APT-C-36](/groups/G0099) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [MuddyWater](/groups/G0069) <small style="color:#929393">(v6.0&#8594;v7.0)</small>
* [WIRTE](/groups/G0090) <small style="color:#929393">(v2.0&#8594;v3.0)</small>

#### Minor Version Changes

* [APT28](/groups/G0007) <small style="color:#929393">(v5.2&#8594;v5.3)</small>
* [Gamaredon Group](/groups/G0047) <small style="color:#929393">(v3.2&#8594;v3.3)</small>
* [Kimsuky](/groups/G0094) <small style="color:#929393">(v5.1&#8594;v5.2)</small>
* [Wizard Spider](/groups/G0102) <small style="color:#929393">(v4.0&#8594;v4.1)</small>

#### Patches

* [APT29](/groups/G0016) <small style="color:#929393">(v6.2)</small>
* [APT3](/groups/G0022) <small style="color:#929393">(v1.4)</small>
* [APT38](/groups/G0082) <small style="color:#929393">(v3.1)</small>
* [FIN13](/groups/G1016) <small style="color:#929393">(v1.0)</small>
* [Mustang Panda](/groups/G0129) <small style="color:#929393">(v3.0)</small>
* [TA505](/groups/G0092) <small style="color:#929393">(v3.0)</small>
* [Threat Group-1314](/groups/G0028) <small style="color:#929393">(v1.1)</small>
* [Turla](/groups/G0010) <small style="color:#929393">(v5.1)</small>
* [Volt Typhoon](/groups/G1017) <small style="color:#929393">(v2.0)</small>

### Mobile

#### New Groups

* [Kimsuky](/groups/G0094) <small style="color:#eb6635">(v5.2)</small>
* [MONSOON](/groups/G0042) <small style="color:#929393">(v1.0)</small>
* [Patchwork](/groups/G0040) <small style="color:#eb6635">(v1.6)</small>
* [Stolen Pencil](/groups/G0086) <small style="color:#eb6635">(v1.1)</small>
* [WIRTE](/groups/G0090) <small style="color:#eb6635">(v3.0)</small>

#### Major Version Changes

* [MuddyWater](/groups/G0069) <small style="color:#929393">(v6.0&#8594;v7.0)</small>

#### Minor Version Changes

* [APT28](/groups/G0007) <small style="color:#929393">(v5.2&#8594;v5.3)</small>

### ICS

#### Minor Version Changes

* [Wizard Spider](/groups/G0102) <small style="color:#929393">(v4.0&#8594;v4.1)</small>

#### Patches

* [APT38](/groups/G0082) <small style="color:#929393">(v3.1)</small>

## Campaigns

### Enterprise

#### New Campaigns

* [2025 Poland Wiper Attacks](/campaigns/C0063) <small style="color:#929393">(v1.0)</small>
* [Anthropic AI-orchestrated Campaign](/campaigns/C0062) <small style="color:#929393">(v1.0)</small>
* [Operation AkaiRyū](/campaigns/C0060) <small style="color:#929393">(v1.0)</small>
* [Operation Digital Eye](/campaigns/C0061) <small style="color:#929393">(v1.0)</small>

#### Minor Version Changes

* [HomeLand Justice](/campaigns/C0038) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Triton Safety Instrumented System Attack](/campaigns/C0030) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Patches

* [SharePoint ToolShell Exploitation](/campaigns/C0058) <small style="color:#929393">(v1.0)</small>
* [Water Curupira Pikabot Distribution](/campaigns/C0037) <small style="color:#929393">(v1.0)</small>

### ICS

#### New Campaigns

* [2025 Poland Wiper Attacks](/campaigns/C0063) <small style="color:#929393">(v1.0)</small>

#### Minor Version Changes

* [Triton Safety Instrumented System Attack](/campaigns/C0030) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

## Assets

### ICS

#### Minor Version Changes

* [Application Server](/assets/A0008) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Control Server](/assets/A0007) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Data Historian](/assets/A0006) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Distributed Control System (DCS) Controller](/assets/A0017) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Field I/O](/assets/A0013) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Human-Machine Interface (HMI)](/assets/A0002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Intelligent Electronic Device (IED)](/assets/A0005) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Jump Host](/assets/A0012) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Programmable Automation Controller (PAC)](/assets/A0018) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Programmable Logic Controller (PLC)](/assets/A0003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Remote Terminal Unit (RTU)](/assets/A0004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Safety Controller](/assets/A0010) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Virtual Private Network (VPN) Server](/assets/A0011) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Workstation](/assets/A0001) <small style="color:#929393">(v2.0&#8594;v2.1)</small>

## Mitigations

### Enterprise

#### Patches

* [Network Segmentation](/mitigations/M1030) <small style="color:#929393">(v1.2)</small>

### ICS

#### Minor Version Changes

* [Access Management](/mitigations/M0801) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Audit](/mitigations/M0947) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Authorization Enforcement](/mitigations/M0800) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Boot Integrity](/mitigations/M0946) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Code Signing](/mitigations/M0945) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Communication Authenticity](/mitigations/M0802) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Encrypt Network Traffic](/mitigations/M0808) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Encrypt Sensitive Information](/mitigations/M0941) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Filter Network Traffic](/mitigations/M0937) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Human User Authentication](/mitigations/M0804) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Network Allowlists](/mitigations/M0807) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Network Intrusion Prevention](/mitigations/M0931) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Network Segmentation](/mitigations/M0930) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Out-of-Band Communications Channel](/mitigations/M0810) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Restrict File and Directory Permissions](/mitigations/M0922) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Software Process and Device Authentication](/mitigations/M0813) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Static Network Configuration](/mitigations/M0814) <small style="color:#929393">(v1.1&#8594;v1.2)</small>

## Data Components

### Enterprise

#### Major Version Changes

* Application Log Content <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* Cloud Service Enumeration <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* File Access <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* File Creation <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* File Deletion <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* File Modification <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* Module Load <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* Process Access <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* Scheduled Job Creation <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* User Account Authentication <small style="color:#929393">(v2.0&#8594;v3.0)</small>

#### Minor Version Changes

* Command Execution <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Driver Metadata <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* File Metadata <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Group Enumeration <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Host Status <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Instance Modification <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Network Connection Creation <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Network Traffic Content <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Network Traffic Flow <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* OS API Execution <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Process Creation <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Process Metadata <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Service Modification <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* User Account Metadata <small style="color:#929393">(v2.0&#8594;v2.1)</small>

#### Patches

* Service Metadata <small style="color:#929393">(v2.0)</small>
* Windows Registry Key Modification <small style="color:#929393">(v2.0)</small>

### Mobile

#### New Data Components

* Application Log Content <small style="color:#eb6635">(v3.0)</small>
* Application State <small style="color:#929393">(v1.0)</small>
* Cloud Service Enumeration <small style="color:#eb6635">(v3.0)</small>
* File Access <small style="color:#eb6635">(v3.0)</small>
* File Creation <small style="color:#eb6635">(v3.0)</small>
* File Deletion <small style="color:#eb6635">(v3.0)</small>
* File Metadata <small style="color:#eb6635">(v2.1)</small>
* File Modification <small style="color:#eb6635">(v3.0)</small>
* Module Load <small style="color:#eb6635">(v3.0)</small>
* Process Access <small style="color:#eb6635">(v3.0)</small>
* Scheduled Job Creation <small style="color:#eb6635">(v3.0)</small>
* User Account Authentication <small style="color:#eb6635">(v3.0)</small>

#### Minor Version Changes

* API Calls <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Application Assets <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Application Permission <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Command Execution <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Host Status <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Network Communication <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Network Connection Creation <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Network Traffic Content <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Network Traffic Flow <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* OS API Execution <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Process Creation <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Process Metadata <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Protected Configuration <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* System Notifications <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* System Settings <small style="color:#929393">(v2.0&#8594;v2.1)</small>

### ICS

#### Major Version Changes

* Application Log Content <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* File Access <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* File Creation <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* File Deletion <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* File Modification <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* Module Load <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* Scheduled Job Creation <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* User Account Authentication <small style="color:#929393">(v2.0&#8594;v3.0)</small>

#### Minor Version Changes

* Command Execution <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* File Metadata <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Network Connection Creation <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Network Traffic Content <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Network Traffic Flow <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* OS API Execution <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Process Creation <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Process History/Live Data <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Process Metadata <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Process/Event Alarm <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Service Modification <small style="color:#929393">(v2.0&#8594;v2.1)</small>

#### Patches

* Service Metadata <small style="color:#929393">(v2.0)</small>
* Windows Registry Key Modification <small style="color:#929393">(v2.0)</small>

## Detection Strategies

### Enterprise

#### New Detection Strategies

* [Detect Social Engineering](/detectionstrategies/DET0899) <small style="color:#929393">(v1.0)</small>
* [Detect Windows Firewall](/detectionstrategies/DET0901) <small style="color:#929393">(v1.0)</small>
* [Detection Strategy for Invisible Unicode](/detectionstrategies/DET0920) <small style="color:#929393">(v1.0)</small>
* [Detection of Audio-Visual Content](/detectionstrategies/DET0918) <small style="color:#929393">(v1.0)</small>
* [Detection of Defense Impairment](/detectionstrategies/DET0900) <small style="color:#929393">(v1.0)</small>
* [Detection of Generate Content](/detectionstrategies/DET0916) <small style="color:#929393">(v1.0)</small>
* [Detection of Query Public AI Services](/detectionstrategies/DET0919) <small style="color:#929393">(v1.0)</small>
* [Detection of Written Content](/detectionstrategies/DET0917) <small style="color:#929393">(v1.0)</small>

#### Minor Version Changes

* [Detection of Defense Impairment through Disabled or Modified Tools across OS Platforms.](/detectionstrategies/DET0497) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Patches

* [Detect Disabled Windows Event Log](/detectionstrategies/DET0187) <small style="color:#929393">(v1.0)</small>
* [Detection Strategy for Defense Impairment via Prevent Command History Logging across OS platforms.](/detectionstrategies/DET0563) <small style="color:#929393">(v1.0)</small>
* [Detection Strategy for Disable or Modify Cloud Log](/detectionstrategies/DET0289) <small style="color:#929393">(v1.0)</small>
* [Detection Strategy for Disable or Modify Linux Audit System Log](/detectionstrategies/DET0062) <small style="color:#929393">(v1.0)</small>
* [Detection Strategy for Exploitation for Stealth](/detectionstrategies/DET0595) <small style="color:#929393">(v1.0)</small>
* [Detection for Spoofing Tool UI across OS Platforms](/detectionstrategies/DET0311) <small style="color:#929393">(v1.0)</small>
* [Detection of Remote Service Session Hijacking for RDP.](/detectionstrategies/DET0588) <small style="color:#929393">(v1.0)</small>
* [Detection of Unauthorized Network Firewall Rule Modification](/detectionstrategies/DET0306) <small style="color:#929393">(v1.0)</small>

#### Deprecations

* [Detection Strategy for Impair Defenses Across Platforms](/detectionstrategies/DET0317) <small style="color:#929393">(v1.0)</small>
* [Detection Strategy for Impair Defenses Indicator Blocking](/detectionstrategies/DET0239) <small style="color:#929393">(v1.0)</small>

### ICS

#### New Detection Strategies

* [Detection of Block Communications](/detectionstrategies/DET0910) <small style="color:#929393">(v1.0)</small>
* [Detection of Block Ethernet](/detectionstrategies/DET0911) <small style="color:#929393">(v1.0)</small>
* [Detection of Block Operational Technology Message](/detectionstrategies/DET0903) <small style="color:#929393">(v1.0)</small>
* [Detection of Block Wi-Fi](/detectionstrategies/DET0912) <small style="color:#929393">(v1.0)</small>
* [Detection of Broadcast Discovery](/detectionstrategies/DET0908) <small style="color:#929393">(v1.0)</small>
* [Detection of Firmware Modification](/detectionstrategies/DET0904) <small style="color:#929393">(v1.0)</small>
* [Detection of Insecure Credentials](/detectionstrategies/DET0905) <small style="color:#929393">(v1.0)</small>
* [Detection of Multicast Discovery](/detectionstrategies/DET0909) <small style="color:#929393">(v1.0)</small>
* [Detection of Online Edit](/detectionstrategies/DET0915) <small style="color:#929393">(v1.0)</small>
* [Detection of Port Scan](/detectionstrategies/DET0907) <small style="color:#929393">(v1.0)</small>
* [Detection of Program Append](/detectionstrategies/DET0914) <small style="color:#929393">(v1.0)</small>
* [Detection of Program Download All](/detectionstrategies/DET0913) <small style="color:#929393">(v1.0)</small>
* [Detection of Siemens Project File Format Infection](/detectionstrategies/DET0906) <small style="color:#929393">(v1.0)</small>
* [Detection of Unauthorized Message](/detectionstrategies/DET0902) <small style="color:#929393">(v1.0)</small>

## Analytics

### Enterprise

#### New Analytics

* [Analytic 2033](/detectionstrategies/DET0899#AN2033) <small style="color:#929393">(v1.0)</small>
* [Analytic 2034](/detectionstrategies/DET0899#AN2034) <small style="color:#929393">(v1.0)</small>
* [Analytic 2035](/detectionstrategies/DET0899#AN2035) <small style="color:#929393">(v1.0)</small>
* [Analytic 2036](/detectionstrategies/DET0899#AN2036) <small style="color:#929393">(v1.0)</small>
* [Analytic 2037](/detectionstrategies/DET0899#AN2037) <small style="color:#929393">(v1.0)</small>
* [Analytic 2038](/detectionstrategies/DET0900#AN2038) <small style="color:#929393">(v1.0)</small>
* [Analytic 2039](/detectionstrategies/DET0900#AN2039) <small style="color:#929393">(v1.0)</small>
* [Analytic 2040](/detectionstrategies/DET0900#AN2040) <small style="color:#929393">(v1.0)</small>
* [Analytic 2041](/detectionstrategies/DET0900#AN2041) <small style="color:#929393">(v1.0)</small>
* [Analytic 2042](/detectionstrategies/DET0900#AN2042) <small style="color:#929393">(v1.0)</small>
* [Analytic 2043](/detectionstrategies/DET0901#AN2043) <small style="color:#929393">(v1.0)</small>
* [Analytic 2044](/detectionstrategies/DET0497#AN2044) <small style="color:#929393">(v1.0)</small>
* [Analytic 2059](/detectionstrategies/DET0916#AN2059) <small style="color:#929393">(v1.0)</small>
* [Analytic 2060](/detectionstrategies/DET0917#AN2060) <small style="color:#929393">(v1.0)</small>
* [Analytic 2061](/detectionstrategies/DET0918#AN2061) <small style="color:#929393">(v1.0)</small>
* [Analytic 2062](/detectionstrategies/DET0919#AN2062) <small style="color:#929393">(v1.0)</small>
* [Analytic 2063](/detectionstrategies/DET0920#AN2063) <small style="color:#929393">(v1.0)</small>
* [Analytic 2064](/detectionstrategies/DET0920#AN2064) <small style="color:#929393">(v1.0)</small>
* [Analytic 2065](/detectionstrategies/DET0920#AN2065) <small style="color:#929393">(v1.0)</small>

#### Minor Version Changes

* [Analytic 1370](/detectionstrategies/DET0497#AN1370) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1371](/detectionstrategies/DET0497#AN1371) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1372](/detectionstrategies/DET0497#AN1372) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1373](/detectionstrategies/DET0497#AN1373) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1374](/detectionstrategies/DET0497#AN1374) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1452](/detectionstrategies/DET0525#AN1452) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1612](/detectionstrategies/DET0587#AN1612) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1614](/detectionstrategies/DET0587#AN1614) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Patches

* [Analytic 0551](/detectionstrategies/DET0192#AN0551) <small style="color:#929393">(v1.0)</small>
* [Analytic 1615](/detectionstrategies/DET0587#AN1615) <small style="color:#929393">(v1.0)</small>
* [Analytic 1616](/detectionstrategies/DET0587#AN1616) <small style="color:#929393">(v1.0)</small>
* [Analytic 1617](/detectionstrategies/DET0587#AN1617) <small style="color:#929393">(v1.0)</small>
* [Analytic 1940](/detectionstrategies/DET0808#AN1940) <small style="color:#929393">(v1.0)</small>
* [Analytic 1959](/detectionstrategies/DET0827#AN1959) <small style="color:#929393">(v1.0)</small>
* [Analytic 2026](/detectionstrategies/DET0894#AN2026) <small style="color:#929393">(v1.0)</small>

### Mobile

#### Major Version Changes

* [Analytic 1650](/detectionstrategies/DET0602#AN1650) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Analytic 1693](/detectionstrategies/DET0626#AN1693) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Analytic 1694](/detectionstrategies/DET0626#AN1694) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Analytic 1708](/detectionstrategies/DET0635#AN1708) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Analytic 1774](/detectionstrategies/DET0674#AN1774) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Analytic 1782](/detectionstrategies/DET0679#AN1782) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Analytic 1795](/detectionstrategies/DET0686#AN1795) <small style="color:#929393">(v1.0&#8594;v2.0)</small>

#### Minor Version Changes

* [Analytic 1644](/detectionstrategies/DET0598#AN1644) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1645](/detectionstrategies/DET0599#AN1645) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1646](/detectionstrategies/DET0600#AN1646) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1647](/detectionstrategies/DET0600#AN1647) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1648](/detectionstrategies/DET0601#AN1648) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1649](/detectionstrategies/DET0601#AN1649) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1652](/detectionstrategies/DET0603#AN1652) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1653](/detectionstrategies/DET0604#AN1653) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1654](/detectionstrategies/DET0604#AN1654) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1657](/detectionstrategies/DET0607#AN1657) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1658](/detectionstrategies/DET0607#AN1658) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1663](/detectionstrategies/DET0610#AN1663) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1664](/detectionstrategies/DET0610#AN1664) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1665](/detectionstrategies/DET0611#AN1665) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1666](/detectionstrategies/DET0612#AN1666) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1669](/detectionstrategies/DET0614#AN1669) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1670](/detectionstrategies/DET0614#AN1670) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1675](/detectionstrategies/DET0617#AN1675) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1676](/detectionstrategies/DET0617#AN1676) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1677](/detectionstrategies/DET0618#AN1677) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1678](/detectionstrategies/DET0618#AN1678) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1681](/detectionstrategies/DET0620#AN1681) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1682](/detectionstrategies/DET0620#AN1682) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1683](/detectionstrategies/DET0621#AN1683) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1684](/detectionstrategies/DET0621#AN1684) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1697](/detectionstrategies/DET0628#AN1697) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1698](/detectionstrategies/DET0628#AN1698) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1701](/detectionstrategies/DET0630#AN1701) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1702](/detectionstrategies/DET0631#AN1702) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1706](/detectionstrategies/DET0634#AN1706) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1710](/detectionstrategies/DET0636#AN1710) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1711](/detectionstrategies/DET0637#AN1711) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1712](/detectionstrategies/DET0638#AN1712) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1713](/detectionstrategies/DET0639#AN1713) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1714](/detectionstrategies/DET0639#AN1714) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1715](/detectionstrategies/DET0640#AN1715) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1716](/detectionstrategies/DET0641#AN1716) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1717](/detectionstrategies/DET0641#AN1717) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1718](/detectionstrategies/DET0642#AN1718) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1719](/detectionstrategies/DET0643#AN1719) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1720](/detectionstrategies/DET0643#AN1720) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1721](/detectionstrategies/DET0644#AN1721) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1722](/detectionstrategies/DET0644#AN1722) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1723](/detectionstrategies/DET0645#AN1723) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1724](/detectionstrategies/DET0645#AN1724) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1725](/detectionstrategies/DET0646#AN1725) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1726](/detectionstrategies/DET0646#AN1726) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1727](/detectionstrategies/DET0647#AN1727) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1728](/detectionstrategies/DET0648#AN1728) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1729](/detectionstrategies/DET0648#AN1729) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1730](/detectionstrategies/DET0649#AN1730) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1731](/detectionstrategies/DET0650#AN1731) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1732](/detectionstrategies/DET0650#AN1732) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1733](/detectionstrategies/DET0651#AN1733) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1734](/detectionstrategies/DET0651#AN1734) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1737](/detectionstrategies/DET0653#AN1737) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1738](/detectionstrategies/DET0653#AN1738) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1739](/detectionstrategies/DET0654#AN1739) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1740](/detectionstrategies/DET0654#AN1740) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1741](/detectionstrategies/DET0655#AN1741) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1742](/detectionstrategies/DET0655#AN1742) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1743](/detectionstrategies/DET0656#AN1743) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1747](/detectionstrategies/DET0658#AN1747) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1748](/detectionstrategies/DET0658#AN1748) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1751](/detectionstrategies/DET0661#AN1751) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1752](/detectionstrategies/DET0661#AN1752) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1753](/detectionstrategies/DET0662#AN1753) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1754](/detectionstrategies/DET0662#AN1754) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1755](/detectionstrategies/DET0663#AN1755) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1756](/detectionstrategies/DET0663#AN1756) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1758](/detectionstrategies/DET0665#AN1758) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1759](/detectionstrategies/DET0665#AN1759) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1762](/detectionstrategies/DET0667#AN1762) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1763](/detectionstrategies/DET0667#AN1763) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1764](/detectionstrategies/DET0668#AN1764) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1767](/detectionstrategies/DET0670#AN1767) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1768](/detectionstrategies/DET0670#AN1768) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1770](/detectionstrategies/DET0672#AN1770) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1771](/detectionstrategies/DET0672#AN1771) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1772](/detectionstrategies/DET0673#AN1772) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1773](/detectionstrategies/DET0673#AN1773) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1776](/detectionstrategies/DET0675#AN1776) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1777](/detectionstrategies/DET0675#AN1777) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1778](/detectionstrategies/DET0676#AN1778) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1779](/detectionstrategies/DET0676#AN1779) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1780](/detectionstrategies/DET0677#AN1780) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1781](/detectionstrategies/DET0678#AN1781) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1784](/detectionstrategies/DET0680#AN1784) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1785](/detectionstrategies/DET0680#AN1785) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1788](/detectionstrategies/DET0682#AN1788) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1789](/detectionstrategies/DET0682#AN1789) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1793](/detectionstrategies/DET0685#AN1793) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1794](/detectionstrategies/DET0685#AN1794) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1797](/detectionstrategies/DET0687#AN1797) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1800](/detectionstrategies/DET0689#AN1800) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1801](/detectionstrategies/DET0690#AN1801) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1802](/detectionstrategies/DET0691#AN1802) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1803](/detectionstrategies/DET0691#AN1803) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1804](/detectionstrategies/DET0692#AN1804) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1805](/detectionstrategies/DET0692#AN1805) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1806](/detectionstrategies/DET0693#AN1806) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1807](/detectionstrategies/DET0694#AN1807) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1808](/detectionstrategies/DET0695#AN1808) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1809](/detectionstrategies/DET0695#AN1809) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1812](/detectionstrategies/DET0697#AN1812) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1815](/detectionstrategies/DET0699#AN1815) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1816](/detectionstrategies/DET0700#AN1816) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1817](/detectionstrategies/DET0700#AN1817) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1820](/detectionstrategies/DET0702#AN1820) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1821](/detectionstrategies/DET0702#AN1821) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1822](/detectionstrategies/DET0703#AN1822) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1823](/detectionstrategies/DET0704#AN1823) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1824](/detectionstrategies/DET0704#AN1824) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1825](/detectionstrategies/DET0705#AN1825) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1826](/detectionstrategies/DET0705#AN1826) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1827](/detectionstrategies/DET0706#AN1827) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1828](/detectionstrategies/DET0706#AN1828) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1829](/detectionstrategies/DET0707#AN1829) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1830](/detectionstrategies/DET0707#AN1830) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1837](/detectionstrategies/DET0711#AN1837) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1840](/detectionstrategies/DET0713#AN1840) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1841](/detectionstrategies/DET0713#AN1841) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1842](/detectionstrategies/DET0714#AN1842) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1847](/detectionstrategies/DET0717#AN1847) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1848](/detectionstrategies/DET0718#AN1848) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1849](/detectionstrategies/DET0718#AN1849) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1850](/detectionstrategies/DET0719#AN1850) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1851](/detectionstrategies/DET0720#AN1851) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1852](/detectionstrategies/DET0720#AN1852) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1853](/detectionstrategies/DET0721#AN1853) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1854](/detectionstrategies/DET0721#AN1854) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

### ICS

#### New Analytics

* [Analytic 2045](/detectionstrategies/DET0902#AN2045) <small style="color:#929393">(v1.0)</small>
* [Analytic 2046](/detectionstrategies/DET0903#AN2046) <small style="color:#929393">(v1.0)</small>
* [Analytic 2047](/detectionstrategies/DET0904#AN2047) <small style="color:#929393">(v1.0)</small>
* [Analytic 2048](/detectionstrategies/DET0905#AN2048) <small style="color:#929393">(v1.0)</small>
* [Analytic 2049](/detectionstrategies/DET0906#AN2049) <small style="color:#929393">(v1.0)</small>
* [Analytic 2050](/detectionstrategies/DET0907#AN2050) <small style="color:#929393">(v1.0)</small>
* [Analytic 2051](/detectionstrategies/DET0908#AN2051) <small style="color:#929393">(v1.0)</small>
* [Analytic 2052](/detectionstrategies/DET0909#AN2052) <small style="color:#929393">(v1.0)</small>
* [Analytic 2053](/detectionstrategies/DET0910#AN2053) <small style="color:#929393">(v1.0)</small>
* [Analytic 2054](/detectionstrategies/DET0911#AN2054) <small style="color:#929393">(v1.0)</small>
* [Analytic 2055](/detectionstrategies/DET0912#AN2055) <small style="color:#929393">(v1.0)</small>
* [Analytic 2056](/detectionstrategies/DET0913#AN2056) <small style="color:#929393">(v1.0)</small>
* [Analytic 2057](/detectionstrategies/DET0914#AN2057) <small style="color:#929393">(v1.0)</small>
* [Analytic 2058](/detectionstrategies/DET0915#AN2058) <small style="color:#929393">(v1.0)</small>

#### Minor Version Changes

* [Analytic 1864](/detectionstrategies/DET0731#AN1864) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Analytic 1922](/detectionstrategies/DET0790#AN1922) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

#### Patches

* [Analytic 1879](/detectionstrategies/DET0746#AN1879) <small style="color:#929393">(v1.0)</small>

## Contributors to this release

* Alberto Garcia
* Alex Soler, AttackIQ
* Alex Wong
* Arad Inbar, Fidelis Security
* Arun Seelagan, CISA
* Austin Clark, @c2defense
* Blake Strom, Microsoft Threat Intelligence
* Caio Silva
* Cian Heasley
* Contributor: Dominik Breitenbacher, ESET
* Daniel Feichter, @VirtualAllocEx, Infosec Tirol
* Dominik Breitenbacher, ESET
* Dongwook Kim, KISA
* Dragos Threat Intelligence
* Emile Kenning, Sophos
* Expel
* Gal Singer, @galsinger29, Team Nautilus Aqua Security
* Gilberto Pérez
* Gordon Long, LegioX/Zoom, asaurusrex
* Ibrahim Ali Khan
* Jaesang Oh, KC7 Foundation
* Janantha Marasinghe
* Joe Gumke, U.S. Bank
* Jorell Magtibay, National Australia Bank Limited
* Kiyohito Yamamoto, RedLark, NTT Communications
* Kyaw Pyiyt Htet (@KyawPyiytHtet)
* Lab52 by S2 Grupo
* Liran Ravich, CardinalOps
* Lucas Heiligenstein
* Manikantan Srinivasan, NEC Corporation India
* Marco Pedrinazzi, @pedrinazziM, InTheCyber
* Matt Snyder, VMware
* Mayuresh Dani, Qualys
* Menachem Goldstein
* Nathaniel Quist, Palo Alto Networks
* Nay Myo Hlaing (Ethan), DBS Bank
* Patrick Mkhael (aka Pinguino)
* Pawel Partyka, Microsoft Threat Intelligence
* Pedro Rodriguez
* Pooja Natarajan, NEC Corporation India
* Prasad Somasamudram, McAfee
* Prasanth Sadanala, Cigna Information Protection (CIP) - Threat Response Engineering Team
* Rich Rafferty (NR Labs)
* Rob Smith
* Sarathkumar Rajendran, Microsoft Defender365
* Sekhar Sarukkai, McAfee
* Serhii Melnyk
* SeungYoul Yoo, AhnLab
* Stijn Geerts
* Syed Ummar Farooqh, McAfee
* Taewoo Lee, KISA
* Takemasa Kamatani , NEC Corporation
* Tim (Wadhwa-)Brown
* Tommaso Tosi, @tosto92, InTheCyber
* Uriel Kosayev
* Vikas Singh, Sophos
* Víctor Alba
* Wai Linn Oo, Kernellix Co.,Ltd.
* Wietze Beukema @Wietze
* Yusuke Kubo, RedLark, NTT Communications
* Ziv Karliner, @ziv_kr, Team Nautilus Aqua Security
