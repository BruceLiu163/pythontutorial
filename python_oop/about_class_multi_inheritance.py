#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python支持多重继承
    多重继承：这种设计通常称之为MixIn
"""


class Animal(object):
    def eat(self):
        print('Eating...')


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class RunnableMixIn(object):
    def run(self):
        print('Running ...')


class FlyableMixIn(object):
    def fly(self):
        print('Flying...')


class Dog(Mammal, RunnableMixIn):
    pass


class Bat(Mammal, FlyableMixIn):
    pass


dog1 = Dog()
dog1.run()
dog1.eat()
bat1 = Bat()
bat1.eat()
bat1.fly()
