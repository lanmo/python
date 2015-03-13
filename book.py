#!/usr/bin/python
# coding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from pyquery import PyQuery as pq
import urllib
count = 0

def download(uri) :
   d = pq(url=uri)
   divs = d('.thumb-holder')
   global count

   linkas = [(pq(a).find('a').attr('href'),pq(a).find('.thumbtitle').text()) for a in divs]
   next = d('#navigation-next').find('a').attr('href')

   for linkurl,title in linkas:
      link = pq(url = linkurl) 
      downs = [pq(t).attr('href') for t in link('.post-content').find('.download-link')]
      count += 1
      print count
      for down in downs :
         index = down.rindex('.')
         urllib.urlretrieve(down, './temp/' + title + down[index:-1])

   if next :
       download(next)

url = 'http://book.zi5.me/'
download(url)
