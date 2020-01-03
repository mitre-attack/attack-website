from git import Repo
import os
import shutil
import json
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
    import stat
    if not os.access(path, os.W_OK):
        # Is the error an access error ?
        os.chmod(path, stat.S_IWUSR)
        func(path)
    else:
        raise

def deploy():
    """ Deploy previous versions to website directory """
    
    prev_versions_deploy_folder = os.path.join(config.web_directory, "previous")

    # delete previous copy of attack-archives
    if os.path.exists(config.archives_directory):
        shutil.rmtree(config.archives_directory, onerror=onerror) 
    # download new version of attack-archives
    Repo.clone_from(config.archives_repo, config.archives_directory)
    build_markdown() # build archives page markdown
    
    # remove previously deployed previous versions
    if os.path.exists(prev_versions_deploy_folder):
        for child in os.listdir(prev_versions_deploy_folder):
            if os.path.isdir(os.path.join(prev_versions_deploy_folder, child)): 
                shutil.rmtree(prev_versions_deploy_folder)

    # copy individual versions from attack-archives to output
    for version in os.listdir(config.archives_directory):
        if os.path.isdir(os.path.join(config.archives_directory, version)) and not version.endswith(".git"):
            shutil.copytree(os.path.join(config.archives_directory, version), os.path.join(prev_versions_deploy_folder, version))
    
    # write robots.txt to disallow crawlers
    with open(os.path.join(config.web_directory, "robots.txt"), "w", encoding='utf8') as robots:
        robots.write(f"User-agent: *\nDisallow: /{config.subdirectory}/previous/")

def build_markdown():
    # import archives data
    with open(os.path.join(config.archives_directory, "archives.json"), "r") as archives:
        archives_data = {"versions": sorted(json.loads(archives.read()), key=lambda p: datetime.strptime(p["date_end"], "%B %d, %Y"), reverse=True) }
    
    # build previous-versions page markdown
    subs = config.previous_md + json.dumps(archives_data)
    with open(os.path.join(config.previous_markdown_path, "previous.md"), "w", encoding='utf8') as md_file:
        md_file.write(subs)
        

