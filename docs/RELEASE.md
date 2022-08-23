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
* Verify that all changes desired in the next release are present in the `develop` branch, including merging finished feature/bugfix branches.
* Use `towncrier` to update the `CHANGELOG`
  * Update the website version number in `pyproject.toml`
  * Run `towncrier --draft`.
  * If everything looks good, then proceed with `towncrier`.
    * This will remove the newsfragment files and make a git commit.
* Build the website locally to do one final test that it looks correct
  * e.g. `python update-attack.py --attack-brand --extras --no-test-exitstatus`
* Commit and push changes to the `develop` branch.
* Open a pull request from `develop` to `master` <https://github.com/mitre-attack/attack-website/pulls>.
