# -*- coding: utf-8 -*-
from collections import OrderedDict, namedtuple

class Module:
    def __init__(self):
        self.name = None
        self.string = None
        self.namespace = None
        self.author = None
        self.category = None
        self.installable = True
        self.description = None
        self.version = None
        self.depends = ['base']
        self.attributes_to_ignore = ['models', 'groups', 'data_files', 'test_files', 'demo_files']
        self.models = OrderedDict()
        self.groups = OrderedDict()
        self.data_files = []
        self.test_files = []
        self.demo_files = []

    def namespaces(self):
        namespaces = [ m.namespace for m in self.models.values() if m.namespace ]
        return list(set(namespaces))


class Model:
    def __init__(self, name):
        self._name = name
        self._description = None
        self._order = None
        self._table = None
        self._rec_name = None
        self._inherit = []
        self.attributes_to_ignore =  ['fields', 'methods', 'namespace', 'shortname']
        self.fields = []
        self.methods = []
        name_parts = name.split('.')
        self.namespace = name_parts[0]
        self.shortname = '.'.join(name_parts[1:])


class Field:
    def __init__(self, name, model):
        self.model = model
        self.name = name
        self.type = None
        # Basic fields
        self.string = None
        self.help = None
        self.readonly = None
        self.required = None
        self.index = None
        self.default = None
        self.groups = None
        self.copy = None
        self.oldname = None
        self.track_visibility = None
        self.related = None
        self.invisible = None
        # Computed fields
        self.compute = None
        self.inverse = None
        self.search = None
        self.store = None
        self.compute_sudo = None
        # Char Fields
        self.size = None
        self.trim = None
        # Float Fields
        self.digits = None
        # Float Text
        self.translate = None
        # Selection
        self.selection = None
        self.selection_add = None
        # Relational Fields
        self.comodel_name = None
        self.domain = None
        self.context = None
        self.ondelete = None
        self.auto_join = None
        # One2Many Fields
        self.inverse_name = None
        self.limit = None
        # Many2Many
        self.relation = None
        self.column1 = None
        self.column2 = None
        self.attributes_to_ignore = ['attributes_to_ignore', 'model']


    def build_methods(self):
        Method = namedtuple('Method', ['name'])
        if self.compute:
            value = eval(self.compute)
            if isinstance(value, str):
                self.model.methods.append(Method(name=value))
            elif value:
                self.model.methods.append(Method(name='_compute_{}'.format(self.name)))
        if self.inverse:
            value = eval(self.inverse)
            if isinstance(value, str):
                self.model.methods.append(Method(name=value))
            elif value:
                self.model.methods.append(Method(name='_inverse_{}'.format(self.name)))
        if self.search:
            value = eval(self.search)
            if isinstance(value, str):
                self.model.methods.append(Method(name=value))
            elif value:
                self.model.methods.append(Method(name='_search_{}'.format(self.name)))
