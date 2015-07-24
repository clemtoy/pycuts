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

 
def condexec(variable, usevar=False):
    """ Ex: condexec(2)(neg, -5, neu, 5, pos) returns the result of neu() as -5 <= 2 < 5
            condexec(2, usevar=True)(neg, -5, neu, 5, pos) returns the result of neu(variable) """
    def f(*ranges):
        if len(ranges) % 2 == 0 or sorted(ranges[1::2]) != list(ranges[1::2]):
            raise AttributeError('Incorrect ranges.')
        if variable < ranges[1]:
            return ranges[0](variable) if usevar else ranges[0]()
        if variable >= ranges[-2]:
            return ranges[-1](variable) if usevar else ranges[-1]()
        r = ranges[1:-1]
        for i in range(1, len(r), 2):
            if r[i - 1] <= variable <= r[i + 1]:
                return r[i](variable) if usevar else r[i]()  
    return f


def procedure(*func):
    """ Ex: procedure((sum, (3, 3, 4)),(sorted, [1,3,2])) returns {<function sum>: 10, <function sorted>: [1, 2, 3]} """
    return {f:f(*args) for f, *args in func}


def flatten(lst):
    """ Ex: flatten([[1, 2], [[3, 4], [5, 6]], 7]) returns [1, 2, 3, 4, 5, 6, 7] """
    res = []
    for item in lst:
        res += item if isinstance(item, list) else [item]
    return flatten(res) if any(isinstance(item, list) for item in res) else res


def attlist(lst, name):
    """ Ex: attlist(lst, 'v') is equivalent to [item.v for item in lst] """
    return [o.__dict__[name] for o in lst]

