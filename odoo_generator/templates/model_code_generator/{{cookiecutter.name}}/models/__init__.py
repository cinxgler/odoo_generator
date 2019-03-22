{% for namespace in cookiecutter._module.namespaces() %}
from . import {{namespace}}{% endfor %}
