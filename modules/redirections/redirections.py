import os
import uuid

from modules import site_config, util

from . import redirections_config


def generate_redirections() -> None:
    """Responsible for verifying redirects directory and starting off markdown generation process."""
    # Create content pages directory if does not already exist
    util.buildhelpers.create_content_pages_dir()

    # Verify if directory exists
    if not os.path.isdir(site_config.redirects_markdown_path):
        os.mkdir(site_config.redirects_markdown_path)

    # Generate redirections from json file
    util.buildhelpers.generate_redirections(
        redirections_filename=redirections_config.redirections_location, redirect_md=site_config.redirect_md_index
    )

    generated_save_as = set()

    for domain in site_config.domains:
        if domain["deprecated"]:
            continue
        generate_markdown_files(domain=domain["name"], generated_save_as=generated_save_as)


def generate_markdown_files(domain, generated_save_as) -> None:
    """Given a domain, changes all the old links to new redirected links."""
    # Reads the json attack STIX and creates a list of the ATT&CK Tactics
    ms = util.relationshipgetters.get_ms()

    for types in redirections_config.general_redirects_types:
        objs = util.stixhelpers.get_all_of_type(src=ms[domain], types=types)
        for obj in objs:
            # new_attack_id, old_attack_id = get_new_and_old_ids(obj=obj)

            attack_id = util.buildhelpers.get_attack_id(object=obj)

            # x_mitre_old_attack_id is a custom STIX field only set on Technique objects that were originally in PRE-ATT&CK
            pre_attack_id = obj.get("x_mitre_old_attack_id", None)

            if obj.get("revoked"):
                revoked_by_obj = util.stixhelpers.get_revoked_by(stix_id=obj["id"], src=ms[domain])

                if revoked_by_obj:
                    revoked_attack_id = util.buildhelpers.get_attack_id(object=revoked_by_obj)

                    if revoked_attack_id:
                        generate_obj_redirect(
                            redirect_link=redirections_config.general_redirects_dict[types[0]],
                            domain=domain,
                            old_attack_id=old_attack_id,
                            new_attack_id=revoked_attack_id,
                            generated_save_as=generated_save_as,
                        )

                        if old_attack_id != new_attack_id:
                            generate_obj_redirect(
                                redirect_link=redirections_config.general_redirects_dict[types[0]],
                                domain=domain,
                                old_attack_id=new_attack_id,
                                new_attack_id=revoked_attack_id,
                                generated_save_as=generated_save_as,
                            )
            else:
                generate_obj_redirect(
                    redirect_link=redirections_config.general_redirects_dict[types[0]],
                    domain=domain,

                    attack_id=attack_id,

                    old_attack_id=old_attack_id,
                    new_attack_id=new_attack_id,

                    generated_save_as=generated_save_as,

                    pre_attack_id=pre_attack_id,
                )

    if domain == "mobile-attack":
        for types in redirections_config.mobile_redirect_types_dict:
            objs = util.stixhelpers.get_all_of_type(src=ms[domain], types=types)
            for obj in objs:
                new_attack_id, old_attack_id = get_new_and_old_ids(obj=obj)

                if new_attack_id:
                    generate_obj_redirect(
                        redirect_link=redirections_config.mobile_redirect_dict[types[0]],
                        domain=domain,
                        old_attack_id=old_attack_id,
                        new_attack_id=new_attack_id,
                        generated_save_as=generated_save_as,
                    )


def _write_redirect_file(data, generated_save_as) -> None:
    save_as = f"{data['from']}/index.html"
    if save_as in generated_save_as:
        return

    generated_save_as.add(save_as)

    subs = site_config.redirect_md_index.substitute(data)
    redirect_file = os.path.join(site_config.redirects_markdown_path, f"{data['title']}.md")
    with open(redirect_file, "w", encoding="utf8") as md_file:
        md_file.write(subs)


def generate_obj_redirect(redirect_link, domain, attack_id, generated_save_as, pre_attack_id=None) -> None:
    """Responsible for generating redirects markdown for given data."""
    data = {}

    if pre_attack_id:
        data["title"] = pre_attack_id + str(uuid.uuid1())
        if util.buildhelpers.is_sub_tid(sub_tid=pre_attack_id):
            pre_attack_id_url_safe = util.buildhelpers.redirection_subtechnique(sub_tid=pre_attack_id)
    else:
        data["title"] = attack_id + str(uuid.uuid1())

    # Check if old id or new id are subtechniques and change to redirection format
    if util.buildhelpers.is_sub_tid(sub_tid=attack_id):
        old_attack_id_url_safe = util.buildhelpers.redirection_subtechnique(sub_tid=attack_id)

    data["to"] = f"/{redirect_link['new']}/{new_attack_id}"

    # Redirect old mediawiki url patterns to current website patterns
    if domain in redirections_config.redirects_paths:
        data["from"] = f"{redirections_config.redirects_paths[domain]}{redirect_link['old']}/{old_attack_id}"
        _write_redirect_file(data=data, generated_save_as=generated_save_as)

    if old_attack_id != new_attack_id:
        data["from"] = f"{redirect_link['new']}/{old_attack_id}"
        redirect_file = os.path.join(site_config.redirects_markdown_path, f"{redirect_link['new']}{data['title']}.md")
        data["title"] = os.path.splitext(os.path.basename(redirect_file))[0]
        _write_redirect_file(data=data, generated_save_as=generated_save_as)


def get_new_and_old_ids(obj):
    """Given a STIX object."""
    new_attack_id = util.buildhelpers.get_attack_id(object=obj)
    if new_attack_id:
        if obj.get("x_mitre_old_attack_id"):
            old_attack_id = obj["x_mitre_old_attack_id"]
        else:
            old_attack_id = new_attack_id
    else:
        old_attack_id = None

    return new_attack_id, old_attack_id
