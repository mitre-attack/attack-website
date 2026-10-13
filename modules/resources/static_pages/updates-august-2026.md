Title: Updates - August 2026
Date: August 2026
Category: Cyber Threat Intelligence
Authors: Adam Pennington
Template: resources/update-post
url: /resources/updates/updates-august-2026
save_as: resources/updates/updates-august-2026/index.html

| Version | Start Date | End Date | Data | Changelog |
|:--------|:-----------|:---------|:-----|:----------|
| [ATT&CK v19](/versions/v19) | August 6, 2026 | October 13, 2026 | [v19.2 on MITRE/CTI](https://github.com/mitre/cti/releases/tag/ATT%26CK-v19.2) | 19.1 - 19.2 [Details](/docs/changelogs/v19.1-v19.2/changelog-detailed.html) ([JSON](/docs/changelogs/v19.1-v19.2/changelog.json)) |

**Note: This page covers the ATT&CK v19.2 release. For the original ATT&CK v19 release notes, see [Updates - April 2026](/resources/updates/updates-april-2026/).**

The August 2026 **v19.2** ATT&CK Agile release updates Groups and Software for Enterprise.

This is ATT&CK’s first Agile release, a narrower-scope release model that publishes targeted updates to Groups, Software, and Campaigns outside the standard biannual cadence when significant threat activity emerges or expands between scheduled releases.

This agile release adds ShinyHunters, TeamPCP, software entries tied to CI/CD and software supply chain attacks, and Kali365. These additions capture high-impact threat activity seen in current intrusions, including credential and identity token theft, attacks on developer and cloud environments, abuse of trusted software channels to spread, phishing leading users to execute attacker-controlled actions, and the monetization of access through extortion, resale, and follow-on compromise.

- ShinyHunters (G1057) is a cybercriminal group active since at least 2019 that steals credentials and personally identifiable information for resale or extortion. Public reporting also links it to The Community (The Com) and to collaborative activity described under names such as Scattered Lapsus Hunters, Scattered Lapsus Shiny Hunters, and SLSH.
- TeamPCP (G1056) is a financially motivated, cloud-native threat group that shifted from ransomware and cryptocurrency theft to worm-driven credential theft and software supply chain attacks targeting CI/CD workflows. This release also adds Shai-Hulud (S9008), Mini Shai-Hulud (S9043), CanisterWorm (S9042), and TeamPCP Cloud Stealer (S9041) to capture the software associated with this activity.
- Kali365 (S9044) is a phishing-as-a-service kit that uses targeted lures to trick users into copying and pasting attacker-controlled commands, generates device codes on demand, and steals OAuth tokens and session cookies through adversary-in-the-middle collection.
