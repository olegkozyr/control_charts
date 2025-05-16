import numpy as np


class ChartPlot:
    @staticmethod
    def plot_limits(ax, limits, lw=2, ls='-', xlabel=None, ylabel=None, colors=None):
        if colors is None:
            colors = {'ucl': 'red', 'cl': 'green', 'lcl': 'orange'}

        if ylabel is None:
            ylabel = {'ucl': 'ucl', 'cl': 'cl', 'lcl': 'lcl'}

        if not limits.ucl is None:
            ax.axhline(limits.ucl, lw=lw, ls=ls, c=colors['ucl'],
                       label=f'{ylabel["ucl"]} = {round(limits.ucl, 2)}')
        if not limits.cl is None:
            ax.axhline(limits.cl, lw=lw, ls=ls, c=colors['cl'],
                       label=f'{ylabel["cl"]} = {round(limits.cl, 2)}')
        if not limits.lcl is None:
            ax.axhline(limits.lcl, lw=lw, ls=ls, c=colors['lcl'],
                       label=f'{ylabel["lcl"]} = {round(limits.lcl, 2)}')
        if not xlabel is None:
            ax.set_xlabel(xlabel)

    @staticmethod
    def proces_disruption(y, ucl, lcl):
        disruption_inds = None

        if not y is None:
            ucl_disruptions = y > ucl
            if not lcl is None:
                lcl_disruptions = y < lcl
            else:
                lcl_disruptions = np.full_like(ucl_disruptions, False)

            disruption_inds = np.logical_or(ucl_disruptions, lcl_disruptions)

        return disruption_inds

    @staticmethod
    def plot_disruptions(ax, x, y, ucl, lcl, markersize):
        disruption_inds = ChartPlot.proces_disruption(y,
                                                      ucl,
                                                      lcl)
        if not disruption_inds is None:
            ax.scatter(x[disruption_inds],
                       y[disruption_inds],
                       s=markersize ** 2,
                       c='red',
                       zorder=2)
        else:
            disruption_inds = [0]

        return sum(disruption_inds)
