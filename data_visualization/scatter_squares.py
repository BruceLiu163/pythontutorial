#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# For more information, please browse https://matplotlib.org/

import matplotlib.pyplot as plt


# simple
def scatter_simple():
    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 4, 9, 16, 25]
    plt.scatter(x_values, y_values, edgecolors='none', s=400)

    # set title、x-axis、y-axis
    plt.title('Square Numbers', fontsize=24)
    plt.xlabel('Value', fontsize=24)
    plt.ylabel('Square of Value', fontsize=14)
    plt.show()


# basic setting
def scatter_setting():
    x_values = list(range(1, 1001))
    y_values = [x ** 2 for x in x_values]
    plt.scatter(x_values, y_values, edgecolors='none', s=4)

    # set title、x-axis、y-axis
    plt.title('Square Numbers', fontsize=24)
    plt.xlabel('Value', fontsize=24)
    plt.ylabel('Square of Value', fontsize=14)

    # set axis's scope
    plt.axis([0, 1100, 0, 1100000])

    plt.show()


# set color = 'red'
def scatter_color():
    x_values = list(range(1, 1001))
    y_values = [x ** 2 for x in x_values]
    plt.scatter(x_values, y_values, c='red', edgecolors='none', s=4)

    # set title、x-axis、y-axis
    plt.title('Square Numbers', fontsize=24)
    plt.xlabel('Value', fontsize=24)
    plt.ylabel('Square of Value', fontsize=14)

    # set axis's scope
    plt.axis([0, 1100, 0, 1100000])

    plt.show()


# set gradient color by y_values
def scatter_gradient_color():
    x_values = list(range(1, 1001))
    y_values = [x ** 2 for x in x_values]
    plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=4)

    # set title、x-axis、y-axis
    plt.title('Square Numbers', fontsize=24)
    plt.xlabel('Value', fontsize=24)
    plt.ylabel('Square of Value', fontsize=14)

    # set axis's scope
    plt.axis([0, 1100, 0, 1100000])

    # plt.show()
    plt.savefig('squares_plot.png', bbox_inches='tight')


scatter_simple()
scatter_setting()
scatter_color()
scatter_gradient_color()
