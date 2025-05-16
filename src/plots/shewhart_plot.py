import matplotlib.pyplot as plt
from . plot import Plot
from . chart_plot import ChartPlot
from . inits import one_chart_figsize


class ShewhartPlot:
    default_figsize = Plot.default_figsize
    default_markersize = Plot.default_marker_size

    @staticmethod
    def _plot_shewhart(ax, x, y,
                       limits,
                       ylabel,
                       markersize):
        ax.plot(x, y, marker='o',
                markersize=markersize,
                c='blue')
        ChartPlot.plot_limits(ax, limits)
        ax.set_ylabel(ylabel)
        ax.grid()
        ax.legend()

        disruptions_count = ChartPlot.plot_disruptions(ax, x, y, limits.ucl,
                                                       limits.lcl, markersize)

        return disruptions_count

    @staticmethod
    def _plot_2shewharts(x, y1, y2,
                         y1_limits,
                         y2_limits,
                         ylabels=None,
                         figsize=default_figsize):
        if ylabels is None:
            ylabels = {'y1': r'$\bar x_1$',
                       'y2': r'$\bar x_2$'}

        fig, axes = plt.subplots(2, 1, figsize=figsize)

        disruptions_count = ShewhartPlot._plot_shewhart(axes[0], x, y1,
                                                        y1_limits,
                                                        ylabels['y1'],
                                                        ShewhartPlot.default_markersize)
        print(f'disruptions_y1 = {disruptions_count}')

        disruptions_count = ShewhartPlot._plot_shewhart(axes[1], x, y2,
                                                        y2_limits,
                                                        ylabels['y2'],
                                                        ShewhartPlot.default_markersize)
        print(f'disruptions_y2 = {disruptions_count}')

        axes[1].set_xlabel('m')

        plt.tight_layout()

        return fig, axes

    def _plot_disordered(ax, x, y):
        if not y is None:
            ax.plot(x, y, marker='o',
                    markersize=Plot.default_marker_size,
                    c='lime', label='розладнаний')
            ax.legend()

    @staticmethod
    def plot_2shewharts_disordered(x, y1, y2,
                                   y1_limits,
                                   y2_limits,
                                   y1_disordered=None,
                                   y2_disordered=None,
                                   ylabels=None,
                                   path=None,
                                   file=None,
                                   figsize=default_figsize):
        fig, axes = ShewhartPlot._plot_2shewharts(x, y1, y2,
                                                  y1_limits,
                                                  y2_limits,
                                                  ylabels,
                                                  figsize)

        ax = axes[0]
        ShewhartPlot._plot_disordered(ax, x, y1_disordered)
        disruptions_count = ChartPlot.plot_disruptions(ax, x, y1_disordered,
                                                       y1_limits.ucl,
                                                       y1_limits.lcl,
                                                       ShewhartPlot.default_markersize)
        print(f'disruptions_y1_desorder = {disruptions_count}')
        ax = axes[1]
        ShewhartPlot._plot_disordered(ax, x, y2_disordered)
        disruptions_count = ChartPlot.plot_disruptions(ax, x, y2_disordered,
                                                       y2_limits.ucl,
                                                       y2_limits.lcl,
                                                       ShewhartPlot.default_markersize)
        print(f'disruptionss_y1_desorder = {disruptions_count}')

        if file is None:
            file = 'shewhart_plot_disordered'
        Plot.save_plot(fig, path, file)

        plt.show()

    @staticmethod
    def plot_2shewharts(
            x, y1, y2,
            y1_limits,
            y2_limits,
            ylabels=None,
            path=None,
            file=None,
            figsize=default_figsize):
        fig, _ = ShewhartPlot._plot_2shewharts(x, y1, y2,
                                               y1_limits,
                                               y2_limits,
                                               ylabels,
                                               figsize)

        if file is None:
            file = 'shewhart_plot'
        Plot.save_plot(fig, path, file)

        plt.show()


    @staticmethod
    def plot_shewhart(x, y,
                      y_limits,
                      ylabel=None,
                      path=None,
                      file=None,
                      figsize=one_chart_figsize):
        if ylabel is None:
            ylabel = {'y': r'$\bar x$'}

        fig, ax = plt.subplots(1, 1, figsize=figsize)
        disruptions_count = ShewhartPlot._plot_shewhart(ax, x, y,
                                                        y_limits,
                                                        ylabel['y'],
                                                        ShewhartPlot.default_markersize)
        print(f'disruptions_y = {disruptions_count}')

        ax.set_xlabel('m')
        plt.tight_layout()

        if file is None:
            file = 'shewhart_plot'
        Plot.save_plot(fig, path, file)

        plt.show()


    @staticmethod
    def plot_shewhart(x, y,
                      y_limits,
                      ylabel=None,
                      path=None,
                      file=None,
                      figsize=one_chart_figsize):
        if ylabel is None:
            ylabel = {'y': r'$\bar x$'}

        fig, ax = plt.subplots(1, 1, figsize=figsize)
        disruptions_count = ShewhartPlot._plot_shewhart(ax, x, y,
                                                        y_limits,
                                                        ylabel['y'],
                                                        ShewhartPlot.default_markersize)
        print(f'disruptions_y = {disruptions_count}')

        ax.set_xlabel('m')
        plt.tight_layout()

        if file is None:
            file = 'shewhart_plot'
        Plot.save_plot(fig, path, file)

        plt.show()



