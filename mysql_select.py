#!/usr/bin/python
# coding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import MySQLdb

#建立连接
db = MySQLdb.connect(host='192.168.242.44',
                     user='develop',
                     passwd='p3m12d',
                     db='focus_assistant_qa',
                     port=3306)

cursor = db.cursor()

sql = 'select * from message_98'

cursor.execute(sql)

result = cursor.fetchall()
for row in result :
    print row[1]

db.close()
