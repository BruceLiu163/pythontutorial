#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The zen of Python, by Tim Peters
# Beautiful is better than ugly.
# 优美胜于丑陋

# Explicit is better than implicit.
# 明了胜于晦涩

# Simple is better than complex.
# 简洁胜于复杂

# Complex is better than complicated.
# 复杂胜于凌乱

# Flat is better than nested.
# 扁平胜于嵌套

# Sparse is better than dense.
# 间隔胜于紧凑

# Readability counts.
# 可读性很重要

# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# 即使假借特例的实用性之名，也不可违背这些规则

# Errors should never pass silently.
# Unless explicitly silenced.
# 不要包容所有错误，除非你确定需要这么做

# In the face of ambiguity, refuse the temptation to guess.
# 当存在多种可能，不要尝试猜测

# There should be one-- and preferably only one --obvious way to do it.
# 而是尽量找一种，最好唯一一种明显的解决方案

# Although that way may not be obvious at first unless you're Dutch.

# 虽然这并不容易，因为你不是Python之父
# Now is better than never.
# Although never is often better than *right* now.
# 做也许好过不做，但不假思索就动手还不如不做

# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# 如果你无法向人描述你的方案，那肯定不是一个好方案；反之亦然

# Namespaces are one honking great idea -- let's do more of those!
# 命名空间是一种绝妙的理念，我们应当多加利用

import pygal
from data_visualization.die import Die

die_six_1 = Die()
die_six_2 = Die()

results = []
for roll_num in range(1000):
    result = die_six_1.roll() + die_six_2.roll()
    results.append(result)

frequencies = []
max_result = die_six_1.num_side + die_six_2.num_side
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.title = 'Results of rolling two D6 dice 1000 times.'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')
