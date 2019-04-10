"""Allow odoo_generator to be executable through `python -m odoo_generator`."""
from .cli import main


if __name__ == "__main__":  # pragma: no cover
    main(prog_name="odoo_generator")
