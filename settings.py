#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'yanqing.wang'
SITENAME = u'oreki.moe'
SITEURL = u'//oreki.moe'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = ((u'氷菓', 'http://www.kyotoanimation.co.jp/kotenbu/'),)

SOCIAL = (('Github', 'https://github.com/faith0811'),
          ('Twitter', 'https://twitter.com/wyq0811'),)

DEFAULT_PAGINATION = 10

THEME = 'pelican-svbhack'
TAGLINE = u''
USER_LOGO_URL = SITEURL + '/images/oreki.jpeg'

DISQUS_SITENAME = 'orekimoe'
GOOGLE_ANALYTICS = 'UA-75598333-1'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}
