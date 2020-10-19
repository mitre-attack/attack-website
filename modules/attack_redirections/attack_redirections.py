import os
import uuid
from modules import site_config
from modules import util
from . import attack_redirections_config

def generate_attack_redirections():
    """Responsible for verifying redirects directory and starting off
       markdown generation process
    """

    # Create content pages directory if does not already exist
    util.buildhelpers.create_content_pages_dir()

    # Verify if directory exists
    if not os.path.isdir(site_config.redirects_markdown_path):
        os.mkdir(site_config.redirects_markdown_path)

    # Generate redirections
    util.buildhelpers.generate_redirections(attack_redirections_config.attack_redirections_location)

    for domain in site_config.domains:
        generate_markdown_files(domain)
    
def generate_markdown_files(domain):
    """Given a domain, changes all the old links to new redirected links"""

    # Reads the json attack STIX and creates a list of the ATT&CK Tactics

    ms = util.relationshipgetters.get_ms()

    for key in attack_redirections_config.general_redirects_dict:
        objs = util.stixhelpers.get_all_of_type(ms[domain], key)
        for obj in objs:
            new_attack_id, old_attack_id = get_new_and_old_ids(obj)

            if new_attack_id:
                if obj.get('revoked'):

                    revoked_by_obj = util.stixhelpers.get_revoked_by(obj['id'], ms[domain])

                    if revoked_by_obj:
                        revoked_attack_id = util.buildhelpers.get_attack_id(revoked_by_obj)

                        if revoked_attack_id:
                            generate_obj_redirect(attack_redirections_config.general_redirects_dict[key], revoked_attack_id, old_attack_id, domain)

                            if old_attack_id != new_attack_id:
                                generate_obj_redirect(attack_redirections_config.general_redirects_dict[key], revoked_attack_id, new_attack_id, domain)
                else:
                    generate_obj_redirect(attack_redirections_config.general_redirects_dict[key], new_attack_id, old_attack_id, domain)

    if domain == "mobile-attack":
        for key in attack_redirections_config.mobile_redirect_dict:
            objs = util.stixhelpers.get_all_of_type(ms[domain], key)
            for obj in objs:
                new_attack_id, old_attack_id = get_new_and_old_ids(obj)

                if new_attack_id:
                    generate_obj_redirect(attack_redirections_config.mobile_redirect_dict[key], new_attack_id, old_attack_id, domain)

    generate_tactic_redirects(ms, domain)


def generate_tactic_redirects(ms, domain):
    """Responsible for generating tactic redirects markdown"""

    tactics = util.stixhelpers.get_all_of_type(ms[domain], 'x-mitre-tactic')

    data = {}
    for tactic in tactics:

        attack_id = util.buildhelpers.get_attack_id(tactic)

        if attack_id:

            data['title'] = tactic["name"].replace(' ', '_') + "-" + domain + str(uuid.uuid1())
            data['to'] = "/tactics/" + attack_id
            data['from'] = attack_redirections_config.redirects_paths[domain] + tactic['name'].replace(' ', '_')

        subs = site_config.redirect_md.substitute(data)

        with open(os.path.join(site_config.redirects_markdown_path, data['title'] + ".md"), "w", encoding='utf8') as md_file:
            md_file.write(subs)

def generate_obj_redirect(redirect_link, new_attack_id, old_attack_id, domain):
    """Responsible for generating redirects markdown for given data"""

    data = {}

    data['title'] = old_attack_id + str(uuid.uuid1())

    # Check if new id or old id are subtechniques and change to redirection format
    if(util.buildhelpers.is_sub_tid(new_attack_id)):
        new_attack_id = util.buildhelpers.redirection_subtechnique(new_attack_id)
    
    if(util.buildhelpers.is_sub_tid(old_attack_id)):
        old_attack_id = util.buildhelpers.redirection_subtechnique(old_attack_id)

    data['to'] =  "/" + redirect_link['new'] + "/" + new_attack_id
    data['from'] = attack_redirections_config.redirects_paths[domain] + redirect_link['old'] + "/" + old_attack_id 

    subs = site_config.redirect_md.substitute(data)

    with open(os.path.join(site_config.redirects_markdown_path, data['title'] + ".md"), "w", encoding='utf8') as md_file:
        md_file.write(subs)

    if new_attack_id != old_attack_id:
        data['from'] = redirect_link['new'] + "/" + old_attack_id

        subs = site_config.redirect_md.substitute(data)

        with open(os.path.join(site_config.redirects_markdown_path, redirect_link["new"] + data['title'] + ".md"), "w", encoding='utf8') as md_file:
            md_file.write(subs)

def get_new_and_old_ids(obj):
    """Given an object, return current or new ATT&CK id and old ATT&CK
       id if there is one
    """

    new_attack_id = util.buildhelpers.get_attack_id(obj)
    if new_attack_id:
        if obj.get('x_mitre_old_attack_id'):
            old_attack_id = obj['x_mitre_old_attack_id']
        else:
            old_attack_id = new_attack_id
    else:
        old_attack_id = None

    return new_attack_id, old_attack_id