#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__slots__:
    正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。
    可以通过__slots__变量，来限制类的实例可以定义的变量；

    __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用
    除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
"""


class Student(object):
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


class HighSchoolStudent(Student):
    __slots__ = ('gender',)


stu_1 = Student('Bruce', 20)
print(stu_1.name, stu_1.age)

# stu_1.gender = 'F'    #

high_stu_1 = HighSchoolStudent('Bruce', 20)
high_stu_1.gender = 'F'
print(high_stu_1.gender)
