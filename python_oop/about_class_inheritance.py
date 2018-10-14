#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
inheritance:
    继承
    在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类
    继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
polymorphism:
    多态
    利用多态，可以实现经典的开闭原则
        对扩展开放
        对修改封闭

    动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
    Python的“file-like object“就是一种鸭子类型。
"""


class Animal(object):
    def run(self):
        print('Animal is running ...')


class Dog(Animal):
    def run(self):
        print('Dog is running ...')


class Cat(Animal):
    def run(self):
        print('Cat is running ...')


animal_1 = Animal()
dog = Dog()
cat = Cat()
animal_1.run()
dog.run()
cat.run()


def run_all(animal):
    """利用多态属性，可以接受Animal及其子类"""
    animal.run()
    animal.run()


run_all(animal_1)
run_all(dog)
run_all(cat)
