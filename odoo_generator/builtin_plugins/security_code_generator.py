# -*- coding: utf-8 -*-
from odoo_generator.odoo_generator import CodeGenerator
from cookiecutter.main import cookiecutter


class SecurityCodeGenerator(CodeGenerator):
    """Generate XML and CSV files for security configuration"""
    def add_metadata_attributes(self, module, model, field, spec):
        """Add lists of files to be included in the module manifest

        Args:
            - module(metadada.Module): Current module object
            - model(metadada.Model): Current model object
            - field(metadada.Field): Current field object
            - spec(Dict): Spec with the data to be used to update the module, model or fields metadata
        """
        if 'security/ir.model.access.csv' not in module.data_files:
            module.data_files.append('security/ir.model.access.csv')

    def do_generate(self, module, templates_dir, output_dir):
        cookiecutter(
            templates_dir + '/security_code_generator/',
            no_input=True,
            overwrite_if_exists=True,
            output_dir=output_dir,
            extra_context={
                'name': module.name,
                'namespace': module.namespace,
                '_module': module, # Using _ as prefix to avoid cookiecutter convert the obj to str
            },
        )
