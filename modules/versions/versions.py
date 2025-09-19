import concurrent.futures as cf
import functools
import io
import json
import os
import re
import shutil
import subprocess
import tarfile
import tempfile
from datetime import datetime
from pathlib import Path

import requests
from loguru import logger

from modules import site_config, util

from . import versions_config

ALLOWED = r"-?\w\$\.!\*'()/"
SRC_RE = re.compile(rf'src=["\'](?!/versions/)([{ALLOWED}]+)["\']')
HREF_RE = re.compile(r'href=(["\'])((?!/(versions|resources)/)/[^"\']*)\1')
META_REDIR_RE = re.compile(r'content="0; url=(["\']?)(?!/(versions|resources)/|https?://)(/[^"\'>]*)\1')
LIVE_BTN_RE = re.compile(rf'href=["\']/versions/v[\w-]+/([{ALLOWED}]+)["\'](.*)>[Ll]ive [Vv]ersion</a>')


def generate_versions():
    """Responsible for generating the versions pages."""
    # Move templates to templates directory
    util.buildhelpers.move_templates(versions_config.module_name, versions_config.versions_templates_path)

    # Create resources and versions directories
    os.makedirs(site_config.resources_markdown_path, exist_ok=True)
    os.makedirs(versions_config.versions_markdown_path, exist_ok=True)

    # Ensure directories exist
    versions_config.prev_versions_deploy_folder = os.path.join(
        site_config.web_directory, versions_config.prev_versions_path
    )
    os.makedirs(versions_config.prev_versions_deploy_folder, exist_ok=True)

    with open("data/versions.json", "r") as f:
        versions = json.load(f)

    logger.info("Deploying preserved versions …")
    with cf.ThreadPoolExecutor() as executor:
        list(executor.map(deploy_previous_version, versions["previous"]))

    build_markdown(versions=versions)

    # write robots.txt to disallow crawlers
    os.makedirs(site_config.web_directory, exist_ok=True)
    with open(os.path.join(site_config.web_directory, "robots.txt"), "w", encoding="utf8") as robots:
        robots.write(
            f"User-agent: *\n"
            f"Disallow: {site_config.subdirectory}/previous/\n"
            f"Disallow: {site_config.subdirectory}/{versions_config.prev_versions_path}/"
        )


def deploy_current_version():
    """Build a permalink of the current version.

    This is only called by the search module's preserve_current_version().
    """
    versions_config.prev_versions_deploy_folder = os.path.join(
        site_config.web_directory, versions_config.prev_versions_path
    )

    with open("data/versions.json", "r") as f:
        version_data = json.load(f)["current"]

    version_path = version_data["name"].split(".")[0]
    version_full_path = os.path.join(versions_config.prev_versions_deploy_folder, version_path)

    os.makedirs(version_full_path, exist_ok=True)
    for item in os.listdir(site_config.web_directory):
        # skip versions directories when copying
        if item == "versions":
            continue
        # copy the current version into a preserved version
        src = os.path.join(site_config.web_directory, item)
        dest = os.path.join(version_full_path, item)
        # copy depending on file type
        if os.path.exists(dest):
            print(f"error copying {src}: path {dest} already exists | {item}")
        if os.path.isdir(src):
            shutil.copytree(src, dest)
        else:  # is file
            shutil.copy(src, dest)

    # run archival scripts
    archive(
        version_data=version_data,
        version_path=version_full_path,
        is_current=True,
    )


def create_tar_gz(source_dir, output_path):
    """Create a tar.gz archive from source_dir."""
    logger.info(f"Creating tar.gz archive: {output_path}")
    with tarfile.open(output_path, "w:gz") as tar:
        tar.add(source_dir, arcname=".")
    logger.info(f"Archive created: {output_path}")


def extract_tar_gz(archive_path, dest_path):
    """Extract a .tar.gz archive to dest_path."""
    os.makedirs(dest_path, exist_ok=True)
    with tarfile.open(archive_path, "r:gz") as tar:
        tar.extractall(path=dest_path)


def download_archive(url, local_path):
    """Download a website archive file from GitHub. Returns True if download succeeded."""
    try:
        logger.info(f"Downloading website archive from {url} to {local_path}")
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        with open(local_path, "wb") as f:
            f.write(r.content)
        logger.info(f"Successfully downloaded archive: {local_path}")
        return True
    except Exception as ex:
        logger.warning(f"Failed to download archive from {url}: {ex}")
        return False


def export_commit(commit: str, dest_path: str) -> None:
    """Materialise `commit` into `dest_path` using `git archive`.

    Equivalent to: git archive <commit> | tar -x -C <dest_path>
    """
    os.makedirs(dest_path, exist_ok=True)

    # Create a tar stream of the commit
    proc = subprocess.run(
        ["git", "archive", "--format=tar", commit],
        stdout=subprocess.PIPE,
        check=True,
    )
    # Extract the tar stream in-memory
    with tarfile.open(fileobj=io.BytesIO(proc.stdout)) as tar:
        tar.extractall(path=dest_path)


def export_git_archive_to_file(commit: str, output_path: Path) -> None:
    """Create a git archive file for the given commit."""
    logger.info(f"Creating git archive for commit {commit} > {output_path}")
    with open(output_path, "wb") as out:
        subprocess.run(
            ["git", "archive", "--format=tar.gz", commit],
            stdout=out,
            check=True,
        )
    logger.info(f"Git archive created: {output_path}")


def deploy_previous_version(version_data):
    """
    Build a version of the site to /prev_versions_path.

    Attempts to deploy using a local archive, then remote URL,
    falling back to git archive if neither is available.
    """
    version_name = version_data["name"]  # e.g. v16.1
    logger.info(f"Building website for ATT&CK {version_name}")

    vpath = version_name.split(".")[0]
    dest_path = os.path.join(versions_config.prev_versions_deploy_folder, vpath)

    # Find the archive directory to use based on environment variable or command line argument
    archive_dir = site_config.ATTACK_VERSION_ARCHIVES
    if site_config.args.version_archive_dir:
        archive_dir = site_config.args.version_archive_dir

    os.makedirs(archive_dir, exist_ok=True)
    archive_filename = f"website-{version_name}.tar.gz"
    archive_path = os.path.join(archive_dir, archive_filename)
    archive_url = (
        f"https://github.com/mitre-attack/attack-website/releases/download/archived-website-files/{archive_filename}"
    )

    if os.path.exists(archive_path):
        logger.info(f"{version_name}: extracting from local archive {archive_filename}")
        extract_tar_gz(archive_path=archive_path, dest_path=dest_path)
        return

    if download_archive(url=archive_url, local_path=archive_path):
        logger.info(f"{version_name}: extracting downloaded archive {archive_filename}")
        extract_tar_gz(archive_path=archive_path, dest_path=dest_path)
        return

    # this saves the cleaned up version archive for the future
    logger.warning(f"{version_name}: download failed, falling back to git archive")
    create_version_archive(version_data=version_data, output_dir=archive_dir)
    extract_tar_gz(archive_path=archive_path, dest_path=dest_path)


def process_html_file(path: str, version_url_path: str, is_current: bool, version_data: dict):
    """Rewrite one HTML file in place."""
    try:
        with open(path, "r", encoding="utf8") as f:
            html = f.read()

        ### regex replacements
        # replace links so that they properly point to where the version is stored
        html = SRC_RE.sub(lambda m: f'src="/{version_url_path}{m.group(1)}"', html)
        html = HREF_RE.sub(lambda m: f"href={m.group(1)}/{version_url_path}/{m.group(2)[1:]}{m.group(1)}", html)
        html = META_REDIR_RE.sub(
            lambda m: f'content="0; url=/{version_url_path}{"/" if m.group(3) == "/" else m.group(3)}'
            + (m.group(1) if m.group(1) else ""),
            html,
        )
        # update live version links on the versioning button
        html = LIVE_BTN_RE.sub(lambda m: f'href="/{m.group(1)}"{m.group(2)}>Live Version</a>', html)

        ### simple string replacements
        # update links to previous-versions to point to the main site instead of an archived page
        html = html.replace(f"/{version_url_path}/resources/previous-versions/", "/resources/versions/")
        html = html.replace(f"/{version_url_path}/resources/versions/", "/resources/versions/")
        # update links to updates to point to main site instead of archived page
        html = html.replace(f"/{version_url_path}/resources/updates/", "/resources/updates/")

        # update links to docs
        html = html.replace(f"/{version_url_path}/docs/", "/docs/")

        # update versioning button to show the permalink site version: "back to main site"
        html = html.replace("version-button live", "version-button permalink")
        # remove banner message if it is present
        html = html.replace("banner-message", "d-none")
        html = html.replace("under-development", "d-none")

        # banner injection
        if is_current:
            marking = (
                "Currently viewing "
                f'<a href="{version_data["cti_url"]}" target="_blank">'
                f"ATT&CK {version_data['name']}"
                "</a> "
                "which is the current version of ATT&CK."
            )
        else:
            marking = (
                "Currently viewing "
                f'<a href="{version_data["cti_url"]}" target="_blank">'
                f"ATT&CK {version_data['name']}"
                "</a> "
                f"which was live between {version_data['date_start']} and {version_data['date_end']}."
            )
        banner_html = (
            '<div class="container-fluid version-banner">'
            '<div class="icon-inline baseline mr-1">'
            f'<img src="/{version_url_path}/theme/images/icon-warning-24px.svg"></div>'
            f"{marking} "
            '<a href="/resources/versions/">Learn more about the versioning '
            'system</a> or <a href="/">see the live site</a>.</div>'
        )
        html = html.replace("<!-- !previous versions banner! -->", banner_html)
        html = html.replace("<!-- !versions banner! -->", banner_html)

        # Special case!
        if version_url_path == "versions/v13" and "techniques/T1037/004/index.html" in path:
            logger.info("REMOVING BROKEN LINK in /versions/v13/techniques/T1037/004/index.html")
            # Replace <a href="/versions/v13/techniques/T1053/004">Launchd</a> with Launchd
            # ATT&CK v13 somehow missed T1053.004 in the STIX and it was later brought back and deprecated
            html = re.sub(
                r'<a\s+href="/versions/v13/techniques/T1053/004"[^>]*>(.*?)</a>',
                r"\1",
                html,
                flags=re.IGNORECASE | re.DOTALL,
            )

        # overwrite with updated html
        with open(path, "w", encoding="utf8") as f:
            f.write(html)

    except Exception as e:
        logger.warning(f"Failed to process {path}: {e}")


def process_html_files(version_data: dict, version_path: str, is_current: bool = False):
    """Process all HTML files in a version directory."""
    version = version_data["name"].split(".")[0]
    version_url_path = f"versions/{version}"

    logger.info(f"{version}: rewriting html")

    worker = functools.partial(
        process_html_file, version_url_path=version_url_path, is_current=is_current, version_data=version_data
    )
    html_files = []
    for root, _, files in os.walk(version_path):
        html_files.extend(os.path.join(root, f) for f in files if f.endswith(".html"))

    with cf.ThreadPoolExecutor() as pool:
        pool.map(worker, html_files)


def process_search_files(version_data: dict, version_path: str):
    """Process search-related JavaScript files in a version directory."""
    version = version_data["name"].split(".")[0]
    version_url_path = f"versions/{version}"

    logger.info(f"{version}: rewriting search files")

    # tweak settings.js / for search capability. works for ATT&CK v7 onwards
    settings_path = os.path.join(version_path, "theme", "scripts", "settings.js")
    if os.path.exists(settings_path):
        with open(settings_path, "r", encoding="utf8") as sf:
            contents = sf.read()
        contents = re.sub(r'base_url ?= ?"(.+?)"', rf'base_url = "/{version_url_path}\1"', contents)
        contents = re.sub(r"tour_steps ?= .*?;", "tour_steps = {};", contents)
        with open(settings_path, "w", encoding="utf8") as sf:
            sf.write(contents)
    else:
        # legacy search path for ATT&CK version 6 and prior
        # NOTE: search.js and search_babelized.js are in v7-v12, but they don't need to be updated since settings.js is updated above
        for search_file_name in ["search.js", "search_babelized.js"]:
            search_file_path = os.path.join(version_path, "theme", "scripts", search_file_name)
            if os.path.exists(search_file_path):
                with open(search_file_path, "r", encoding="utf8") as f:
                    search_contents = f.read()
                search_contents = re.sub(
                    r'site_base_url ?= ?""', f'site_base_url = "/{version_url_path}"', search_contents
                )
                with open(search_file_path, "w", encoding="utf8") as f:
                    f.write(search_contents)


def saferemove(p):
    """Safely remove a file or directory."""
    if not os.path.exists(p):
        return
    if os.path.isfile(p):
        os.remove(p)
    elif os.path.isdir(p):
        shutil.rmtree(p)


def remove_unwanted_files(extract_dir):
    """Remove unnecessary files and directories from previous website version."""
    logger.info("Cleaning extracted archive (removing unnecessary files/folders)…")
    targets = [
        ".git",
        ".well-known",
        "beta",
        "docs",
        "mobile",
        "previous",
        "versions",
        "w",
        "wiki",
        "resources",
        "CNAME",
        "robots.txt",
        "assets.html",
        "campaigns.html",
        "groups.html",
        "software.html",
        "tactics.html",
        "techniques.html",
        "full-coverage.html",
        "macro-technique-refinement.html",
    ]
    for rel_path in targets:
        target_path = os.path.join(extract_dir, rel_path)
        saferemove(target_path)
    logger.info("Cleaning complete.")


def archive(version_data: dict, version_path: str, is_current: bool = False):
    """Post-process an exported version folder.

    – remove unnecessary files,
    – rewrite all HTML files (parallel),
    – tweak settings.js / search_bundle.js (kept from the old code).
    """
    remove_unwanted_files(extract_dir=version_path)
    process_html_files(version_data, version_path, is_current)
    process_search_files(version_data, version_path)
    fix_permissions(version_path)


def fix_permissions(root_dir):
    """Set directories to 755 and files to 644 recursively."""
    for dirpath, dirnames, filenames in os.walk(root_dir):
        os.chmod(dirpath, 0o755)
        for filename in filenames:
            os.chmod(os.path.join(dirpath, filename), 0o644)


def create_version_archive(version_data: dict, output_dir: str = "attack-version-archives"):
    """Create a cleaned archive for a specific version.

    This function is designed to be called from archive-website.py
    for batch processing versions into archives.
    """
    version_label = version_data["name"]
    commit_to_use = version_data["commit"]

    logger.info(f"--- Processing version {version_label} ---")

    cleaned_dir = Path(output_dir)
    cleaned_dir.mkdir(parents=True, exist_ok=True)

    cleaned_archive_name = f"website-{version_label}.tar.gz"
    cleaned_archive_path = cleaned_dir / cleaned_archive_name

    # main temp dir for extracted/cleaned contents
    with tempfile.TemporaryDirectory() as tmpdir:
        # dedicated temp dir for git archive tarball
        with tempfile.TemporaryDirectory() as archive_tmpdir:
            archive_tmp_path = Path(archive_tmpdir)
            git_archive_name = f"website-{version_label}-git-archive.tar.gz"
            git_archive_path = archive_tmp_path / git_archive_name

            export_git_archive_to_file(commit_to_use, git_archive_path)
            extract_tar_gz(git_archive_path, tmpdir)

        archive(version_data=version_data, version_path=tmpdir, is_current=False)

        create_tar_gz(tmpdir, cleaned_archive_path)

    logger.info(f"--- Finished version {version_label} ---\n")


def build_markdown(versions):
    """Build markdown for the versions list page."""
    # build urls
    versions["current"]["url"] = versions["current"]["name"].split(".")[0]
    versions["current"]["changelog_label"] = " ".join(versions["current"]["changelog"].split("-")[1:]).title()

    for versionGroup in ["previous", "older"]:  # apply transforms to both previous and older
        for version_data in versions[versionGroup]:
            version_data["url"] = version_data["name"].split(".")[0]
            version_data["changelog_label"] = " ".join(version_data["changelog"].split("-")[1:]).title()

    # sort previous versions by date
    versions_data = {
        "current": versions["current"],
        "previous": sorted(
            versions["previous"], key=lambda p: datetime.strptime(p["date_end"], "%B %d, %Y"), reverse=True
        ),
        "older": sorted(versions["older"], key=lambda p: datetime.strptime(p["date_end"], "%B %d, %Y"), reverse=True),
    }

    # build previous-versions page markdown
    subs = versions_config.versions_md + json.dumps(versions_data)
    with open(os.path.join(versions_config.versions_markdown_path, "versions.md"), "w", encoding="utf8") as md_file:
        md_file.write(subs)
