# Release Process

In order to publish the ATT&CK website, follow the process outlined here.
Hopefully to no one's surprise, only members with appropriate access can follow these steps.

## Banner update only

If you are only updating the banner and nothing else, follow these steps.

* Go to <https://github.com/mitre-attack/attack-website>
* Update `website-banner.production`. You may not include double quotes for "reasons".
  * If you are turning the banner off, then keep the file, but delete the contents.
* That's it!

## Website changes (but no ATT&CK content changes)

* Merge the `master` branch into the `develop` branch, since commits to `master` may have been made for banner updates.
  * `git merge origin/master`
* Verify that all features/bugs/documentation updates are tied to issues from the [issue tracker](https://github.com/mitre-attack/attack-website/issues).
  * Make sure that each issue that is addressed has a corresponding `<issue-#>.[feature | bugfix | doc | misc]` in the `newsfragments/` directory.
* Verify that all required changes for the next release are present in the `develop` branch, including merging finished feature/bugfix branches.
  * Update any dependencies needed in `requirements.txt`.
  * If applicable, update the year in `modules/website_build/static_pages/terms-of-use.md`
* Use `towncrier` to update the `CHANGELOG`
  * Update the website version number in `pyproject.toml`
  * Run `towncrier --draft`.
  * If everything looks good, then proceed with running `towncrier`.
    * This will remove the newsfragment files and make a git commit.
* Build the website locally to do one final test that it looks correct
  * e.g. `python update-attack.py --attack-brand --extras --no-test-exitstatus`
  * Look in the generated `reports/broken-links-report.txt` for broken links.
    Any broken links that start with `/versions/v*` can be ignored.
* Commit and push changes to the `develop` branch.
* Open a pull request from `develop` to `master` <https://github.com/mitre-attack/attack-website/pulls>.
  * PR naming convention: "Update website to X.Y.Z"
* After the PR is accepted, tag the commit in the master branch and push the changes

    ```bash
    git pull
    git checkout master
    git tag -a "website-vX.Y.Z" -m "website-vX.Y.Z"
    git push --tags  # no need to `git push`, since that was done in the PR itself
    ```

## ATT&CK Content updates

This section to be filled out later...
