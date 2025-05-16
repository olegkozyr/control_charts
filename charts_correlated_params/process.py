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

y_add = fun(x, 1., a)
y_mul = fun(x, b, 0.)

## shewhart

# 1. normal process
fig, ax = plt.subplots(1, 1, figsize=two_chart_figsize)
ax.plot(points, x, marker='o', color='blue', label='x')
ax.plot(points, y_add, marker='d', color='brown', label=f'$y_a$=x{a}')
ax.plot(points, y_mul, marker='*', color='lime', label=f'$y_m$={b}*x')

limits = sh.ShewhartMethods.shewhart_limits(mean, sigma, n)
ChartPlot.plot_limits(ax, limits)
disruptions_count = ChartPlot.plot_disruptions(ax, points, x, limits.ucl, limits.lcl, 6)
print(f'disruptions_y1 = {disruptions_count}')

ax.set_xlabel('m')
ax.grid()
ax.legend(loc=1, fontsize='small')
ax.set_title('номінальні межі')
plt.tight_layout()
Plot.save_plot(fig, path, 'shewhart_plot_02_normal')
plt.show()

# 2. process with additive correction
fig, ax = plt.subplots(1, 1, figsize=two_chart_figsize)
ax.plot(points, x, marker='o', color='blue', label='x')
ax.plot(points, y_add, marker='d', color='brown', label=f'$y_a$=x{a}')

limits_add = copy(limits)
limits_add.ucl += a
limits_add.cl += a
limits_add.lcl += a
ylabel = {'ucl': '$ucl^*_a$', 'cl': '$cl^*_a$', 'lcl': '$lcl^*_a$'}
ChartPlot.plot_limits(ax, limits_add, ls='dashed', ylabel=ylabel)

ax.set_xlabel('m')
ax.grid()
ax.legend(loc=1, fontsize='small')
ax.set_title('адитивна похибка та корекція меж')
plt.tight_layout()
Plot.save_plot(fig, path, 'shewhart_plot_02_add')
plt.show()

# 3. limits with multiplicative correction
fig, ax = plt.subplots(1, 1, figsize=two_chart_figsize)
ax.plot(points, x, marker='o', color='blue', label='x')
ax.plot(points, y_mul, marker='*', color='lime', label=f'$y_m$={b}*x')

limits_mul = copy(limits)
limits_mul.ucl *= b
limits_mul.cl *= b
limits_mul.lcl *= b
ylabel = {'ucl': '$ucl^*_m$', 'cl': '$cl^*_m$', 'lcl': '$lcl^*_m$'}
ChartPlot.plot_limits(ax, limits_mul, ls='dashed', ylabel=ylabel)

ax.set_xlabel('m')
ax.grid()
ax.legend(loc=1, fontsize='small')
ax.set_title('мультиплікативна похибка та корекція меж')
plt.tight_layout()
Plot.save_plot(fig, path, 'shewhart_plot_02_mul')
plt.show()



# 2. addition arror
#
# # _, ax = plt.subplots()
# # ax.plot(points, x, marker='o', label='x')
# # ax.plot(points, y1, marker='d', label=f'y={b}x')
# # ax.plot(points, (x - y1)**2, marker='*', label='(x - y)^2')
# # ax.set_xlabel('m')
# # ax.set_ylabel('x')
# # ax.grid()
# # ax.legend()
# # plt.show()
#
#
# limits_scaled = copy(limits)
# limits_scaled.ucl *= b
# limits_scaled.cl = None
# limits_scaled.lcl *= b
#
# fig, ax = plt.subplots(1, 1, figsize=two_chart_figsize)
# ax.plot(points, x, marker='o', color='blue', label='x')
# ax.plot(points, y, marker='d', color='brown', label=f'y={a}')
# ax.plot(points, y1, marker='*', color='lime', label=f'y={b}x')
#
# ChartPlot.plot_limits(ax, limits)
# disruptions_count = ChartPlot.plot_disruptions(ax, points, y, limits.ucl, limits.lcl, 6)
# print(f'disruptions_y1 = {disruptions_count}')
#
# ylabel = {'ucl': 'ucl*', 'cl': 'cl*', 'lcl': 'lcl*'}
# ChartPlot.plot_limits(ax, limits_scaled, ls='dashed', ylabel=ylabel)
#
# ax.set_xlabel('m')
# ax.grid()
# ax.legend(loc=0, fontsize='small')
# Plot.save_plot(fig, path, 'shewhart_plot')
# plt.show()
#
#
