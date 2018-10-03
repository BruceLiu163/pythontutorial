#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint


class Die():
    """表示一个骰子的类"""
    def __init__(self, num_side=6):
        """骰子默认是6个面"""
        self.num_side = num_side

    def roll(self):
        """返回一个位于1和骰子面之间的随机数"""
        return randint(1, self.num_side)

