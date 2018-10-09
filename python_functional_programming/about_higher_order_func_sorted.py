#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sorted():sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
"""
from operator import itemgetter

L1 = [36, 5, -12, 9, -21]
L2 = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L1, key=abs))
print(sorted(L1, key=abs, reverse=True))

print(sorted(L2, key=str.lower))
print(sorted(L2, key=str.lower, reverse=True))

L3 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(L3, key=itemgetter(0)))
print(sorted(L3, key=itemgetter(1)))
print(sorted(L3, key=lambda t: t[1]))
print(sorted(L3, key=itemgetter(1), reverse=True))
print(sorted(L3, key=lambda t: t[1], reverse=True))
