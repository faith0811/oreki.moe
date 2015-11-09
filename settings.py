#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'折木 奉太郎'
SITENAME = u'oreki.moe'
SITEURL = u'http://oreki.moe'

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
TAGLINE = u'不做也行的事情就不做，非做不可的事情一切从简。'
USER_LOGO_URL = SITEURL + '/images/oreki.jpeg'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}
