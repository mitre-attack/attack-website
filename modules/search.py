"""Builds search indexes for lunr.js"""
import collections
import json
import os
from lunr import lunr
from .util import find_index_id
from .stixhelpers import get_tactic_list, get_examples, get_techniques
from stix2 import MemoryStore
from . import config


def generate_index():
    delimiter = "|||"

    documents = []
    for mitigation in config.mitigation_list:
        document = {}
        url = get_url(mitigation)

        if url:
            if mitigation.get('x_mitre_deprecated') or mitigation.get('revoked'):
                continue
            document['id'] = mitigation['external_references'][0]['external_id']
            document['key'] = url + delimiter + mitigation['name'] + " (ID: " + document['id'] + ")"
            document['title'] = mitigation['name']
            document['body'] = mitigation['description'].replace("<code>", "").replace("</code>", "").replace("<br>", "").replace("</br>", "")
            document['detection'] = ""
            document['contributors'] = ""
            document['examples'] = ""
            document['aliases'] = ""

            if len(list(filter(lambda otherdoc: otherdoc["key"] == document["key"], documents))) == 0:
                documents.append(document)
    for group in config.group_list:
        document = {}
        url = get_url(group)

        if url:
            if group.get('x_mitre_deprecated') or group.get('revoked'):
                continue
            document['id'] = group['external_references'][0]['external_id']
            document['key'] = url + delimiter + group['name'] + " (ID: " + document['id'] + ")"
            document['title'] = group['name']
            document['body'] = group['description'].replace("<code>", "").replace("</code>", "").replace("<br>", "").replace("</br>", "")
            document['detection'] = ""
            document['contributors'] = ""
            document['examples'] = ""

            if 'x_mitre_old_attack_id' in group:
                document['key'] = url + delimiter + group['name'] + " (ID: " + document['id'] + ', old ID: ' + \
                                  group['x_mitre_old_attack_id'] + ")"
                document['id'] += ', ' + group['x_mitre_old_attack_id']

            if 'x_mitre_contributors' in group:
                for contributor in group['x_mitre_contributors']:
                    document['contributors'] += contributor + ', '
                document['contributors'] = document['contributors'][:-2]

            document['aliases'] = ""
            group_aliases = group['aliases'][1:]
            if len(group_aliases) > 0:
                if len(group_aliases) > 1:
                    document['key'] = document['key'] + " (Assoc. Groups: "
                else:
                    document['key'] = document['key'] + " (Assoc. Group: "

                for alias in group_aliases:
                    document['aliases'] = document['aliases'] + alias + "\n"
                    document['key'] = document['key'] + alias + ", "
                document['key'] = document['key'][:-2] + ")"
            document['aliases'] = document['aliases'][:-1]
            documents.append(document)

    for sw in config.software_list:
        document = {}
        url = get_url(sw)
        if url:
            if sw.get('x_mitre_deprecated') or sw.get('revoked'):
                continue
            document['id'] = sw['external_references'][0]['external_id']
            document['key'] = url + delimiter + sw['name'] + " (ID: " + document['id'] + ")"
            document['title'] = sw['name']
            document['body'] = sw['description'].replace("<code>", "").replace("</code>", "").replace("<br>", "").replace("</br>", "")
            document['detection'] = ""
            document['contributors'] = ""
            document['examples'] = ""

            if 'x_mitre_old_attack_id' in sw:
                document['key'] = url + delimiter + sw['name'] + " (ID: " + document['id'] + ', old ID: ' + \
                                  sw['x_mitre_old_attack_id'] + ")"
                document['id'] += ', ' + sw['x_mitre_old_attack_id']

            if 'x_mitre_contributors' in sw:
                for contributor in sw['x_mitre_contributors']:
                    document['contributors'] += contributor + ', '
                document['contributors'] = document['contributors'][:-2]

            document['aliases'] = ""
            sw_aliases = sw['x_mitre_aliases'][1:]
            if len(sw_aliases) > 0:
                if len(sw_aliases) > 1:
                    document['key'] = document['key'] + " (Assoc. SW: "
                else:
                    document['key'] = document['key'] + " (Assoc. SW: "

                for alias in sw_aliases:
                    document['aliases'] = document['aliases'] + alias + "\n"
                    document['key'] = document['key'] + alias + ", "
                document['key'] = document['key'][:-2] + ")"
            document['aliases'] = document['aliases'][:-1]
            documents.append(document)

    for domain in config.domains:
        tactics = get_tactic_list(config.ms[domain])
        for tactic in tactics:
            document = {}
            url = get_url(tactic)
            if url:
                if tactic.get('x_mitre_deprecated') or tactic.get('revoked'):
                    continue
                document['id'] = tactic['external_references'][0]['external_id']
                document['key'] = url + delimiter + tactic['name'] + " (ID: " + document['id'] + ")"
                document['title'] = tactic['name']
                document['body'] = tactic['description']
                document['detection'] = ""
                document['contributors'] = ""
                document['aliases'] = ""
                document['examples'] = ""

                if 'x_mitre_old_attack_id' in tactic:
                    document['key'] = url + delimiter + tactic['name'] + " (ID: " + document['id'] + ', old ID: ' + \
                                      tactic['x_mitre_old_attack_id'] + ")"
                    document['id'] += ', ' + tactic['x_mitre_old_attack_id']

                exists = False
                for doc in documents:
                    if doc['key'] == document['key']:
                        exists = True
                if not exists:
                    documents.append(document)

        for technique in config.technique_list:
            document = {}
            url = get_url(technique)
            if url:
                if technique.get('x_mitre_deprecated') or technique.get('revoked'):
                    continue
                document['id'] = technique['external_references'][0]['external_id']
                document['key'] = url + delimiter + technique['name'] + " (ID: " + document['id'] + ")"
                document['title'] = technique['name']
                document['body'] = technique['description'].replace("<code>", "").replace("</code>", "").replace("<br>", "").replace("</br>", "")
                document['detection'] = ""
                document['contributors'] = ""
                document['examples'] = ""
                examples, x = get_examples(technique['id'], config.ms[domain])

                for example in examples:
                    if example:
                        document['examples'] += " " + example['name'] + " " + example['description'].replace("<code>", "").replace("</code>", "").replace("<br>", "").replace("</br>", "")

                if 'x_mitre_old_attack_id' in technique:
                    document['key'] = url + delimiter + technique['name'] + " (ID: " + document['id'] + ', old ID: ' + \
                                      technique['x_mitre_old_attack_id'] + ")"
                    document['id'] += ', ' + technique['x_mitre_old_attack_id']

                if 'x_mitre_detection' in technique:
                    document['detection'] = technique['x_mitre_detection'].replace("<code>", "").replace("</code>", "").replace("<br>", "").replace("</br>", "")

                if 'x_mitre_contributors' in technique:
                    for contributor in technique['x_mitre_contributors']:
                        document['contributors'] += contributor + ', '
                    document['contributors'] = document['contributors'][:-2]

                document['aliases'] = ""
                documents.append(document)

    idx = lunr(ref='key',
    fields=[dict(field_name="id", boost=10), dict(field_name="title", boost=10), dict(field_name="aliases", boost=5),
            dict(field_name="contributors", boost=5), dict(field_name="examples", boost=10), "body", "detection"],
            documents=documents)

    # Verify if website directory exists
    if not os.path.isdir(config.web_directory):
        os.makedirs(config.web_directory)

    with open(os.path.join(config.web_directory, "index.json"), "w", encoding='utf8') as f:
        f.write(json.dumps(idx.serialize()))


def get_url(obj):
    if isinstance(obj.get("external_references"), collections.Iterable):
        ext_ref = obj['external_references']
        found_index = find_index_id(ext_ref)

        if found_index != -1:
            if ext_ref[found_index].get("url"):
                url = ext_ref[found_index]["url"].replace("https://attack.mitre.org", "")
                return url
    return None
