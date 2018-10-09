#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
filter():接受函数，Iterable；将函数分别作用在列表的每个元素上，根据返回True和False决定是保留还是放弃元素；
    返回的是Iterator,Iterator

"""
L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L2 = ['A', '', 'B', None, 'C', '  ']


def is_odd(n):
    return n % 2 == 1;


def not_empty(s):
    return s and s.strip()


print(list(filter(is_odd, L1)))
print(list(filter(not_empty, L2)))


def is_palindrome(n):
    return str(n) == str(n)[::-1]


print(list(filter(is_palindrome, range(1, 1000))))
