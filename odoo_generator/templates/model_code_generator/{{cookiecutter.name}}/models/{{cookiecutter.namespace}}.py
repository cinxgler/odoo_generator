# -*- coding: utf-8 -*-
##############################################################################
# see LICENSE.TXT
##############################################################################

from odoo import models, fields, api
from odoo.exceptions import ValidationError

{% for model in cookiecutter._module.models.values() if model.namespace == namespace %}
class {{ model._name }}(models.Model):
    _name = '{{ model._name }}'

    # -------------------
    # Fields
    # -------------------

    # -------------------
    # methods
    # -------------------

    # -------------------
    # Workflow methods
    # -------------------

{% endfor %}
