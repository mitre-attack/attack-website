Title: Updates - October 2024
Date: October 2024
Category: Cyber Threat Intelligence
Authors: Adam Pennington
Template: resources/update-post
url: /resources/updates/updates-october-2024
save_as: resources/updates/updates-october-2024/index.html

| Version | Start Date | End Date | Data | Changelogs |
|:--------|:-----------|:---------|:-----|:-----------|
| [ATT&CK v16](/versions/v16) | October 31, 2024 | April 21, 2025 | [v16.0 on MITRE/CTI](https://github.com/mitre/cti/releases/tag/ATT%26CK-v16.0) <br> [v16.1 on MITRE/CTI](https://github.com/mitre/cti/releases/tag/ATT%26CK-v16.1) | 15.1 - 16.0 [Details](/docs/changelogs/v15.1-v16.0/changelog-detailed.html) ([JSON](/docs/changelogs/v15.1-v16.0/changelog.json)) <br> 16.0 - 16.1 [Details](/docs/changelogs/v16.0-v16.1/changelog-detailed.html) ([JSON](/docs/changelogs/v16.0-v16.1/changelog.json)) |

The October 2024 (v16) ATT&CK release updates Techniques, Groups, Campaigns and Software for Enterprise.

The biggest changes in ATT&CK v16 are a refactoring of Cloud platforms to better reflect real-world adversary activity along with improvements to platform descriptions, a dramatic expansion in the number of techniques with detection notes and analytics, and continued improvements to coverage of criminal threat actors. As a result of Cloud platform refactoring, the Azure AD, Office 365, and Google Workspace platforms have been removed from Enterprise ATT&CK and the [Identity Provider](/matrices/enterprise/cloud/identityprovider/) and [Office Suite](/matrices/enterprise/cloud/officesuite/) platforms have been added in their place. An [accompanying blog post](https://medium.com/mitre-attack/attack-v16-561c76af94cf) describes these changes as well as additional improvements across Enterprise ATT&CK's various platforms.

This release also includes a [human-readable detailed changelog](/docs/changelogs/v15.1-v16.0/changelog-detailed.html) showing more specifically what changed in updated ATT&CK objects, and a [machine-readable JSON changelog](/docs/changelogs/v15.1-v16.0/changelog.json), whose format is described in [ATT&CK's Github](https://github.com/mitre-attack/mitreattack-python/blob/master/mitreattack/diffStix/README.md).

This version of ATT&CK contains 844 Pieces of Software, 186 Groups, and 42 Campaigns
Broken out by domain:

* Enterprise: 14 Tactics, 203 Techniques, 453 Sub-Techniques, 159 Groups, 710 Pieces of Software, 34 Campaigns, 44 Mitigations, and 37 Data Sources
* Mobile: 12 Tactics, 73 Techniques, 46 Sub-Techniques, 13 Groups, 112 Pieces of Software, 2 Campaigns, 13 Mitigations, and 6 Data Sources
* ICS: 12 Tactics, 83 Techniques, 0 Sub-Techniques, 14 Groups, 22 Pieces of Software, 6 Campaigns, 52 Mitigations, 14 Assets, and 17 Data Sources



## Release Notes Terminology

* New: ATT&CK objects which are only present in the new release.
* Major version changes: ATT&CK objects that have a major version change. (e.g. 1.0 → 2.0)
* Minor version changes: ATT&CK objects that have a minor version change. (e.g. 1.0 → 1.1)
* Other version changes: ATT&CK objects that have a version change of any other kind. (e.g. 1.0 → 1.2)
* Patches: ATT&CK objects that have been patched while keeping the version the same. (e.g., 1.0 → 1.0 but something immaterial like a typo, a URL, or some metadata was fixed)
* Revocations: ATT&CK objects which are revoked by a different object.
* Deprecations: ATT&CK objects which are deprecated and no longer in use, and not replaced.
* Deletions: ATT&CK objects which are no longer found in the STIX data.


## Techniques

### Enterprise

#### New Techniques

* Account Manipulation: [Additional Local or Domain Groups](/techniques/T1098/007) <small style="color:#929393">(v1.0)</small>
* Adversary-in-the-Middle: [Evil Twin](/techniques/T1557/004) <small style="color:#929393">(v1.0)</small>
* Application Layer Protocol: [Publish/Subscribe Protocols](/techniques/T1071/005) <small style="color:#929393">(v1.0)</small>
* Command and Scripting Interpreter: [Lua](/techniques/T1059/011) <small style="color:#929393">(v1.0)</small>
* Data Destruction: [Lifecycle-Triggered Deletion](/techniques/T1485/001) <small style="color:#929393">(v1.0)</small>
* Data from Information Repositories: [Customer Relationship Management Software](/techniques/T1213/004) <small style="color:#929393">(v1.0)</small>
* Data from Information Repositories: [Messaging Applications](/techniques/T1213/005) <small style="color:#929393">(v1.0)</small>
* Event Triggered Execution: [Udev Rules](/techniques/T1546/017) <small style="color:#929393">(v1.0)</small>
* Execution Guardrails: [Mutual Exclusion](/techniques/T1480/002) <small style="color:#929393">(v1.0)</small>
* Indicator Removal: [Relocate Malware](/techniques/T1070/010) <small style="color:#929393">(v1.0)</small>
* Masquerading: [Masquerade Account Name](/techniques/T1036/010) <small style="color:#929393">(v1.0)</small>
* [Modify Cloud Resource Hierarchy](/techniques/T1666) <small style="color:#929393">(v1.0)</small>
* Obfuscated Files or Information: [Polymorphic Code](/techniques/T1027/014) <small style="color:#929393">(v1.0)</small>
* Resource Hijacking: [Bandwidth Hijacking](/techniques/T1496/002) <small style="color:#929393">(v1.0)</small>
* Resource Hijacking: [Cloud Service Hijacking](/techniques/T1496/004) <small style="color:#929393">(v1.0)</small>
* Resource Hijacking: [Compute Hijacking](/techniques/T1496/001) <small style="color:#929393">(v1.0)</small>
* Resource Hijacking: [SMS Pumping](/techniques/T1496/003) <small style="color:#929393">(v1.0)</small>
* Steal or Forge Kerberos Tickets: [Ccache Files](/techniques/T1558/005) <small style="color:#929393">(v1.0)</small>
* Trusted Developer Utilities Proxy Execution: [ClickOnce](/techniques/T1127/002) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* Data Obfuscation: [Protocol or Service Impersonation](/techniques/T1001/003) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Modify Cloud Compute Infrastructure: [Modify Cloud Compute Configurations](/techniques/T1578/005) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* Obfuscated Files or Information: [Fileless Storage](/techniques/T1027/011) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Resource Hijacking](/techniques/T1496) <small style="color:#929393">(v1.5&#8594;v2.0)</small>

#### Minor Version Changes

* [Abuse Elevation Control Mechanism](/techniques/T1548) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
    * [TCC Manipulation](/techniques/T1548/006) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Temporary Elevated Cloud Access](/techniques/T1548/005) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Account Access Removal](/techniques/T1531) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Account Discovery](/techniques/T1087) <small style="color:#929393">(v2.4&#8594;v2.5)</small>
    * [Cloud Account](/techniques/T1087/004) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [Email Account](/techniques/T1087/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Account Manipulation](/techniques/T1098) <small style="color:#929393">(v2.6&#8594;v2.7)</small>
    * [Additional Cloud Credentials](/techniques/T1098/001) <small style="color:#929393">(v2.7&#8594;v2.8)</small>
    * [Additional Cloud Roles](/techniques/T1098/003) <small style="color:#929393">(v2.4&#8594;v2.5)</small>
    * [Additional Email Delegate Permissions](/techniques/T1098/002) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
    * [Device Registration](/techniques/T1098/005) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Acquire Infrastructure: [Domains](/techniques/T1583/001) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* Acquire Infrastructure: [Serverless](/techniques/T1583/007) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Active Scanning: [Scanning IP Blocks](/techniques/T1595/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Application Layer Protocol](/techniques/T1071) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* [Automated Collection](/techniques/T1119) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Automated Exfiltration: [Traffic Duplication](/techniques/T1020/001) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Brute Force](/techniques/T1110) <small style="color:#929393">(v2.5&#8594;v2.6)</small>
    * [Credential Stuffing](/techniques/T1110/004) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
    * [Password Cracking](/techniques/T1110/002) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [Password Guessing](/techniques/T1110/001) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
    * [Password Spraying](/techniques/T1110/003) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
* [Cloud Service Dashboard](/techniques/T1538) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Cloud Service Discovery](/techniques/T1526) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Command and Scripting Interpreter](/techniques/T1059) <small style="color:#929393">(v2.4&#8594;v2.5)</small>
    * [Cloud API](/techniques/T1059/009) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [JavaScript](/techniques/T1059/007) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* Compromise Accounts: [Cloud Accounts](/techniques/T1586/003) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Compromise Host Software Binary](/techniques/T1554) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* Compromise Infrastructure: [Domains](/techniques/T1584/001) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* Compromise Infrastructure: [Serverless](/techniques/T1584/007) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Create Account](/techniques/T1136) <small style="color:#929393">(v2.4&#8594;v2.5)</small>
    * [Cloud Account](/techniques/T1136/003) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
* Credentials from Password Stores: [Credentials from Web Browsers](/techniques/T1555/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Credentials from Password Stores: [Password Managers](/techniques/T1555/005) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Data Destruction](/techniques/T1485) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* Data Manipulation: [Runtime Data Manipulation](/techniques/T1565/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Data from Cloud Storage](/techniques/T1530) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* [Data from Information Repositories](/techniques/T1213) <small style="color:#929393">(v3.3&#8594;v3.4)</small>
    * [Code Repositories](/techniques/T1213/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Confluence](/techniques/T1213/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Sharepoint](/techniques/T1213/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Domain or Tenant Policy Modification](/techniques/T1484) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
    * [Trust Modification](/techniques/T1484/002) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Drive-by Compromise](/techniques/T1189) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
* Dynamic Resolution: [Domain Generation Algorithms](/techniques/T1568/002) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Email Collection](/techniques/T1114) <small style="color:#929393">(v2.5&#8594;v2.6)</small>
    * [Email Forwarding Rule](/techniques/T1114/003) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
    * [Remote Email Collection](/techniques/T1114/002) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Endpoint Denial of Service](/techniques/T1499) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Application Exhaustion Flood](/techniques/T1499/003) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [Application or System Exploitation](/techniques/T1499/004) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [Service Exhaustion Flood](/techniques/T1499/002) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Event Triggered Execution](/techniques/T1546) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Execution Guardrails](/techniques/T1480) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Exfiltration Over Alternative Protocol](/techniques/T1048) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Exfiltration Over Web Service](/techniques/T1567) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
    * [Exfiltration Over Webhook](/techniques/T1567/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Exploit Public-Facing Application](/techniques/T1190) <small style="color:#929393">(v2.5&#8594;v2.6)</small>
* [Exploitation for Credential Access](/techniques/T1212) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
* [Financial Theft](/techniques/T1657) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Forge Web Credentials](/techniques/T1606) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
    * [SAML Tokens](/techniques/T1606/002) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Gather Victim Host Information](/techniques/T1592) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Gather Victim Identity Information: [Credentials](/techniques/T1589/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Gather Victim Network Information: [DNS](/techniques/T1590/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Hide Artifacts](/techniques/T1564) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [Email Hiding Rules](/techniques/T1564/008) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* Hijack Execution Flow: [DLL Search Order Hijacking](/techniques/T1574/001) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Impair Defenses](/techniques/T1562) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
    * [Disable or Modify Cloud Firewall](/techniques/T1562/007) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [Disable or Modify Cloud Logs](/techniques/T1562/008) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [Impersonation](/techniques/T1656) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Indicator Removal](/techniques/T1070) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
    * [Clear Mailbox Data](/techniques/T1070/008) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Timestomp](/techniques/T1070/006) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Indirect Command Execution](/techniques/T1202) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Inhibit System Recovery](/techniques/T1490) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Input Capture](/techniques/T1056) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [Credential API Hooking](/techniques/T1056/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Inter-Process Communication](/techniques/T1559) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Internal Spearphishing](/techniques/T1534) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Log Enumeration](/techniques/T1654) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Modify Authentication Process](/techniques/T1556) <small style="color:#929393">(v2.4&#8594;v2.5)</small>
    * [Conditional Access Policies](/techniques/T1556/009) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Domain Controller Authentication](/techniques/T1556/001) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
    * [Hybrid Identity](/techniques/T1556/007) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Multi-Factor Authentication](/techniques/T1556/006) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [Password Filter DLL](/techniques/T1556/002) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
    * [Pluggable Authentication Modules](/techniques/T1556/003) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
    * [Reversible Encryption](/techniques/T1556/005) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Modify Cloud Compute Infrastructure: [Create Cloud Instance](/techniques/T1578/002) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Modify Cloud Compute Infrastructure: [Create Snapshot](/techniques/T1578/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Modify Cloud Compute Infrastructure: [Delete Cloud Instance](/techniques/T1578/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Multi-Factor Authentication Request Generation](/techniques/T1621) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Network Denial of Service](/techniques/T1498) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Direct Network Flood](/techniques/T1498/001) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
    * [Reflection Amplification](/techniques/T1498/002) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* OS Credential Dumping: [/etc/passwd and /etc/shadow](/techniques/T1003/008) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* OS Credential Dumping: [DCSync](/techniques/T1003/006) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* OS Credential Dumping: [LSA Secrets](/techniques/T1003/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* OS Credential Dumping: [LSASS Memory](/techniques/T1003/001) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* Obfuscated Files or Information: [Compile After Delivery](/techniques/T1027/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Office Application Startup](/techniques/T1137) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
    * [Add-ins](/techniques/T1137/006) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Office Template Macros](/techniques/T1137/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Office Test](/techniques/T1137/002) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [Outlook Forms](/techniques/T1137/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Outlook Home Page](/techniques/T1137/004) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Outlook Rules](/techniques/T1137/005) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Password Policy Discovery](/techniques/T1201) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
* [Permission Groups Discovery](/techniques/T1069) <small style="color:#929393">(v2.5&#8594;v2.6)</small>
    * [Cloud Groups](/techniques/T1069/003) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Phishing](/techniques/T1566) <small style="color:#929393">(v2.5&#8594;v2.6)</small>
    * [Spearphishing Link](/techniques/T1566/002) <small style="color:#929393">(v2.6&#8594;v2.7)</small>
    * [Spearphishing Voice](/techniques/T1566/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Process Injection: [ListPlanting](/techniques/T1055/015) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Proxy: [Multi-hop Proxy](/techniques/T1090/003) <small style="color:#929393">(v2.1&#8594;v2.2)</small>
* Remote Services: [Cloud Services](/techniques/T1021/007) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Scheduled Task/Job: [At](/techniques/T1053/002) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* Scheduled Task/Job: [Cron](/techniques/T1053/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* Scheduled Task/Job: [Scheduled Task](/techniques/T1053/005) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
* [Search Closed Sources](/techniques/T1597) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Search Victim-Owned Websites](/techniques/T1594) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* Server Software Component: [SQL Stored Procedures](/techniques/T1505/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Serverless Execution](/techniques/T1648) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Software Deployment Tools](/techniques/T1072) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* Stage Capabilities: [SEO Poisoning](/techniques/T1608/006) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Steal Application Access Token](/techniques/T1528) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Steal Web Session Cookie](/techniques/T1539) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Steal or Forge Authentication Certificates](/techniques/T1649) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Steal or Forge Kerberos Tickets](/techniques/T1558) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
    * [AS-REP Roasting](/techniques/T1558/004) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* System Binary Proxy Execution: [Rundll32](/techniques/T1218/011) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* [System Location Discovery](/techniques/T1614) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [System Services](/techniques/T1569) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
    * [Launchctl](/techniques/T1569/001) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Taint Shared Content](/techniques/T1080) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Transfer Data to Cloud Account](/techniques/T1537) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Trusted Relationship](/techniques/T1199) <small style="color:#929393">(v2.3&#8594;v2.4)</small>
* [Unsecured Credentials](/techniques/T1552) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
    * [Bash History](/techniques/T1552/003) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
    * [Chat Messages](/techniques/T1552/008) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Group Policy Preferences](/techniques/T1552/006) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
    * [Private Keys](/techniques/T1552/004) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Use Alternate Authentication Material](/techniques/T1550) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
    * [Application Access Token](/techniques/T1550/001) <small style="color:#929393">(v1.6&#8594;v1.7)</small>
    * [Web Session Cookie](/techniques/T1550/004) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [User Execution](/techniques/T1204) <small style="color:#929393">(v1.6&#8594;v1.7)</small>
    * [Malicious File](/techniques/T1204/002) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
    * [Malicious Link](/techniques/T1204/001) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Valid Accounts](/techniques/T1078) <small style="color:#929393">(v2.6&#8594;v2.7)</small>
    * [Cloud Accounts](/techniques/T1078/004) <small style="color:#929393">(v1.7&#8594;v1.8)</small>
    * [Default Accounts](/techniques/T1078/001) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [Web Service](/techniques/T1102) <small style="color:#929393">(v1.1&#8594;v1.2)</small>

#### Patches

* Account Discovery: [Domain Account](/techniques/T1087/002) <small style="color:#929393">(v1.2)</small>
* [Acquire Infrastructure](/techniques/T1583) <small style="color:#929393">(v1.4)</small>
    * [Malvertising](/techniques/T1583/008) <small style="color:#929393">(v1.0)</small>
    * [Virtual Private Server](/techniques/T1583/003) <small style="color:#929393">(v1.1)</small>
* Active Scanning: [Vulnerability Scanning](/techniques/T1595/002) <small style="color:#929393">(v1.0)</small>
* Adversary-in-the-Middle: [DHCP Spoofing](/techniques/T1557/003) <small style="color:#929393">(v1.1)</small>
* [Application Window Discovery](/techniques/T1010) <small style="color:#929393">(v1.3)</small>
* [Audio Capture](/techniques/T1123) <small style="color:#929393">(v1.0)</small>
* [Boot or Logon Autostart Execution](/techniques/T1547) <small style="color:#929393">(v1.2)</small>
    * [Kernel Modules and Extensions](/techniques/T1547/006) <small style="color:#929393">(v1.3)</small>
    * [Port Monitors](/techniques/T1547/010) <small style="color:#929393">(v1.2)</small>
    * [Registry Run Keys / Startup Folder](/techniques/T1547/001) <small style="color:#929393">(v2.0)</small>
    * [Shortcut Modification](/techniques/T1547/009) <small style="color:#929393">(v1.2)</small>
* [Browser Extensions](/techniques/T1176) <small style="color:#929393">(v1.3)</small>
* [Cloud Administration Command](/techniques/T1651) <small style="color:#929393">(v2.0)</small>
* [Cloud Infrastructure Discovery](/techniques/T1580) <small style="color:#929393">(v1.3)</small>
* Command and Scripting Interpreter: [AppleScript](/techniques/T1059/002) <small style="color:#929393">(v1.2)</small>
* Command and Scripting Interpreter: [PowerShell](/techniques/T1059/001) <small style="color:#929393">(v1.4)</small>
* Command and Scripting Interpreter: [Unix Shell](/techniques/T1059/004) <small style="color:#929393">(v1.2)</small>
* Command and Scripting Interpreter: [Visual Basic](/techniques/T1059/005) <small style="color:#929393">(v1.4)</small>
* Command and Scripting Interpreter: [Windows Command Shell](/techniques/T1059/003) <small style="color:#929393">(v1.4)</small>
* [Compromise Infrastructure](/techniques/T1584) <small style="color:#929393">(v1.5)</small>
    * [Network Devices](/techniques/T1584/008) <small style="color:#929393">(v1.0)</small>
    * [Web Services](/techniques/T1584/006) <small style="color:#929393">(v1.2)</small>
* [Container Administration Command](/techniques/T1609) <small style="color:#929393">(v1.2)</small>
* [Credentials from Password Stores](/techniques/T1555) <small style="color:#929393">(v1.2)</small>
    * [Cloud Secrets Management Stores](/techniques/T1555/006) <small style="color:#929393">(v1.0)</small>
    * [Keychain](/techniques/T1555/001) <small style="color:#929393">(v1.1)</small>
    * [Securityd Memory](/techniques/T1555/002) <small style="color:#929393">(v1.2)</small>
    * [Windows Credential Manager](/techniques/T1555/004) <small style="color:#929393">(v1.1)</small>
* Data Manipulation: [Stored Data Manipulation](/techniques/T1565/001) <small style="color:#929393">(v1.1)</small>
* Data Manipulation: [Transmitted Data Manipulation](/techniques/T1565/002) <small style="color:#929393">(v1.1)</small>
* [Data Obfuscation](/techniques/T1001) <small style="color:#929393">(v1.1)</small>
* [Data Staged](/techniques/T1074) <small style="color:#929393">(v1.4)</small>
    * [Local Data Staging](/techniques/T1074/001) <small style="color:#929393">(v1.1)</small>
    * [Remote Data Staging](/techniques/T1074/002) <small style="color:#929393">(v1.1)</small>
* [Data from Removable Media](/techniques/T1025) <small style="color:#929393">(v1.2)</small>
* [Deploy Container](/techniques/T1610) <small style="color:#929393">(v1.3)</small>
* [Develop Capabilities](/techniques/T1587) <small style="color:#929393">(v1.1)</small>
* Disk Wipe: [Disk Structure Wipe](/techniques/T1561/002) <small style="color:#929393">(v1.1)</small>
* Domain or Tenant Policy Modification: [Group Policy Modification](/techniques/T1484/001) <small style="color:#929393">(v1.0)</small>
* Event Triggered Execution: [Change Default File Association](/techniques/T1546/001) <small style="color:#929393">(v1.0)</small>
* Event Triggered Execution: [Unix Shell Configuration Modification](/techniques/T1546/004) <small style="color:#929393">(v2.1)</small>
* [Exploitation for Client Execution](/techniques/T1203) <small style="color:#929393">(v1.4)</small>
* [Forced Authentication](/techniques/T1187) <small style="color:#929393">(v1.3)</small>
* [Gather Victim Identity Information](/techniques/T1589) <small style="color:#929393">(v1.3)</small>
    * [Employee Names](/techniques/T1589/003) <small style="color:#929393">(v1.0)</small>
* Hide Artifacts: [NTFS File Attributes](/techniques/T1564/004) <small style="color:#929393">(v1.1)</small>
* Hijack Execution Flow: [Path Interception by Search Order Hijacking](/techniques/T1574/008) <small style="color:#929393">(v1.0)</small>
* Hijack Execution Flow: [Services Registry Permissions Weakness](/techniques/T1574/011) <small style="color:#929393">(v1.1)</small>
* Impair Defenses: [Disable or Modify System Firewall](/techniques/T1562/004) <small style="color:#929393">(v1.2)</small>
* Impair Defenses: [Spoof Security Alerting](/techniques/T1562/011) <small style="color:#929393">(v1.0)</small>
* Indicator Removal: [File Deletion](/techniques/T1070/004) <small style="color:#929393">(v1.1)</small>
* Input Capture: [Web Portal Capture](/techniques/T1056/003) <small style="color:#929393">(v1.0)</small>
* Inter-Process Communication: [XPC Services](/techniques/T1559/003) <small style="color:#929393">(v1.0)</small>
* [Masquerading](/techniques/T1036) <small style="color:#929393">(v1.7)</small>
    * [Match Legitimate Name or Location](/techniques/T1036/005) <small style="color:#929393">(v1.2)</small>
    * [Rename System Utilities](/techniques/T1036/003) <small style="color:#929393">(v1.1)</small>
* [Modify Cloud Compute Infrastructure](/techniques/T1578) <small style="color:#929393">(v1.2)</small>
* [Multi-Factor Authentication Interception](/techniques/T1111) <small style="color:#929393">(v2.1)</small>
* [Native API](/techniques/T1106) <small style="color:#929393">(v2.2)</small>
* [Network Sniffing](/techniques/T1040) <small style="color:#929393">(v1.6)</small>
* [Non-Standard Port](/techniques/T1571) <small style="color:#929393">(v1.1)</small>
* [OS Credential Dumping](/techniques/T1003) <small style="color:#929393">(v2.2)</small>
    * [Cached Domain Credentials](/techniques/T1003/005) <small style="color:#929393">(v1.1)</small>
    * [Proc Filesystem](/techniques/T1003/007) <small style="color:#929393">(v1.2)</small>
    * [Security Account Manager](/techniques/T1003/002) <small style="color:#929393">(v1.1)</small>
* Obfuscated Files or Information: [Command Obfuscation](/techniques/T1027/010) <small style="color:#929393">(v1.0)</small>
* Obfuscated Files or Information: [Encrypted/Encoded File](/techniques/T1027/013) <small style="color:#929393">(v1.0)</small>
* Obfuscated Files or Information: [HTML Smuggling](/techniques/T1027/006) <small style="color:#929393">(v1.1)</small>
* [Obtain Capabilities](/techniques/T1588) <small style="color:#929393">(v1.1)</small>
    * [Artificial Intelligence](/techniques/T1588/007) <small style="color:#929393">(v1.0)</small>
    * [Digital Certificates](/techniques/T1588/004) <small style="color:#929393">(v1.2)</small>
    * [Tool](/techniques/T1588/002) <small style="color:#929393">(v1.1)</small>
* Phishing: [Spearphishing Attachment](/techniques/T1566/001) <small style="color:#929393">(v2.2)</small>
* Phishing: [Spearphishing via Service](/techniques/T1566/003) <small style="color:#929393">(v2.0)</small>
* [Phishing for Information](/techniques/T1598) <small style="color:#929393">(v1.3)</small>
    * [Spearphishing Attachment](/techniques/T1598/002) <small style="color:#929393">(v1.1)</small>
    * [Spearphishing Link](/techniques/T1598/003) <small style="color:#929393">(v1.6)</small>
* [Power Settings](/techniques/T1653) <small style="color:#929393">(v1.0)</small>
* Process Injection: [Process Hollowing](/techniques/T1055/012) <small style="color:#929393">(v1.3)</small>
* [Protocol Tunneling](/techniques/T1572) <small style="color:#929393">(v1.0)</small>
* Remote Services: [VNC](/techniques/T1021/005) <small style="color:#929393">(v1.1)</small>
* Remote Services: [Windows Remote Management](/techniques/T1021/006) <small style="color:#929393">(v1.2)</small>
* [Scheduled Task/Job](/techniques/T1053) <small style="color:#929393">(v2.3)</small>
    * [Container Orchestration Job](/techniques/T1053/007) <small style="color:#929393">(v1.3)</small>
    * [Systemd Timers](/techniques/T1053/006) <small style="color:#929393">(v1.2)</small>
* [Search Open Websites/Domains](/techniques/T1593) <small style="color:#929393">(v1.1)</small>
    * [Search Engines](/techniques/T1593/002) <small style="color:#929393">(v1.0)</small>
* Server Software Component: [Terminal Services DLL](/techniques/T1505/005) <small style="color:#929393">(v1.0)</small>
* [Service Stop](/techniques/T1489) <small style="color:#929393">(v1.2)</small>
* Stage Capabilities: [Link Target](/techniques/T1608/005) <small style="color:#929393">(v1.4)</small>
* Stage Capabilities: [Upload Malware](/techniques/T1608/001) <small style="color:#929393">(v1.2)</small>
* Steal or Forge Kerberos Tickets: [Kerberoasting](/techniques/T1558/003) <small style="color:#929393">(v1.2)</small>
* [Supply Chain Compromise](/techniques/T1195) <small style="color:#929393">(v1.6)</small>
* System Binary Proxy Execution: [CMSTP](/techniques/T1218/003) <small style="color:#929393">(v2.1)</small>
* [System Information Discovery](/techniques/T1082) <small style="color:#929393">(v2.5)</small>
* System Script Proxy Execution: [SyncAppvPublishingServer](/techniques/T1216/002) <small style="color:#929393">(v1.0)</small>
* System Services: [Service Execution](/techniques/T1569/002) <small style="color:#929393">(v1.2)</small>
* Unsecured Credentials: [Cloud Instance Metadata API](/techniques/T1552/005) <small style="color:#929393">(v1.4)</small>
* Unsecured Credentials: [Container API](/techniques/T1552/007) <small style="color:#929393">(v1.2)</small>
* Unsecured Credentials: [Credentials In Files](/techniques/T1552/001) <small style="color:#929393">(v1.2)</small>
* Unsecured Credentials: [Credentials in Registry](/techniques/T1552/002) <small style="color:#929393">(v1.1)</small>
* Use Alternate Authentication Material: [Pass the Ticket](/techniques/T1550/003) <small style="color:#929393">(v1.1)</small>
* Valid Accounts: [Local Accounts](/techniques/T1078/003) <small style="color:#929393">(v1.4)</small>
* [Virtualization/Sandbox Evasion](/techniques/T1497) <small style="color:#929393">(v1.3)</small>
    * [System Checks](/techniques/T1497/001) <small style="color:#929393">(v2.2)</small>
    * [Time Based Evasion](/techniques/T1497/003) <small style="color:#929393">(v1.2)</small>
    * [User Activity Based Checks](/techniques/T1497/002) <small style="color:#929393">(v1.1)</small>
* [Windows Management Instrumentation](/techniques/T1047) <small style="color:#929393">(v1.5)</small>
* [XSL Script Processing](/techniques/T1220) <small style="color:#929393">(v1.2)</small>

### Mobile

#### Patches

* [Clipboard Data](/techniques/T1414) <small style="color:#929393">(v3.1)</small>
* Hide Artifacts: [Suppress Application Icon](/techniques/T1628/001) <small style="color:#929393">(v1.1)</small>
* Input Capture: [GUI Input Capture](/techniques/T1417/002) <small style="color:#929393">(v1.1)</small>

### ICS

#### Patches

* [Denial of Service](/techniques/T0814) <small style="color:#929393">(v1.1)</small>

## Software

### Enterprise

#### New Software

* [Apostle](/software/S1133) <small style="color:#929393">(v1.0)</small>
* [BFG Agonizer](/software/S1136) <small style="color:#929393">(v1.0)</small>
* [BPFDoor](/software/S1161) <small style="color:#929393">(v1.0)</small>
* [CHIMNEYSWEEP](/software/S1149) <small style="color:#929393">(v1.0)</small>
* [Covenant](/software/S1155) <small style="color:#929393">(v1.0)</small>
* [Cuckoo Stealer](/software/S1153) <small style="color:#929393">(v1.0)</small>
* [DEADWOOD](/software/S1134) <small style="color:#929393">(v1.0)</small>
* [DUSTPAN](/software/S1158) <small style="color:#929393">(v1.0)</small>
* [DUSTTRAP](/software/S1159) <small style="color:#929393">(v1.0)</small>
* [FRP](/software/S1144) <small style="color:#929393">(v1.0)</small>
* [Gootloader](/software/S1138) <small style="color:#929393">(v1.0)</small>
* [IMAPLoader](/software/S1152) <small style="color:#929393">(v1.0)</small>
* [INC Ransomware](/software/S1139) <small style="color:#929393">(v1.0)</small>
* [IPsec Helper](/software/S1132) <small style="color:#929393">(v1.0)</small>
* [Latrodectus](/software/S1160) <small style="color:#929393">(v1.0)</small>
* [LunarLoader](/software/S1143) <small style="color:#929393">(v1.0)</small>
* [LunarMail](/software/S1142) <small style="color:#929393">(v1.0)</small>
* [LunarWeb](/software/S1141) <small style="color:#929393">(v1.0)</small>
* [Manjusaka](/software/S1156) <small style="color:#929393">(v1.0)</small>
* [MgBot](/software/S1146) <small style="color:#929393">(v1.0)</small>
* [Moneybird](/software/S1137) <small style="color:#929393">(v1.0)</small>
* [MultiLayer Wiper](/software/S1135) <small style="color:#929393">(v1.0)</small>
* [NPPSPY](/software/S1131) <small style="color:#929393">(v1.0)</small>
* [Nightdoor](/software/S1147) <small style="color:#929393">(v1.0)</small>
* [Pikabot](/software/S1145) <small style="color:#929393">(v1.0)</small>
* [Playcrypt](/software/S1162) <small style="color:#929393">(v1.0)</small>
* [ROADSWEEP](/software/S1150) <small style="color:#929393">(v1.0)</small>
* [Raccoon Stealer](/software/S1148) <small style="color:#929393">(v1.0)</small>
* [Raspberry Robin](/software/S1130) <small style="color:#929393">(v1.0)</small>
* [Spica](/software/S1140) <small style="color:#929393">(v1.0)</small>
* [VPNFilter](/software/S1010) <small style="color:#eb6635">(v2.0)</small>
* [VersaMem](/software/S1154) <small style="color:#929393">(v1.0)</small>
* [ZeroCleare](/software/S1151) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [BabyShark](/software/S0414) <small style="color:#929393">(v1.2&#8594;v2.0)</small>
* [Ebury](/software/S0377) <small style="color:#929393">(v1.3&#8594;v2.0)</small>
* [MacMa](/software/S1016) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [OutSteel](/software/S1017) <small style="color:#929393">(v1.0&#8594;v2.0)</small>
* [Saint Bot](/software/S1018) <small style="color:#929393">(v1.0&#8594;v2.0)</small>

#### Minor Version Changes

* [ASPXSpy](/software/S0073) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [AdFind](/software/S0552) <small style="color:#929393">(v1.4&#8594;v1.5)</small>
* [Amadey](/software/S1025) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [BloodHound](/software/S0521) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
* [Brute Ratel C4](/software/S1063) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Bumblebee](/software/S1039) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Cobalt Strike](/software/S0154) <small style="color:#929393">(v1.12&#8594;v1.13)</small>
* [Cyclops Blink](/software/S0687) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Emotet](/software/S0367) <small style="color:#929393">(v1.5&#8594;v1.6)</small>
* [Empire](/software/S0363) <small style="color:#929393">(v1.7&#8594;v1.8)</small>
* [EvilBunny](/software/S0396) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [GLOOXMAIL](/software/S0026) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Gold Dragon](/software/S0249) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [IcedID](/software/S0483) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [Impacket](/software/S0357) <small style="color:#929393">(v1.6&#8594;v1.7)</small>
* [Nltest](/software/S0359) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [PoetRAT](/software/S0428) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* [PsExec](/software/S0029) <small style="color:#929393">(v1.6&#8594;v1.7)</small>
* [QakBot](/software/S0650) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [QuasarRAT](/software/S0262) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [RawDisk](/software/S0364) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Remsec](/software/S0125) <small style="color:#929393">(v1.3&#8594;v1.4)</small>
* [SILENTTRINITY](/software/S0692) <small style="color:#929393">(v1.0&#8594;v1.1)</small>
* [Wevtutil](/software/S0645) <small style="color:#929393">(v1.1&#8594;v1.2)</small>
* [ftp](/software/S0095) <small style="color:#929393">(v2.0&#8594;v2.1)</small>
* [gh0st RAT](/software/S0032) <small style="color:#929393">(v3.2&#8594;v3.3)</small>

#### Patches

* [AADInternals](/software/S0677) <small style="color:#929393">(v1.2)</small>
* [Astaroth](/software/S0373) <small style="color:#929393">(v2.3)</small>
* [BLACKCOFFEE](/software/S0069) <small style="color:#929393">(v1.1)</small>
* [ChChes](/software/S0144) <small style="color:#929393">(v1.1)</small>
* [CreepyDrive](/software/S1023) <small style="color:#929393">(v1.0)</small>
* [DDKONG](/software/S0255) <small style="color:#929393">(v1.0)</small>
* [DarkGate](/software/S1111) <small style="color:#929393">(v1.0)</small>
* [DarkWatchman](/software/S0673) <small style="color:#929393">(v1.2)</small>
* [FinFisher](/software/S0182) <small style="color:#929393">(v1.4)</small>
* [Flagpro](/software/S0696) <small style="color:#929393">(v1.0)</small>
* [GrimAgent](/software/S0632) <small style="color:#929393">(v1.1)</small>
* [HAPPYWORK](/software/S0214) <small style="color:#929393">(v1.0)</small>
* [Janicab](/software/S0163) <small style="color:#929393">(v1.1)</small>
* [Koadic](/software/S0250) <small style="color:#929393">(v2.0)</small>
* [MailSniper](/software/S0413) <small style="color:#929393">(v1.1)</small>
* [Micropsia](/software/S0339) <small style="color:#929393">(v1.2)</small>
* [Mimikatz](/software/S0002) <small style="color:#929393">(v1.9)</small>
* [Miner-C](/software/S0133) <small style="color:#929393">(v1.0)</small>
* [NanoCore](/software/S0336) <small style="color:#929393">(v1.1)</small>
* [PoisonIvy](/software/S0012) <small style="color:#929393">(v2.2)</small>
* [ROADTools](/software/S0684) <small style="color:#929393">(v1.0)</small>
* [RedLeaves](/software/S0153) <small style="color:#929393">(v1.2)</small>
* [Ruler](/software/S0358) <small style="color:#929393">(v1.1)</small>
* [SHUTTERSPEED](/software/S0217) <small style="color:#929393">(v1.0)</small>
* [SLOTHFULMEDIA](/software/S0533) <small style="color:#929393">(v1.0)</small>
* [Ursnif](/software/S0386) <small style="color:#929393">(v1.5)</small>
* [WINERACK](/software/S0219) <small style="color:#929393">(v1.0)</small>
* [Windows Credential Editor](/software/S0005) <small style="color:#929393">(v1.1)</small>
* [Winexe](/software/S0191) <small style="color:#929393">(v1.0)</small>

### Mobile

#### Patches

* [Anubis](/software/S0422) <small style="color:#929393">(v1.3)</small>
* [Exobot](/software/S0522) <small style="color:#929393">(v1.0)</small>
* [FinFisher](/software/S0182) <small style="color:#929393">(v1.4)</small>

#### Deprecations

* [Marcher](/software/S0317) <small style="color:#929393">(v1.0)</small>

### ICS

#### New Software

* [Fuxnet](/software/S1157) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [VPNFilter](/software/S1010) <small style="color:#929393">(v1.1&#8594;v2.0)</small>

## Groups

### Enterprise

#### New Groups

* [Agrius](/groups/G1030) <small style="color:#929393">(v1.0)</small>
* [Daggerfly](/groups/G1034) <small style="color:#929393">(v1.0)</small>
* [INC Ransom](/groups/G1032) <small style="color:#929393">(v1.0)</small>
* [Moonstone Sleet](/groups/G1036) <small style="color:#929393">(v1.0)</small>
* [Play](/groups/G1040) <small style="color:#929393">(v1.0)</small>
* [RedCurl](/groups/G1039) <small style="color:#929393">(v1.0)</small>
* [Saint Bear](/groups/G1031) <small style="color:#929393">(v1.0)</small>
* [Star Blizzard](/groups/G1033) <small style="color:#929393">(v1.0)</small>
* [TA577](/groups/G1037) <small style="color:#929393">(v1.0)</small>
* [TA578](/groups/G1038) <small style="color:#929393">(v1.0)</small>
* [Winter Vivern](/groups/G1035) <small style="color:#929393">(v1.0)</small>

#### Major Version Changes

* [Aquatic Panda](/groups/G0143) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [CURIUM](/groups/G1012) <small style="color:#929393">(v2.0&#8594;v3.0)</small>
* [Ember Bear](/groups/G1003) <small style="color:#929393">(v1.1&#8594;v2.0)</small>
* [Kimsuky](/groups/G0094) <small style="color:#929393">(v4.0&#8594;v5.0)</small>
* [Volt Typhoon](/groups/G1017) <small style="color:#929393">(v1.1&#8594;v2.0)</small>

#### Minor Version Changes

* [APT28](/groups/G0007) <small style="color:#929393">(v5.0&#8594;v5.1)</small>
* [APT29](/groups/G0016) <small style="color:#929393">(v6.0&#8594;v6.1)</small>
* [APT41](/groups/G0096) <small style="color:#929393">(v4.0&#8594;v4.1)</small>
* [Blue Mockingbird](/groups/G0108) <small style="color:#929393">(v1.2&#8594;v1.3)</small>
* [Gamaredon Group](/groups/G0047) <small style="color:#929393">(v3.0&#8594;v3.1)</small>
* [HEXANE](/groups/G1001) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* [Indrik Spider](/groups/G0119) <small style="color:#929393">(v4.0&#8594;v4.1)</small>
* [Magic Hound](/groups/G0059) <small style="color:#929393">(v6.0&#8594;v6.1)</small>
* [MuddyWater](/groups/G0069) <small style="color:#929393">(v5.0&#8594;v5.1)</small>
* [OilRig](/groups/G0049) <small style="color:#929393">(v4.0&#8594;v4.1)</small>
* [Sandworm Team](/groups/G0034) <small style="color:#929393">(v4.0&#8594;v4.1)</small>
* [Turla](/groups/G0010) <small style="color:#929393">(v5.0&#8594;v5.1)</small>
* [ZIRCONIUM](/groups/G0128) <small style="color:#929393">(v2.0&#8594;v2.1)</small>

#### Patches

* [APT17](/groups/G0025) <small style="color:#929393">(v1.1)</small>
* [APT3](/groups/G0022) <small style="color:#929393">(v1.4)</small>
* [APT38](/groups/G0082) <small style="color:#929393">(v3.0)</small>
* [Akira](/groups/G1024) <small style="color:#929393">(v1.0)</small>
* [Andariel](/groups/G0138) <small style="color:#929393">(v2.0)</small>
* [Chimera](/groups/G0114) <small style="color:#929393">(v2.2)</small>
* [Earth Lusca](/groups/G1006) <small style="color:#929393">(v2.0)</small>
* [TeamTNT](/groups/G0139) <small style="color:#929393">(v1.3)</small>
* [menuPass](/groups/G0045) <small style="color:#929393">(v3.0)</small>

### Mobile

#### Minor Version Changes

* [APT28](/groups/G0007) <small style="color:#929393">(v5.0&#8594;v5.1)</small>
* [Sandworm Team](/groups/G0034) <small style="color:#929393">(v4.0&#8594;v4.1)</small>

#### Patches

* [Earth Lusca](/groups/G1006) <small style="color:#929393">(v2.0)</small>

### ICS

#### Minor Version Changes

* [HEXANE](/groups/G1001) <small style="color:#929393">(v2.2&#8594;v2.3)</small>
* [OilRig](/groups/G0049) <small style="color:#929393">(v4.0&#8594;v4.1)</small>
* [Sandworm Team](/groups/G0034) <small style="color:#929393">(v4.0&#8594;v4.1)</small>

#### Patches

* [APT38](/groups/G0082) <small style="color:#929393">(v3.0)</small>

## Campaigns

### Enterprise

#### New Campaigns

* [APT41 DUST](/campaigns/C0040) <small style="color:#929393">(v1.0)</small>
* [HomeLand Justice](/campaigns/C0038) <small style="color:#929393">(v1.0)</small>
* [KV Botnet Activity](/campaigns/C0035) <small style="color:#929393">(v1.0)</small>
* [Pikabot Distribution February 2024](/campaigns/C0036) <small style="color:#929393">(v1.0)</small>
* [Versa Director Zero Day Exploitation](/campaigns/C0039) <small style="color:#929393">(v1.0)</small>
* [Water Curupira Pikabot Distribution](/campaigns/C0037) <small style="color:#929393">(v1.0)</small>

#### Minor Version Changes

* [SolarWinds Compromise](/campaigns/C0024) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

## Mitigations

### Enterprise

#### New Mitigations

* [Out-of-Band Communications Channel](/mitigations/M1060) <small style="color:#929393">(v1.0)</small>

#### Minor Version Changes

* [Active Directory Configuration](/mitigations/M1015) <small style="color:#929393">(v1.1&#8594;v1.2)</small>

#### Patches

* [Audit](/mitigations/M1047) <small style="color:#929393">(v1.2)</small>
* [Credential Access Protection](/mitigations/M1043) <small style="color:#929393">(v1.1)</small>
* [Execution Prevention](/mitigations/M1038) <small style="color:#929393">(v1.2)</small>
* [Filter Network Traffic](/mitigations/M1037) <small style="color:#929393">(v1.1)</small>
* [Limit Software Installation](/mitigations/M1033) <small style="color:#929393">(v1.0)</small>
* [Network Intrusion Prevention](/mitigations/M1031) <small style="color:#929393">(v1.0)</small>
* [Privileged Account Management](/mitigations/M1026) <small style="color:#929393">(v1.1)</small>
* [User Training](/mitigations/M1017) <small style="color:#929393">(v1.2)</small>

#### Minor Version Changes

* [Software Process and Device Authentication](/mitigations/M0813) <small style="color:#929393">(v1.0&#8594;v1.1)</small>

## Data Sources

### Enterprise

#### Patches

* [Active Directory](/datasources/DS0026) <small style="color:#929393">(v1.0)</small>
* [Application Log](/datasources/DS0015) <small style="color:#929393">(v1.0)</small>
* [Cloud Service](/datasources/DS0025) <small style="color:#929393">(v1.0)</small>
* [Firewall](/datasources/DS0018) <small style="color:#929393">(v1.0)</small>
* [Group](/datasources/DS0036) <small style="color:#929393">(v1.0)</small>
* [Logon Session](/datasources/DS0028) <small style="color:#929393">(v1.1)</small>
* [User Account](/datasources/DS0002) <small style="color:#929393">(v1.1)</small>
* [Web Credential](/datasources/DS0006) <small style="color:#929393">(v1.0)</small>

### ICS

#### Patches

* [Application Log](/datasources/DS0015) <small style="color:#929393">(v1.0)</small>
* [Logon Session](/datasources/DS0028) <small style="color:#929393">(v1.1)</small>
* [User Account](/datasources/DS0002) <small style="color:#929393">(v1.1)</small>

## Contributors to this release

* @grahamhelton3
* Ale Houspanossian
* Arun Seelagan, CISA
* Asritha Narina
* Aung Kyaw Min Naing, @Nolan
* Barbara Louis-Sidney (OWN-CERT)
* Catherine Williams, BT Security
* Centre for Cybersecurity Belgium (CCB)
* Cris Tomboc, Truswave SpiderLabs
* Csaba Fitzl @theevilbit of Kandji
* Daniel Acevedo, Blackbot
* DeFord L. Smith
* Denise Tan
* Diego Sappa, Securonix
* Domenico Mazzaferro Palmeri
* Dray Agha, Huntress Labs
* Eder Pérez Ignacio, @ch4ik0
* Eduardo González Hernández (@codexlynx)
* Fernando Bacchin
* Furkan Celik, PURE7
* Hakan KARABACAK
* Harikrishnan Muthu, Cyble
* Harry Hill, BT Security
* Inna Danilevich
* Jai Minton, CrowdStrike
* James Emery-Callcott, Emerging Threats Team, Proofpoint
* James P Callahan, Professional Paranoid
* Jamie Williams (U ω U), PANW Unit 42
* Jennifer Kim Roman, CrowdStrike
* Joe Gumke, U.S. Bank
* Jorge Orchilles
* Liran Ravich, CardinalOps
* Madhukar Raina (Senior Security Researcher - Hack The Box, UK)
* Manikantan Srinivasan, NEC Corporation India
* Marco Pedrinazzi, @pedrinazziM
* Massimo Giaimo, Würth Group Cyber Defence Center
* Matt Anderson, @‌nosecurething, Huntress
* Matt Brenton
* Menachem Goldstein
* Michael Forret, Quorum Cyber
* Mike Hartley @mikehartley10
* Nagahama Hiroki – NEC Corporation Japan
* Naveen Vijayaraghavan
* Nilesh Dherange (Gurucul)
* Obsidian Security
* Onur Atali
* OWN
* Phyo Paing Htun (ChiLai)
* Pooja Natarajan, NEC Corporation India
* ReliaQuest
* Riku Katsuse, NEC Corporation
* Ruben Groenewoud, Elastic
* Sam Seabrook, Duke Energy
* Sarathkumar Rajendran, Microsoft Defender365
* Sareena Karapoola, NEC Corporation India
* Sharon Brizinov, Claroty Team82 Research
* Sofia Sanchez Margolles
* Subhash Thapa
* Swachchhanda Shrawan Poudel
* Takemasa Kamatani, NEC Corporation
* TruKno
* Vito Alfano, Group-IB
* Wirapong Petshagun
* Wojciech Reguła @_r3ggi
* Ye Yint Min Thu Htut, Active Defense Team, DBS Bank
* Yoshihiro Kori, NEC Corporation
* Zaw Min Htun, @z3tae
