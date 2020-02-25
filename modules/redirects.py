import os
from . import site_config
from . import stixhelpers
from . import util

def generate():
    """Responsible for verifying redirects directory and starting off
       markdown generation process
    """

    # Verify if directory exists
    if not os.path.isdir(config.redirects_markdown_path):
        os.mkdir(config.redirects_markdown_path)

    for domain in site_config.domains:
        generate_markdown_files(domain)
    
    # Generate image redirections
    generate_image_redirects()

    # Generate contribution redirections
    generate_contribute_redirect()

    # Generate training redirection
    generate_training_redirects()
    # Generate redirects not associated with any domain
    generate_misc_redirects()
    
def generate_markdown_files(domain):
    """Given a domain, changes all the old links to new redirected links"""

    # Reads the json attack STIX and creates a list of the ATT&CK Tactics

    for key in config.general_redirects_dict:
        objs = stixhelpers.get_all_of_type(config.ms[domain], key)
        for obj in objs:
            new_attack_id, old_attack_id = get_new_and_old_ids(obj)

            if new_attack_id:
                generate_obj_redirect(config.general_redirects_dict[key], new_attack_id, old_attack_id, domain)

                if obj.get('revoked'):

                    revoked_by_obj = stixhelpers.get_revoked_by(obj['id'], config.ms[domain])

                    if revoked_by_obj:
                        revoked_attack_id = util.get_attack_id(revoked_by_obj)

                        if revoked_attack_id:
                            generate_obj_redirect(config.general_redirects_dict[key], revoked_attack_id, old_attack_id, domain)

                            if old_attack_id != new_attack_id:
                                generate_obj_redirect(config.general_redirects_dict[key], revoked_attack_id, new_attack_id, domain)

    if domain == "mobile-attack":
        for key in config.mobile_redirect_dict:
            objs = stixhelpers.get_all_of_type(config.ms[domain], key)
            for obj in objs:
                new_attack_id, old_attack_id = get_new_and_old_ids(obj)

                if new_attack_id:
                    generate_obj_redirect(config.mobile_redirect_dict[key], new_attack_id, old_attack_id, domain)

    generate_other_redirects(domain)
    generate_tactic_redirects(domain)

def generate_image_redirects():
    """Responsible for generating image redirects markdown"""

    data = {}
    for image in config.redirects_images:

        data['title'] = image['old'].split("/")[2]
        data['redirect_link'] = image['new']
        data['path'] = config.redirects_images_path + image['old']

        subs = config.redirect_md.substitute(data)

        with open(os.path.join(config.redirects_markdown_path, data['title'] + ".md"), "w", encoding='utf8') as md_file:
            md_file.write(subs)

def generate_training_redirects():
    """Responsible for generating training redirect markdowns"""

    for training in config.training_redict_dict:
        subs = config.redirect_md.substitute(training)

        with open(os.path.join(config.redirects_markdown_path, training['title'] + ".md"), "w", encoding='utf8') as md_file:
            md_file.write(subs)
       
def generate_contribute_redirect():
    """Responsible for generating contribute redirects markdown"""

    with open(os.path.join(config.redirects_markdown_path, "Contributing_to_MITRE_ATTACK.md"), "w", encoding='utf8') as md_file:
        md_file.write(config.contributing_md)

def generate_tactic_redirects(domain):
    """Responsible for generating tactic redirects markdown"""

    tactics = stixhelpers.get_all_of_type(config.ms[domain], 'x-mitre-tactic')

    data = {}
    for tactic in tactics:

        attack_id = util.get_attack_id(tactic)

        if attack_id:

            data['title'] = tactic["name"].replace(' ', '_') + "-" + domain
            data['redirect_link'] = "/tactics/" + attack_id
            data['path'] = config.redirects_paths[domain] + tactic['name'].replace(' ', '_')

        subs = config.redirect_md.substitute(data)

        with open(os.path.join(config.redirects_markdown_path, data['title'] + ".md"), "w", encoding='utf8') as md_file:
            md_file.write(subs)

def generate_other_redirects(domain):
    """Responsible for generation of redirects for old site's URLs that aren't
       individual objects
    """

    data = {}
    for redirect in config.redirects_domain[domain]:

        data['title'] = redirect['old'] + "-" + domain
        data['redirect_link'] = redirect['new']
        data['path'] = config.redirects_paths[domain] + redirect['old']

        subs = config.redirect_md.substitute(data)

        # Write redirect page for a single object
        with open(os.path.join(config.redirects_markdown_path, data['title'] + ".md"), "w", encoding='utf8') as md_file:
            md_file.write(subs)

def generate_misc_redirects():
    """generate redirects not associated with any domain"""
    for redirect in config.other_redirects:
        data = {}
        data["title"] = "-".join(redirect["from"].split("/"))
        data["redirect_link"] = redirect["to"]
        data['path'] =redirect['from']

        subs = config.redirect_md.substitute(data)

        with open(os.path.join(config.redirects_markdown_path, data['title'] + ".md"), "w", encoding='utf8') as md_file:
            md_file.write(subs)

def generate_obj_redirect(redirect_link, new_attack_id, old_attack_id, domain):
    """Responsible for generating redirects markdown for given data"""

    data = {}

    data['title'] = old_attack_id
    data['redirect_link'] =  "/" + redirect_link['new'] + "/" + new_attack_id
    data['path'] = config.redirects_paths[domain] + redirect_link['old'] + "/" + old_attack_id 

    subs = config.redirect_md.substitute(data)

    with open(os.path.join(config.redirects_markdown_path, data['title'] + ".md"), "w", encoding='utf8') as md_file:
        md_file.write(subs)

    if new_attack_id != old_attack_id:
        data['path'] = redirect_link['new'] + "/" + old_attack_id

        subs = config.redirect_md.substitute(data)

        with open(os.path.join("content/pages", redirect_link["new"], data['title'] + ".md"), "w", encoding='utf8') as md_file:
            md_file.write(subs)


def get_new_and_old_ids(obj):
    """Given an object, return current or new ATT&CK id and old ATT&CK
       id if there is one
    """

    new_attack_id = util.get_attack_id(obj)
    if new_attack_id:
        if obj.get('x_mitre_old_attack_id'):
            old_attack_id = obj['x_mitre_old_attack_id']
        else:
            old_attack_id = new_attack_id
    else:
        old_attack_id = None

    return new_attack_id, old_attack_id
