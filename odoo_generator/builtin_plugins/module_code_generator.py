# -*- coding: utf-8 -*-
from odoo_generator.odoo_generator import CodeGenerator
from cookiecutter.main import cookiecutter


class ModuleCodeGenerator(CodeGenerator):
    def do_generate(self, module, templates_dir, output_dir):
        cookiecutter(
            templates_dir + '/module_code_generator/',
            no_input=True,
            overwrite_if_exists=True,
            output_dir=output_dir,
            extra_context={
                'name': module.name,
                'namespace': module.namespace,
                '_module': module, # Using _ as prefix to avoid cookiecutter convert the obj to str
            },
        )
