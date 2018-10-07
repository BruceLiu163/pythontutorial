#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
comprehensions:列表生成式
    会一次性将所有的元素生成，可能存在的弊端是占用大量内存
"""
import os
L = [x * x for x in range(1, 11) if x % 2 == 0]
print(L)

L1 = [(m + n).lower() for m in 'ABC' for n in 'XYZ']
print(L1)

L2 = [d for d in os.listdir('.')]
print(L2)

