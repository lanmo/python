#!/usr/bin/python
# coding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#能写中文了
sequence = raw_input("Sequence: ")
sequence = unicode(sequence, 'utf-8')
screen_with = 80
text_with = len(sequence)
print "text with=" + str(text_with)
box_with = text_with + 6
margin_left = (screen_with - text_with) //2
left = (box_with - 2 - text_with) //2

print
print ' ' * margin_left + '+' +'-' * (box_with - 2) + '+'
print ' ' * margin_left + '|' + ' '* (box_with -2 ) + '|'
print ' ' * margin_left + '|' + ' ' * left + sequence + ' ' * left + '|'
print ' ' * margin_left + '|' + ' '* (box_with -2 ) + '|'
print ' ' * margin_left + '+' +'-' * (box_with - 2) + '+'
