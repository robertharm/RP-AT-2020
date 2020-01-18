# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Barrierefreies und maschinenlesbares Österreichisches Regierungsprogramm 2020-2024'
html_title = "Österreichisches Regierungsprogramm 2020-2024, barrierefrei, maschinenlesbar"
copyright = '2020, erstellt und publiziert durch "Die neue Volkspartei/Die Grünen – Die Grüne Alternative", maschinenlesbar und barrierefrei bearbeitet von Jens Klein, Robert Harm und Helfern.'
author = 'Die neue Volkspartei/Die Grünen – Die Grüne Alternative - nachbearbeitet durch Jens Klein, Robert Harm und Helfern'

# The full version, including alpha/beta/rc tags
release = '1.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.githubpages',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'de'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_materialdesign_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Extension configuration -------------------------------------------------
todo_include_todos = True
html_theme_options = {
    # https://github.com/myyasuda/sphinx_materialdesign_theme#html-theme-options
    # 'primary_color': 'blue',
    'accent_color': 'deep_purple',
    'header_links': [
        ('Regierungsprogramm 2020-2024', 'index', False, 'home'),
        ('Suche', 'search', False, 'search'),
        ('Stichwortverzeichnis', 'genindex', False, 'sort_by_alpha'),
        ("Open3", "https://www.open3.at", True, 'group'),
        ("GitHub", "https://github.com/jensens/RP-AT-2020", True, 'link')
    ],
    'twitter_site': "@open3",
    'twitter_creator': "@yenzenz",
    'og_description': project + ' #opendata #open-by-default #a11y'
}

# -- Additional config -------------------------------------------------------
# Language to be used for generating the HTML full-text search index.
# This defaults to the global language selected with language. If there is no
# support for this language, "en" is used which selects the English language.
html_search_language = 'de'


# html_logo
# If given, this must be the name of an image file (path relative to the
# configuration directory) that is the logo of the docs. It is placed at the
# top of the sidebar; its width should therefore not exceed 200 pixels.
# Default: None.

html_logo = 'open3-logo.png'
html_add_permalinks = True
html_split_index = True

# html_sidebars = {}