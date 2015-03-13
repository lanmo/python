#!/usr/bin/python
# coding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import socket
#客户端程序
s = socket.socket()

host = socket.gethostname()
print host
port = 1234

s.connect((host,port))

print s.recv(1024)
