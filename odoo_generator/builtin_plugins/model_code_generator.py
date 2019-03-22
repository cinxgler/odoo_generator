# -*- coding: utf-8 -*-
from odoo_generator.odoo_generator import CodeGenerator
from cookiecutter.main import cookiecutter

class ModelCodeGenerator(CodeGenerator):
    def do_generate(self, module, templates_dir, output_dir):
        for namespace in module.namespaces():
            cookiecutter(
                templates_dir + '/model_code_generator/',
                no_input=True,
                overwrite_if_exists=True,
                output_dir=output_dir,
                extra_context={
                    'name': module.name,
                    'namespace': namespace,
                    '_module': module, # Using _ as prefix to avoid cookiecutter convert the obj to str
                },
            )
