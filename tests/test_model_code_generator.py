#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `module_code_generator` package."""

import sys
import ast
import shutil
import unittest
from odoo_generator import odoo_generator
from odoo_generator.builtin_plugins.module_code_generator import ModuleCodeGenerator
from odoo_generator.builtin_plugins.model_code_generator import ModelCodeGenerator


class TestOdooModuleGenerator(unittest.TestCase):

    def test_build_module(self):
        definition = [
            {
                'model_name': '__manifest__',
                'name': 'name',
                'type': '',
                'arguments': 'test_module',
                'string': '',
                'help': '',
            },
            {
                'model_name': '',
                'name': 'string',
                'type': '',
                'arguments': 'This is a Test Module',
                'string': '',
                'help': '',
            },
            {
                'model_name': '',
                'name': 'namespace',
                'type': '',
                'arguments': 'test_module',
                'string': '',
                'help': '',
            },
            {
                'model_name': '',
                'name': 'depends',
                'type': '',
                'arguments': 'website|mail',
                'string': '',
                'help': '',
            },
            {
                'model_name': 'prueba.modelo',
                'name': 'name',
                'type': 'char',
                'arguments': '',
                'string': 'Nombre',
                'help': 'ESte es un field',
            },
        ]
        line_generator = (line for line in definition)
        builder = odoo_generator.MetamodelBuilder()
        module = builder.build(line_generator)
        templates_dir = None
        output_dir = '/tmp/test_build_module'
        try:
            shutil.rmtree(output_dir)
        except FileNotFoundError as e:
            pass

        ModelCodeGenerator().generate(module, templates_dir, output_dir)
