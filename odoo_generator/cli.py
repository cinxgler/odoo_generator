#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

import click
from yapsy.PluginManager import PluginManager

from odoo_generator import odoo_generator


@click.command()
@click.option('--templates_dir', default=None, help='Folder with custom templates to use for all plugins.')
@click.option('--output_dir', default='./', help='Folder where the generated code will be stored')
@click.argument('specs_filename')
def main(templates_dir, output_dir, specs_filename):
    """Console script for odoo_generator."""
    # Loads plugins
    manager = PluginManager()
    manager.setPluginPlaces([os.path.dirname(__file__) + "/builtin_plugins"])
    manager.collectPlugins()

    # Get a list of plugin's methods to add extra metadata in module definition
    add_attribute_functions = []
    for pluginInfo in manager.getAllPlugins():
        manager.activatePluginByName(pluginInfo.name)
        add_attribute_functions.append(pluginInfo.plugin_object.add_metadata_attributes)

    # Builds module metadata from CSV file
    builder = odoo_generator.MetamodelBuilder()
    line_generator = odoo_generator.csv_reader(specs_filename)
    module = builder.build(line_generator, add_attribute_functions)

    # Generate module code
    for pluginInfo in manager.getAllPlugins():
        pluginInfo.plugin_object.generate(module, templates_dir, output_dir)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
