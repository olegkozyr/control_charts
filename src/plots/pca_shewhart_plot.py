from . shewhart_plot import ShewhartPlot
from . plot import Plot


class PCAShewhartPlot:
    default_figsize = Plot.default_figsize
    default_markersize = Plot.default_marker_size

    _default_ylabels = {'y1': r'$\bar f_1$',
                        'y2': r'$\bar f_2$'}

    @staticmethod
    def plot_2pcashewharts(x, f1, f2,
                           f1_limits,
                           f2_limits,
                           ylabels=None,
                           path=None,
                           file=None,
                           figsize=default_figsize):
        if ylabels is None:
            ylabels = PCAShewhartPlot._default_ylabels
        if file is None:
            file = 'pca_shewhart_plot'
        ShewhartPlot.plot_2shewharts(x, f1, f2,
                                     f1_limits,
                                     f2_limits,
                                     ylabels,
                                     path,
                                     file,
                                     figsize)

    @staticmethod
    def plot_2pcashewharts_disordered(x, f1, f2,
                                      f1_limits,
                                      f2_limits,
                                      f1_disordered=None,
                                      f2_disordered=None,
                                      ylabels=None,
                                      path=None,
                                      file=None,
                                      figsize=default_figsize):
        if ylabels is None:
            ylabels = PCAShewhartPlot._default_ylabels
        if file is None:
            file = 'pca_shewhart_plot_disordered'
        ShewhartPlot.plot_2shewharts_disordered(x, f1, f2,
                                                f1_limits,
                                                f2_limits,
                                                f1_disordered,
                                                f2_disordered,
                                                ylabels,
                                                path,
                                                file,
                                                figsize)

