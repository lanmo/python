#!/usr/bin/python
# coding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import socket
#服务端程序
s = socket.socket()

host = socket.gethostname()
print '域名'+ str(host)

port = 1234
s.bind((host,port))
s.listen(5)

while True :
    c, addr = s.accept()
    print 'Got connection from '
    print addr
    c.send('Thank you for connecting.....')
    c.close()
