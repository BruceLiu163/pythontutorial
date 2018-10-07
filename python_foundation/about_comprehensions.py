#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
列表生成式

"""
import os
L = [x * x for x in range(1, 11) if x % 2 == 0]
print(L)

L1 = [(m + n).lower() for m in 'ABC' for n in 'XYZ']
print(L1)

L2 = [d for d in os.listdir('.')]
print(L2)

