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
# Modularization
## ATT&CK Website version 3.0
### Improvements
- The tour is generated through an independent module and steps are chosen depending the available modules. See issue [#166](https://github.com/mitre-attack/attack-website/issues/166).

### Fixes
- Fixed navigator links on groups and software pages that were repeating the domain on the URI. See issue [#169](https://github.com/mitre-attack/attack-website/issues/169).
- Fixed subdirectory support for navigator links on groups and software pages. See issue [#170](https://github.com/mitre-attack/attack-website/issues/170).

# Sub-techniques Beta
## ATT&CK Website version 2.1
### New Features
- Added tooltips to all matrices to show tactic IDs, technique IDs, and sub-technique IDs when hovering over tactic names, technique names, and sub-technique names. See issue [#120](https://github.com/mitre-attack/attack-website/issues/120).

### Improvements
- The site is now easier to rebrand; color themes and logos can now be changed with simple modifications to the site code. See issue [#80](https://github.com/mitre-attack/attack-website/issues/80)
- Added horizontal scroll indicators to matrices so that it's easier to tell when there's more to the left or right. See issue [#93](https://github.com/mitre-attack/attack-website/issues/93).
- The website tour route is now generated dynamically, allowing the site to adapt the tour to custom STIX content. See issue [#110](https://github.com/mitre-attack/attack-website/issues/110).
- Added Navigator layers to the changelog of the sub-techniques update. See issue [#126](https://github.com/mitre-attack/attack-website/issues/126).

### Fixes
- Added internet explorer support for the sub-techniques matrix. Improved behavior of sub-techniques matrix in Edge browser. See issue [#114](https://github.com/mitre-attack/attack-website/issues/114).
- Fixed bug where sidenav wouldn't open the correct tactic when opening the sub-technique of a technique. See issue [#78](https://github.com/mitre-attack/attack-website/issues/78).
- Fixed bug where contributors wouldn't appear in search. See issue[#150](https://github.com/mitre-attack/attack-website/issues/150).
- Added horizontal scroll indicators to matrices so that it's easier to tell when there's more to the left or right. See issue [#93](https://github.com/mitre-attack/attack-website/issues/93).
- Fixed sizing of homepage twitter card for better mobile device compatibility. See issue [#92](https://github.com/mitre-attack/attack-website/issues/92).
- Fixed a crash that occurred when building the site with mitigations that have no relationships with techniques. See issue [#153](https://github.com/mitre-attack/attack-website/issues/153).
- Fixed outdated ATT&CK Navigator link on the contact page. See issue [#143](https://github.com/mitre-attack/attack-website/issues/143).
- Updated incorrect technique count on March 2020 update. See issue [#141](https://github.com/mitre-attack/attack-website/issues/141).

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
- Added the "take a tour" feature. The tour feature guides the user through the sub-technique changes. Click "take a tour" on the homepage or follow [this link](https://attack.mitre.org/beta/?tour=true) to start the tour automatically. See issue [#28](https://github.com/mitre-attack/attack-website/issues/28).

### Improvements
- Improvements to deprecated techniques. See issue [#116](https://github.com/mitre-attack/attack-website/issues/116).
    - Page content except for the deprecation warning now omitted to discourage continued use
    - Now hidden from search (both ours and search engines')
    - No longer found in technique lists, etc
- ATT&CK Archives now allows for archived versions to be "retired." Retired versions are removed from the /previous/ directory and replaced with links to the raw data and HTML. See issue [#102](https://github.com/mitre-attack/attack-website/issues/102).
- Lists within data cards, e.g the platforms of a technique, are now in alphabetical order. See issue [#84](https://github.com/mitre-attack/attack-website/issues/84).
- Matrix timestamps are now calculated from the modified date on the x-mitre-matrix STIX object. Additionally, said timestamps are now formatted the same as modified dates on other pages of the website. See issue [#27](https://github.com/mitre-attack/attack-website/issues/27).
- Revisions to the layout of the matrix pages to improve readability when multiple matrices occur within a domain.

## [ATT&CK Content version 7.0-beta](https://github.com/mitre/cti/tree/4d3f22d81af2424f3885b4390793ee8eb256d10d)
See release notes [here](https://attack.mitre.org/beta/resources/updates/updates-march-2020/index.html).

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
