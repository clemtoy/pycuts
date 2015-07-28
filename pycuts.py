# -*- coding:utf-8 -*-
"""
Clement Michard (c) 2015
"""

from __future__ import division


def attlist(lst, name):
    """ Ex: attlist(lst, 'v') is equivalent to [item.v for item in lst] """
    return [o.__dict__[name] for o in lst]


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
    
    
def flatten(lst):
    """ Ex: flatten([[1, 2], [[3, 4], [5, 6]], 7]) returns [1, 2, 3, 4, 5, 6, 7] """
    res = []
    for item in lst:
        res += item if isinstance(item, list) else [item]
    return flatten(res) if any(isinstance(item, list) for item in res) else res


def procedure(*func):
    """ Ex: procedure((sum, (3, 3, 4)),(sorted, [1,3,2])) returns {<function sum>: 10, <function sorted>: [1, 2, 3]} """
    return {f:f(*args) for f, *args in func}


def splitlist(lst, *splt):
    """ Ex: split([1,2,3,4,5,6,7,8,9,10], 3, 7) returns [[1, 2], [4, 5, 6], [8, 9, 10]] """
    from itertools import groupby
    return [list(gp) for k, gp in groupby(lst, lambda i:i in splt) if not k]

def test(test_func):
    """ Ex:
        @test(function_of_tests)
        def function_whose_result_will_be_tested_by_function_of_tests:
            ...
    """
    def decorator(func_to_test):
        def wrapper(*args, **kwargs):
            res = func_to_test(*args, **kwargs)
            test_func(res)
            return res
        return wrapper
    return decorator
