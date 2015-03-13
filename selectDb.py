#!/usr/bin/python
# coding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import MySQLdb as db

print """统计sessionId出现两次及以上的情况："""

#建立数据库连接
connect = db.connect(host='192.168.242.44',
                     user='develop',
                     passwd='p3m12d',
                     db='focus_assistant_qa',
                     port=3306)

cursor = connect.cursor(cursorclass=db.cursors.DictCursor)

sql = "select * from message_3 where id=1851"
cursor.execute(sql)

result =  cursor.fetchall()
for row in result :
    print row['group_id']

