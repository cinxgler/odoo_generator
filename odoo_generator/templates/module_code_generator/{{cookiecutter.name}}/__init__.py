{% for package in cookiecutter._module.init_packages -%}
from . import {{ package }}
{% endfor %}
