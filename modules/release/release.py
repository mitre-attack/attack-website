
from loguru import logger
from mitreattack.diffStix.changelog_helper import get_new_changelog_md
from mitreattack.download_stix import download_attack_stix
from modules import site_config

from . import release_config


def generate_release_changelog():
    old_version = site_config.args.release[0]
    new_version = site_config.args.release[1]
    create_changelogs(old_version, new_version)

def create_changelogs(old_version, new_version):
    output_folder = f"modules/resources/docs/changelogs/v{old_version}-v{new_version}"
    download_attack_stix(download_dir="attack-releases")
    get_new_changelog_md(
        domains=["enterprise-attack", "mobile-attack", "ics-attack"],
        layers=[
            f"{output_folder}/layer-enterprise.json",
            f"{output_folder}/layer-mobile.json",
            f"{output_folder}/layer-ics.json",
        ],
        old=f"attack-releases/stix-2.0/v{old_version}",
        new=f"attack-releases/stix-2.0/v{new_version}",
        show_key=True,
        # site_prefix: str = "",
        verbose=True,
        include_contributors=True,
        markdown_file=f"{output_folder}/changelog.md",
        html_file=f"{output_folder}/index.html",
        html_file_detailed=f"{output_folder}/changelog-detailed.html",
        json_file=f"{output_folder}/changelog.json",
    )
