#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
map():接受2个参数，第一个为函数，第二个为Iterable对象；
    map将传入的函数依次作用在Iterable的每个元素上，并返回新的Iterator对象
"""


def f(x):
    return x * x


L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r = map(f, L)
print(list(r))

# 将数字列表，快速转换为字符串列表
print(list(map(str, L)))


L1 = ['adam', 'LISA', 'barT']


def my_format(s):
    return s.lower().capitalize()


print(list(map(my_format, L1)))
