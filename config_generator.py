#!/usr/bin/env python

# ------------------------------------------------------------------------
# Demonstrates how to generate Cisco configuration using Python and Jinja2
#
# (C) 2021 Osama Abbas, Cairo, Egypt
# Released under GNU Public License (GPL)
# email oabbas2512@gmail.com
# ------------------------------------------------------------------------

from os import path, mkdir
from json import load, loads
from jinja2 import Environment, FileSystemLoader
import webbrowser
from time import sleep

# Global Vars
j2_template = "switch.j2"
output_dir = "configs"
params_file = "params.json"
config_params = load(open(params_file))

# Handle Jinja template
env = Environment(loader=FileSystemLoader("./"), trim_blocks=True, lstrip_blocks=True)
config_template = env.get_template(j2_template)

# Create configs directory if not already created
if not path.exists(output_dir):
    mkdir(output_dir)

# Generate config template
for param in config_params:
    res = config_template.render(param)
    file_name = param["hostname"]
    file_ext = ".ios"
    file_location = path.join(output_dir, file_name + file_ext)
    file = open(file_location, "w")
    file.write(res)
    file.close()
    print("Configuration file '%s' is created successfully!" % (file_name + file_ext))

    # Open file in default Text Editor for the file extension
    sleep(1)
    webbrowser.open(file_location)
