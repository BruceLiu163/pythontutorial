#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
slice:
    [0:10:1]:从索引0开始，直到索引10结束，不包括索引10,；
        0可以省略：[:10:1]
        1表示step
        [0:10] [:10]
        [0:10:2] [:10:2]
        [:] 表示原样复制一个list
        [-10:]  后10个元素

    字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串
    字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串
    字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串
"""

L = list(range(100))
T = tuple(range(100))
print(L)
print(L[0:10])
print(L[:10])
print(L[:10:2])
print(L[-10:])
print(L[:])

print(T[:10])
print(T[:])
print(T[-10:])
print(T[::10])

print('abcdefghigklmnopqrstuvwxyz'[::5])


