#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Iteration:
    for ... in
    list,tuple,dict,str等都可以进行迭代
        for key in list:
        for key in tuple:
        for ch in 'abc':
    dict默认迭代的是key，dict.values()进行values的迭代
        for key in dict:
        for value in dict.values():
        for k, v in dict.items():

    Python内置的enumerate函数可以把一个list变成索引-元素对
        for i, value in enumerate(['A', 'B', 'C']):

    example:
        for x, y in [(1, 2), (3, 4), (5, 6)]:
        for i, value in enumerate(['A', 'B', 'C']):

    通过collections模块的Iterable类型判断一个对象是可迭代对象
"""
from collections.abc import Iterable

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
for x, y in [(1, 2), (3, 4), (5, 6)]:
    print(x, y)

print(isinstance('abc', Iterable))
