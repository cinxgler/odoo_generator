# -*- coding: utf-8 -*-
from odoo_generator.odoo_generator import CodeGenerator
from cookiecutter.main import cookiecutter

class ViewCodeGenerator(CodeGenerator):
    """Generate XML files with the view"""
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
                    'namespace': model.namespace,
                    'model_filename': self.get_filename_for_model(model),
                    '_module': module, # Using _ as prefix to avoid cookiecutter convert the obj to str
                    '_model': model,
                },
            )
