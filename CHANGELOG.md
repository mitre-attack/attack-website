# v4.2.1 (2024-11-12)

## Features

* Release ATT&CK content version 16.1.
  See detailed changes [here](https://github.com/mitre/cti/releases/tag/ATT%26CK-v16.1).

# v4.2.0 (2024-10-31)

## Features

* Release ATT&CK content version 16.0.
  See detailed changes [here](https://github.com/mitre/cti/releases/tag/ATT%26CK-v16.0).

# v4.1.6 (2024-08-15)

## Docs

* Add updated ATT&CK poster on Getting Started page.
* Update training pages to have embedded YouTube player.

# v4.1.5 (2024-07-18)

## Misc

* Added new ATT&CK trainings.
* Moved sidebar headings around to add ATT&CKcon to be at the top level.

# v4.1.4 (2024-06-19)

## Misc

* Updated CTI Training to latest version.
* Updated banner related to ATT&CKcon 5.0.

# v4.1.3 (2024-05-02)

* Release ATT&CK content version 15.1.
  See detailed changes [here](https://github.com/mitre/cti/releases/tag/ATT%26CK-v15.1).

# v4.1.2 (2024-04-23)

* Release [ATT&CK content version 15.0](https://github.com/mitre/cti/releases/tag/ATT%26CK-v15.0).
  See the release notes [here](https://attack.mitre.org/resources/updates/updates-april-2024/).

# v4.1.1 (2024-02-05)

## Misc

* Added Lightning Talk YouTube links for ATT&CKCon 4.0

## Bugfixes

* Changed priority of random page module to be able to load pages from the random page button and dropdown
* Fixed title and images on attack data and tools page

# v4.1.0 (2024-01-22)

## Bugfixes

* Updated Benefactors page. [#477](https://github.com/mitre-attack/attack-website/issues/477)
* Fixed offline hosting issue for Fontawesome fonts. [#488](https://github.com/mitre-attack/attack-website/issues/488)

# v4.0.8 (2023-11-22)

## Bugfixes

* Add mobile datasources to excel output.

## Misc

* Updated Caldera description.
* Enforce better SSL security practices when building the website.

# v4.0.7 (2023-11-14)

## Features

* Release ATT&CK content version 14.1.
  See detailed changes [here](https://github.com/mitre/cti/releases/tag/ATT%26CK-v14.1).

# v4.0.6 (2023-10-31)

## Features

* Data sources table can now be sorted and filtered based on domains. [#454](https://github.com/mitre-attack/attack-website/issues/454)
* Release [ATT&CK content version 14.0](https://github.com/mitre/cti/releases/tag/ATT%26CK-v14.0).
  See the release notes [here](https://attack.mitre.org/resources/updates/updates-october-2023/).

# v4.0.5 (2023-09-01)

## Features

* The sidebar is now collapsable and displayed properly in mobile view [#450](https://github.com/mitre-attack/attack-website/issues/450)

## Bugfixes

* Changed the UUID generation logic to use CONTENT_VERSION and WEBSITE_VERSION as seeds for idempotent UUID creation. This prevents the creation of redundant IndexedDB tables. [#455](https://github.com/mitre-attack/attack-website/issues/455)

# v4.0.4 (2023-08-11)

## Features

* Sidebar is now resizable. [#349](https://github.com/mitre-attack/attack-website/issues/349)
* Update the resource pages to have a sidebar. [#441](https://github.com/mitre-attack/attack-website/issues/441)
* Add a page for the ATT&CK brand guide. [#445](https://github.com/mitre-attack/attack-website/issues/445)
* Clean up the FAQ and ATT&CKcon pages in the Resources section to split them into more readable pages. [#446](https://github.com/mitre-attack/attack-website/issues/446)

## Bugfixes

* Minor adjustment to print layout to not show scrollbars anymore. [#403](https://github.com/mitre-attack/attack-website/issues/403)

## Improved Documentation

* Update README and developer documentation on how to set up local environment using Docker. [#427](https://github.com/mitre-attack/attack-website/issues/427)

## Misc

* Configure Sonarcloud to track project metrics better. [#431](https://github.com/mitre-attack/attack-website/issues/431)

# v4.0.3 (2023-05-09)

## Features

* Release ATT&CK content version 13.1.
  See detailed changes [here](https://github.com/mitre/cti/releases/tag/ATT%26CK-v13.1).

# v4.0.2 (2023-04-27)

## Features

* Release [ATT&CK content version 13.0](https://github.com/mitre/cti/releases/tag/ATT%26CK-v13.0).
  See the release notes [here](https://attack.mitre.org/resources/updates/updates-april-2023/).

## Misc

* Center align the Contact page information. [#399](https://github.com/mitre-attack/attack-website/issues/399)
* Update mitreattack-python to latest. [#400](https://github.com/mitre-attack/attack-website/issues/400)

# v4.0.1 (2022-11-08)

## Features

* Release ATT&CK content version 12.1.
  See detailed changes [here](https://github.com/mitre/cti/releases/tag/ATT%26CK-v12.1).

## Bugfixes

* Fixed Data Source pages to not display sections for Data Components that have no detections associated with them.

## Miscellaneous

* Refactored CHANGELOG headers to conform to latest template for version and date.

# v4.0.0 (2022-10-25)

## Features

* Release [ATT&CK content version 12.0](https://github.com/mitre/cti/releases/tag/ATT%26CK-v12.0).
  See the release notes [here](https://attack.mitre.org/resources/updates/updates-october-2022/).
* Add support for [Campaigns](https://github.com/mitre/cti/blob/master/USAGE.md#campaigns) [#384](https://github.com/mitre-attack/attack-website/issues/384)

# v3.6.7 (2022-08-24)

## Bugfixes

* Update mitreattack-python library dependency to get diff_stix script to work again. [#386](https://github.com/mitre-attack/attack-website/issues/386)

# v3.6.6 (2022-08-23)

## Bugfixes

* Removed deprecated objects from search results. [#352](https://github.com/mitre-attack/attack-website/issues/352)

# v3.6.5 (2022-07-17)

## Bugfixes

* Resource pages now display properly when displayed on large monitors. [#378](https://github.com/mitre-attack/attack-website/issues/378)

# v3.6.4 (2022-07-07)

This release promotes the Mobile sub-techniques from beta to stable.
It also fixes a few minor STIX abnormalities for ICS Techniques.

## Features

* Release ATT&CK content version 11.3.
* Updated resources page with ATT&CKcon 3.0 presentations.

# v3.6.3 (2022-06-30)

## Bugfixes

* Deprecated subtechniques will no longer be displayed.
* Add [mobile-subtechniques-crosswalk.json](https://attack.mitre.org/docs/subtechniques/mobile-subtechniques-crosswalk.json)

## Features

* Added optional Google Analytics to the attack-theme Pelican template
* Fixed link in v11 Updates page to go to Boot or Logon Autostart Execution: Plist Modification (T1547.011)

# v3.6.2 (2022-05-24)

## Features

* Release ATT&CK content version 11.2.
  See detailed changes [here](https://github.com/mitre/cti/releases/tag/ATT%26CK-v11.2).

# v3.6.1 (2022-05-12)

## Features

* Release ATT&CK content version 11.1.
  See detailed changes [here](https://github.com/mitre/cti/releases/tag/ATT%26CK-v11.1).
* Update requirements.txt dependencies to latest versions of libraries, and only includes libraries directly used

# v3.6.0 (2022-04-25)

## Features

* Release [ATT&CK content version 11.0](https://github.com/mitre/cti/releases/tag/ATT%26CK-v11.0).
  See the release notes [here](https://attack.mitre.org/resources/updates/updates-april-2022/).
* Add LinkById test that checks STIX used to build the site for any unparseable ATT&CK IDs. LinkById is a construct used in ATT&CK Workbench

## Bugfixes

* Fixed brackets inside of descriptions from being duplicated. See issue [#353](https://github.com/mitre-attack/attack-website/issues/343).
* Fixed non-deprecated relationships between mitigations and techniques from showing up on technique pages. See issue [#358](https://github.com/mitre-attack/attack-website/issues/358).
* Fixed non-deprecated software created by Workbench from appearing as deprecated in the page's description. See issue [#355](https://github.com/mitre-attack/attack-website/issues/355).

# v3.5.0 (2022-01-07)

## Features

* Updated ATT&CK Navigator and layer versions. See issue [#343](https://github.com/mitre-attack/attack-website/issues/343).

# v3.4.3 (2021-11-24)

## Bugfixes

* Fixed footer on tactic list pages. See issue [#339](https://github.com/mitre-attack/attack-website/issues/339).
* Fixed table scrolling on technique and tactic list pages.
* Fixed deprecation marker on tactic list pages for deprecated domains.

# v3.4.2 (2021-11-10)

## Features

* Release ATT&CK content version 10.1.
  See detailed changes [here](https://github.com/mitre/cti/releases/tag/ATT%26CK-v10.1).
* Added deprecation card to deprecated mitigations, groups, and software as already observed in deprecated techniques.

## Bugfixes

* Fixed an issue where release notes were incorrectly linking data source pages.

# v3.4.1 (2021-10-27)

## Features

* Minor UI readability improvement to toolbar that displays ATT&CK content and website version.
* Added random query string to site.js to prevent that file from being cached between releases.
* ATT&CK in Excel only creates hyperlinks to documents that were created by attackToExcel.py.

## Bugfixes

* Fixed an issue where deprecated and revoked sub-techniques could appear on matrices.

# v3.4.0 (2021-10-21)

## Features

* Release [ATT&CK content version 10.0](https://github.com/mitre/cti/releases/tag/ATT%26CK-v10.0).
  See the release notes [here](https://attack.mitre.org/resources/updates/updates-october-2021/).
* Added support for data sources and data components. See issue [#321](https://github.com/mitre-attack/attack-website/issues/321).
  * Added data sources pages that may be found under /datasources/DS####
  * Updated technique pages by moving data source mappings to detection section
* Improved side navigation elements:
  * Side-navs now scroll independently of the main page contents, making it easier to work with long pages.
  * The side-nav title (e.g "mitigations") will now stay in the view when scrolled.
  * The side-nav will now scroll to the active page link when initialized.
* Added definitions to technique, tactic, mitigation list pages.
* Improved supports remote definition for techniques.

## Bugfixes

* Fixed dockerfile to not fail due to test warning. See issue [#326](https://github.com/mitre-attack/attack-website/issues/326).
* Fixed build from crashing when a technique does not have a defined platform. See issue [#329](https://github.com/mitre-attack/attack-website/issues/329).
* Fixed build from crashing when a tactic does not have defined techniques. See issue [#73](https://github.com/mitre-attack/attack-website/issues/73).
* Fixed build from crashing when an object that supports references does not have a defined reference. See issue [#321](https://github.com/mitre-attack/attack-website/issues/321).

# v3.3.1 (2021-07-01)

## Features

* Updated docs to clarify that both STIX 2.0 and STIX 2.1 input data is supported. See issue [#317](https://github.com/mitre-attack/attack-website/issues/317).
* Updated [privacy policy](https://attack.mitre.org/resources/legal-and-branding/privacy/).

## Bugfixes

* Hyperlinks in matrices will no longer direct users to attack.mitre.org on custom instances of the site. See issue [#319](https://github.com/mitre-attack/attack-website/issues/319).

# v3.3.0 (2021-06-30)

## Features

* Improved usability of matrix side layout to better differentiate tactic columns. See issue [#273](https://github.com/mitre-attack/attack-website/issues/273).
* Improved matrix layout selection to include layout in dropdown title. See issue [#277](https://github.com/mitre-attack/attack-website/issues/277).
* Added links to tactics in the technique information card. See issue [#288](https://github.com/mitre-attack/attack-website/issues/288).
* Updated the [working with ATT&CK](https://attack.mitre.org/resources/attack-data-and-tools/) page to mention [ATT&CK Workbench](https://github.com/center-for-threat-informed-defense/attack-workbench-frontend) and [STIX 2.1 support](https://github.com/mitre-attack/attack-stix-data).
* Updated matrix poster to most recent version of ATT&CK.

## Bugfixes

* Moved and renamed redirections module to main modules. Prevents broken hyperlinks from revoked objects that would appear when running the build without the optional --extras flag. See issue [#278](https://github.com/mitre-attack/attack-website/issues/278).
* Fixed broken links on the Getting Started page. See issue [#281](https://github.com/mitre-attack/attack-website/issues/281).
* Updated Dockerfile to build from Ubuntu 20.04 LTS. See issue [#312](https://github.com/mitre-attack/attack-website/issues/312).

# v3.2.3 (2021-06-16)

## Features

* Added support for deprecated relationships, software and groups. Deprecated relationships, software and groups will not appear on the website UI but can be added to STIX bundles. See issue [#302](https://github.com/mitre-attack/attack-website/issues/302) and [#305](https://github.com/mitre-attack/attack-website/issues/305).
* Added support for input data with more than one object with the same STIX or ATT&CK ID which can occur if there are multiple versions of the object present in the data. Website will display the most recently modified object depending on the deprecation status. See issue [#304](https://github.com/mitre-attack/attack-website/issues/304).
* Sorted sub-techniques by ATT&CK ID on Techniques Used tables. See issue [#314](https://github.com/mitre-attack/attack-website/issues/314).

## Bugfixes

* Fixed Dockerfile which would not run on the current website version. See issue [#313](https://github.com/mitre-attack/attack-website/issues/313).
* Fixed some issues where objects would appear in the wrong domain under specific circumstances. See issue [#310](https://github.com/mitre-attack/attack-website/issues/310).

# v3.2.2 (2021-05-20)

## Features

* Improved testing of external links to report all instances of non-200 responses (instead of just 404 responses) and provide better reporting on the results of the test.

## Bugfixes

* Added missing groups excel in the ATT&CK in Excel section of [Working with ATT&CK](https://attack.mitre.org/resources/attack-data-and-tools/).
* Fixed CTI training ticket number 4473845 -> 473845. See issue [#296](https://github.com/mitre-attack/attack-website/issues/296).

# v3.2.1 (2021-04-29)

## Bugfixes

* Removing duplicate "Command: Command Execution" data source from (sub-)techniques.

# v3.2.0 (2021-04-29)

## Features

* Release [ATT&CK content version 9.0](https://github.com/mitre/cti/releases/tag/ATT%26CK-v9.0).
  See the release notes [here](https://attack.mitre.org/resources/updates/updates-april-2021/index.html).
* Replaced GCP, AWS and Azure platforms with Infrastructure-as-a-Service (IaaS). See issue [#276](https://github.com/mitre-attack/attack-website/issues/276).
* Added Google Workspace platform to Cloud platform list.
* Added Containers platform to enterprise platform list.
* Add support for STIX 2.1.
  * `note` SDOs will now be rendered on object pages when present in the STIX data.
* Improved configuration allowing user to pull data from any HTTP endpoint instead of relying on data stored in the repository. Configuration of data endpoints can be found in `modules/site_config.py`. See issue [#139](https://github.com/mitre-attack/attack-website/issues/139).
* Added tooltips describing fields to the card on object pages. See issue [#148](https://github.com/mitre-attack/attack-website/issues/148).
  * Added to fields on technique pages: Tactics, Platforms, System Requirements, Permissions Required, Effective Permissions, Data Sources, Supports Remote, Defense Bypassed, Impact Type, CAPEC ID, and MTC ID.
  * Added to field on group pages: Associated Groups.
  * Added to fields on software pages: Associated Software, Type, and Platforms.
* Added generation of Navigator layers for mitigations, and updated navigator layer version to 4.2. See issue [#234](https://github.com/mitre-attack/attack-website/issues/234).
* Added ATT&CK IDs to Mitigations and Procedure Examples on technique pages, and software and group home pages. See issues [#235](https://github.com/mitre-attack/attack-website/issues/235) and [#236](https://github.com/mitre-attack/attack-website/issues/236).
* Improved the [Working with ATT&CK](https://attack.mitre.org/resources/attack-data-and-tools/) page with additional information about ATT&CK data and the tools with which it can be manipulated. The new page also includes generated Excel spreadsheets representing the ATT&CK knowledge base (see also [mitreattack-python](https://github.com/mitre-attack/mitreattack-python)'s attackToExcel converter). See issue [#142](https://github.com/mitre-attack/attack-website/issues/142).
* Data sources in technique cards are now hyperlinks to the [attack-datasources GitHub repository](https://github.com/mitre-attack/attack-datasources).

## Bugfixes

* Fixed a bug with automatic redirection generation which was causing some redirects to build in the wrong directory.

# v3.1.1 (2021-03-23)

## Features

* Updated ATT&CKcon page with ATT&CKcon Power Hour.

# v3.1 (2021-01-27)

## Features

* Release ATT&CK content version 8.2.
  See detailed changes [here](https://github.com/mitre/cti/releases/tag/ATT%26CK-v8.2).
* Updated Navigator layers to version 4.1 so that users are no longer warned that they are out of date.
* Updated introductory video on [getting started](https://attack.mitre.org/resources/) page.

# No website version update (2020-11-12)

## Features

* Release ATT&CK content version 8.1.
  See detailed changes [here](https://github.com/mitre/cti/releases/tag/ATT%26CK-v8.1).
* new reporting and procedure examples for `G0102`

## Bugfixes

* Fixed typo "stressor" to "stresser"
* Fixed type and version for `S0154`
* Fixed contributors for `T1598`, `T1598.001`, `T1598.002`, `T1598.003`, and `S0514`

# v3.0 (2020-10-27)

## Features

* Release [ATT&CK content version 8.0](https://github.com/mitre/cti/releases/tag/ATT%26CK-v8.0).
  See the release notes [here](https://attack.mitre.org/resources/updates/updates-october-2020/index.html).
* Added a link on the home page that takes the user to a random page within a specified category. See issue [#98](https://github.com/mitre-attack/attack-website/issues/98).
* Base template does not get overwritten when site configuration data changes. See issue [#147](https://github.com/mitre-attack/attack-website/issues/147).
* STIX cleaning code is now moved into macro. References are now sorted in order of appearance. See issue [#161](https://github.com/mitre-attack/attack-website/issues/161).
* The tour is generated through an independent module and steps are chosen depending the available modules. See issue [#166](https://github.com/mitre-attack/attack-website/issues/166).
* Modules and test arguments are now required if flags are presented. See issue [#177](https://github.com/mitre-attack/attack-website/issues/177).
* The search index is now loaded from cache (when available), resulting in faster search loading for most browsers. See issue [#167](https://github.com/mitre-attack/attack-website/issues/167).
* Updated website dependencies. See issue [#181](https://github.com/mitre-attack/attack-website/issues/181).
* Matrix layouts on the home page and matrices page now persist across pages and sessions. See issue [#165](https://github.com/mitre-attack/attack-website/issues/165).
* Added [Network matrix](https://attack.mitre.org/matrices/network). See issue [#230](https://github.com/mitre-attack/attack-website/issues/230).
* Removed PRE-ATT&CK domain to support migration into the new tactics in Enterprise-ATT&CK; see the [PRE matrix](https://attack.mitre.org/matrices/PRE) for the replacing tactics. See issue [#222](https://github.com/mitre-attack/attack-website/issues/222).
* Added [PRE matrix](https://attack.mitre.org/matrices/PRE). See issue [#251](https://github.com/mitre-attack/attack-website/issues/251).
* Website built by users are visually distinct from attack.mitre.org unless brand flag is added as an argument. See issue [#240](https://github.com/mitre-attack/attack-website/issues/240).
* Website is built without specific related ATT&CK content such as resources, contribute, and blog unless specified. See issue [#241](https://github.com/mitre-attack/attack-website/issues/241).

## Bugfixes

* Fixed bug where bootstrap dropdown menu buttons require two clicks to open the first time they are opened. See issue [#152](https://github.com/mitre-attack/attack-website/issues/152).
* Fixed subdirectory support for navigator links on groups and software pages. See issue [#170](https://github.com/mitre-attack/attack-website/issues/170).
* Fixed typo on the Training page. See issue [#180](https://github.com/mitre-attack/attack-website/issues/180).
* Fixed (for most scenarios) slow loading of the search index when using Firefox. See issues [#167](https://github.com/mitre-attack/attack-website/issues/167) and [#187](https://github.com/mitre-attack/attack-website/issues/187).
* Fixed versioning feature ran under a subdirectory. See issue [#200](https://github.com/mitre-attack/attack-website/issues/200).

# v2.1.4 (2020-08-08)

## Features

* Updated roadmap and matrix poster on the [resources](https://attack.mitre.org/resources/) page. See issue [#255](https://github.com/mitre-attack/attack-website/issues/255).

# v2.1.3 (2020-08-06)

## Features

* Added note on the [CTI training page](https://attack.mitre.org/resources/learn-more-about-attack/training/cti/) to indicate that ATT&CK v6 should be used instead of ATT&CK v7. See issue [#221](https://github.com/mitre-attack/attack-website/issues/221).

# No website version update (2020-07-15)

## Features

* Release [ATT&CK content version 7.2](https://github.com/mitre/cti/releases/tag/ATT%26CK-v7.2).

## Bugfixes

* Removed Windows platform from Modify Authentication Process: [Pluggable Authentication Modules](https://attack.mitre.org/techniques/T1556/003/).
* Updated contributors for Account Manipulation: [Additional Azure Service Principal Credentials](https://attack.mitre.org/techniques/T1098/001/).
* Added missing `x_mitre_is_subtechnique` field to several techniques.
* Updated T1064 in the sub-technique crosswalks.

# v2.1.2 (2020-07-13)

## Features

* Release [ATT&CK content version 7.1](https://github.com/mitre/cti/releases/tag/ATT%26CK-v7.1).
* Added links to ATT&CK Navigator layers for the July 2020 release. See issues [attack-website#208](https://github.com/mitre-attack/attack-website/issues/208), and [attack-navigator#194](https://github.com/mitre-attack/attack-navigator/issues/194).
* Updated contribute page. See issue [#207](https://github.com/mitre-attack/attack-website/issues/207).

## STIX Bugfixes

* Removed Azure platform from Brute Force: [Password Cracking](https://attack.mitre.org/techniques/T1110/002/).
* Added Linux and macOS platforms to [Deobfuscate/Decode Files or Information](https://attack.mitre.org/techniques/T1140/) and Impair Defenses: [Indicator Blocking](https://attack.mitre.org/techniques/T1562/006/).
* Updated contributor information on [Masquerading](https://attack.mitre.org/techniques/T1036/) and Event Triggered Execution: [Component Object Model Hijacking](https://attack.mitre.org/techniques/T1546/015/).
* Fixed broken citations on [Multi Factor Authentication](https://attack.mitre.org/mitigations/M1032/), [Enterprise Policy](https://attack.mitre.org/mitigations/M1012/), [Encrypt Sensitive Information](https://attack.mitre.org/mitigations/M1041/), [Audit](https://attack.mitre.org/mitigations/M1047/), [Access Notifications](https://attack.mitre.org/techniques/T1517/) and [Data from Cloud Storage Object](https://attack.mitre.org/techniques/T1530/).
* Fixes for various STIX objects (mostly relationships) which were included in the wrong domain bundle. These changes do not affect what's displayed on the ATT&CK Website, but rather corrects where the data is found in the source STIX bundles. See issue [MITRE/CTI#74](https://github.com/mitre/cti/issues/74).

| Change | About |
    |:-------|:------------|
    | Removed the relationship [Dark Caracal](https://attack.mitre.org/groups/G0070/) ⟹ [Pallas](https://attack.mitre.org/software/S0399/) from enterprise-attack | Relationship moved to mobile |
    | Removed the relationship [Bouncing Golf](https://attack.mitre.org/groups/G0097/) ⟹ [GolfSpy](https://attack.mitre.org/software/S0421/) from enterprise-attack | Relationship moved to mobile |
    | Removed the group [Bouncing Golf](https://attack.mitre.org/groups/G0097/) from enterprise-attack | Group should be mobile only (was previously in both domain bundles) |
    | Added the relationship [Dark Caracal](https://attack.mitre.org/groups/G0070/) ⟹ [FinFisher](https://attack.mitre.org/software/S0182/) to mobile-attack | Relationship was only present in enterprise, but since both objects are in both domains the relationship should be duplicated across bundles. |
    | Added the relationship [Dark Caracal](https://attack.mitre.org/groups/G0070/) ⟹ [Pallas](https://attack.mitre.org/software/S0399/) to mobile-attack | Relationship moved from enterprise |
    | Added the relationship [Bouncing Golf](https://attack.mitre.org/groups/G0097/) ⟹ [GolfSpy](https://attack.mitre.org/software/S0421/) to mobile-attack | Relationship moved from enterprise |

### Website Bugfixes

* Corrected the end date of v6 in the [preserved version](https://attack.mitre.org/versions/v6/), on the [Versions of ATT&CK page](https://attack.mitre.org/resources/versions/), and [v6 release notes](https://attack.mitre.org/resources/updates/updates-october-2019/index.html). See issue [#204](https://github.com/mitre-attack/attack-website/issues/204).
* Removed links to the `/beta/` website from the changelog and March 2020 release notes. See issue [#205](https://github.com/mitre-attack/attack-website/issues/205).
* Updated the broken citation tests to catch malformed citations where `Citation:` is not followed by a space. See issue [#209](https://github.com/mitre-attack/attack-website/issues/209).
* Fixed bug where the "Versions of ATT&CK" segment of the tour would loop instead of sending the user back to the site index. See issue [#203](https://github.com/mitre-attack/attack-website/issues/203).
* Fixed the preserved v6 and v3 versions of the site so that the search interface doesn't send the user to the current site when they click on links. See issue [#215](https://github.com/mitre-attack/attack-website/issues/215).
* Fixed a typo on the enterprise matrices.

# v2.1.1 (2020-07-08)

## Features

* Improved matrix page header layout with versioning feature. See issue [#190](https://github.com/mitre-attack/attack-website/issues/190).
* Added versioning feature to [tour](https://attack.mitre.org/?tour=true). See issue [#191](https://github.com/mitre-attack/attack-website/issues/191).

## Bugfixes

* Fixed number of tactics displayed on tactics overview pages. See issue [#183](https://github.com/mitre-attack/attack-website/issues/183).
* Fixed objects without descriptions not showing up on techniques used tables. See issue [#186](https://github.com/mitre-attack/attack-website/issues/186).
* Fixed a bug where contributor lists were delimited with commas instead of semicolons on group and software pages. See issue [#196](https://github.com/mitre-attack/attack-website/issues/196).

# v2.1 (2020-07-08)

## Features

* Release [ATT&CK content version 7.0](https://github.com/mitre/cti/releases/tag/ATT%26CK-v7.0).
  See the release notes [here](https://attack.mitre.org/resources/updates/updates-july-2020/index.html).
* Added tooltips to all matrices to show tactic IDs, technique IDs, and sub-technique IDs when hovering over tactic names, technique names, and sub-technique names. See issue [#120](https://github.com/mitre-attack/attack-website/issues/120).
* The site is now easier to rebrand; color themes and logos can now be changed with simple modifications to the site code. See issue [#80](https://github.com/mitre-attack/attack-website/issues/80).
* Added horizontal scroll indicators to matrices so that it's easier to tell when there's more to the left or right. See issue [#93](https://github.com/mitre-attack/attack-website/issues/93).
* The website tour route is now generated dynamically, allowing the site to adapt the tour to custom STIX content. See issue [#110](https://github.com/mitre-attack/attack-website/issues/110).
* Added Navigator layers to the changelog of the sub-techniques update. See issue [#126](https://github.com/mitre-attack/attack-website/issues/126).
* Updated [contribute page](https://attack.mitre.org/resources/engage-with-attack/contribute). See issue [#162](https://github.com/mitre-attack/attack-website/issues/162).

## Bugfixes

* Added internet explorer support for the sub-techniques matrix. Improved behavior of sub-techniques matrix in Edge browser. See issue [#114](https://github.com/mitre-attack/attack-website/issues/114).
* Fixed bug where sidenav wouldn't open the correct tactic when opening the sub-technique of a technique. See issue [#78](https://github.com/mitre-attack/attack-website/issues/78).
* Fixed bug where contributors wouldn't appear in search. See issue[#150](https://github.com/mitre-attack/attack-website/issues/150).
* Added horizontal scroll indicators to matrices so that it's easier to tell when there's more to the left or right. See issue [#93](https://github.com/mitre-attack/attack-website/issues/93).
* Fixed sizing of homepage twitter card for better mobile device compatibility. See issue [#92](https://github.com/mitre-attack/attack-website/issues/92).
* Fixed a crash that occurred when building the site with mitigations that have no relationships with techniques. See issue [#153](https://github.com/mitre-attack/attack-website/issues/153).
* Fixed outdated ATT&CK Navigator link on the contact page. See issue [#143](https://github.com/mitre-attack/attack-website/issues/143).
* Updated incorrect technique count on March 2020 update. See issue [#141](https://github.com/mitre-attack/attack-website/issues/141).

# v2.0 (2020-07-07)

## Features

* Release [ATT&CK content version 7.0-beta](https://github.com/mitre/cti/releases/tag/ATT%26CK-v7.0-beta).
  See the release notes [here](https://attack.mitre.org/resources/updates/updates-march-2020/index.html).
* Added sub-techniques.
  * Added pages for sub-techniques. Sub-technique pages are found under their parent technique, e.g /techniques/T####/###. Sub-technique names and IDs are prefixed with that of their parent technique. Otherwise they are largely formatted like techniques. See issue [#23](https://github.com/mitre-attack/attack-website/issues/23).
  * Added sub-technique listing card to techniques with sub-techniques. See issue [#24](https://github.com/mitre-attack/attack-website/issues/24).
  * Updated techniques used/mitigated lists to differentiate sub-techniques and techniques. See issue [#25](https://github.com/mitre-attack/attack-website/issues/25).
  * Added sub-techniques to side-navigation and technique/tactic lists. See issue [#26](https://github.com/mitre-attack/attack-website/issues/26).
  * Updated FAQ with sub-technique information. See issue [#41](https://github.com/mitre-attack/attack-website/issues/41).
  * Updated ATT&CK Matrix layout to support sub-techniques.
    * Two layouts of the matrix are available:
      * the "side" layout (default), where sub-techniques appear in an adjacent sub-column of the tactic.
      * the "flat" layout, where sub-techniques appear nested beneath their parent similar to an indented list.
        The control to toggle between them appears only when sub-techniques are present in the matrix.
    * Sub-techniques can be hidden and shown under their parent by clicking the gray sidebar.
    * Show-all / hide-all buttons were added to show/hide all sub-techniques. See issue [#43](https://github.com/mitre-attack/attack-website/issues/43).
    * Added "help" button to matrices which plays the matrix portion of the sub-technique tour. See issue [#28](https://github.com/mitre-attack/attack-website/issues/28).
  * Added sub-technique support for technique usage ATT&CK Navigator layers on group and software pages. See issue [#29](https://github.com/mitre-attack/attack-website/issues/29).
* Added the "take a tour" feature. The tour feature guides the user through the sub-technique changes. Click "take a tour" on the homepage or follow [this link](https://attack.mitre.org/?tour=true) to start the tour automatically. See issue [#28](https://github.com/mitre-attack/attack-website/issues/28).
* Improvements to deprecated techniques. See issue [#116](https://github.com/mitre-attack/attack-website/issues/116).
  * Page content except for the deprecation warning now omitted to discourage continued use
  * Now hidden from search (both ours and search engines')
  * No longer found in technique lists, etc
* ATT&CK Archives now allows for archived versions to be "retired." Retired versions are removed from the /previous/ directory and replaced with links to the raw data and HTML. See issue [#102](https://github.com/mitre-attack/attack-website/issues/102).
* Lists within data cards, e.g the platforms of a technique, are now in alphabetical order. See issue [#84](https://github.com/mitre-attack/attack-website/issues/84).
* Matrix timestamps are now calculated from the modified date on the x-mitre-matrix STIX object. Additionally, said timestamps are now formatted the same as modified dates on other pages of the website. See issue [#27](https://github.com/mitre-attack/attack-website/issues/27).
* Revisions to the layout of the matrix pages to improve readability when multiple matrices occur within a domain.

# v1.3.1 (2020-06-17)

## Bugfixes

* Fixed navigator links on groups and software pages that were repeating the domain on the URI. See issues [#169](https://github.com/mitre-attack/attack-website/issues/169) and [#192](https://github.com/mitre-attack/attack-website/issues/192).

# v1.3 (2020-06-10)

This update includes a major refactor of the ATT&CK catalog versioning system, previously referred to as "previous versions."

## Features

* Versions have been moved from `/previous/monthYear` to `/versions/v#` which should be more predictable and consistent with the way the versions are referred to elsewhere. Redirects have been created so that users who bookmarked the old URLs will get sent to the new ones. See issue [#174](https://github.com/mitre-attack/attack-website/issues/174).
* Added a permalink to the current version of the site. See issue [#175](https://github.com/mitre-attack/attack-website/issues/175).
  * Current version is preserved alongside other versions in `/versions/`.
  * Object pages on the live website now have a "version permalink" leading to a frozen version of that page.
  * Permalink and previous versions now have a "live version" link leading to the most recent version of that page.
* Revised the version list. Find the new version list on the [Versions of ATT&CK page](https://attack.mitre.org/resources/versions), which replaced the "previous versions" page.
  * Now formatted as an easy to read table.
  * Added links to the data on [MITRE/CTI](https://github.com/mitre/cti) for each version.
  * Revised blurb on how versions work to explain our methodology behind the catalog version numbers and versioning system.
* Updated past release notes to mention the version number for each release.

# No website version update (2020-03-31)

The sub-techniques beta is now live! Read the <a target='_blank' href='https://medium.com/mitre-attack/attack-subs-what-you-need-to-know-99bce414ae0b'>release blog post</a> for more details.

## Features

* Added sub-techniques release announcement banner.
* Added sub-techniques release docs

# No website version update (2020-03-09)

## Features

* Release [ATT&CK content version 6.3](https://github.com/mitre/cti/releases/tag/ATT%26CK-v6.3).

## Bugfixes

* Fixed typo in M1026.
* Updated copyright statement marking-definition to match that on [https://attack.mitre.org](https://attack.mitre.org).
* Fixed invalid bundle IDs on marking-definition objects.

# v1.2.4 (2020-03-06)

## Bugfixes

* Minor revision to the ATT&CK logo.

# v1.2.3 (2020-03-04)

## Features

* Updated trademark language. See issue [#54](https://github.com/mitre-attack/attack-website/issues/54).
* Updated ATT&CK™ to ATT&CK®. See issue [#55](https://github.com/mitre-attack/attack-website/issues/55).
* Update wordmarks to have ® instead of ™. See issue [#56](https://github.com/mitre-attack/attack-website/issues/56).
* Updated "How Should I reference the name ATT&CK" in FAQ. See issue [#57](https://github.com/mitre-attack/attack-website/issues/57).
* Updated copyrights to 2020. See issue [#58](https://github.com/mitre-attack/attack-website/issues/58).
* Updated README. See issue [#59](https://github.com/mitre-attack/attack-website/issues/59).

# v1.2.2 (2020-02-20)

## Bugfixes

* Added redirects to for matrix poster and roadmap. See issue [#85](https://github.com/mitre-attack/attack-website/issues/85)

# v1.2.1 (2020-02-18)

## Features

* Updated the _roadmap_ and _matrix poster_ documents on the [General Information](https://attack.mitre.org/resources/) page.

## Bugfixes

* Fixed PRE-ATT&CK side-navigation toggle on tactics and techniques. See issue [#81](https://github.com/mitre-attack/attack-website/issues/81).

# v1.2 (2020-02-17)

## Features

* Added Docker support, enabling users to easily build and host a docker container of the ATT&CK Website. See issue [#17](https://github.com/mitre-attack/attack-website/issues/17).
* Added configuration options to specify url of attached [ATT&CK Navigator](https://github.com/mitre-attack/attack-navigator) instance. See issue [#18](https://github.com/mitre-attack/attack-website/issues/18).
* Added the ability to configure site to be hosted from a subdirectory. See issue [#15](https://github.com/mitre-attack/attack-website/issues/15).
* Added talks and links to videos to the [General Information](https://attack.mitre.org/resources/) page.
* Updated navigation drawer on technique, tactic, and mitigation pages to make domains more accessible. See issue [#53](https://github.com/mitre-attack/attack-website/issues/53).
* Major overhaul of site search UI. See issue [#4](https://github.com/mitre-attack/attack-website/issues/4).

## Bugfixes

* Sticky footer should be less temperamental when the page resizes. See issue [#51](https://github.com/mitre-attack/attack-website/issues/51).

# v1.1.1 (2020-01-07)

## Features

* Added links to [ATT&CK for ICS](https://collaborate.mitre.org/attackics/index.php/Main_Page).

# v1.1 (2020-01-03)

## Features

* Added created and last modified dates to object pages. See issue [#38](https://github.com/mitre-attack/attack-website/issues/38).
* Added ATT&CK training to website. See issue [#22](https://github.com/mitre-attack/attack-website/issues/22).
* Improved maintainability of ATT&CKcon page and added ATT&CKcon 2.0 content. See issue [#19](https://github.com/mitre-attack/attack-website/issues/19).
* Improved maintainability of FAQ page, and added FAQ entries for sub-techniques and the relationships of ATT&CK and other models. See issues [#30](https://github.com/mitre-attack/attack-website/issues/30), [#41](https://github.com/mitre-attack/attack-website/issues/41).
* Added website and content version number to the footer. See issue [#10](https://github.com/mitre-attack/attack-website/issues/10).
* Added changelog page to website reachable by version number link in the footer.

# v1.0.4 (2019-12-05)

## Bugfixes

* Fixed a typo in the software side-navigation header. See issue [#39](https://github.com/mitre-attack/attack-website/issues/39).

# v1.0.3 (2019-12-02)

## Features

* Release [ATT&CK content version 6.2](https://github.com/mitre/cti/releases/tag/ATT%26CK-v6.2).
* Updated roadmap to latest version. See issue [#31](https://github.com/mitre-attack/attack-website/issues/31).

## Bugfixes

* Updated contributors for T1036 and T1497.

# v1.0.2 (2019-11-25)

## Bugfixes

* Removed google analytics and google-site-verification from source code. See issue [#11](https://github.com/mitre-attack/attack-website/issues/11).

# v1.0.1 (2019-11-22)

## Bugfixes

* Fixed incorrect initial state for the side-navigation on the cloud matrix page. See issue [#8](https://github.com/mitre-attack/attack-website/issues/8).

# v1.0 (2019-11-21)

This is the initial release of the website source code.

## Features

* Release [ATT&CK content version 6.1](https://github.com/mitre/cti/releases/tag/ATT%26CK-v6.1).

## Bugfixes

* Fixed missing external_reference value in Office Application Startup (T1137).

# No website version (2019-10-24)

## Features

* Release [ATT&CK content version 6.0](https://github.com/mitre/cti/releases/tag/ATT%26CK-v6.0).
  See the release notes [here](https://attack.mitre.org/resources/updates/updates-october-2019/index.html).
