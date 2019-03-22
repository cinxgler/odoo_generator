# -*- coding: utf-8 -*-

"""Console script for odoo_generator."""
from yapsy.PluginManager import PluginManager
import sys
import click


@click.command()
def main(args=None):
    """Console script for odoo_generator."""
    click.echo("Replace this message by putting your code into "
               "odoo_generator.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")

    manager = PluginManager()
    manager.setPluginPlaces(["plugins"])
    manager.collectPlugins()


    builder = odoo_generator.MetamodelBuilder()
    add_attribute_functions = []
    for pluginInfo in simplePluginManager.getPluginsOfCategory("MetadataBuilder"):
        manager.activatePluginByName(pluginInfo.name)
        add_attribute_functions.append(pluginInfo.plugin_object.add_attributes)

    module = builder.build(line_generator, add_attribute_functions)

    for pluginInfo in simplePluginManager.getPluginsOfCategory("CodeGenerator"):
        pluginInfo.plugin_object.generate_code(module)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
