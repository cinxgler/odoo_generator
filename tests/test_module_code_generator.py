#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `module_code_generator` package."""

import sys
import ast
import shutil
import unittest
from odoo_generator import odoo_generator
from odoo_generator.builtin_plugins.module_code_generator import ModuleCodeGenerator


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
        ModuleCodeGenerator().generate(module, templates_dir, output_dir)
        with open("{}/test_module/__manifest__.py".format(output_dir),'r') as fh:
            manifest = ast.literal_eval(fh.read())
        self.assertEqual(definition[1]['arguments'], manifest['name'])
        self.assertEqual(['base'] + definition[3]['arguments'].split('|'), manifest['depends'])
