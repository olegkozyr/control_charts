import matplotlib.pyplot as plt

from .plot import Plot
from .chart_plot import ChartPlot
from .inits import one_chart_figsize
from ..charts.shewhart import Limits


class HotellingPlot:
    _default_hotelling_figsize = one_chart_figsize
    _default_markersize = Plot.default_marker_size
    _ylabel = r'$T^2_H$'

    @staticmethod
    def _limit(ax, ucl):
        limits = Limits(ucl, None, None)
        ChartPlot.plot_limits(ax, limits)

        return limits

    @staticmethod
    def _disruptions(ax, x, t2, limits):
        disruptions_count = ChartPlot.plot_disruptions(ax, x, t2,
                                                       limits.ucl,
                                                       limits.lcl,
                                                       HotellingPlot._default_markersize)
        print(f'disruptions_y = {disruptions_count}')

        return disruptions_count

    @staticmethod
    def _plot(ax, x, t2, c='blue', plot_label=None):
        ax.plot(x, t2, marker='o',
                markersize=HotellingPlot._default_markersize,
                c=c, label=plot_label)

    @staticmethod
    def _finish(ax, ylabel, legend_loc=1):
        ax.set_xlabel('m')
        ax.set_ylabel(ylabel)
        ax.grid()
        ax.legend(loc=legend_loc)
        plt.tight_layout()

    @staticmethod
    def plot_hotelling(
            x, t2, ucl,
            ylabel=None,
            path=None,
            file=None,
            figsize=_default_hotelling_figsize):
        if ylabel is None:
            ylabel = HotellingPlot._ylabel

        fig, ax = plt.subplots(figsize=figsize)
        HotellingPlot._plot(ax, x, t2)
        limits = HotellingPlot._limit(ax, ucl)
        HotellingPlot._disruptions(ax, x, t2, limits)
        HotellingPlot._finish(ax, ylabel)

        if file is None:
            file = 'hotelling_plot'
        Plot.save_plot(fig, path, file)

        plt.show()

    @staticmethod
    def plot_hotelling_criterion(
            x, t2, ucl,
            ylabel=None,
            path=None,
            file=None,
            figsize=_default_hotelling_figsize):
        if ylabel is None:
            ylabel = HotellingPlot._ylabel

        fig, ax = plt.subplots(figsize=figsize)
        HotellingPlot._plot(ax, x, t2[:, 0], plot_label=r'$T^2_{H_{x1}}$')
        HotellingPlot._plot(ax, x, t2[:, 1], 'green', plot_label=r'$T^2_{H_{x2}}$')
        limits = HotellingPlot._limit(ax, ucl)
        HotellingPlot._disruptions(ax, x, t2[:, 0], limits)
        HotellingPlot._disruptions(ax, x, t2[:, 1], limits)
        HotellingPlot._finish(ax, ylabel)

        if file is None:
            file = 'hotelling_criterion_plot'
        Plot.save_plot(fig, path, file)

        plt.show()
