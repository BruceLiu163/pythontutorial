#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
reduce():
    reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
    reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
    reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
"""
from functools import reduce

L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L2 = [1, 3, 5, 7, 9]


def add(x, y):
    return x + y


print(reduce(add, L2))


def fn(x, y):
    return 10 * x + y


print(reduce(fn, L2))


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(fn, map(char2num, '13579')))


def prod(my_list):
    def my_plus(x, y):
        return x * y

    return reduce(my_plus, my_list)


print(prod(L1))
print(prod(L2))
