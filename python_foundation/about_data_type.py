#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python区分大小写
# Python是动态语言（变量本身类型不固定）；与之对应的是静态语言（在定义变量时候必须指定变量类型）

# 这一节，我们讲学习Python的基本数据类型
# 整数、浮点数、字符串、布尔值、空值、列表、字典、自定义数据类型、bytes

# 字符串：用单引号or双引号
# \表示转意符：\n \t \\
# r''：''内部的字符串默认不转意
# '''...''' 用于表示多行内容

# 布尔值：True、False
# 运算符：and(both True is True)、or(anyone True is True)、not

# 空值是Python的一个特殊字符，用None表示

# bytes类型的数据用b前缀的单引号或者双引号

# 变量：
# 变量命名规则：大小写英文、数字和_组合，且不能用数字开头
# 变量使用'='复制

# 常量：就是不能变的变量

n = 123
f = 456.789
s1 = 'Hello, Bruce'
s2 = 'Hello, \'Bruce\''
s3 = r'Hello, "Bruce"'
s4 = r'''Hello,
Bruce!'''

print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)


