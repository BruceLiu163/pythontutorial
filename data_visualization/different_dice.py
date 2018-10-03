#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from data_visualization.die import Die
import pygal

# two die
die_six = Die()
die_ten = Die(10)
results = []
for roll_num in range(50000):
    results.append(die_six.roll() + die_ten.roll())

max_result = die_ten.num_side + die_six.num_side
frequencies = []
for value in range(2, max_result+1):
    frequencies.append(results.count(value))

hist = pygal.Bar()

hist.title = 'Results of rolling a D6 and D10 50,000 times'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'
hist.add('D6 + D10', frequencies)
hist.render_to_file('different_dice_visual.svg')




