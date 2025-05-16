#import sys
#sys.path.insert(0, '/home/helgi/Documents/python/control_charts/charts/control_charts')

from src.charts import shewhart as sh
from src.plots.chart_plot import ChartPlot
from src.plots.plot import Plot
from src.process_model.models import random_process

from src.plots.tools import create_directory
from src.plots.inits import one_chart_figsize, two_chart_figsize

import numpy as np
import matplotlib.pyplot as plt

from copy import copy


path = 'process_pics_01'
create_directory(path)

## data for modeling
alpha = 0.005
p = 1

n = 5
m = 10
mean = 4.5
sigma = 1.0

points = np.arange(m)

def fun(x, b, a):
    y = b*x + a

    return y

x = random_process(mean, sigma, n, m)
x[5] *= 1.2
x[6] *= 0.82

b = 0.8
a = -0.8

y_mul_add = fun(x, b, a)

## shewhart

# 1. normal process
fig, ax = plt.subplots(1, 1, figsize=two_chart_figsize)
ax.plot(points, x, marker='o', color='blue', label='x')
ax.plot(points, y_mul_add, marker='d', color='brown', label=f'y={b}*x{a}')

limits = sh.ShewhartMethods.shewhart_limits(mean, sigma, n)
ChartPlot.plot_limits(ax, limits)
disruptions_count = ChartPlot.plot_disruptions(ax, points, x, limits.ucl, limits.lcl, 6)
print(f'disruptions_y1 = {disruptions_count}')

ax.set_xlabel('m')
ax.grid()
ax.legend(loc=1, fontsize='small')
ax.set_title('номінальні межі')
plt.tight_layout()
Plot.save_plot(fig, path, 'shewhart_plot_03_mul_add')
plt.show()

# 2. process with additive correction
fig, ax = plt.subplots(1, 1, figsize=two_chart_figsize)
ax.plot(points, x, marker='o', color='blue', label='x')
ax.plot(points, y_mul_add, marker='d', color='brown', label=f'y={b}*x{a}')

limits_mul_add = copy(limits)
limits_mul_add.ucl = limits_mul_add.ucl * b + a
limits_mul_add.cl = limits_mul_add.cl * b + a
limits_mul_add.lcl = limits_mul_add.lcl * b + a
ylabel = {'ucl': 'ucl*', 'cl': 'cl*', 'lcl': 'lcl*'}
ChartPlot.plot_limits(ax, limits_mul_add, ls='dashed', ylabel=ylabel)

ax.set_xlabel('m')
ax.grid()
ax.legend(loc=1, fontsize='small')
ax.set_title('b*x+a та корекція меж')
plt.tight_layout()
Plot.save_plot(fig, path, 'shewhart_plot_03_corrected')
plt.show()


