# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here.
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CV.ersatile'
copyright = '2025, Ricardo Santiago Araújo'
author = 'Ricardo Santiago Araújo'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.duration', # to &see a short durations report at the end of the console output
    'sphinx.ext.doctest', # to perform unit tests with command 'make doctest'
    'sphinx.ext.autodoc', # reuse Python docstrings in the documentation, rather than having to write the information in two places.
    'sphinx.ext.autosummary', # generates documents that contain all the necessary autodoc directives.
    'sphinx.ext.napoleon',  # For Google/NumPy style docstrings
    "sphinx_autodoc_typehints", # Automatically document types in function signatures
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']


### OPTION: ALABASTER THEME
if False:
    html_theme = "alabaster"
    html_theme_options = {  # for alabaster theme
        # "logo": "media/logo.png",  # if you have a logo
        "github_user": "RicardoSantiagoAraujoLP",  # optional GitHub link
        "github_repo": "loki_pipeline",
        "description": "Loki pipeline docs",
        "fixed_sidebar": True,
    }

### OPTION: RTD THEME
if False:
    html_theme = "sphinx_rtd_theme"
    html_theme_options = {  # for sphinx_rtd_theme : https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
        "logo_only": False,  # Show only logo, no project name
        # "display_version": True,  # Show version in top-right
        "prev_next_buttons_location": "bottom",  # or 'top'
        "style_nav_header_background": "#059C67",  # top nav bar color
        "style_external_links": True,
        # 'collapse_navigation': False, # keep sidebar expanded
        # 'sticky_navigation': True,     # sidebar sticks when scrolling
    }

### OPTION: FURO THEME
if True:
    html_theme = "furo"
    html_theme_options = {  # for furo theme
        "light_css_variables": {
            "color-brand-primary": "#059C67",
            "color-brand-content": "#0D4A37",
        },
        "dark_css_variables": {
            "color-brand-primary": "#059C67",
            "color-brand-content": "#0D4A37",
        },
    }


# FURTHER CUSTOMIZATION
html_favicon = "_static/media/logo.png"  # path relative to the _static folder
html_logo = "_static/media/logo.png"  # path relative to the _static folder
html_css_files = [
    "custom.css",
]

# -- Options for EPUB output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-epub-output

epub_show_urls = 'footnote'
