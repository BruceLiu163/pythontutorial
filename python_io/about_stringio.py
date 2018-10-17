#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
StringIO:
    基于内存的io读写str
BytesIO:
    在内存中读写bytes,二进制操作

上面两个和文件的读写接口保持一致的
"""

from io import StringIO
from io import BytesIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

ff = StringIO('Shanghai\nBeijing\nChongqing\n')
while True:
    s = ff.readline()
    if s == '':
        break
    print(s.strip())

bf = BytesIO()
bf.write('中文'.encode('utf-8'))
print(bf.getvalue())
