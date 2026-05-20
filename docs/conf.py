# Configuration file for the Sphinx documentation builder.
# eGovERA Solution Architecture Framework

project = 'eGovERA Solution Architecture Framework'
copyright = '© Copyright 2026, European Commission, DIGIT'
html_show_sphinx = False
author = 'Interoperability Architecture Solutions Action'
release = '1.0.0'

extensions = ['sphinx.ext.autosectionlabel',
    'sphinx.ext.githubpages',]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Avoid duplicate label warnings for common section names across files
autosectionlabel_prefix_document = True

html_theme = 'sphinx_rtd_theme'
html_logo = 'images/media/logo.png'
html_static_path = ['_static']
html_css_files = ['custom.css']

html_theme_options = {
    'analytics_anonymize_ip': False,
    'logo_only': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'vcs_pageview_mode': '',
    'style_nav_header_background': '#2980B9',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
}
