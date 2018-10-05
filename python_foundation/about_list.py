#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 序列都可以进行的操作有：索引、切片、加、乘、检查成员
# list是可变有序集合，可以添加、删除元素
# 可变有序 可变有序 可变有序 可变有序 可变有序 可变有序 可变有序 可变有序 可变有序
# 使用[]进行初始化赋值
# list内部元素的数据类型可以不同
# 使用从0开始的索引获取对应位置的元素；倒序使用-1，-2，-3表示从末尾开始的索引位置
# 索引超出范围，抛出IndexError错误
# 通过len()函数获取list的元素个数
# 空的list，长度为0

# 列表函数：len(list),max(list),min(list),list(seq)
# len(list):列表元素个数
# max(list):返回列表元素最大值
# min(list):返回列表元素最小值
# list(seq):将元组转换为列表

# 列表方法：append(),count(),extend(),index(),insert(),pop(),remove(),reverse(),sort(),clear(),copy()
# append():在列表末尾添加新的对象
# count():统计某个元素在列表中出现的次数
# extend():在列表末尾一次性追加另一个序列的多个值（用新列表扩展原来的列表）
# index():从列表中找出某个值第一个匹配项的索引位置
# pop():移除列表中的一个元素（默认最后一个元素），并返回该元素的值
# remove():移除列表中某个值的第一个匹配项
# reverse():反向列表总的与元素
# sort():对原列表进行排序
# clear():清空列表
# copy():复制列表

# 列表脚本操作符：+，*，in
# +：表示组合
# *：表示重复
# in：表示是否存在于列表
# for x in list:xxx 表示迭代

families = ['Bruce', 'Rachel', 'Tina', 'Tom']
# 空的list，长度为0
L = []
print(families)
print(families[0], families[1], families[2], families[3])
print(families[-1], families[-2], families[-3], families[-4])
print('families has', len(families), 'elements')

# append(),insert(),pop()
# append():在列表末尾追加元素
families.append('Jack Ma')
print(families)
# insert():把元素插入到指定位置
families.insert(0, 'Alice')
print(families)
# pop():删除指定位置的元素，不填入参数的时候，默认删除list末尾的元素
families.pop()
print(families)
families.pop(0)
print(families)

# reverse():将list翻转
families.reverse()
print(families)







