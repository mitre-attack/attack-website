# Release Process

In order to publish the ATT&CK website, follow the process outlined here.
Hopefully to no one's surprise, only members with appropriate access can follow these steps.

## Banner update only

If you are only updating the banner and nothing else, follow these steps.

* Go to <https://github.com/mitre-attack/attack-website>
* Update `website-banner.production`. You may not include double quotes for "reasons".
  * If you are turning the banner off, then keep the file, but delete the contents.
* That's it!

## Website changes

1. Verify that all features/bugs/documentation updates are tied to issues from the [issue tracker](https://github.com/mitre-attack/attack-website/issues).

    * Make sure that each issue that is addressed has a corresponding `<issue-#>.[feature | bugfix | doc | misc]` in the `newsfragments/` directory.

2. Merge the `master` branch into the `develop` branch, since commits to `master` may have been made for banner updates.

    ```bash
    git checkout develop
    git merge origin/master
    ```

3. Verify that all required changes for the next release are present in the `develop` branch, including merging finished feature/bugfix branches.

    * Update the website version number in `pyproject.toml`
    * Update any dependencies needed in `requirements.txt`.
    * If applicable, update the year in the following files:
        * `attack-theme/templates/general/base-template.html`
        * `modules/website_build/static_pages/terms-of-use.md`
        * `NOTICE.txt`
        * `LICENSE.txt`
        * `README.md`

4. Use `towncrier` to update the `CHANGELOG`

     * Run `towncrier --draft`.
     * If everything looks good, then proceed with running `towncrier`.
         * This will delete the newsfragment files.
         * Doublecheck the `CHANGELOG.md` file since the template isn't perfect and whitespace issues get introduced.
             * Here is an example of `towncrier` output.
               Notice that it adds a bunch of hyphens under the main header and adds a trailing newline.
               These lines can be removed to ensure consistency with the rest of the CHANGELOG.md file.

      ```text
        # v4.0.0 (2022-10-25)
        --------------------- <--- DELETE THIS LINE
        ## Features

        * Add support for [Campaigns](https://github.com/mitre/cti/blob/master/USAGE.md#campaigns) [#384]
        (https://github.com/mitre-attack/attack-website/issues/384)
        <newline>
        <newline>  <-- DELETE THIS LINE
      ```

    * Run `git status`, then stage and commit changes to `CHANGELOG.md` and removed files from `newsfragments/`.

5. If this website build includes ATT&CK/STIX content updates, see the appropriate section below for either Major or Minor ATT&CK releases

6. Build the website locally to do one final test that it looks correct

    * e.g. `python update-attack.py --attack-brand --extras --no-test-exitstatus`
    * Look in the generated `reports/broken-links-report.txt` for broken links.
      Any broken links that start with `/versions/v*` can be ignored.

7. Commit and push changes to the `develop` branch.

8. Open a pull request from `develop` to `master` <https://github.com/mitre-attack/attack-website/pulls>.

    * PR naming convention: "Update website to X.Y.Z"

9. After the PR is accepted, tag the commit in the master branch and push the changes

    ```bash
    git checkout master
    git pull
    git tag -a "website-vX.Y.Z" -m "website-vX.Y.Z"
    git push
    git push --tags
    ```

## ATT&CK Content updates

Consult these sections as needed for step 5 in the above list.

* Create a detailed changelog for the release:
  * Create a new folder: `modules/resources/docs/changelogs/v<previous-ATT&CK-version>-v<current-ATT&CK-version>`
  * Create a detailed changelog using mitreattack-python

  ```sh
  # Clone mitreattack-python repo and download latest ATT&CK STIX
  git clone git@github.com:mitre-attack/mitreattack-python.git
  cd mitreattack-python
  python3 -m venv venv
  . venv/bin/activate
  pip install -r requirements-dev.txt
  pip install -e .
  cd examples/
  download_attack_stix --all

  # update the generate_multiple_attack_diffs.py file to have the correct comparison pairs
  # run the script
  python generate_multiple_attack_diffs.py

  ```

  * Manually modify the detailed changelog's href's at the top for links to the Navigator layers and changelog.json
    * TODO: one day modify the script above to not need this edit anymore
  * Put the following files from the `diff_stix` command into the folder created above
    * `changelog-detailed.html`
    * `changelog.json`
    * Any ATT&CK Navigator layer files that were generated

### Major release

* Update `data/versions.json`
  * Current: all information should reference the latest release
  * Previous:
    * Dates should not overlap
    * `cti_url`: should be tag URL for the release on the mitre/cti repo
    * `commit`: should be sha256 hash of latest commit from mitre-attack/attack-website on the `gh-pages` branch prior to new content release


* Run the `archive-website.py` script to get the previously released archives of the ATT&CK website
  * Upload the `tar.gz` of the latest previous version of the website to the [Archived Website Files](https://github.com/mitre-attack/attack-website/releases/tag/archived-website-files) release
  * Optional - If sufficient changes were made to the archive process the re-upload all `tar.gz` files
* Update notes
  * Add new file: `modules/resources/static_pages/updates-<month>-<year>.md`
  * Update former updates announcement file to specify end date of old release
* Update CHANGELOG.md
  * Add a bullet point to the Features section in the following format

  ```markdown
  * Release [ATT&CK content version X.Y](https://github.com/mitre/cti/releases/tag/ATT%26CK-vX.Y).
    See the release notes [here](https://attack.mitre.org/resources/updates/updates-<month>-<year>/).
  ```
* Update the `layer_version` and `navigator_version` in `modules/site_config.py` if navigator version or navigator layer version has been updated.<br>
Check the layer specification version [here](https://github.com/mitre-attack/attack-navigator/blob/master/layers/spec/) and the navigator version [here](https://github.com/mitre-attack/attack-navigator/blob/master/CHANGELOG.md).

### Minor release

* Update `data/versions.json`
  * Current: all information should reference the latest release
  * Previous: leave alone!
* Update `modules/resources/static_pages/updates-<month>-<year>.md`
  * Minor releases currently don't get their own update page, so make the following updates to the table at the top of the page:
    * Under the Data column: Add a new entry for the latest tag, using `<br />` to separate them
    * Under the Changelogs column: Add a new entry for the latest detailed changelog, for both HTML and JSON (also using `<br />` as a separator)
* Update CHANGELOG.md
  * Add a bullet point to the Features section in the following format

  ```markdown
  * Release ATT&CK content version X.Y.
    See detailed changes [here](https://github.com/mitre/cti/releases/tag/ATT%26CK-vX.Y).
  ```
* Update the `layer_version` and `navigator_version` in `modules/site_config.py` if navigator version or navigator layer version has been updated.<br>
Check the layer specification version [here](https://github.com/mitre-attack/attack-navigator/blob/master/layers/spec/) and the navigator version [here](https://github.com/mitre-attack/attack-navigator/blob/master/CHANGELOG.md).
