# -*- coding: utf-8 -*-
"""Allow odoo_generator to be executable from a checkout or zip file."""
import runpy

if __name__ == "__main__":
    runpy.run_module("odoo_generator", run_name="__main__")
