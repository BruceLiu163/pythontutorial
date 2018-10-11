#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数

__:以双下划线开头的变量，在类的外部不能访问；
__xxx__:双下划线开头，双下划线结尾的都是特殊变量，可以在类的外部访问；
_:单下划线开头，表示是private变量；但是可以被类的外部直接访问；
    “虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

    强烈不建议在类的外部访问private变量

"""


class Student(object):

    def __init__(self, name, score, gender='F'):
        self.__name = name
        self.__score = score
        self.__gender = gender

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    def print_score(self):
        print("%s %s" % self.__name, self.__score)

    def get_grade(self):
        if self.__score > 90:
            return 'A'
        elif self.__score > 80:
            return 'B'
        elif self.__score > 60:
            return 'C'
        else:
            return 'D'


tina = Student('Tina', 100)
tony = Student('Tony', 30)
print(tina.get_grade())
print(tony.get_grade())

