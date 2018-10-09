#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Higher-order function:函数可以接受函数作为参数
函数可以赋值给变量；变量可以指向函数；
函数名也是变量；


"""
f = abs
print(f(-1))


def my_add(x, y, f):
    return f(x) + f(y)


print(my_add(-5, -10, abs))










