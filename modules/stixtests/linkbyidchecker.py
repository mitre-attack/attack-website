import os
import re

import stix2
from loguru import logger
from tabulate import tabulate

from modules import site_config, util

from . import stixtests_config


def linkbyid_check():
    """Check for broken LinkByIds in STIX objects."""
    # this gets non-deprecated domains: enterprise, mobile for now. ics soon. skips pre
    non_deprecated_stix_memory_stores = util.relationshipgetters.get_srcs()

    all_stix_objects = []
    for memory_store in non_deprecated_stix_memory_stores:
        stix_objects_in_domain = memory_store.query()
        all_stix_objects.extend(stix_objects_in_domain)

    stix_types_that_should_have_attack_ids = (
        # STIX 2.0
        stix2.v20.sdo.AttackPattern,
        stix2.v20.sdo.CourseOfAction,
        stix2.v20.sdo.IntrusionSet,
        stix2.v20.sdo.Malware,
        stix2.v20.sdo.Tool,
        # STIX 2.1
        stix2.v21.sdo.AttackPattern,
        stix2.v21.sdo.CourseOfAction,
        stix2.v21.sdo.IntrusionSet,
        stix2.v21.sdo.Malware,
        stix2.v21.sdo.Tool,
    )
    custom_stix_types_that_should_have_attack_ids = (
        "x-mitre-data-source",
        "x-mitre-tactic",
    )

    all_attack_ids = []
    stix_id_to_attack_id = {}
    stix_id_to_stix_object = {}
    all_data_components = []
    for stix_object in all_stix_objects:
        _id = stix_object["id"]

        stix_id_to_stix_object[_id] = stix_object

        external_references = stix_object.get("external_references")
        if isinstance(stix_object, stix_types_that_should_have_attack_ids) or _id.startswith(
            custom_stix_types_that_should_have_attack_ids
        ):
            if external_references:
                if "external_id" in external_references[0]:
                    attack_id = external_references[0]["external_id"]
                    stix_id = _id

                    all_attack_ids.append(attack_id)
                    stix_id_to_attack_id[stix_id] = attack_id
            else:
                logger.error(f"STIX object does not have an expected ATT&CK ID: {_id}")

        if _id.startswith("x-mitre-data-component"):
            all_data_components.append(stix_object)

    data_component_stix_id_to_datasource_attack_id = {}
    for data_component in all_data_components:
        data_source_stix_id = data_component["x_mitre_data_source_ref"]
        data_source_attack_id = stix_id_to_attack_id[data_source_stix_id]
        data_component_stix_id_to_datasource_attack_id[data_component["id"]] = data_source_attack_id

    # when searching for these regexes, be sure to ignore the case
    old_linkbyid_syntax = r"{{LinkById\|(.*?)}}"
    new_linkbyid_syntax = r"\(LinkById: (.*?)\)"

    link_by_id_warnings = []
    for stix_object in all_stix_objects:
        _id = stix_object.get("id")
        name = stix_object.get("name")
        description = stix_object.get("description")
        external_references = stix_object.get("external_references")
        is_subtechnique = stix_object.get("x_mitre_is_subtechnique")

        attack_id = None
        if external_references:
            if "external_id" in external_references[0]:
                attack_id = external_references[0]["external_id"]

        pretty_name = ""
        if isinstance(stix_object, stix2.v21.sro.Relationship):
            source = stix_object["source_ref"]
            target = stix_object["target_ref"]

            if source.startswith("x-mitre-data-component"):
                source_attack_id = data_component_stix_id_to_datasource_attack_id[source]
            else:
                source_attack_id = stix_id_to_attack_id[source]

            target_attack_id = stix_id_to_attack_id[target]

            url = util.stixhelpers.get_url_from_stix(
                stix_object=stix_id_to_stix_object[source], is_subtechnique=is_subtechnique
            )

            if url:
                pretty_name = f"[{source_attack_id}]({url})'s relationship to {target_attack_id}"
            else:
                pretty_name = f"{source_attack_id}'s relationship to {target_attack_id}"
        else:
            if name:
                url = util.stixhelpers.get_url_from_stix(stix_object=stix_object, is_subtechnique=is_subtechnique)
                if url:
                    pretty_name = f"[{attack_id}]({url}) {name}"
                else:
                    pretty_name = f"[{attack_id}] {name}"
            else:
                pretty_name = f"[{attack_id}] {_id}"

        if description:
            attack_ids_in_description = re.findall(old_linkbyid_syntax, description, re.IGNORECASE)
            for attack_id_in_description in attack_ids_in_description:
                # These warnings are for using the old {{LinkById|X0000}} syntax
                warning = {
                    "Object with broken data": pretty_name,
                    "Section found in": "Description",
                    # sort of abusing "Unknown LinkById" here, but it works well enough
                    "Unknown LinkById": f"{{{{LinkById\|{attack_id_in_description}}}}}",
                }
                link_by_id_warnings.append(warning)

            # add in any ATT&CK IDs found from the newer (LinkById: X0000) syntax
            attack_ids_in_description.extend(re.findall(new_linkbyid_syntax, description, re.IGNORECASE))
            for attack_id_in_description in attack_ids_in_description:
                # These ATT&CK IDs are referenced in the description, but not found anywhere!
                if attack_id_in_description not in all_attack_ids:
                    warning = {
                        "Object with broken data": pretty_name,
                        "Section found in": "Description",
                        "Unknown LinkById": attack_id_in_description,
                    }
                    link_by_id_warnings.append(warning)

    exit_code = write_report(
        report_file=os.path.join(site_config.test_report_directory, stixtests_config.linkbyids_report_filename),
        report_title="Broken LinkByIds Report",
        broken_items=link_by_id_warnings,
    )

    # Return exit code and how many broken LinkByIds were found
    return exit_code, len(link_by_id_warnings)


def write_report(report_file, report_title, broken_items):
    # logger.info(f"Writing report: {report_title}")
    with open(report_file, "w") as f:
        f.write(f"{report_title}:\n\n")

        if broken_items:
            f.write(f"{len(broken_items)} LinkByIDs could not be parsed:\n\n")
            f.write(tabulate(broken_items, headers="keys", tablefmt="github"))
            exit_code = stixtests_config.BROKEN_LINKBYID
        else:
            f.write("No broken citations found\n")
            exit_code = stixtests_config.SUCCESS

    return exit_code
