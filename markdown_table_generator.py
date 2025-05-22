# Parameters to provide
major_version_change = ["16.1", "17.0"]
# Use for point releases
minor_version_change = ["17.0", "17.1"] 


version = "[ATT&CK v17](/versions/v17)"
start_date = "April 22, 2025"
end_date = "Current version of ATT&CK"


def generate_table(version, start_date, end_date, data_links, changelog_links):
    """Use to create markdown tables for the changelog."""
    formatted_data = " <br /> ".join(data_links)
    formatted_changelogs = " <br /> ".join(changelog_links)
    
    # Create the table
    table = f"""
                | Version | Start Date | End Date | Data | Changelogs |
                |:--------|:-----------|:---------|:-----|:-----------|
                | {version} | {start_date} | {end_date}  | {formatted_data} | {formatted_changelogs} |
            """
    return table.strip()

# Provide lists of links for data and changelogs
data_links = [
    f"[v{major_version_change[1]} on MITRE/CTI](https://github.com/mitre/cti/releases/tag/ATT%26CK-v{major_version_change[1]})",
    # Use for point releases
    f"[v{minor_version_change[1]} on MITRE/CTI](https://github.com/mitre/cti/releases/tag/ATT%26CK-v{minor_version_change[1]})"
]

changelog_links = [
    f"{major_version_change[0]} - {minor_version_change[0]} [Details](/docs/changelogs/v{major_version_change[0]}-v{minor_version_change[0]}/changelog-detailed.html) ([JSON](/docs/changelogs/v{major_version_change[0]}-v{minor_version_change[0]}/changelog.json))",
    # Use for point releases
    f"{major_version_change[1]} - {minor_version_change[1]} [Details](/docs/changelogs/v{major_version_change[1]}-v{minor_version_change[1]}/changelog-detailed.html) ([JSON](/docs/changelogs/v{major_version_change[1]}-v{minor_version_change[1]}/changelog.json))",
]

# Generate and print the table
print(generate_table(version, start_date, end_date, data_links, changelog_links))