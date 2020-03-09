from git import Repo
import os
import shutil
import json
import stat
from datetime import datetime
from modules import site_config
from . import resources_config

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

def deploy():
    # delete previous copy of attack-archives
    if os.path.exists(resources_config.archives_directory):
        shutil.rmtree(resources_config.archives_directory, onerror=onerror) 
    # download new version of attack-archives
    Repo.clone_from(resources_config.archives_repo, resources_config.archives_directory)
    build_markdown() # build archives page markdown
    
    # remove previously deployed previous versions
    if os.path.exists(resources_config.prev_versions_deploy_folder):
        for child in os.listdir(resources_config.prev_versions_deploy_folder):
            if os.path.isdir(os.path.join(resources_config.prev_versions_deploy_folder, child)): 
                shutil.rmtree(resources_config.prev_versions_deploy_folder)

    # copy individual versions from attack-archives to output
    for version in os.listdir(resources_config.archives_directory):
        if os.path.isdir(os.path.join(resources_config.archives_directory, version)) and not version.endswith(".git"):
            shutil.copytree(os.path.join(resources_config.archives_directory, version), os.path.join(resources_config.prev_versions_deploy_folder, version))
    
    if not os.path.isdir(site_config.web_directory):
        os.mkdir(site_config.web_directory)
        
    # write robots.txt to disallow crawlers
    with open(os.path.join(site_config.web_directory, "robots.txt"), "w", encoding='utf8') as robots:
        robots.write("User-agent: *\nDisallow: /previous/")

def build_markdown():
    # import archives data
    with open(os.path.join(resources_config.archives_directory, "archives.json"), "r") as archives:
        archives_data = {"versions": sorted(json.loads(archives.read()), key=lambda p: datetime.strptime(p["date_end"], "%B %d, %Y"), reverse=True) }
    
    # build previous-versions page markdown
    subs = resources_config.previous_md + json.dumps(archives_data)
    with open(os.path.join(resources_config.previous_markdown_path, "previous.md"), "w", encoding='utf8') as md_file:
        md_file.write(subs)