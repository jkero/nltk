# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:04:17 2019

@author: jk
"""

import feedparser
llog = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")
print(len(llog.entries))
print(llog.entries[6].title)
for  i in range(len(llog.entries)):
    print (llog.entries[i].title)