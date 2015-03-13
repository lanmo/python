#!/usr/bin/python
# coding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def search(sequence, number, lower, upper):
    '二分法查找'
    if lower == upper :
        assert number == sequence[upper]
        return lower
    else :
        middle = (lower + upper) // 2
        if number > sequence[middle] :
            return search(sequence, number, middle + 1, upper)
        else :
            return search(sequence, number, lower, middle)

seq = [34,67,8,123,4,100,95]
seq.sort()
print seq
x = search(seq, 123, 0, len(seq))
print x
