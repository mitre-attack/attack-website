from git import Repo
import os
import shutil
import stat
import json
import stat
from datetime import datetime
from . import config

# Error handler for windows by:
# https://stackoverflow.com/questions/2656322/shutil-rmtree-fails-on-windows-with-access-is-denied
def onerror(func, path, exc_info):
    """
    Error handler for ``shutil.rmtree``.

    If the error is due to an access error (read only file)
    it attempts to add write permission and then retries.

    If the error is for another reason it re-raises the error.

    Usage : ``shutil.rmtree(path, onerror=onerror)``
    """
    try:
        if not os.access(path, os.W_OK):
            # Is the error an access error ?
            os.chmod(path, stat.S_IWUSR)
            func(path)
    except:
        raise

prev_versions_path = "versions"
prev_versions_deploy_folder = os.path.join(config.web_directory, prev_versions_path)

def deploy():
    """ Deploy previous versions to website directory """
    

    # delete previous copy of attack-archives
    if os.path.exists(config.archives_directory):
        shutil.rmtree(config.archives_directory, onerror=onerror) 
    # download new version of attack-website for use in versioning
    archives_repo = Repo.clone_from(config.archives_repo, config.archives_directory, branch="feature/#174-numbered-versions")

    # remove previously deployed previous versions
    if os.path.exists(prev_versions_deploy_folder):
        for child in os.listdir(prev_versions_deploy_folder):
            if os.path.isdir(os.path.join(prev_versions_deploy_folder, child)): 
                shutil.rmtree(prev_versions_deploy_folder)

    with open("data/archives.json", "r") as f:
        versions = json.load(f)

    for version in versions:
        build_version(version, archives_repo)

    # # copy individual versions from attack-archives to output
    # for version in os.listdir(config.archives_directory):
    #     if os.path.isdir(os.path.join(config.archives_directory, version)) and not version.endswith(".git"):
    #         shutil.copytree(os.path.join(config.archives_directory, version), os.path.join(prev_versions_deploy_folder, version))
    
    # write robots.txt to disallow crawlers
    # with open(os.path.join(config.web_directory, "robots.txt"), "w", encoding='utf8') as robots:
    #     robots.write(f"User-agent: *\nDisallow: /{config.subdirectory}/previous/\nDisallow:/{config.subdirectory}/{prev_versions_path}/")

def build_version(version, repo):
    """build a version of the site to /prev_versions_path. version is a version from archives.json, repo is a reference to the attack-website Repo object"""
    # check out the commit for that version
    repo.git.checkout(version["commit"])
    # copy over files
    shutil.copytree(os.path.join(config.archives_directory), os.path.join(prev_versions_deploy_folder, version["name"]))
    # run archival scripts on version
    # TODO
    # build alias for version
    for alias in version["aliases"]:
        build_alias(version["name"], alias)


def build_alias(version, alias):
    """build redirects from alias to version
    version is the path of the version, e.g "v5"
    alias is the alias to build, e.g "october2018"
    """
    for root, folder, files in os.walk(os.path.join(prev_versions_deploy_folder, version)):
        # subfolder = root.split(os.path.join(config.web_directory, "previous", version))[1] # actual subfolder of the version currently being walked
        for thefile in files:
            # where the file should go
            newRoot = root.replace(version, alias).replace(prev_versions_path, "previous")
            # file to build
            redirectFrom = os.path.join(newRoot, thefile)
            
            # where this file should point to
            if thefile == "index.html": 
                redirectTo = root # index.html is implicit
            else:
                redirectTo = "/".join([root, thefile])  # file is not index.html so it needs to be specified explicitly
            redirectTo = redirectTo.split("output")[1] # remove output folder from path

            # write the redirect file
            if not os.path.isdir(newRoot):
                os.makedirs(newRoot, exist_ok=True) # make parents as well
            with open(redirectFrom, "w") as f:
                f.write(f'<meta http-equiv="refresh" content="0; url={redirectTo}"/>')

def build_markdown():
    # import archives data
    with open(os.path.join(config.archives_directory, "archives.json"), "r") as archives:
        raw_archives = json.load(archives)
        archives_data = {"versions": sorted(raw_archives, key=lambda p: datetime.strptime(p["date_end"], "%B %d, %Y"), reverse=True) }
    
    # build previous-versions page markdown
    subs = config.previous_md + json.dumps(archives_data)
    with open(os.path.join(config.previous_markdown_path, "previous.md"), "w", encoding='utf8') as md_file:
        md_file.write(subs)
    
    return raw_archives


