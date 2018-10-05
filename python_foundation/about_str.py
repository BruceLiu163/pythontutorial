#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 字符串及其编码的学习
# ASCII、Unicode、UTF-8

# ASCII编码：127个字符

# Unicode编码：期望把所有的语言都统一到一套编码里面
# ASCII编码是1个字节，Unicode是两个字节

# UTF-8编码：在Unicode的基础上转化为“可变长编码”
# UTF-8编码中，英文字母1个字节、汉字通常3个字节、生僻字有4-6个字节

# ord()函数获取字符串的整数表示；chr()函数把编码转换为对应的字符串
print(ord('A'))
print(chr(66))
print(chr(25991))

# bytes类型数据：使用b''或者b""表示
print(b'ABC')
print('ABC')

# str 与 bytes之间可以通过函数进行相互转化
# encode():str --> bytes
# decode():bytes --> str
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# len()函数：计算str包含多少个字符，计算bytes包含字节数
print(len('ABC'))
print(len(b'ABC'))
print(len('中文'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))

# str的format,通过%来实现，与C语言实现方式一致
# 常见占位符：%d,%f,%s,%x(整数、浮点数、字符串、十六进制整数)
# 前面几个占位符，后面就跟几个变量或者值，顺序要对应好；如果只有一个占位符，括号可以省略
print('Hello, %s, you have $%d.' % ('Bruce', 123))
# 格式化整数和浮点数，还可以指定是否补0和整数，小数的位数
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.14159)
# format()函数是另外一种格式化字符串的方法，使用{0}，{1}表示占位符
print('Hello, {0}, you have ${1:.1f}'.format('Bruce', 18.256))








