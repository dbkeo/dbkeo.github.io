#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'dan keogh'
SITENAME = u'dbkeo.github.io'
SITEURL = 'http://dbkeo.github.io'
DESCRIPTION = 'Collaborative research. Data. Cryptocurrency lately. 2015 <a href="https://twitter.com/SoftwareSaved">@SoftwareSaved</a> Fellow. PhD student at University College London. Minor delays.'
TWITTER_USERNAME = 'tompollard'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Theme
THEME = '/Users/danielkeogh/Documents/Website/dbkeo.github.io/theme'
GRV_URL = '/theme/images/side_profile.jpg' # looking sidew
# GRV_URL = '/theme/images/prof2.jpg' # looking up

# Blogroll
# LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# GITHUB_URL = 'https://github.com/tompollard/tompollard.github.io/tree/source/'

# Syntax highlighting
MD_EXTENSIONS = ['codehilite(css_class=codehilite code)']

# Social widget
SOCIAL = (
	('Twitter', 'http://twitter.com/tompollard'),
    ('LinkedIn', 'http://www.linkedin.com/in/tomjpollard'),
    ('Github', 'https://www.github.com/tompollard'),
    )

DEFAULT_PAGINATION = 10

# Plugins
PLUGIN_PATH = '/Users/danielkeogh/Documents/Website/pelican-plugins-master'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
