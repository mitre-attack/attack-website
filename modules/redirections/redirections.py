import os
import uuid

from loguru import logger

from modules import site_config, util

from . import redirections_config


def generate_redirections():
    """Responsible for verifying redirects directory and starting off markdown generation process."""
    # Create content pages directory if does not already exist
    util.buildhelpers.create_content_pages_dir()

    # Verify if directory exists
    if not os.path.isdir(site_config.redirects_markdown_path):
        os.mkdir(site_config.redirects_markdown_path)

    # Generate redirections
    util.buildhelpers.generate_redirections(
        redirections_filename=redirections_config.redirections_location, redirect_md=site_config.redirect_md_index
    )

    for domain in site_config.domains:
        if domain["deprecated"] or (redirections_config.redirects_paths.get(domain["name"]) == None):
            continue
        generate_markdown_files(domain["name"])


def generate_markdown_files(domain):
    """Given a domain, changes all the old links to new redirected links."""
    # Reads the json attack STIX and creates a list of the ATT&CK Tactics
    ms = util.relationshipgetters.get_ms()

    for types in redirections_config.general_redirects_types:
        objs = util.stixhelpers.get_all_of_type(ms[domain], types)
        for obj in objs:
            new_attack_id, old_attack_id = get_new_and_old_ids(obj)

            if new_attack_id:
                if obj.get("revoked"):
                    revoked_by_obj = util.stixhelpers.get_revoked_by(obj["id"], ms[domain])

                    if revoked_by_obj:
                        revoked_attack_id = util.buildhelpers.get_attack_id(revoked_by_obj)

                        if revoked_attack_id:
                            generate_obj_redirect(
                                redirect_link=redirections_config.general_redirects_dict[types[0]],
                                new_attack_id=revoked_attack_id,
                                old_attack_id=old_attack_id,
                                domain=domain,
                            )

                            if old_attack_id != new_attack_id:
                                generate_obj_redirect(
                                    redirect_link=redirections_config.general_redirects_dict[types[0]],
                                    new_attack_id=revoked_attack_id,
                                    old_attack_id=new_attack_id,
                                    domain=domain,
                                )
                else:
                    generate_obj_redirect(
                        redirect_link=redirections_config.general_redirects_dict[types[0]],
                        new_attack_id=new_attack_id,
                        old_attack_id=old_attack_id,
                        domain=domain,
                    )

    if domain == "mobile-attack":
        for types in redirections_config.mobile_redirect_types_dict:
            objs = util.stixhelpers.get_all_of_type(ms[domain], types)
            for obj in objs:
                new_attack_id, old_attack_id = get_new_and_old_ids(obj)

                if new_attack_id:
                    generate_obj_redirect(
                        redirections_config.mobile_redirect_dict[types[0]], new_attack_id, old_attack_id, domain
                    )

    generate_tactic_redirects(ms, domain)
    generate_datasource_redirects(ms, domain)


def generate_tactic_redirects(ms, domain):
    """Responsible for generating tactic redirects markdown."""
    tactics = util.stixhelpers.get_all_of_type(ms[domain], ["x-mitre-tactic"])

    data = {}
    for tactic in tactics:
        attack_id = util.buildhelpers.get_attack_id(tactic)

        if attack_id:
            clean_tactic_name = tactic["name"].replace(" ", "_")
            old_site_prefix = redirections_config.redirects_paths[domain]
            redirect_title = f"{clean_tactic_name}-{domain}-{uuid.uuid1()}"

            data = {
                "title": redirect_title,
                "from": f"{old_site_prefix}{clean_tactic_name}",
                "to": f"/tactics/{attack_id}",
            }

        subs = site_config.redirect_md_index.substitute(data)

        with open(
            os.path.join(site_config.redirects_markdown_path, data["title"] + ".md"), "w", encoding="utf8"
        ) as md_file:
            md_file.write(subs)


def generate_datasource_redirects(ms, domain):
    """Responsible for generating data source redirects markdown."""
    datasources = util.stixhelpers.get_all_of_type(ms[domain], ["x-mitre-data-source"])

    data = {}
    for ds in datasources:
        ext_refs = ds.get("external_references")
        if ext_refs:
            i = util.buildhelpers.find_index_id(ext_refs)
            if i != util.buildhelpers.util_config.NOT_FOUND:
                attack_id = ext_refs[i]["external_id"]
                invalid_url = "data-sources" in ext_refs[i]["url"]

                if not invalid_url:
                    continue  # skip this datasource

                ds_redirect_title = f"{attack_id}-{uuid.uuid1()}"
                data = {
                    "title": ds_redirect_title,
                    "from": f"data-sources/{attack_id}",
                    "to": f"/datasources/{attack_id}",
                }

        subs = site_config.redirect_md_index.substitute(data)
        with open(
            os.path.join(site_config.redirects_markdown_path, data["title"] + ".md"), "w", encoding="utf8"
        ) as md_file:
            md_file.write(subs)


def generate_obj_redirect(redirect_link, new_attack_id, old_attack_id, domain):
    """Responsible for generating redirects markdown for given data."""
    data = {}

    data["title"] = old_attack_id + str(uuid.uuid1())

    # Check if new id or old id are subtechniques and change to redirection format
    if util.buildhelpers.is_sub_tid(new_attack_id):
        new_attack_id = util.buildhelpers.redirection_subtechnique(new_attack_id)

    if util.buildhelpers.is_sub_tid(old_attack_id):
        old_attack_id = util.buildhelpers.redirection_subtechnique(old_attack_id)

    data["to"] = f"/{redirect_link['new']}/{new_attack_id}"
    data["from"] = f"{redirections_config.redirects_paths[domain]}{redirect_link['old']}/{old_attack_id}"

    subs = site_config.redirect_md_index.substitute(data)

    redirect_file = os.path.join(site_config.redirects_markdown_path, f"{data['title']}.md")
    with open(redirect_file, "w", encoding="utf8") as md_file:
        md_file.write(subs)

    if new_attack_id != old_attack_id:
        data["from"] = f"{redirect_link['new']}/{old_attack_id}"

        subs = site_config.redirect_md_index.substitute(data)

        redirect_file = os.path.join(site_config.redirects_markdown_path, f"{redirect_link['new']}{data['title']}.md")
        with open(redirect_file, "w", encoding="utf8") as md_file:
            md_file.write(subs)


def get_new_and_old_ids(obj):
    """Given an object, return current or new ATT&CK id and old ATT&CK id if there is one."""
    new_attack_id = util.buildhelpers.get_attack_id(obj)
    if new_attack_id:
        if obj.get("x_mitre_old_attack_id"):
            old_attack_id = obj["x_mitre_old_attack_id"]
        else:
            old_attack_id = new_attack_id
    else:
        old_attack_id = None

    return new_attack_id, old_attack_id
