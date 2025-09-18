import argparse
import json
import multiprocessing
import os

from loguru import logger

from modules.versions.versions import create_version_archive


def main():
    """Process previous versions of ATT&CK website."""
    parser = argparse.ArgumentParser(
        description="Process previous versions of ATT&CK website and create version archives"
    )
    parser.add_argument(
        "--archive-dir",
        "-a",
        default="attack-version-archives",
        help="Directory where version archives will be created (default: attack-version-archives)",
    )

    args = parser.parse_args()
    archive_dir = args.archive_dir

    # Create archive directory if it doesn't exist
    os.makedirs(archive_dir, exist_ok=True)

    with open("data/versions.json", "r") as f:
        version_json = json.load(f)

    logger.info(f"Processing previous versions of ATT&CK website to {archive_dir}")

    processes = []
    for version_data in version_json["previous"]:
        archive_path = os.path.join(archive_dir, f"website-{version_data['name']}.tar.gz")
        if os.path.exists(archive_path):
            logger.info(f"Archive already exists for {version_data['name']}: {archive_path} -- skipping.")
            continue

        p = multiprocessing.Process(
            target=create_version_archive,
            args=(version_data, archive_dir),
            name=f"Process-{version_data['name']}",
        )
        processes.append(p)
        p.start()
        logger.info(f"Started process for {version_data['name']} (PID: {p.pid})")

    for p in processes:
        p.join()
        logger.info(f"Process {p.name} for version finished (PID: {p.pid})")

    logger.info("All versions processed")


if __name__ == "__main__":
    main()
