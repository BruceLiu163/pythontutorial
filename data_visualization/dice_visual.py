#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.title = 'Results of rolling two D6 dice 1000 times.'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')








