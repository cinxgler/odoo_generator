# -*- coding: utf-8 -*-
from odoo_generator.odoo_generator import CodeGenerator
from cookiecutter.main import cookiecutter


class ViewCodeGenerator(CodeGenerator):
    """Generate XML files with the view's code"""

    def add_metadata_attributes(self, module, model, field, spec):
        """Add lists of files to be included in the module manifest

        Args:
            - module(metadada.Module): Current module object
            - model(metadada.Model): Current model object
            - field(metadada.Field): Current field object
            - spec(Dict): Spec with the data to be used to update the module, model or fields metadata
        """
        if 'views/menus.xml' not in module.data_files:
            module.data_files.append('views/menus.xml')
        filename = "views/{}_views.xml".format(self.get_filename_for_model(model))
        if filename not in module.data_files:
            module.data_files.append(filename)

    def do_generate(self, module, templates_dir, output_dir):
        models = module.models.values()
        for model in models:
            cookiecutter(
                templates_dir + '/model_view_generator/',
                no_input=True,
                overwrite_if_exists=True,
                output_dir=output_dir,
                extra_context={
                    'name': module.name,
                    'namespace': module.namespace,
                    'model_filename': self.get_filename_for_model(model),
                    '_module': module, # Using _ as prefix to avoid cookiecutter convert the obj to str
                    '_model': model,
                },
            )
