#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
partial:偏函数
    主要作用是对原有的函数进行包装，主要体现在固化默认参数上

    functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），
    返回一个新的函数，调用这个新函数会更简单
"""
import functools

int2 = functools.partial(int, base=10)
print(int2('232'))

max2 = functools.partial(max, 10)
print(max2(5, 8))


def my_add(x, y):
    return x + y


def my_plus_one(x):
    return functools.partial(my_add, x, 1)()


print(my_plus_one(5))


