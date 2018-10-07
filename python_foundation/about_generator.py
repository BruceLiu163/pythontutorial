#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generator:生成器
    在Python中，这种一边循环一边计算的机制，称为生成器：generator

    第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
        g
    如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
        fib()
"""
g = (x * x for x in range(10))
for n in g:
    print(n)


def fib(max_num):
    """列表生成器，使用yield；定义了斐波拉契数列的推算规则"""
    n, a, b = 0, 0, 1
    while n < max_num:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


f = fib(10)
print(f)
for n in f:
    print(n)
