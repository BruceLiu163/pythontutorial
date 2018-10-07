#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Iterator:迭代器
    可以被next()函数调用，并不断返回下一个值的对象成为迭代器。
    可以使用isinstance()判断一个对象是否是Iterator
    生成器都是Iterator(迭代器)
    list,tuple,dict,set,str都不是迭代器,都是可迭代对象

    Iterator对象表示一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据返回StopIteration错误
    可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度。
    Iterator的计算是惰性的，只有在需要返回下一个数据的时候它才会计算

    通过iter()函数，可以将Iterable转换为Iterator


    Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

Iterable:可迭代对象
    集合数据类型：
        list,tuple,dict,set,str等
        generator:包括生成器和带yield的generator function
    可以使用isinstance()判断一个对象是否是Iterable

    通过iter()函数，可以将Iterable转换为Iterator
    通过iter()函数，可以将Iterable转换为Iterator

"""
from collections.abc import Iterable
from collections.abc import Iterator

# list,tuple,dict,set,str都是可迭代对象 Iterable
print(isinstance([], Iterable))
print(isinstance((), Iterable))
print(isinstance({}, Iterable))
print(isinstance(set(['a', 'b', 'c']), Iterable))
print(isinstance('abc', Iterable))

# list,tuple,dict,set,str都不是迭代器 Iterator
print(isinstance([], Iterator))
print(isinstance((), Iterator))
print(isinstance({}, Iterator))
print(isinstance(set(['a', 'b', 'c']), Iterator))
print(isinstance('abc', Iterator))

# 通过iter()函数，可以将list,tuple,dict,set,str对象转换为迭代器 Iterator
print(isinstance(iter([]), Iterator))
print(isinstance(iter(()), Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance(iter(set(['a', 'b', 'c'])), Iterator))
print(isinstance(iter('abc'), Iterator))


