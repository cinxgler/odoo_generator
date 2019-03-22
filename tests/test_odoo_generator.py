#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `odoo_generator` package."""


import unittest
from click.testing import CliRunner

from odoo_generator import exceptions
from odoo_generator import odoo_generator
from odoo_generator import metamodel
from odoo_generator import cli


class TestOdoo_generator(unittest.TestCase):
    """Tests for `odoo_generator` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    @unittest.skip
    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'odoo_generator.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

    def test_read_module_definition(self):
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
                'model_name': '',
                'name': 'IGNORE',
                'type': '',
                'arguments': 'NOTHING TO ADD',
                'comodel': '',
                'string': '',
                'help': '',
            },
            {
                'model_name': '',
                'name': 'models',
                'type': '',
                'arguments': 'NOTHING TO ADD',
                'comodel': '',
                'string': '',
                'help': '',
            },
            {
                'model_name': '',
                'name': 'depends',
                'type': '',
                'arguments': 'project',
                'comodel': '',
                'string': '',
                'help': '',
            },
            {}
        ]
        module = metamodel.Module()
        builder = odoo_generator.MetamodelBuilder()
        for spec in definition:
            builder.add_module_attribute(module, spec)

        self.assertEqual('my_module_name', module.name)
        self.assertEqual('my_namespace', module.namespace)
        self.assertEqual('This is my module name', module.string)
        self.assertEqual(['base','website', 'mail','project'], module.depends)
        self.assertEqual(False, hasattr(module, 'IGNORE') )
        self.assertEqual(False, hasattr(module, 'comodel') )
        self.assertEqual(0, len(module.models))
        self.assertEqual(0, len(module.groups))

    def test_read_model_definition(self):
        definition = [
            {
                'model_name': 'MyModel',
                'name': 'name',
                'type': 'char',
                'arguments': '',
                'comodel': '',
                'string': 'Field Name',
                'help': 'This is Field\'s name',
                '_description': 'This is my model',
                '_order': 'id ASC',
                '_table': 'my_own_table',
                '_rec_name': 'name',
                '_inherit': 'res.users|mail.thread',
                'fields': 'IGNORE',
            },
            {
                'model_name': 'MyModel',
                'name': 'counter',
                'type': 'integer',
                'arguments': '',
                'comodel': '',
                'string': 'Field Name 2',
                'help': 'This is Field2\'s name',
                '_description': '',
                '_order': '',
                '_table': '',
                '_rec_name': '',
                'fields': '',
            },
            {}
        ]
        model = metamodel.Model('MyModel')
        builder = odoo_generator.MetamodelBuilder()
        for spec in definition:
            builder.add_model_attribute(model, spec)

        self.assertEqual('MyModel', model._name)
        self.assertEqual(definition[0]['_description'], model._description)
        self.assertEqual(definition[0]['_order'], model._order)
        self.assertEqual(definition[0]['_table'], model._table)
        self.assertEqual(definition[0]['_rec_name'], model._rec_name)
        self.assertEqual(definition[0]['_inherit'].split('|'), model._inherit)
        self.assertEqual(0, len(model.fields))
        self.assertEqual(False, hasattr(model, 'comodel'))

    def test_read_basic_field_definition(self):
        definition = [
            {
                'model_name': 'MyModel',
                'name': 'name',
                'type': 'char',
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
                'fields': 'IGNORE',
            },
            {
                'model_name': 'MyModel',
                'name': 'name',
                'type': 'char',
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
                '_description': 'This is my model',
                '_order': 'id ASC',
                '_table': 'my_own_table',
                '_rec_name': 'name',
                '_inherit': 'res.users|mail.thread',
                'fields': 'IGNORE',
            },
            {
                'model_name': 'MyModel',
                'name': 'name',
                'type': 'char',
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
                '_description': 'This is my model',
                '_order': 'id ASC',
                '_table': 'my_own_table',
                '_rec_name': 'name',
                '_inherit': 'res.users|mail.thread',
                'fields': 'IGNORE',
            },
            {}
        ]
        model = metamodel.Model('MyModel')
        builder = odoo_generator.MetamodelBuilder()
        for spec in definition:
            builder.add_model_field(model, spec)

        self.assertEqual(3, len(model.fields))
        self.assertEqual(definition[0]['name'], model.fields[0].name)
        self.assertEqual(definition[0]['type'], model.fields[0].type)
        self.assertEqual(definition[0]['readonly'], model.fields[0].readonly)
        self.assertEqual(definition[0]['required'], model.fields[0].required)
        self.assertEqual(definition[0]['index'], model.fields[0].index)
        self.assertEqual(definition[0]['default'], model.fields[0].default)
        self.assertEqual(definition[0]['groups'], model.fields[0].groups)
        self.assertEqual(definition[0]['copy'], model.fields[0].copy)
        self.assertEqual(definition[0]['oldname'], model.fields[0].oldname)
        self.assertEqual(definition[0]['string'], model.fields[0].string)
        self.assertEqual(definition[0]['help'], model.fields[0].help)
        self.assertEqual(definition[0]['selection'], model.fields[0].selection)
        self.assertEqual(definition[0]['selection_add'], model.fields[0].selection_add)

        self.assertEqual(definition[1]['name'], model.fields[1].name)
        self.assertEqual(definition[1]['type'], model.fields[1].type)
        self.assertEqual(definition[1]['readonly'], model.fields[1].readonly)
        self.assertEqual(definition[1]['required'], model.fields[1].required)
        self.assertEqual(definition[1]['index'], model.fields[1].index)
        self.assertEqual(definition[1]['default'], model.fields[1].default)
        self.assertEqual(None, model.fields[1].groups)
        self.assertEqual(definition[1]['copy'], model.fields[1].copy)
        self.assertEqual(definition[1]['oldname'], model.fields[1].oldname)
        self.assertEqual(definition[1]['string'], model.fields[1].string)
        self.assertEqual(definition[1]['help'], model.fields[1].help)

        self.assertEqual(definition[2]['name'], model.fields[2].name)
        self.assertEqual(definition[2]['type'], model.fields[2].type)
        self.assertEqual(None, model.fields[2].readonly)
        self.assertEqual(None, model.fields[2].required)
        self.assertEqual(None, model.fields[2].index)
        self.assertEqual(None, model.fields[2].default)
        self.assertEqual(None, model.fields[2].groups)
        self.assertEqual(None, model.fields[2].copy)
        self.assertEqual(None, model.fields[2].oldname)
        self.assertEqual(None, model.fields[2].string)
        self.assertEqual(None, model.fields[2].help)

    def test_read_relational_field_definition(self):
        definition = [
            {
                'model_name': 'MyModel',
                'name': 'name',
                'type': 'many2one',
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
                'model_name': 'MyModel',
                'name': 'name',
                'type': 'many2many',
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
                'model_name': 'MyModel',
                'name': 'name',
                'type': 'one2many',
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
            {}
        ]
        model = metamodel.Model('MyModel')
        builder = odoo_generator.MetamodelBuilder()
        for spec in definition:
            builder.add_model_field(model, spec)

        self.assertEqual(3, len(model.fields))
        self.assertEqual(definition[0]['name'], model.fields[0].name)
        self.assertEqual(definition[0]['type'], model.fields[0].type)
        self.assertEqual(definition[0]['domain'], model.fields[0].domain)
        self.assertEqual(definition[0]['context'], model.fields[0].context)
        self.assertEqual(definition[0]['ondelete'], model.fields[0].ondelete)
        self.assertEqual(definition[0]['auto_join'], model.fields[0].auto_join)
        self.assertEqual(None, model.fields[0].inverse_name)
        self.assertEqual(None, model.fields[0].limit)
        self.assertEqual(None, model.fields[0].relation)
        self.assertEqual(None, model.fields[0].column1)
        self.assertEqual(None, model.fields[0].column2)

        self.assertEqual(definition[1]['name'], model.fields[1].name)
        self.assertEqual(definition[1]['type'], model.fields[1].type)
        self.assertEqual(definition[1]['domain'], model.fields[1].domain)
        self.assertEqual(definition[1]['context'], model.fields[1].context)
        self.assertEqual(definition[1]['ondelete'], model.fields[1].ondelete)
        self.assertEqual(definition[1]['auto_join'], model.fields[1].auto_join)
        self.assertEqual(None, model.fields[1].inverse_name)
        self.assertEqual(definition[1]['limit'], model.fields[1].limit)
        self.assertEqual(definition[1]['relation'], model.fields[1].relation)
        self.assertEqual(definition[1]['column1'], model.fields[1].column1)
        self.assertEqual(definition[1]['column2'], model.fields[1].column2)

        self.assertEqual(definition[2]['name'], model.fields[2].name)
        self.assertEqual(definition[2]['type'], model.fields[2].type)
        self.assertEqual(None, model.fields[2].domain)
        self.assertEqual(None, model.fields[2].context)
        self.assertEqual(definition[2]['ondelete'], model.fields[2].ondelete)
        self.assertEqual(definition[2]['auto_join'], model.fields[2].auto_join)
        self.assertEqual(definition[2]['inverse_name'], model.fields[2].inverse_name)
        self.assertEqual(definition[2]['limit'], model.fields[2].limit)
        self.assertEqual(None, model.fields[2].relation)
        self.assertEqual(None, model.fields[2].column1)
        self.assertEqual(None, model.fields[2].column2)


    def test_read_computed_field_definition(self):
        definition = [
            {
                'model_name': 'MyModel',
                'name': 'name',
                'type': 'char',
                'arguments': '',
                'compute': '"_compute"',
                'inverse': '"_inverse"',
                'search': '"_search"',
                'store': 'True',
                'compute_sudo': 'True',
            },
            {
                'model_name': 'MyModel',
                'name': 'name',
                'type': 'char',
                'arguments': '',
                'compute': 'True',
                'inverse': 'True',
                'search': '1',
                'store': '',
                'compute_sudo': '',
            },
            {
                'model_name': 'MyModel',
                'name': 'name',
                'type': 'char',
                'arguments': '',
                'compute': '',
                'inverse': 'False',
                'search': '0',
                'store': '',
                'compute_sudo': '',
            },
            {}
        ]
        model = metamodel.Model('MyModel')
        builder = odoo_generator.MetamodelBuilder()
        for spec in definition:
            builder.add_model_field(model, spec)

        self.assertEqual(3, len(model.fields))
        self.assertEqual(6, len(model.methods))
        self.assertEqual(eval(definition[0]['compute']), model.methods[0]['name'])
        self.assertEqual(eval(definition[0]['inverse']), model.methods[1]['name'])
        self.assertEqual(eval(definition[0]['search']), model.methods[2]['name'])
        self.assertEqual('_compute_name', model.methods[3]['name'])
        self.assertEqual('_inverse_name', model.methods[4]['name'])
        self.assertEqual('_search_name', model.methods[5]['name'])

        self.assertEqual(definition[0]['store'], model.fields[0].store)
        self.assertEqual(definition[0]['compute_sudo'], model.fields[0].compute_sudo)
        self.assertEqual(None, model.fields[1].store)
        self.assertEqual(None, model.fields[1].compute_sudo)
        self.assertEqual(None, model.fields[2].store)
        self.assertEqual(None, model.fields[2].compute_sudo)

    def test_preprocess_line(self):
        line = {
            'name': ' to clean ',
            'type': '" not to clean "',
            'arguments': 'value ',
        }
        result = odoo_generator.preprocess(line)
        expected = {
            'name': 'to clean',
            'type': '" not to clean "',
            'arguments': 'value',
        }
        self.assertEqual(expected, result)

        line = {
            'name': 'value',
            'arguments': 'name =" new_value "|limit=12 |domain= [("a","=","b")]|selection=[("a","Option A")]',
        }
        result = odoo_generator.preprocess(line)
        expected = {
            'name': '" new_value "',
            'arguments': 'name =" new_value "|limit=12 |domain= [("a","=","b")]|selection=[("a","Option A")]',
            'limit': '12',
            'domain': '[("a","=","b")]',
            'selection': '[("a","Option A")]',
        }
        self.assertEqual(expected, result)

        line = {
            'arguments': 'name=value',
        }
        result = odoo_generator.preprocess(line)
        expected = {
            'name': 'value',
            'arguments': 'name=value',
        }
        self.assertEqual(expected, result)

        line = {
            'arguments': 'name=value|',
        }
        result = odoo_generator.preprocess(line)
        expected = {
            'name': 'value',
            'arguments': '',
        }
        self.assertEqual(expected, result)

        line = {
            'arguments': 'name=value|arg_value|arg_value2',
        }
        result = odoo_generator.preprocess(line)
        expected = {
            'name': 'value',
            'arguments': 'arg_value2'
        }
        self.assertEqual(expected, result)

        line = {
            'arguments': ' ',
        }
        result = odoo_generator.preprocess(line)
        expected = {
            'arguments': '',
        }
        self.assertEqual(expected, result)

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
                'model_name': 'test_module.model_1',
                'name': 'name',
                'type': 'string',
                'arguments': 'compute=1',
                'string': 'Name',
                'help': '',
            },
            {
                'model_name': '',
                'name': 'count',
                'type': 'integer',
                'arguments': 'readonly=1',
                'string': 'Count',
                'help': '',
            },
            {
                'model_name': 'test_module.model_2',
                'name': 'name',
                'type': 'string',
                'arguments': 'required=1',
                'string': 'Name',
                'help': '',
            },
            {
                'model_name': '',
                'name': 'user_id',
                'type': 'many2one',
                'arguments': 'comodel_name=res.users',
                'string': 'User',
                'help': 'Select an user',
            },
            {
                'model_name': 'test_module.model_1',
                'name': 'model_2_ids',
                'type': 'many2many',
                'arguments': 'comodel_name=test_module.model_2',
                'string': 'Many 2 Many',
                'help': '',
            },
        ]
        line_generator = (line for line in definition)
        builder = odoo_generator.MetamodelBuilder()
        module = builder.build(line_generator)
        models = list(module.models.values()) # Should return a generator with the models ordered by the insertion order,
                                              # then to access by index we convert it into a list
        self.assertEqual(2, len(module.models))
        self.assertEqual('test_module.model_1', models[0]._name)
        self.assertEqual('test_module.model_2', models[1]._name)
        self.assertEqual(3, len(models[0].fields))
        self.assertEqual(2, len(models[1].fields))

        definition = [
            {
                'model_name': '',
                'name': 'depends',
                'type': '',
                'arguments': 'website|mail',
                'string': '',
                'help': '',
            },
            {
                'model_name': 'test_module.model_1',
                'name': 'name',
                'type': 'string',
                'arguments': 'compute=1',
                'string': 'Name',
                'help': '',
            },
        ]
        line_generator = (line for line in definition)
        builder = odoo_generator.MetamodelBuilder()
        with self.assertRaises(exceptions.ParserException) as cm:
            module = builder.build(line_generator)
