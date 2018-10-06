#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
循环的练习
for(for ... else)
while(while ... else)
break:提前退出循环
continue:跳过当次循环
"""


def sum_for(begin=1, end=100, step=1):
    """根据给定的开始、结束参数及步长求和"""
    sum1 = 0
    for x in list(range(begin, end, step)):
        sum1 = sum1 + x
    else:
        print('For is finished.')
    return sum1


def sum_while(begin=1, end=100, step=1):
    """根据给定的开始、结束参数及步长求和"""
    sum1 = 0
    n = begin
    while n < end:
        sum1 = sum1 + n
        n = n + step
    else:
        print('While is finished')
    return sum1


print(sum_for(1, 10, 2))
print(sum_while(1, 10, 2))






