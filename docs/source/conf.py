import os
import sys

sys.path.insert(0, os.path.abspath('../'))

# -- Project information -----------------------------------------------------
project = 'DataExplorer'
copyright = '2025, Nadia BEN YOUSSEF - Jihed BHAR'
author = 'Nadia BEN YOUSSEF - Jihed BHAR'


# The full version, including alpha/beta/rc tags
release = '0.1.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
     'sphinx.ext.autodoc',
     'sphinx.ext.viewcode',
     'sphinx.ext.napoleon',
     'sphinx.ext.githubpages'
]

templates_path = ['_templates']

language = 'French'


exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
