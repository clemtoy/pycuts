# -*- coding:utf-8 -*-

from __future__ import division

def avg(iterable):
    """ Ex: avg([2, 4]) returns 3 """ 
    return sum(iterable) / len(iterable)

def condassign(variable):
    """ Ex: condassign(2)('neg', -5, 'neu', 5, 'pos') returns 'neu' as -5 <= 2 < 5 """
    def f(*ranges):
        if len(ranges) % 2 == 0 or sorted(ranges[1::2]) != list(ranges[1::2]):
            raise AttributeError('Incorrect ranges.')
        if variable < ranges[1]:
            return ranges[0]
        if variable >= ranges[-2]:
            return ranges[-1]
        r = ranges[1:-1]
        for i in range(1, len(r), 2):
            if r[i - 1] <= variable <= r[i + 1]:
                return r[i]  
    return f

