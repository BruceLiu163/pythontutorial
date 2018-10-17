#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
io:
    file read
    file write

with:
    default close

file-like object:
    open()函数返回的这种有read()方法的对象，在Python中统称为file-like Object.
    file-like Object对象不需要特定的继承，只需要有read()方法就好

"""

try:
    f = open('test.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

# 使用with语法，帮我们自动调用close
with open('test.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())
    # print(f.read())

# with open('test_write.txt', 'w') as ff:
#     ff.write('Hello, World!\n')  # 默认会覆盖原有内容

with open('test_write.txt', 'a') as ff:
    ff.write('Hello, append!\n')
