# -*- coding: utf-8 -*-

from collections import OrderedDict
from . import metamodel
from . import exceptions

from abc import ABC, abstractmethod
from unittest.mock import patch
import os


import logging
_logger = logging.getLogger(__name__)


def preprocess(line):
    """Return a dictionary with trimmed strings, all columns are mapped, the arguments column are transformed to its own dict entry.
    """
    arguments = line['arguments']
    arguments = arguments.split(LIST_SEPARATOR)
    new_arguments = {}
    for part in arguments:
        pieces = part.split('=', 1)
        if len(pieces) == 2:
            key = pieces[0].strip()
            value = pieces[1].strip()
            new_arguments[key] = value
        else:
            value = pieces[0].strip()
            new_arguments['arguments'] = value
    line.update(new_arguments)
    new_line = { key: value.strip() for key, value in line.items()}
    return new_line

def csv_reader(filename):
    """Reads a CSV file and return line by line cleaned using `preprocess` function.

    Args:
        - filename(String): Path to CSV file

    Returns:
        - Generator: Returns a file line Dict
    """
    with open(filename, 'r') as handle:
        reader = csv.DictReader(handle)
        for line in reader:
            line = preprocess(line)
            yield line


LIST_SEPARATOR = '|'
class MetamodelBuilder:
    """This class generates a Module and all its Models and Fields from a spec"""

    def add_module_attribute(self, module, spec):
        """Maps the 'spec' to attributes in the module object.

        Args:
            - module: Instance of metamodel.Module
            - spec: Dictionary with name and value to assign (spec['arguments'])

        """
        if not spec:
            return module
        attribute_name = spec['name']
        attribute_value = spec['arguments']
        if attribute_name in module.attributes_to_ignore:
            return module
        if attribute_name in vars(module).keys():
            current_value = getattr(module, attribute_name)
            if isinstance(current_value, list):
                current_value.extend(attribute_value.split(LIST_SEPARATOR))
            else:
                setattr(module, attribute_name, attribute_value)
        return module

    def add_model_attribute(self, model, spec):
        """Check if the spec contains keys related to model attributes and add them to the `model`.

        Args:
            - model: Instance of metamodel.Model
            - spec: Dictionary with name and value to assign (spec['arguments'])

        """
        for attribute_name in vars(model).keys():
            if attribute_name in model.attributes_to_ignore:
                continue
            value = spec.get(attribute_name)
            if value:
                current_value = getattr(model, attribute_name)
                if isinstance(current_value, list):
                    current_value.extend(value.split(LIST_SEPARATOR))
                else:
                    setattr(model, attribute_name, value)
        return model

    def add_model_field(self, model, spec):
        """Create a metamodel.Field using the attributes defined in the spec
        """
        if not spec:
            return None
        field = metamodel.Field(spec['name'], model)
        for attribute_name in vars(field).keys():
            if attribute_name in field.attributes_to_ignore:
                continue
            value = spec.get(attribute_name)
            if value is None or value is '':
                continue

            current_value = getattr(field, attribute_name)
            if isinstance(current_value, list):
                current_value.extend(value.split(LIST_SEPARATOR))
            else:
                setattr(field, attribute_name, value)
        model.fields.append(field)
        field.build_methods()
        return field

    def build(self, file_iterator, add_attributes_functions=[]):
        """Creates a module from the structure defined in the file.

        Args:
            - file_iterator(Generator): Generator that returns a dictionary with all the fields to populate the Module, model and fields.
            - add_atributes_functions(List[Callable]): List with callables that receive Metadata.Module, Metadata.Model, Metadata.Field and line (dict)

        Returns:
            - metadada.Module: Object composed of metadada.Model and metadata.Field objects
        """
        module = metamodel.Module()
        last_model_name = None
        for line in file_iterator:
            _logger.debug(line)
            if line['model_name']:
                last_model_name = line['model_name']
            if not line['model_name'] and last_model_name:
                line['model_name'] = last_model_name
            if not line['model_name']:
                raise exceptions.ParserException('Line doesn\'t refer to any Model name')

            if last_model_name == '__manifest__':
                self.add_module_attribute(module, line)
            else:
                if not last_model_name in module.models:
                    module.models[last_model_name] = metamodel.Model(last_model_name)
                model = module.models[last_model_name]
                self.add_model_attribute(model, line)
                field = self.add_model_field(model, line)
                for add_attribute_func in add_attributes_functions:
                    add_attribute_func(module, model, field, line)
        return module


class CodeGenerator(ABC):
    def generate(self, module, templates_dir, output_dir='./'):
        if templates_dir is None:
            templates_dir = os.path.dirname(__file__) + '/templates'

        with patch('cookiecutter.main.dump') as mocked_dump:
            mocked_dump.return_value = True # As the module object passed in extra_context[_module]
                                            # is not serializable cookiecutter raises an exception,
                                            # so a patch to avoid the error is used
            self.do_generate(module, templates_dir, output_dir)
        return True

    @abstractmethod
    def do_generate(module, templates_dir, output_dir):
        pass
