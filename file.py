#!/usr/bin/python
# coding: utf-8

import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

f = open('some.txt','r')
result = f.readlines()
print result
