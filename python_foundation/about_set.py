#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
set：无序不重复元素序列
使用{}或者set()函数创建集合；创建空集合必须使用set(),{}会被认为是空的字典
set可以使用的运算符：-,&,|,^
&:求两个集合的交集
|:求两个集合的并集
-:对集合去掉重复
^:不同时包含的元素

method:
add():为set添加元素
clear():移除set中的所有元素
copy():拷贝一个集合，浅拷贝
difference():返回多个集合的差集
difference_update():移除集合中的元素，该元素在指定的集合也存在
discard():删除集合中指定的元素
intersection():返回集合的交集
intersection_update():删除集合中的元素，该元素在指定的集合不存在
isdisjoint():判断两个集合是否包含同样的元素，如果没有返回True，否则返回False
issubset():判断指定集合是否为该方法参数集合的子集
pop():随机移除元素
remove():移除指定元素
symmetric_difference():返回两个集合中不重复的元素集合
symmetric_difference_update():移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中
union():返回两个集合的并集
update():给集合添加元素
"""

a = set(['a', 'b', 'c'])
b = set(['c', 'd', 'e'])
print(a & b, a-b, a | b, a ^ b)

c = {x for x in 'abcdefghigklmn' if x not in 'abc'}
print(c)

a.pop()
print(a)
a.add('d')
print(a)
a.update({1, 3})
print(a)
a.remove(3)
a.discard(3)
print(a)






