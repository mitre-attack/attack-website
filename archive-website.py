import json
import multiprocessing
import os

from loguru import logger

from modules.versions.versions import create_version_archive

ARCHIVE_DIR = "attack-version-archives"


def main():
    """Process previous versions of ATT&CK website."""
    with open("data/versions.json", "r") as f:
        version_json = json.load(f)

    logger.info("Processing previous versions of ATT&CK website")

    processes = []
    for version_data in version_json["previous"]:
        archive_path = os.path.join(ARCHIVE_DIR, f"website-{version_data['name']}.tar.gz")
        if os.path.exists(archive_path):
            logger.info(f"Archive already exists for {version_data['name']}: {archive_path} -- skipping.")
            continue

        p = multiprocessing.Process(
            target=create_version_archive,
            args=(version_data, ARCHIVE_DIR),
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
