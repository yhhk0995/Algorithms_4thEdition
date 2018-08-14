# -*- coding: utf8 -*-

import matplotlib.pyplot as plt
import numpy as np

# two types of Artists:
# primitive: Line2D, Rectangle, Text, AxesImage, etc.
# container: figure, subplot, axes (places to put primitive)

fig = plt.figure()  # create a figure instance

# ax1 = fig.add_subplot(2, 1, 1)  # 2 rows, 1 column, 1st plot
# ax2 = fig.add_subplot(2, 1, 2)  # 2 rows, 1 column, 1st plot

ax1 = fig.add_axes([0.1, 0.6, 0.8, 0.35])  # [left, bottom, width, height]
ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.35])  # [left, bottom, width, height]

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2 * np.pi * t)

# ax.plot会生成一个Line2D对象，并添加到ax.lines列表中。返回值即为该list。
# 此时，line就指向ax.lines的第一个对象
line, = ax1.plot(t, s, color="blue", lw=2)  # line width
# del ax1.lines[0]
# ax1.lines.remove(line)
text_x = ax1.set_xlabel("data_t")  # # returns a Text instance (one type of Artist primitive)
text_y = ax1.set_ylabel('data_s')

# Fixing random state for reproducibility
np.random.seed(20180802)

n, bins, patches = ax2.hist(np.random.randn(1000), 50, facecolor='yellow', edgecolor='blue')
ax2.set_xlabel('time (s)')

ax2.clear()
ax2.bar(range(10), range(10), align='center')

plt.show()