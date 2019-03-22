{
    "name": "{{ cookiecutter._module.string }}",
    "version": "{{ cookiecutter._module.version or '1.0' }}",
    "depends": [{% for dependency in cookiecutter._module.depends %}
        '{{ dependency }}',{% endfor %}
    ],
    "author": "{{ cookiecutter._module.author or 'Odoo Generator' }}",
    "category": "{{ cookiecutter._module.category or 'Odoo Generator' }}",
    'data': [{% for file_path in cookiecutter._module.data_files %}
        "{{ file_path }}",{% endfor %}
    ],
    'test': [{% for file_path in cookiecutter._module.test_files %}
        "{{ file_path }}",{% endfor %}
    ],
    'demo': [{% for file_path in cookiecutter._module.demo_files %}
        "{{ file_path }}",{% endfor %}
    ],
    'installable': {{ cookiecutter._module.installable }},
    'description': """{{ cookiecutter._module.description or 'Module generated using Odoo Generator' }}
    """,
}
