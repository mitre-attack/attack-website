import argparse

from dotenv import load_dotenv
from loguru import logger
from mitreattack.diffStix.changelog_helper import get_new_changelog_md
from mitreattack.download_stix import download_attack_stix

load_dotenv()

def get_parsed_args():
    """Create argument parser and parse arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Build the ATT&CK website changelogs between two versions.\n"
            "Provide the old ATT&CK version and the new ATT&CK version.\n"
            "Example usage - python3 generate_changelog.py 16.0 16.1"
        )
    )
    
    parser.add_argument(
        "old_version",
        help="Old ATT&CK version number. Example: '16.0'."
    )
    parser.add_argument(
        "new_version",
        help="New ATT&CK version number. Example: '16.1'."
    )   
    args = parser.parse_args()

    return args

def generate_release_changelog(args):
    old_version = args.old_version
    new_version = args.new_version
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
        html_file_detailed=f"{output_folder}/changelog-detailed.html",
        json_file=f"{output_folder}/changelog.json",
    )

if __name__ == "__main__":
    # Get args
    args = get_parsed_args()

    generate_release_changelog(args)
    
    logger.debug(f"Changelog between {args.old_version} and {args.new_version} created")
