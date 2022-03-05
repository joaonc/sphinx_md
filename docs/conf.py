# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
import os
import sys
sys.path.insert(0, os.path.abspath('../app'))
sys.path.insert(1, os.path.abspath('../tests'))


# -- Project information -----------------------------------------------------

project = 'Sphinx MD'
copyright = '2022, Joao Coelho'
author = 'Joao Coelho'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx_autodoc_typehints',
    'sphinxcontrib_autodoc_filterparams',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['docs/_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.venv']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['docs/_static']

# -- Myst options  ----------------------------------------------------------
# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
myst_enable_extensions = [
    'colon_fence',
]


# -- Callbacks  ------------------------------------------------------------
def sphinxcontrib_autodoc_filterparams(func, param):
    """
    Filter parameters from functions/methods in documentation.
    This is called once per parameter per function.

    https://github.com/erikkemperman/sphinxcontrib-autodoc-filterparams

    :param func: Current function.
    :param param: Current parameter.
    :return: `True` then the parameter will be documented, otherwise it will be excluded.
    """
    # TODO: Resolve https://github.com/erikkemperman/sphinxcontrib-autodoc-filterparams/issues/3
    # TODO: Also split by '/' for MacOS/Linux
    module_name = str(sys.modules[func.__module__]).split('\\')[-1]
    return not (module_name.startswith('test_') and func.__name__.startswith('test_'))
