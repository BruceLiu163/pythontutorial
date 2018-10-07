#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
返回函数：
    高阶函数除了接受函数作为参数外，同样支持将函数作为返回值；
闭包：
    内部返回的函数会保存外部函数的相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”
"""


def calc_sum(*args):
    total = 0
    for i in args:
        total = total + i
    return total


def lazy_calc_sum(*args):
    """返回一个函数，当函数返回的时候，传入的参数会被保存在内部的函数中"""
    """返回的函数没有被立即执行，直到再次调用才会执行"""
    def init_calc_sum():
        total = 0
        for i in args:
            total = total + i
        return total
    return init_calc_sum


f1 = lazy_calc_sum(1, 3, 5, 7)
f2 = lazy_calc_sum(1, 3, 5, 7)
print(f1)
print(f1())
# 每次调用都返回一个新的函数，肯定不相等
print(f1 == f2)


def create_counter():
    """利用闭包返回一个计数器函数，每次调用它返回递增整数"""
    s = [0]

    def counter():
        s[0] = s[0] + 1
        return s[0]
    return counter


counter1 = create_counter()
counter2 = create_counter()
print(counter1(), counter1(), counter1(), counter1(), counter1())
print(counter2(), counter2())

