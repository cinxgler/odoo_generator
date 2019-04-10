# -*- coding: utf-8 -*-
from odoo_generator.odoo_generator import CodeGenerator
from cookiecutter.main import cookiecutter

class ModelCodeGenerator(CodeGenerator):
    """Generates models python code using the fields and methods defined in the metadata"""

    def add_metadata_attributes(self, module, model, field, spec):
        """Add model package in the __init__ file of the module

        Args:
            - module(metadada.Module): Current module object
            - model(metadada.Model): Current model object
            - field(metadada.Field): Current field object
            - spec(Dict): Spec with the data to be used to update the module, model or fields metadata
        """
        if 'models' not in module.init_packages:
            module.init_packages.append('models')


    def do_generate(self, module, templates_dir, output_dir):
        models = module.models.values()
        filenames = [ self.get_filename_for_model(m) for m in models ]
        for model in models:
            cookiecutter(
                templates_dir + '/model_code_generator/',
                no_input=True,
                overwrite_if_exists=True,
                output_dir=output_dir,
                extra_context={
                    'name': module.name,
                    'namespace': model.namespace,
                    'model_filename': self.get_filename_for_model(model),
                    '_model_filenames': filenames,
                    '_module': module, # Using _ as prefix to avoid cookiecutter convert the obj to str
                    '_model': model,
                },
            )
