{% macro arguments(field) -%}
    {%- if field.string %}
        string='{{ field.string }}',
    {%- endif -%}
    {%- if field.required %}
        required=True,
    {%- else %}
        required=False,
    {%- endif -%}
    {%- if field.readonly %}
        readonly=True,
    {%- endif -%}
    {%- if field.track_visibility %}
        track_visibility='onchange',
    {%- endif -%}
    {%- if field.digits %}
        digits={{ field.digits }},
    {%- endif -%}
    {%- if field.size %}
        size={{field.size}},
    {%- endif -%}
    {%- if field.invisible %}
        invisible={{field.invisible}},
    {%- endif -%}
    {% if field.related %}
        related='{{field.related}}',
    {%- endif -%}
    {% if field.comodel_name %}
        comodel_name='{{field.comodel_name}}',
    {%- endif -%}
    {% if field.inverse_name %}
        inverse_name='{{field.inverse_name}}',
    {%- endif -%}
    {% if field.compute_sudo %}
        compute_sudo='{{field.compute_sudo}}',
    {%- endif -%}
    {% if field.relation %}
        relation='{{field.relation}}',
    {%- endif -%}
    {% if field.column1 %}
        column1='{{field.column1}}',
    {%- endif -%}
    {% if field.column2 %}
        column2='{{field.column2}}',
    {%- endif -%}
    {% if field.ondelete %}
        ondelete='{{field.ondelete}}',
    {%- endif -%}
    {% if field.compute %}
        compute='{{ field.compute }}',
    {%- endif -%}
    {% if field.store %}
        store={{field.store}},
    {%- endif -%}
    {% if field.help %}
        help='''{{field.help}}''',
    {%- endif -%}
    {% if field.domain %}
        domain="{{field.domain}}",
    {%- endif -%}
    {% if field.selection %}
        selection={{ field.selection }},
    {%- endif -%}
    {% if field.default %}
        default={{ field.default }},
    {%- endif -%}
    {% if field.type == 'binary' %}
        attachment=True,
    {%- endif -%}
{%- endmacro -%}
{%- set model = cookiecutter._model -%}
# -*- coding: utf-8 -*-
##############################################################################
# see LICENSE.TXT
##############################################################################
from odoo import models, fields, api

class {{ model._name.title().replace("_", "").replace(".", "") }}(models.Model):
    {%- for attribute_name in ['_name', '_description', '_inherit', '_order', '_rec_name', '_table'] %}
    {%- set value = model | attr(attribute_name) -%}
    {% if attribute_name == '_inherit' and value %}
    {{ attribute_name }} = {{ value }}
    {%- elif value %}
    {{ attribute_name }} = '{{ value }}'
    {%- endif -%}
    {%- endfor %}

    # -------------------
    # Fields
    # -------------------
    {%- for field in model.fields %}
    {{ field.name }} = fields.{{ field.type }}({{ arguments(field) }}
    )
    {%- endfor %}

    # -------------------
    # methods
    # -------------------
    {%- for method in model.methods %}

    def {{ method.name }}(self):
        pass
    {%- endfor %}

