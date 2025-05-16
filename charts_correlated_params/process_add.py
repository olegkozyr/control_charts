from src.charts import shewhart as sh
from src.plots.chart_plot import ChartPlot
from src.plots.plot import Plot
from src.process_model.models import random_process

from src.plots.tools import create_directory
from src.plots.inits import one_chart_figsize, two_chart_figsize

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

from copy import copy


path = 'process_pics_02'
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
x[1] *= 1.1
x[5] *= 1.1
x[6] *= 0.7

mul = 1
add = -0.8

y_add = fun(x, mul, add)

# 1. process with additive correction

fig = plt.figure(figsize=(10, 6))
gs = fig.add_gridspec(1, 2,  width_ratios=(3, 1), #height_ratios=(1, 1),
                      left=0.1, right=0.9, bottom=0.1, top=0.9,
                      wspace=0.05, hspace=0.05)
# gs = fig.add_gridspec(1, 2)
# Create the Axes.
ax = fig.add_subplot(gs[0, 0])
ax_pdf = fig.add_subplot(gs[0, 1], sharey=ax)

## shewhart
ax.plot(points, x, marker='o',
        lw=2,
        color='black', label=f'$y_a=x$')
#ax.plot(points, y_add, marker='d', color='brown', label=f'$y_a=x{add}$')

limits = sh.ShewhartMethods.shewhart_limits(mean, sigma, n)
c = 'gray'
colors = {'ucl': c, 'cl': c, 'lcl': c}
ChartPlot.plot_limits(ax, limits, lw=3, colors=colors)
#disruptions_count = ChartPlot.plot_disruptions(ax, points, x, limits.ucl, limits.lcl, 6)
#print(f'disruptions_y1 = {disruptions_count}')
inds = x <= limits.lcl
print(inds)
ax.scatter(points[inds], x[inds],
           s=500, c='gray', marker='x',
           zorder=2)

x_pos = points[inds]
y_pos = x[inds]
print(x_pos, y_pos)
ax.annotate(f'$undefind\ alarm$',
            xy=(x_pos, y_pos),
            xytext=(x_pos*0.4, y_pos*0.99),
            arrowprops=dict(facecolor='black',
                                shrink=0.05))

limits_add = copy(limits)
limits_add.ucl += add
limits_add.cl = None
limits_add.lcl += add
ylabel = {'ucl': '$ucl^*_a$', 'cl': '$cl^*_a$', 'lcl': '$lcl^*_a$'}
ChartPlot.plot_limits(ax, limits_add,
                      lw=3,
                      ls='dashed', #(0, (5, 10)),
                      ylabel=ylabel,
                      colors=colors)

# ax.fill_between(points, limits_add.ucl, limits.ucl,
#                     color="none",hatch="X",edgecolor="grey")
# ax.fill_between(points, limits_add.lcl, limits.lcl,
#                     color="none",hatch="X",edgecolor="grey")

inds = x >= limits_add.ucl
print(inds)
ax.scatter(points[inds], x[inds],
           s=500, c='gray', marker='+',
           zorder=2)
x_pos = points[inds][0]
y_pos = x[inds][0]
print(x_pos, y_pos)
ax.annotate(r'$false\ alarms$',
            xy=(x_pos, y_pos),
            xytext=(x_pos*2, y_pos*1.06),
            arrowprops=dict(facecolor='black',
                                shrink=0.05))
x_pos = points[inds][1]
y_pos = x[inds][1]
ax.annotate('',
            xy=(x_pos, y_pos),
            xytext=(x_pos*0.83, y_pos*1.01),
            arrowprops=dict(facecolor='black',
                                shrink=0.05))

ax.tick_params(axis="y", labelleft=False)
x_pos = -1.4
y_pos_scale = 0.99
ax.text(x_pos, limits.ucl*y_pos_scale, '$UCL$')
ax.text(x_pos, limits_add.ucl*y_pos_scale, '$UCL^{*}$')
ax.text(x_pos, limits.cl*y_pos_scale, '$CL$')
ax.text(x_pos, limits.lcl*y_pos_scale, '$LCL$')
ax.text(x_pos, limits_add.lcl*y_pos_scale, '$LCL^{*}$')

ax.set_xlabel('$m$')
ax.grid()
#ax.legend(loc=1, fontsize='small')
#ax.set_title('номінальні межі')

## pdf
# no labels
ax_pdf.tick_params(axis="x", labelbottom=False)
ax_pdf.tick_params(axis="y", labelleft=False)
count = 101
bias = limits.cl * 0.3
x_pdf = np.linspace(limits.lcl-bias, limits.ucl+bias, count)
sigma_pdf = 3.
y_pdf = norm.pdf(np.linspace(-sigma_pdf, sigma_pdf, count))

def hatch_plot(ax, x, y, low, high):
    inds = (x >= low)
    x_hatch = x[inds]
    y_hatch = y[inds]
    x_hatch[(x_hatch >= high)] = high

    ax.plot(y_hatch, x_hatch, c='grey')
    ax.fill_between(y_hatch, x_hatch, low,
                    color="none", hatch="//",
                    edgecolor="grey")

hatch_plot(ax_pdf, x_pdf, y_pdf, limits_add.ucl, limits.ucl)
inds = (x_pdf >= limits.ucl)
x_hatch = x_pdf[inds]
y_hatch = y_pdf[inds]
x_hatch[:] = limits.ucl
ax_pdf.plot(y_hatch, x_hatch, c='grey', lw=3)
inds = (x_pdf >= limits_add.ucl)
x_hatch = x_pdf[inds]
y_hatch = y_pdf[inds]
x_hatch[:] = limits_add.ucl
ax_pdf.plot(y_hatch, x_hatch, c='grey', lw=3,
            ls='dashed')

inds = (x_pdf <= limits.lcl)
x_pdf_hatch = x_pdf[inds]
y_pdf_hatch = y_pdf[inds]
x_pdf_hatch[(x_pdf_hatch <= limits_add.lcl)] = limits_add.lcl
ax_pdf.plot(y_pdf_hatch, x_pdf_hatch, c='grey')
ax_pdf.fill_between(y_pdf_hatch, x_pdf_hatch, limits.lcl,
                    color="none", hatch=r"\\",
                    edgecolor="grey")
inds = (x_pdf <= limits_add.lcl)
x_pdf_hatch = x_pdf[inds]
y_pdf_hatch = y_pdf[inds]
x_pdf_hatch[:] = limits_add.lcl
ax_pdf.plot(y_pdf_hatch, x_pdf_hatch, c='grey',
            lw=3, ls='dashed')
inds = (x_pdf <= limits.lcl)
x_pdf_hatch = x_pdf[inds]
y_pdf_hatch = y_pdf[inds]
x_pdf_hatch[:] = limits.lcl
ax_pdf.plot(y_pdf_hatch, x_pdf_hatch, c='grey',
            lw=3)

ax_pdf.plot(y_pdf, x_pdf, lw=2, c='black')
ax_pdf.grid()

difference_array = np.absolute(x_pdf - limits.ucl*(1.05))
ind = difference_array.argmin()
print(ind)
ax_pdf.annotate('$f(x)$', xy=(y_pdf[ind], x_pdf[ind]),
                xytext=(y_pdf[ind]*2, x_pdf[ind]*1.1),
                arrowprops=dict(facecolor='black',
                                shrink=0.05))
#plt.tight_layout()
Plot.save_plot(fig, path, 'shewhart_plot_00_add')
plt.show()

