#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
函数：函数名是指向一个函数对象的引用，可以把函数名赋值给一个变量，相当于一个别名
函数定义：
    如果没有return语句，默认返回None; return None可以简写为return
函数返回值：
    可以有多个返回值，本质上返回的是一个tuple
"""


def my_abs(x):
    """自定义绝对值函数"""
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def nop():
    pass

a = my_abs
print(a(-1))











