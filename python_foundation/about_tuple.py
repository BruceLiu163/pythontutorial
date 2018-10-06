#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
元组：有序不可变，使用()进行赋值
空的元组可以使用()进行赋值；
在赋值只有1个元素的元组时候，第一个元素后面需要有,
families = ('Rachel',)

元组的元素值不可以修改
元组运算符：+,*,in

元组内置函数：len(tuple),max(tuple),min(tuple),tuple(seq)
len(tuple):计算元组元素个数
max(tuple):返回元组中元素的最大值
min(tuple):返回元组中元素的最小值
tuple(req):将列表转换为元组
"""

families = ('Rachel', 'Bruce', 'Tina', 'Tina')
print(families)
family_one = ('Rachel',)
print(family_one)

tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
tup3 = tup1 + tup2
print(tup3)
tup4 = tup3 * 2
print(tup4)

print(tup4[2:])

print(tup4.count(6))
