#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from data_visualization.die import Die
import pygal

die = Die()
results = []
for roll_num in range(1000):
    results.append(die.roll())

print(results)
frequencies = []

# 统计每面出现次数
for value in range(1, die.num_side+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# 对结果进行可视化展示
hist = pygal.Bar()
hist.title = 'Results of rolling one D6 1000 times'
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')




