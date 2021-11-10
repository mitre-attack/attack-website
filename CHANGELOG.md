<!--    CHANGELOG FORMAT                                                -->
<!--    Completed Entry template:                                       -->
<!--                                                                    -->
<!--    # Date in DD MMM YYYY format                                    -->
<!--    ## ATT&CK Website version ##.##.##                              -->
<!--    ### New Features                                                -->
<!--    ### Improvements                                                -->
<!--    ### Fixes                                                       -->
<!--    ## [ATT&CK Content version ##.##](link to release on mitre/cti) -->
<!--    See the release notes [here](link to release notes).           // if major change -->
<!--    ### Fixes                                                      // else            -->
<!--    Entries for pull request template:                              -->
<!--                                                                    -->
<!--    # Changes staged on develop                                     -->
<!--    ### New Features                                                -->
<!--    ### Improvements                                                -->
<!--    ### Fixes                                                       -->
<!--    VERSION NUMBERING (WEBSITE)                                     -->
<!--                                                                    -->
<!--    website versions are set up in a major.minor.patch format:      -->
<!--    MAJOR updates are when we release major new features or         -->
<!--          pages                                                     -->
<!--    MINOR updates are when we improve a small number of             -->
<!--          existing features                                         -->
<!--    PATCH updates are when a bugfix is made without the             -->
<!--          addition of notable features. When PATCH is 0 it can      -->
<!--          be omitted                                                -->
# 10 November 2021
## [ATT&CK content version 10.1](https://github.com/mitre/cti/releases/tag/ATT%26CK-v10.1)
This minor release includes the following bugfixes:

### Techniques

**Enterprise**

Technique changes:

* Create or Modify System Process: [Launch Agent](/techniques/T1543/001)


Minor Technique changes:

* [Create or Modify System Process](/techniques/T1543)
* [Reflective Code Loading](/techniques/T1620)


**Mobile**

Minor Technique changes:

* [Install Insecure or Malicious Configuration](/techniques/T1478)


### Software

**Enterprise**

Minor Software changes:

* [BS2005](/software/S0014)
* [Kobalos](/software/S0641)
* [MarkiRAT](/software/S0652)


Software deprecations:

* [TRITON](/software/S0609)


**Mobile**

Minor Software changes:

* [Monokle](/software/S0407)


### Groups

**Enterprise**

Minor Group changes:

* [Ferocious Kitten](/groups/G0137)
* [Ke3chang](/groups/G0004)
* [Orangeworm](/groups/G0071)
* [Patchwork](/groups/G0040)
* [Transparent Tribe](/groups/G0134)
* [Winnti Group](/groups/G0044)


### Data Sources and/or Components

**Enterprise**

Minor Data Source and/or Component changes:

* [Active Directory](/datasources/DS0026)
* [Cloud Service](/datasources/DS0025)
* [Cloud Storage](/datasources/DS0010)
* [Cluster](/datasources/DS0031)
* [Command](/datasources/DS0017)
* [Container](/datasources/DS0032)
* [Drive](/datasources/DS0016)
* [Driver](/datasources/DS0027)
* [File](/datasources/DS0022)
* [Firewall](/datasources/DS0018)
* [Firmware](/datasources/DS0001)
* [Group](/datasources/DS0036)
* [Image](/datasources/DS0007)
* [Kernel](/datasources/DS0008)
* [Logon Session](/datasources/DS0028)
* [Module](/datasources/DS0011)
* [Named Pipe](/datasources/DS0023)
* [Network Share](/datasources/DS0033)
* [Network Traffic](/datasources/DS0029)
* [Pod](/datasources/DS0014)
* [Process](/datasources/DS0009)
* [Scheduled Job](/datasources/DS0003)
* [Script](/datasources/DS0012)
* [Sensor Health](/datasources/DS0013)
* [Service](/datasources/DS0019)
* [Snapshot](/datasources/DS0020)
* [User Account](/datasources/DS0002)
* [Volume](/datasources/DS0034)
* [WMI](/datasources/DS0005)


### Contributors to this release

* Center for Threat-Informed Defense (CTID)
* Hiroki Nagahama, NEC Corporation
* Lior Ribak, SentinelOne
* Manikantan Srinivasan, NEC Corporation India
* Pooja Natarajan, NEC Corporation India

## ATT&CK website version 3.4.2
### Improvements
- Added deprecation card to deprecated mitigations, groups, and software as already observed in deprecated techniques.
### Fixes
- Fixed an issue where release notes were incorrectly linking data source pages.

# 27 October 2021
## ATT&CK website version 3.4.1
### Improvements
- Minor UI readability improvement to toolbar that displays ATT&CK content and website version.
- Added random query string to site.js to prevent that file from being cached between releases.
- ATT&CK in Excel only creates hyperlinks to documents that were created by attackToExcel.py.
### Fixes
- Fixed an issue where deprecated and revoked sub-techniques could appear on matrices.

# 21 October 2021

## [ATT&CK content version 10.0](https://github.com/mitre/cti/releases/tag/ATT%26CK-v10.0)
See the release notes [here](https://attack.mitre.org/resources/updates/updates-october-2021/).

## ATT&CK website version 3.4.0
### Improvements
- Added support for data sources and data components. See issue [#321](https://github.com/mitre-attack/attack-website/issues/321).
    - Added data sources pages that may be found under /datasources/DS####
    - Updated technique pages by moving data source mappings to detection section
- Improved side navigation elements:
    - Side-navs now scroll independently of the main page contents, making it easier to work with long pages.
    - The side-nav title (e.g "mitigations") will now stay in the view when scrolled.
    - The side-nav will now scroll to the active page link when initialized.
- Added definitions to technique, tactic, mitigation list pages.
- Improved supports remote definition for techniques.
### Fixes
- Fixed dockerfile to not fail due to test warning. See issue [#326](https://github.com/mitre-attack/attack-website/issues/326).
- Fixed build from crashing when a technique does not have a defined platform. See issue [#329](https://github.com/mitre-attack/attack-website/issues/329).
- Fixed build from crashing when a tactic does not have defined techniques. See issue [#73](https://github.com/mitre-attack/attack-website/issues/73).
- Fixed build from crashing when an object that supports references does not have a defined reference. See issue [#321](https://github.com/mitre-attack/attack-website/issues/321).

# 1 July 2021
## ATT&CK website version 3.3.1
### Improvements
- Updated docs to clarify that both STIX 2.0 and STIX 2.1 input data is supported. See issue [#317](https://github.com/mitre-attack/attack-website/issues/317).
- Updated [privacy policy](https://attack.mitre.org/resources/privacy/).
### Fixes
- Hyperlinks in matrices will no longer direct users to attack.mitre.org on custom instances of the site. See issue [#319](https://github.com/mitre-attack/attack-website/issues/319).

# 30 June 2021
## ATT&CK website version 3.3.0
### Improvements
- Improved usability of matrix side layout to better differentiate tactic columns. See issue [#273](https://github.com/mitre-attack/attack-website/issues/273).
- Improved matrix layout selection to include layout in dropdown title. See issue [#277](https://github.com/mitre-attack/attack-website/issues/277).
- Added links to tactics in the technique information card. See issue [#288](https://github.com/mitre-attack/attack-website/issues/288).
- Updated the [working with ATT&CK](https://attack.mitre.org/resources/working-with-attack/) page to mention [ATT&CK Workbench](https://github.com/center-for-threat-informed-defense/attack-workbench-frontend) and [STIX 2.1 support](https://github.com/mitre-attack/attack-stix-data).
- Updated matrix poster to most recent version of ATT&CK.

### Fixes
- Moved and renamed redirections module to main modules. Prevents broken hyperlinks from revoked objects that would appear when running the build without the optional --extras flag. See issue [#278](https://github.com/mitre-attack/attack-website/issues/278).
- Fixed broken links on the Getting Started page. See issue [#281](https://github.com/mitre-attack/attack-website/issues/281).
- Updated Dockerfile to build from Ubuntu 20.04 LTS. See issue [#312](https://github.com/mitre-attack/attack-website/issues/312).

# 16 June 2021
## ATT&CK website version 3.2.3
### Improvements
- Added support for deprecated relationships, software and groups. Deprecated relationships, software and groups will not appear on the website UI but can be added to STIX bundles. See issue [#302](https://github.com/mitre-attack/attack-website/issues/302) and [#305](https://github.com/mitre-attack/attack-website/issues/305).
- Added support for input data with more than one object with the same STIX or ATT&CK ID which can occur if there are multiple versions of the object present in the data. Website will display the most recently modified object depending on the deprecation status. See issue [#304](https://github.com/mitre-attack/attack-website/issues/304).
- Sorted sub-techniques by ATT&CK ID on Techniques Used tables. See issue [#314](https://github.com/mitre-attack/attack-website/issues/314).
### Fixes
- Fixed Dockerfile which would not run on the current website version. See issue [#313](https://github.com/mitre-attack/attack-website/issues/313).
- Fixed some issues where objects would appear in the wrong domain under specific circumstances. See issue [#310](https://github.com/mitre-attack/attack-website/issues/310).

# 20 May 2021
## ATT&CK website version 3.2.2
### Improvements
- Improved testing of external links to report all instances of non-200 responses (instead of just 404 responses) and provide better reporting on the results of the test.
### Fixes
- Added missing groups excel in the ATT&CK in Excel section of [Working with ATT&CK](https://attack.mitre.org/resources/working-with-attack/).
- Fixed CTI training ticket number 4473845 -> 473845. See issue [#296](https://github.com/mitre-attack/attack-website/issues/296).

# 29 April 2021
## [ATT&CK Content version 9.0](https://github.com/mitre/cti/releases/tag/ATT%26CK-v9.0)
See release notes [here](https://attack.mitre.org/resources/updates/updates-april-2021/index.html).

## ATT&CK website version 3.2.1
### Fixes
- Removing duplicate "Command: Command Execution" data source from (sub-)techniques.

## ATT&CK website version 3.2.0
### Improvements
- Replaced GCP, AWS and Azure platforms with Infrastructure-as-a-Service (IaaS). See issue [#276](https://github.com/mitre-attack/attack-website/issues/276).
- Added Google Workspace platform to Cloud platform list.
- Added Containers platform to enterprise platform list.
- Add support for STIX 2.1.
    - `note` SDOs will now be rendered on object pages when present in the STIX data.
- Improved configuration allowing user to pull data from any HTTP endpoint instead of relying on data stored in the repository. Configuration of data endpoints can be found in `modules/site_config.py`. See issue [#139](https://github.com/mitre-attack/attack-website/issues/139).
- Added tooltips describing fields to the card on object pages. See issue [#148](https://github.com/mitre-attack/attack-website/issues/148).
    - Added to fields on technique pages: Tactics, Platforms, System Requirements, Permissions Required, Effective Permissions, Data Sources, Supports Remote, Defense Bypassed, Impact Type, CAPEC ID, and MTC ID. 
    - Added to field on group pages: Associated Groups. 
    - Added to fields on software pages: Associated Software, Type, and Platforms. 
- Added generation of Navigator layers for mitigations, and updated navigator layer version to 4.2. See issue [#234](https://github.com/mitre-attack/attack-website/issues/234).
- Added ATT&CK IDs to Mitigations and Procedure Examples on technique pages, and software and group home pages. See issues [#235](https://github.com/mitre-attack/attack-website/issues/235) and [#236](https://github.com/mitre-attack/attack-website/issues/236).
- Improved the [Working with ATT&CK](https://attack.mitre.org/resources/working-with-attack/) page with additional information about ATT&CK data and the tools with which it can be manipulated. The new page also includes generated Excel spreadsheets representing the ATT&CK knowledge base (see also [mitreattack-python](https://github.com/mitre-attack/mitreattack-python)'s attackToExcel converter). See issue [#142](https://github.com/mitre-attack/attack-website/issues/142).
- Data sources in technique cards are now hyperlinks to the [attack-datasources GitHub repository](https://github.com/mitre-attack/attack-datasources).

### Fixes
- Fixed a bug with automatic redirection generation which was causing some redirects to build in the wrong directory.
# 23 March 2021
## ATT&CK website version 3.1.1
### Improvements 
- Updated ATT&CKcon page with ATT&CKcon Power Hour.

# 27 January 2021
## [ATT&CK Content version 8.2](https://github.com/mitre/cti/releases/tag/ATT%26CK-v8.2)
ATT&CK version 8.2 contains new reporting for the activity related to the SolarWinds supply chain injection.
### New Techniques:

* Domain Policy Modification: [Domain Trust Modification](https://attack.mitre.org/techniques/T1484/002)
* Domain Policy Modification: [Group Policy Modification](https://attack.mitre.org/techniques/T1484/001)
* [Forge Web Credentials](https://attack.mitre.org/techniques/T1606)
	* [SAML Tokens](https://attack.mitre.org/techniques/T1606/002)
	* [Web Cookies](https://attack.mitre.org/techniques/T1606/001)

### Technique changes:

* Account Manipulation: [Additional Cloud Credentials](https://attack.mitre.org/techniques/T1098/001)
* [Domain Policy Modification](https://attack.mitre.org/techniques/T1484)

### New Software:

* [AdFind](https://attack.mitre.org/software/S0552)
* [BloodHound](https://attack.mitre.org/software/S0521)
* [Raindrop](https://attack.mitre.org/software/S0565)
* [Sunburst](https://attack.mitre.org/software/S0559)
* [Sunspot](https://attack.mitre.org/software/S0562)
* [Teardrop](https://attack.mitre.org/software/S0560)

### New Groups:

* [UNC2452](https://attack.mitre.org/groups/G0118)

## ATT&CK website version 3.1
### Improvements
- Updated Navigator layers to version 4.1 so that users are no longer warned that they are out of date.
- Updated introductory video on [getting started](https://attack.mitre.org/resources/getting-started/) page.

# 12 November 2020
## [ATT&CK Content version 8.1](https://github.com/mitre/cti/releases/tag/ATT%26CK-v8.1)
### Fixes
- Fixed typo "stressor" to "stresser"
- Fixed type and version for `S0154`
- Fixed contributors for `T1598`, `T1598.001`, `T1598.002`, `T1598.003`, and `S0514`

### Additions
- new reporting and procedure examples for `G0102`

# 27 October 2020
## [ATT&CK Content version 8.0](https://github.com/mitre/cti/releases/tag/ATT%26CK-v8.0)
See release notes [here](https://attack.mitre.org/resources/updates/updates-october-2020/index.html).

## ATT&CK Website version 3.0
### Improvements
- Added a link on the home page that takes the user to a random page within a specified category. See issue [#98](https://github.com/mitre-attack/attack-website/issues/98).
- Base template does not get overwritten when site configuration data changes. See issue [#147](https://github.com/mitre-attack/attack-website/issues/147).
- STIX cleaning code is now moved into macro. References are now sorted in order of appearance. See issue [#161](https://github.com/mitre-attack/attack-website/issues/161).
- The tour is generated through an independent module and steps are chosen depending the available modules. See issue [#166](https://github.com/mitre-attack/attack-website/issues/166).
- Modules and test arguments are now required if flags are presented. See issue [#177](https://github.com/mitre-attack/attack-website/issues/177).
- The search index is now loaded from cache (when available), resulting in faster search loading for most browsers. See issue [#167](https://github.com/mitre-attack/attack-website/issues/167).
- Updated website dependencies. See issue [#181](https://github.com/mitre-attack/attack-website/issues/181).
- Matrix layouts on the home page and matrices page now persist across pages and sessions. See issue [#165](https://github.com/mitre-attack/attack-website/issues/165).
- Added [Network matrix](https://attack.mitre.org/matrices/network). See issue [#230](https://github.com/mitre-attack/attack-website/issues/230).
- Removed PRE-ATT&CK domain to support migration into the new tactics in Enterprise-ATT&CK; see the [PRE matrix](https://attack.mitre.org/matrices/PRE) for the replacing tactics. See issue [#222](https://github.com/mitre-attack/attack-website/issues/222).
- Added [PRE matrix](https://attack.mitre.org/matrices/PRE). See issue [#251](https://github.com/mitre-attack/attack-website/issues/251).
- Website built by users are visually distinct from attack.mitre.org unless brand flag is added as an argument. See issue [#240](https://github.com/mitre-attack/attack-website/issues/240).
- Website is built without specific related ATT&CK content such as resources, contribute, and blog unless specified. See issue [#241](https://github.com/mitre-attack/attack-website/issues/241).

### Fixes
- Fixed bug where bootstrap dropdown menu buttons require two clicks to open the first time they are opened. See issue [#152](https://github.com/mitre-attack/attack-website/issues/152).
- Fixed subdirectory support for navigator links on groups and software pages. See issue [#170](https://github.com/mitre-attack/attack-website/issues/170).
- Fixed typo on the Training page. See issue [#180](https://github.com/mitre-attack/attack-website/issues/180).
- Fixed (for most scenarios) slow loading of the search index when using Firefox. See issues [#167](https://github.com/mitre-attack/attack-website/issues/167) and [#187](https://github.com/mitre-attack/attack-website/issues/187).
- Fixed versioning feature ran under a subdirectory. See issue [#200](https://github.com/mitre-attack/attack-website/issues/200).

# 8 August 2020
## ATT&CK Website version 2.1.4
### Improvements
- Updated roadmap and matrix poster on the [resources](https://attack.mitre.org/resources/) page. See issue [#255](https://github.com/mitre-attack/attack-website/issues/255).

# 6 August 2020
## ATT&CK Website version 2.1.3
### Improvements
- Added note on the [CTI training page](https://attack.mitre.org/resources/training/cti/) to indicate that ATT&CK v6 should be used instead of ATT&CK v7. See issue [#221](https://github.com/mitre-attack/attack-website/issues/221).

# 15 July 2020
## [ATT&CK Content version 7.2](https://github.com/mitre/cti/releases/tag/ATT%26CK-v7.2)
This minor release includes the following bugfixes:

- Removed Windows platform from Modify Authentication Process: [Pluggable Authentication Modules](https://attack.mitre.org/techniques/T1556/003/).
- Updated contributors for Account Manipulation: [Additional Azure Service Principal Credentials](https://attack.mitre.org/techniques/T1098/001/).
- Added missing `x_mitre_is_subtechnique` field to several techniques.
- Updated T1064 in the sub-technique crosswalks.

# 13 July 2020
## [ATT&CK Content version 7.1](https://github.com/mitre/cti/releases/tag/ATT%26CK-v7.1)
This minor release includes the following bugfixes:

- Removed Azure platform from Brute Force: [Password Cracking](https://attack.mitre.org/techniques/T1110/002/).
- Added Linux and macOS platforms to [Deobfuscate/Decode Files or Information](https://attack.mitre.org/techniques/T1140/) and Impair Defenses: [Indicator Blocking](https://attack.mitre.org/techniques/T1562/006/).
- Updated contributor information on [Masquerading](https://attack.mitre.org/techniques/T1036/) and Event Triggered Execution: [Component Object Model Hijacking](https://attack.mitre.org/techniques/T1546/015/).
- Fixed broken citations on [Multi Factor Authentication](https://attack.mitre.org/mitigations/M1032/), [Enterprise Policy](https://attack.mitre.org/mitigations/M1012/), [Encrypt Sensitive Information](https://attack.mitre.org/mitigations/M1041/), [Audit](https://attack.mitre.org/mitigations/M1047/), [Access Notifications](https://attack.mitre.org/techniques/T1517/) and [Data from Cloud Storage Object](https://attack.mitre.org/techniques/T1530/).
- Fixes for various STIX objects (mostly relationships) which were included in the wrong domain bundle. These changes do not affect what's displayed on the ATT&CK Website, but rather corrects where the data is found in the source STIX bundles. See issue [MITRE/CTI#74](https://github.com/mitre/cti/issues/74).

| Change | About |
    |:-------|:------------|
    | Removed the relationship [Dark Caracal](https://attack.mitre.org/groups/G0070/) ⟹ [Pallas](https://attack.mitre.org/software/S0399/) from enterprise-attack | Relationship moved to mobile |
    | Removed the relationship [Bouncing Golf](https://attack.mitre.org/groups/G0097/) ⟹ [GolfSpy](https://attack.mitre.org/software/S0421/) from enterprise-attack | Relationship moved to mobile |
    | Removed the group [Bouncing Golf](https://attack.mitre.org/groups/G0097/) from enterprise-attack | Group should be mobile only (was previously in both domain bundles) |
    | Added the relationship [Dark Caracal](https://attack.mitre.org/groups/G0070/) ⟹ [FinFisher](https://attack.mitre.org/software/S0182/) to mobile-attack | Relationship was only present in enterprise, but since both objects are in both domains the relationship should be duplicated across bundles. |
    | Added the relationship [Dark Caracal](https://attack.mitre.org/groups/G0070/) ⟹ [Pallas](https://attack.mitre.org/software/S0399/) to mobile-attack | Relationship moved from enterprise |
    | Added the relationship [Bouncing Golf](https://attack.mitre.org/groups/G0097/) ⟹ [GolfSpy](https://attack.mitre.org/software/S0421/) to mobile-attack | Relationship moved from enterprise |


## ATT&CK Website version 2.1.2
### Improvements
- Added links to ATT&CK Navigator layers for the July 2020 release. See issues [attack-website#208](https://github.com/mitre-attack/attack-website/issues/208), and [attack-navigator#194](https://github.com/mitre-attack/attack-navigator/issues/194).
- Updated contribute page. See issue [#207](https://github.com/mitre-attack/attack-website/issues/207).
### Fixes
- Corrected the end date of v6 in the [preserved version](https://attack.mitre.org/versions/v6/), on the [Versions of ATT&CK page](https://attack.mitre.org/resources/versions/), and [v6 release notes](https://attack.mitre.org/resources/updates/updates-october-2019/index.html). See issue [#204](https://github.com/mitre-attack/attack-website/issues/204).
- Removed links to the `/beta/` website from the changelog and March 2020 release notes. See issue [#205](https://github.com/mitre-attack/attack-website/issues/205).
- Updated the broken citation tests to catch malformed citations where `Citation:` is not followed by a space. See issue [#209](https://github.com/mitre-attack/attack-website/issues/209).
- Fixed bug where the "Versions of ATT&CK" segment of the tour would loop instead of sending the user back to the site index. See issue [#203](https://github.com/mitre-attack/attack-website/issues/203).
- Fixed the preserved v6 and v3 versions of the site so that the search interface doesn't send the user to the current site when they click on links. See issue [#215](https://github.com/mitre-attack/attack-website/issues/215).
- Fixed a typo on the enterprise matrices.

# 8 July 2020
## [ATT&CK Content version 7.0](https://github.com/mitre/cti/releases/tag/ATT%26CK-v7.0)
See release notes [here](https://attack.mitre.org/resources/updates/updates-july-2020/index.html).

## ATT&CK Website version 2.1.1
### Improvements
- Improved matrix page header layout with versioning feature. See issue [#190](https://github.com/mitre-attack/attack-website/issues/190).
- Added versioning feature to [tour](https://attack.mitre.org/?tour=true). See issue [#191](https://github.com/mitre-attack/attack-website/issues/191).
### Fixes
- Fixed number of tactics displayed on tactics overview pages. See issue [#183](https://github.com/mitre-attack/attack-website/issues/183).
- Fixed objects without descriptions not showing up on techniques used tables. See issue [#186](https://github.com/mitre-attack/attack-website/issues/186).
- Fixed a bug where contributor lists were delimited with commas instead of semicolons on group and software pages. See issue [#196](https://github.com/mitre-attack/attack-website/issues/196).

## ATT&CK Website version 2.1
### New Features
- Added tooltips to all matrices to show tactic IDs, technique IDs, and sub-technique IDs when hovering over tactic names, technique names, and sub-technique names. See issue [#120](https://github.com/mitre-attack/attack-website/issues/120).

### Improvements
- The site is now easier to rebrand; color themes and logos can now be changed with simple modifications to the site code. See issue [#80](https://github.com/mitre-attack/attack-website/issues/80).
- Added horizontal scroll indicators to matrices so that it's easier to tell when there's more to the left or right. See issue [#93](https://github.com/mitre-attack/attack-website/issues/93).
- The website tour route is now generated dynamically, allowing the site to adapt the tour to custom STIX content. See issue [#110](https://github.com/mitre-attack/attack-website/issues/110).
- Added Navigator layers to the changelog of the sub-techniques update. See issue [#126](https://github.com/mitre-attack/attack-website/issues/126).
- Updated [contribute page](https://attack.mitre.org/resources/contribute). See issue [#162](https://github.com/mitre-attack/attack-website/issues/162).

### Fixes
- Added internet explorer support for the sub-techniques matrix. Improved behavior of sub-techniques matrix in Edge browser. See issue [#114](https://github.com/mitre-attack/attack-website/issues/114).
- Fixed bug where sidenav wouldn't open the correct tactic when opening the sub-technique of a technique. See issue [#78](https://github.com/mitre-attack/attack-website/issues/78).
- Fixed bug where contributors wouldn't appear in search. See issue[#150](https://github.com/mitre-attack/attack-website/issues/150).
- Added horizontal scroll indicators to matrices so that it's easier to tell when there's more to the left or right. See issue [#93](https://github.com/mitre-attack/attack-website/issues/93).
- Fixed sizing of homepage twitter card for better mobile device compatibility. See issue [#92](https://github.com/mitre-attack/attack-website/issues/92).
- Fixed a crash that occurred when building the site with mitigations that have no relationships with techniques. See issue [#153](https://github.com/mitre-attack/attack-website/issues/153).
- Fixed outdated ATT&CK Navigator link on the contact page. See issue [#143](https://github.com/mitre-attack/attack-website/issues/143).
- Updated incorrect technique count on March 2020 update. See issue [#141](https://github.com/mitre-attack/attack-website/issues/141).

# March 31, 2020
## ATT&CK Website version 2.0
### New Features
- Added sub-techniques.
    - Added pages for sub-techniques. Sub-technique pages are found under their parent technique, e.g /techniques/T####/###. Sub-technique names and IDs are prefixed with that of their parent technique. Otherwise they are largely formatted like techniques. See issue [#23](https://github.com/mitre-attack/attack-website/issues/23).
    - Added sub-technique listing card to techniques with sub-techniques. See issue [#24](https://github.com/mitre-attack/attack-website/issues/24).
    - Updated techniques used/mitigated lists to differentiate sub-techniques and techniques. See issue [#25](https://github.com/mitre-attack/attack-website/issues/25).
    - Added sub-techniques to side-navigation and technique/tactic lists. See issue [#26](https://github.com/mitre-attack/attack-website/issues/26).
    - Updated FAQ with sub-technique information. See issue [#41](https://github.com/mitre-attack/attack-website/issues/41).
    - Updated ATT&CK Matrix layout to support sub-techniques.
        - Two layouts of the matrix are available:
            - the "side" layout (default), where sub-techniques appear in an adjacent sub-column of the tactic.
            - the "flat" layout, where sub-techniques appear nested beneath their parent similar to an indented list.
        The control to toggle between them appears only when sub-techniques are present in the matrix. 
        - Sub-techniques can be hidden and shown under their parent by clicking the gray sidebar. 
        - Show-all / hide-all buttons were added to show/hide all sub-techniques. See issue [#43](https://github.com/mitre-attack/attack-website/issues/43).
        - Added "help" button to matrices which plays the matrix portion of the sub-technique tour. See issue [#28](https://github.com/mitre-attack/attack-website/issues/28).
    - Added sub-technique support for technique usage ATT&CK Navigator layers on group and software pages. See issue [#29](https://github.com/mitre-attack/attack-website/issues/29).
- Added the "take a tour" feature. The tour feature guides the user through the sub-technique changes. Click "take a tour" on the homepage or follow [this link](https://attack.mitre.org/?tour=true) to start the tour automatically. See issue [#28](https://github.com/mitre-attack/attack-website/issues/28).

### Improvements
- Improvements to deprecated techniques. See issue [#116](https://github.com/mitre-attack/attack-website/issues/116).
    - Page content except for the deprecation warning now omitted to discourage continued use
    - Now hidden from search (both ours and search engines')
    - No longer found in technique lists, etc
- ATT&CK Archives now allows for archived versions to be "retired." Retired versions are removed from the /previous/ directory and replaced with links to the raw data and HTML. See issue [#102](https://github.com/mitre-attack/attack-website/issues/102).
- Lists within data cards, e.g the platforms of a technique, are now in alphabetical order. See issue [#84](https://github.com/mitre-attack/attack-website/issues/84).
- Matrix timestamps are now calculated from the modified date on the x-mitre-matrix STIX object. Additionally, said timestamps are now formatted the same as modified dates on other pages of the website. See issue [#27](https://github.com/mitre-attack/attack-website/issues/27).
- Revisions to the layout of the matrix pages to improve readability when multiple matrices occur within a domain.

## [ATT&CK Content version 7.0-beta](https://github.com/mitre/cti/releases/tag/ATT%26CK-v7.0-beta)
See release notes [here](https://attack.mitre.org/resources/updates/updates-march-2020/index.html).

# 17 June 2020
## ATT&CK Website version 1.3.1
### Fixes
- Fixed navigator links on groups and software pages that were repeating the domain on the URI. See issues [#169](https://github.com/mitre-attack/attack-website/issues/169) and [#192](https://github.com/mitre-attack/attack-website/issues/192).

# 10 June 2020
## ATT&CK Website version 1.3
This update includes a major refactor of the ATT&CK catalog versioning system, previously referred to as "previous versions."

- Versions have been moved from `/previous/monthYear` to `/versions/v#` which should be more predictable and consistent with the way the versions are referred to elsewhere. Redirects have been created so that users who bookmarked the old URLs will get sent to the new ones. See issue [#174](https://github.com/mitre-attack/attack-website/issues/174).
- Added a permalink to the current version of the site. See issue [#175](https://github.com/mitre-attack/attack-website/issues/175).
    - Current version is preserved alongside other versions in `/versions/`.
    - Object pages on the live website now have a "version permalink" leading to a frozen version of that page.
    - Permalink and previous versions now have a "live version" link leading to the most recent version of that page.
- Revised the version list. Find the new version list on the [Versions of ATT&CK page](https://attack.mitre.org/resources/versions), which replaced the "previous versions" page.
    - Now formatted as an easy to read table.
    - Added links to the data on [MITRE/CTI](https://github.com/mitre/cti) for each version.
    - Revised blurb on how versions work to explain our methodology behind the catalog version numbers and versioning system.
- Updated past release notes to mention the version number for each release.

# 31 March 2020
The sub-techniques beta is now live! Read the <a target='_blank' href='https://medium.com/mitre-attack/attack-subs-what-you-need-to-know-99bce414ae0b'>release blog post</a> for more details.
### Changes
- Added sub-techniques release announcement banner.
- Added sub-techniques release docs

# 9 March 2020
## [ATT&CK Content version 6.3](https://github.com/mitre/cti/releases/tag/ATT%26CK-v6.3)
### Fixes
- Fixed typo in M1026.
- Updated copyright statement marking-definition to match that on [https://attack.mitre.org](https://attack.mitre.org).
- Fixed invalid bundle IDs on marking-definition objects.

# 6 March 2020
## ATT&CK Website version 1.2.4
### Fixes
- Minor revision to the ATT&CK logo.

# 4 March 2020
## ATT&CK Website version 1.2.3
### Improvements
- Updated trademark language. See issue [#54](https://github.com/mitre-attack/attack-website/issues/54).
- Updated ATT&CK™ to ATT&CK®. See issue [#55](https://github.com/mitre-attack/attack-website/issues/55).
- Update wordmarks to have ® instead of ™. See issue [#56](https://github.com/mitre-attack/attack-website/issues/56).
- Updated "How Should I reference the name ATT&CK" in FAQ. See issue [#57](https://github.com/mitre-attack/attack-website/issues/57).
- Updated copyrights to 2020. See issue [#58](https://github.com/mitre-attack/attack-website/issues/58).
- Updated README. See issue [#59](https://github.com/mitre-attack/attack-website/issues/59).

# 20 February 2020
## ATT&CK Website version 1.2.2
### Fixes
- Added redirects to for matrix poster and roadmap. See issue [#85](https://github.com/mitre-attack/attack-website/issues/85)

# 18 February 2020
## ATT&CK Website version 1.2.1
### Improvements
- Updated the _roadmap_ and _matrix poster_ documents on the [General Information](https://attack.mitre.org/resources/) page.
### Fixes
- Fixed PRE-ATT&CK side-navigation toggle on tactics and techniques. See issue [#81](https://github.com/mitre-attack/attack-website/issues/81).

# 17 February 2020
## ATT&CK Website version 1.2
### New Features
- Added Docker support, enabling users to easily build and host a docker container of the ATT&CK Website. See issue [#17](https://github.com/mitre-attack/attack-website/issues/17). 
- Added configuration options to specify url of attached [ATT&CK Navigator](https://github.com/mitre-attack/attack-navigator) instance. See issue [#18](https://github.com/mitre-attack/attack-website/issues/18).
- Added the ability to configure site to be hosted from a subdirectory. See issue [#15](https://github.com/mitre-attack/attack-website/issues/15).
### Improvements
- Added talks and links to videos to the [General Information](https://attack.mitre.org/resources/) page.
- Updated navigation drawer on technique, tactic, and mitigation pages to make domains more accessible. See issue [#53](https://github.com/mitre-attack/attack-website/issues/53).
- Major overhaul of site search UI. See issue [#4](https://github.com/mitre-attack/attack-website/issues/4).
### Fixes
- Sticky footer should be less temperamental when the page resizes. See issue [#51](https://github.com/mitre-attack/attack-website/issues/51).


# 7 January 2020
## ATT&CK Website version 1.1.1
### Improvements
- Added links to [ATT&CK for ICS](https://collaborate.mitre.org/attackics/index.php/Main_Page).


# 3 January 2020
## ATT&CK Website version 1.1
### New Features
- Added created and last modified dates to object pages. See issue [#38](https://github.com/mitre-attack/attack-website/issues/38).
- Added ATT&CK training to website. See issue [#22](https://github.com/mitre-attack/attack-website/issues/22).
### Improvements
- Improved maintainability of ATT&CKcon page and added ATT&CKcon 2.0 content. See issue [#19](https://github.com/mitre-attack/attack-website/issues/19). 
- Improved maintainability of FAQ page, and added FAQ entries for sub-techniques and the relationships of ATT&CK and other models. See issues [#30](https://github.com/mitre-attack/attack-website/issues/30), [#41](https://github.com/mitre-attack/attack-website/issues/41).
- Added website and content version number to the footer. See issue [#10](https://github.com/mitre-attack/attack-website/issues/10).
- Added changelog page to website reachable by version number link in the footer.


# 5 December 2019
## ATT&CK Website version 1.0.4
### Fixes
- Fixed a typo in the software side-navigation header. See issue [#39](https://github.com/mitre-attack/attack-website/issues/39).

# 2 December 2019
## ATT&CK Website version 1.0.3
### Improvements
- Updated roadmap to latest version. See issue [#31](https://github.com/mitre-attack/attack-website/issues/31).

## [ATT&CK Content version 6.2](https://github.com/mitre/cti/releases/tag/ATT%26CK-v6.2)
### Fixes
- Updated contributors for T1036 and T1497.

# 25 November 2019
## ATT&CK Website version 1.0.2
### Fixes
- Removed google analytics and google-site-verification from source code. See issue [#11](https://github.com/mitre-attack/attack-website/issues/11).

# 22 November 2019
## ATT&CK Website version 1.0.1
### Fixes
- Fixed incorrect initial state for the side-navigation on the cloud matrix page. See issue [#8](https://github.com/mitre-attack/attack-website/issues/8).

# 21 November 2019
## ATT&CK Website version 1.0
This is the initial release of the website source code.

## [ATT&CK Content version 6.1](https://github.com/mitre/cti/releases/tag/ATT%26CK-v6.1)
### Fixes
- Fixed missing external_reference value in Office Application Startup (T1137).

# 24 October 2019
## [ATT&CK Content version 6.0](https://github.com/mitre/cti/releases/tag/ATT%26CK-v6.0)
See release notes [here](https://attack.mitre.org/resources/updates/updates-october-2019/index.html).
