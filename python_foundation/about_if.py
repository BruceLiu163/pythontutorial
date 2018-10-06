#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
if使用练习
特点：从上向下判断，如果某个判断为True,把该判断对应的语句执行后，就忽略掉剩余的else与elif
if condition1:
    execute1
elif condition2:
    execute2
else:
    execute3

常用操作符：>,>=,<,<=,!=
使用缩进来表示代码块
if可以嵌套
"""

age = 5
if age == 1:
    print('age is one')
elif age == 2:
    print('age is two')
elif age > 3:
    print('age more than three')
    if age == 4:
        print('age is 4')
    elif age == 5:
        print('age is five')
else:
    print('haha')
