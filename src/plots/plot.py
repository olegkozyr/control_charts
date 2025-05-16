import matplotlib.pyplot as plt
import os
from . inits import two_chart_figsize


class Plot:
    default_figsize = two_chart_figsize # (5, 5)
    default_marker_size = 4

    @staticmethod
    def save_plot(fig, path, file):
        if not path is None:
            path = os.path.join(path, file)
            fig.savefig(path, bbox_inches="tight")

    @staticmethod
    def plot_factors(x, y1, y2, mean, path=None):
        fig, axes = plt.subplots(2, 1, figsize=Plot.default_figsize)
        ax = axes[0]
        ax.plot(x, y1, marker='o', c='blue')
        ax.axhline(mean[0], c='green')
        ax.set_ylabel(r'$\bar x_1$')
        ax.grid()
        ax = axes[1]
        ax.plot(x, y2, marker='o', c='blue')
        ax.axhline(mean[1], c='green')
        ax.set_xlabel(r'$m$')
        ax.set_ylabel(r'$\bar x_2$')
        ax.grid()
        plt.tight_layout()

        Plot.save_plot(fig, path, 'factors_plot')

        plt.show()

    @staticmethod
    def plot_scatter(y1, y2, mean,
                     path=None,
                     figsize=default_figsize):
        fig, ax = plt.subplots(1, 1, figsize=figsize)
        ax.scatter(y1, y2, c='blue')
        ax.axvline(mean[0], c='green', label='$a_1$ = ' +
                                             f'{mean[0]}')
        ax.axhline(mean[1], c='yellow', label='$a_2$ = ' +
                                              f'{mean[1]}')
        ax.set_xlabel(r'$\bar x_1$')
        ax.set_ylabel(r'$\bar x_2$')
        ax.grid()
        ax.legend()

        Plot.save_plot(fig, path, 'scater_plot')

        plt.show()

