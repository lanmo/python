#!/usr/bin/python
# coding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib,urllib2
from bs4 import BeautifulSoup

def download(url,title):
    urllib.urlretrieve(url,'down/'+title)

uri = 'http://book.huangch.com/browse/category/allbooks'
request = urllib2.Request(uri)
request.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36')
request.add_header('Referer','http://book.huangch.com/')

content = urllib2.urlopen(request).read()

print content
