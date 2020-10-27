from . import attack_redirections 
from . import attack_redirections_config
import json

def get_priority():
    return attack_redirections_config.priority

def get_redirections():
    with open(attack_redirections_config.attack_redirections_location , "r", encoding="utf8") as json_redirections:
        return json.load(json_redirections)
    return []

def run_module():
    return (attack_redirections.generate_attack_redirections(), attack_redirections_config.module_name)