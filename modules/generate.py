# Module that holds all the ATT&CK update build wrappers

import time
import subprocess
import os
import shutil
from modules import clean
from modules import config
from modules import contribute
from modules import group
from modules import matrix
from modules import mitigation
from modules import redirects
from modules import resources
from modules import search
from modules import software
from modules import stixhelpers
from modules import tactic
from modules import technique
from string import Template
from modules import tests
from modules import util
from modules import index
from modules import archives

def group_md_gen():
    util.progress_bar("Group Pages")
    start_time = time.time()
    group.generate()
    end_time = time.time()
    util.progress_bar("Group Pages", end_time - start_time)

def software_md_gen():
    util.progress_bar("Software Pages")
    start_time = time.time()
    software.generate()
    end_time = time.time()
    util.progress_bar("Software Pages", end_time - start_time)

def technique_md_gen():
    util.progress_bar("Technique Pages")
    start_time = time.time()
    technique.generate()
    end_time = time.time()
    util.progress_bar("Technique Pages", end_time - start_time)

def matrix_md_gen():
    util.progress_bar("Matrix Pages")
    start_time = time.time()
    matrix.generate()
    end_time = time.time()
    util.progress_bar("Matrix Pages", end_time - start_time)

def tactic_md_gen():
    util.progress_bar("Tactic Pages")
    start_time = time.time()
    tactic.generate()
    end_time = time.time()
    util.progress_bar("Tactic Pages", end_time - start_time)

def mitigation_md_gen():
    util.progress_bar("Mitigation Pages")
    start_time = time.time()
    mitigation.generate()
    end_time = time.time()
    util.progress_bar("Mitigation Pages", end_time - start_time)

def contribute_md_gen():
    util.progress_bar("Contribute Page")
    start_time = time.time()
    contribute.generate()
    end_time = time.time()
    util.progress_bar("Contribute Page", end_time - start_time)

def resources_md_gen():
    util.progress_bar("Resources Pages")
    start_time = time.time()
    resources.generate()
    end_time = time.time()
    util.progress_bar("Resources Pages", end_time - start_time)

def redirects_md_gen():
    util.progress_bar("Redirection Pages")
    start_time = time.time()
    redirects.generate()
    end_time = time.time()
    util.progress_bar("Redirection Pages", end_time - start_time)

def pelican_content():
    util.progress_bar("Pelican Content")
    # Run pelican with limited output, -q is for quiet
    returned_out = subprocess.check_output("pelican content -q", shell=True)
    util.progress_bar("Pelican Content", float(str(returned_out).split(" ")[13]))

def generate_search_index():
    util.progress_bar("Search Index")
    start_time = time.time()
    search.generate_index()
    end_time = time.time()
    util.progress_bar("Search Index", end_time - start_time)

def previous_versions_gen():
    util.progress_bar("Previous Versions")
    start_time = time.time()
    archives.deploy()
    end_time = time.time()
    util.progress_bar("Previous Versions", end_time - start_time)

def clean_website():
    util.progress_bar("Clean Build")
    start_time = time.time()
    clean.clean_website_build()
    end_time = time.time()
    util.progress_bar("Clean Build", end_time - start_time)