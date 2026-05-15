# Configuration file for the Sphinx documentation builder.
# eGovERA Solution Architecture Framework

project = 'eGovERA Solution Architecture Framework'
copyright = '2026, European Union'
author = 'Interoperability Architecture Solutions team'
release = '1.0.0'

extensions = [
    'sphinx.ext.autosectionlabel',
]

# Avoid duplicate label warnings for common section names across files
autosectionlabel_prefix_document = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_theme_options = {
    'navigation_depth': 4,
    'titles_only': False,
}
