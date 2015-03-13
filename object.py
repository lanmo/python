#!/usr/bin/python
# coding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

__metaclass__ = type

#class Person:
    #def setName(self, name) :
        #self.name = name
    
    #def getName(self) : 
        #return self.name

    #def greet(self) :
        #return 'Hello,World! I am %s.' % self.name

#bar = Person()
#bar.setName("Nanyang")

#boo = Person()
#boo.setName("NNN")

#print bar.greet()
#print boo.greet()
#print type(boo)


##构造函数
#class Person1:
    #def __init__(self):
        #self.name='HH'

#f = Person1()
#print f.name

def aa(values):
    for sublist in values :
        for value in sublist :
            yield value

x = aa([[1,2],[3,4],[5],[6,7,8]])
print list(x)

y = aa([[1,2],[3,4],[5],[6,7,8]])
print list(y)
