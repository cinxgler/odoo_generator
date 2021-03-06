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

    def test_model_generation(self):
        definition = [
            {
                'model_name': '__manifest__',
                'name': 'name',
                'type': '',
                'arguments': 'my_module_name',
                'comodel': '',
                'string': '',
                'help': '',
            },
            {
                'model_name': '',
                'name': 'namespace',
                'type': '',
                'arguments': 'my_namespace',
                'comodel': '',
                'string': '',
                'help': '',
            },
            {
                'model_name': '',
                'name': 'string',
                'type': '',
                'arguments': 'This is my module name',
                'comodel': '',
                'string': '',
                'help': '',
            },
            {
                'model_name': '',
                'name': 'depends',
                'type': '',
                'arguments': 'website|mail',
                'comodel': '',
                'string': '',
                'help': '',
            },
            {
                'model_name': 'my_namespace.my_model',
                'name': 'field1',
                'type': 'Char',
                'arguments': '',
                'readonly': 'False',
                'required': 'False',
                'index': 'False',
                'default': 'False',
                'groups': '',
                'copy': 'False',
                'oldname': 'False',
                'comodel': '',
                'string': 'Field 2 Name',
                'help': 'This is Field2\'s name',
            },
            {
                'model_name': '',
                'name': 'field2',
                'type': 'Char',
                'arguments': '',
                'readonly': 'True',
                'required': 'True',
                'index': 'True',
                'default': '"something"',
                'groups': 'group1,group2',
                'copy': 'True',
                'oldname': 'old_name',
                'comodel': '',
                'string': 'Field Name',
                'help': 'This is Field\'s name',
                '_description': 'This is my model',
                '_order': 'id ASC',
                '_table': 'my_own_table',
                '_rec_name': 'name',
                '_inherit': 'res.users|mail.thread',
                'selection': "[('a','Option A'), ('b','Option B'), ]",
                'selection_add': "[('c','Option C'), ('d','Option D'), ]",
            },
            {
                'model_name': '',
                'name': 'field3',
                'type': 'Char',
                'arguments': '',
                'readonly': '',
                'required': '',
                'index': '',
                'default': '',
                'groups': '',
                'copy': '',
                'oldname': '',
                'comodel': '',
                'string': None,
                'help': None,
            },
{
                'model_name': '',
                'name': 'field4',
                'type': 'Many2one',
                'arguments': '',
                'comodel_name': 'res.users',
                'domain': "[('','','')]",
                'context': '{"value": True}',
                'ondelete': 'cascade',
                'auto_join': 'False',
                'inverse_name': '',
                'limit': '',
                'relation': '',
                'column1': '',
                'column2': '',
            },
            {
                'model_name': '',
                'name': 'field5',
                'type': 'Many2many',
                'arguments': '',
                'comodel_name': 'res.users',
                'domain': "[('','','')]",
                'context': '{"value": True}',
                'ondelete': 'cascade',
                'auto_join': 'False',
                'limit': '12',
                'relation': 'many_many_rel',
                'column1': 'res_user_id',
                'column2': 'my_model_id',
            },
            {
                'model_name': '',
                'name': 'field6',
                'type': 'One2many',
                'arguments': '',
                'comodel_name': 'res.users',
                'domain': "",
                'context': '',
                'ondelete': 'cascade',
                'auto_join': 'False',
                'inverse_name': 'partner_id',
                'limit': '12',
                'relation': '',
                'column1': '',
                'column2': '',
            },
{
                'model_name': '',
                'name': 'field7',
                'type': 'Char',
                'arguments': '',
                'compute': '"_compute_my_own"',
                'inverse': '"_inverse_my_own"',
                'search': '"_search_my_own"',
                'store': 'True',
                'compute_sudo': 'True',
            },
            {
                'model_name': '',
                'name': 'field8',
                'type': 'Char',
                'arguments': '',
                'compute': 'True',
                'inverse': 'True',
                'search': '1',
                'store': '',
                'compute_sudo': '',
            },
            {
                'model_name': '',
                'name': 'field9',
                'type': 'Char',
                'arguments': '',
                'compute': '',
                'inverse': 'False',
                'search': '0',
                'store': '',
                'compute_sudo': '',
            },
            {
                'model_name': 'res.users',
                'name': 'name',
                'type': 'Char',
                'arguments': '',
                'compute': '',
                'inverse': 'False',
                'search': '0',
                'store': '',
                'compute_sudo': '',
            },
            {
                'model_name': 'my_namespace.my_second_model',
                'name': 'name',
                'type': 'Char',
                'arguments': '',
                'compute': '',
                'compute_sudo': '',
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

