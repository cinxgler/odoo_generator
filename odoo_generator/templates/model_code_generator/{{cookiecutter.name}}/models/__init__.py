{% for model_file in cookiecutter._model_filenames -%}
from . import {{model_file}}
{% endfor %}
