# How to customize the ATT&CK Website

## Building the site with custom content

The MITRE ATT&CK Website® is designed to support an evolving knowledge base. The content seen on the site is generated from data in STIX JSON format.
Both STIX 2.0 and STIX 2.1 data is supported.
The data used to generate the live site at [attack.mitre.org](https://attack.mitre.org) can be found on our [mitre/cti](https://github.com/mitre/cti) github repo.

You can generate the website using custom content by replacing the STIX bundle locations in `modules/site_config.py`, `domains`.
A domain location can be a URL (please include http:// or https://), or a local file on disk.
Optionally, you can set the `STIX_LOCATION_ENTERPRISE`, `STIX_LOCATION_MOBILE`, or `STIX_LOCATION_PRE` environment variables to the URL or local file as well.

Matrices are defined in `modules/matrices/matrices_config.py`, you will need to update the structures declared in this file to modify the matrices.

## Configuration

### Changing the theme (colors)

Users wishing to make changes to the ATT&CK website visual theme should take a look at our scss source files in `attack-theme/static/style`.
Changes to the colors defined in `_colors.scss` should automatically propagate across the site.

### Changing logos

The logos used in the header, footer, and on the landing page of the website can be easily changed.
Simply find their keys in the `settings_dict` of `modules/website_build/website_build_config.py`, and update their values to point to the new images.

### Attaching a custom Navigator instance

Links to the [ATT&CK Navigator](https://github.com/mitre-attack/attack-navigator) can be customized to point to a custom instance of that application.
Simply change the `navigator_link` field in `modules/site_config.py` to point to your hosted instance, and all URLs pointing to the Navigator on the site should update automatically.

### Changing the banner

The banner message can be modified or hidden by modifying the `BANNER_ENABLED` and`BANNER_MESSAGE` properties within `modules/site_config.py`.
Optionally, the `BANNER_ENABLED` and `BANNER_MESSAGE` environment variables can be set to a override the banner settings as well.

## Implementation Overview

The ATT&CK Website uses a combination of Python, Pelican and Jinja to convert the STIX content into a set of static HTML files.
When `update-attack.py` is run, it generates a set of markdown files in `content` containing the parsed STIX content.
Pelican then reads these markdown files and uses them with the Jinja templates in `attack-theme/templates` to build the site HTML in the output directory.

## Adding New Features

The website is built from modules.
These modules can be found inside the `modules` directory.
If the `update-attack.py` script is ran without any arguments, it will automatically look for modules inside the `modules` directory and build them.
Modules are divided in two classes, active and supportive modules.
Active modules append a link to the website's main menu and typically generates markdown files.
For example, the `techniques` module is responsible for generating all Technique related markdown pages.
Supportive modules are those who do not appear on the website menu but are critical to the general website build.
An example of a supportive module is the `util` module which has methods and API calls to interface with the STIX bundles.

Modules that are not present on the `modules` directory will not get built and will not appear on the website's main navigation menu.
You can also select specific modules to be ran without removing modules from the directory by running the `update-attack.py` script with the `-m` flag followed by the names of the modules.
For example, run `python3 update-attack.py -m clean techniques website_build` to run a fresh build, generate the techniques markdown files, and generate the HTML files.
Supportive modules need not to be called by arguments flags unless they are optional supportive modules such as the `tests` module.

### Building your own module

To build your own module, create a folder inside of the `modules` directory with the name of the module.
Typically, a module will have three files: `__init__py`, `your_module-s_name.py`, `your_module-s_name_config.py`.
The `__init__.py` file contains methods that are used to determine the run priority or if they will appear on website’s main menu.
For example, if it is an active module that will appear on the website's menu, be sure to include `get_menu()`, `get_priority()`, and `run_module()` in the `__init__.py` file (see the following code snippet for an example).
The module can be added to the website's menu as a single link to the main module page and/or can include links to subpages in a hoverable dropdown menu.
If the module is an active or an optional supportive one, add the name to the argument list (`module_choices`), found in the `update-attack.py` script.

```python
from . import your_module-s_name
from . import your_module-s_name_config

def get_priority():
    return your_module-s_name_config.priority

def get_menu():
    return {
        "display_name": "Name that will be displayed in the navigation menu"
        "module_name": "Your module's name", 
        "url": "/your_module-s_name/", 
        "external_link": False,
        "priority": your_module-s_name_config.priority,
        "children": [
            {
                "display_name": "Module sub-menu page",
                "url": "/your_module-s_name/subpage",
                "external_link": False,
                "children": []
            },
            ...
            {
                "display_name": "Module sub-menu external page",
                "url": "https://attack.mitre.org",
                "external_link": True,
                "children": []            
            }
        ]
    }

def run_module():
    return (your_module-s_name.generate_your_module-s_name(), your_module-s_name_config.module_name)
```

Every module has a given priority number.
This number is used to determine the order on which the modules are ran.
The build script will run the modules in an ascending priority order (lowest priority number will run first).
The priority inside of the `get_menu()` will determine the website's main menu order from left to right; module with the lowest priority number will be on the left.

`your_module-s_name_config.py` typically contains variables or string templates that are shared throughout the module.
`your_module-s_name.py` contains the methods that generate markdown files or are used to help other modules.

Jinja templates that are only used by the module should be stored in the module under a folder named `templates`, and then moved to the general templates folder.
This will help reduce the clutter of unused templates.

Additionally, redirections made by the module should also be stored inside of the module.
Take a look at the available modules for reference (the techniques module is a good one).
