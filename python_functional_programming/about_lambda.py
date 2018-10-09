#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lambda:
    对匿名函数提供了有限支持
    关键字lambda表示匿名函数，冒号前面的x表示函数参数
    匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
    匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
    匿名函数也可以作为一个返回值
"""
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
f = lambda x: x * x
print(f(5))


def my_build(x, y):
    """lambda作为返回值"""
    return lambda: x * x + y * y


print(list(map(lambda x: x * x, L)))
