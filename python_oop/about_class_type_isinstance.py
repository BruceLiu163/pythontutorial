#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
type():
    获取对象的类型
isinstance():
    判断对象是否是某个类型
dir():
    获取一个对象所有的属性和方法
getattr(),setattr(),hasattr()：
    操作一个对象的状态


类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
在Python中，如果你调用len()函数试图获取一个对象的长度，
实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以下面的代码是等价的
len('ABC')
'ABC'.__len__()



在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，
因为相同名称的实例属性将屏蔽掉类属性，
但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
    实例属性属于各个实例所有，互不干扰；
    类属性属于类所有，所有实例共享一个属性；
    不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。

"""


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

    @staticmethod
    def print_1():
        print('This is a static method')

    @classmethod
    def get_count(cls):
        print(cls.count)
        return cls.count


s1 = Student('Bruce')
s2 = Student('Tina')
print(Student.count)

Student.print_1()
Student.get_count()

"""类属性，实例属性"""


class Dog(object):
    # 全局变量，可以使用Dog.name访问全局变量
    name = 'Default Dog name'

    def __init__(self, name):
        self.name = name


dog = Dog('bubu')
print(Dog.name)
print(dog.name)

dog.name = 'lulu'
print(Dog.name)
print(dog.name)
