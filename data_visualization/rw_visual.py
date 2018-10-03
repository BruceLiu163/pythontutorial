#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from data_visualization.random_work import RandomWalk

rw = RandomWalk()
rw.fill_walk()
point_numbers = list(range(rw.num_points))
# plt.scatter(rw.x_values, rw.y_values, s=15)
# edgecolors='none' 删除每个点周围的轮廓
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)

# 重新绘制起点、终点
plt.scatter(0, 0, c='green', edgecolors='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors='none', s=100)

# 隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.show()


