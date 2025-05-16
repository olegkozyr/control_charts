from src.pca import pca
from src.charts import shewhart as sh, hotelling as hot
from src.process_model.models import multivatiate_random_process
from src.disorders.disorder import bias
from src.stats.covariance import sigma_covarience_matrix

from src.plots import plot
from src.plots import shewhart_plot as sh_plot
from src.plots import pca_shewhart_plot as pca_sh_plot
from src.plots import hotelling_plot as hot_plot
from src.plots.tools import create_directory

import numpy as np


path = '../figs/figs_01'
create_directory(path)

## data for modeling
alpha = 0.005
p = 2

seed = 0

n = 5
m = 15
mean = np.array([4.5, 21.])
sigma = np.array([0.3, 1.0])
rho = 0.5

points = np.arange(m)

cov = sigma_covarience_matrix(sigma, rho)
print(f'cov = {cov}')

x = multivatiate_random_process(mean, cov, n, m, seed)
x1 = x[:, 0]
x2 = x[:, 1]

y1 = bias(x1, 1, 0.93)
y1 = bias(y1, 7, 0.94)
y = np.vstack([y1, x2]).T - mean

plot.Plot.plot_factors(points, x1, x2, mean, path)
plot.Plot.plot_scatter(x1, x2, mean, path)

## shewhart
sl1, sl2 = sh.ShewhartMethods.get_limits(mean, sigma, n)
print(f'sl1 = {sl1}\nsl2 = {sl2}')
# sh_plot.ShewhartPlot.plot_2shewharts(points,
#                                      x1, x2,
#                                      sl1, sl2, path=path)
# sh_plot.ShewhartPlot.plot_2shewharts_disordered(points,
#                                                 x1, x2,
#                                                 sl1, sl2,
#                                                 y1_disordered=y1,
#                                                 path=path)
sh_plot.ShewhartPlot.plot_2shewharts(points,
                                     y1, x2,
                                     sl1, sl2, path=path)

## pca
pca_data = pca.PCA_NUM.pca_eig_num(y, cov)
pc = pca_data.pc
lam = pca_data.eig_values
eigenvectors = pca_data.coefs
fsl1, fsl2 = sh.ShewhartPCA.get_limits(lam, n)
pca_sh_plot.PCAShewhartPlot.plot_2pcashewharts(points,
                                               pc[:, 0], pc[:, 1],
                                               fsl1, fsl2, path=path)

## hotelling
t2 = hot.Hotelling.t2_statistics(y, cov, n)
print(f't2 =\n{t2}')
hot_ucl = hot.Hotelling.ucl(1 - alpha, p)
hot_plot.HotellingPlot.plot_hotelling(points, t2, hot_ucl, path=path)

## hotelling criterion
t2h = hot.Hotelling.criterion(y, cov, n)
# hot_plot.HotellingPlot.plot_hotelling_criterion(points, t2h, hot_ucl,
#                                                 path=path)
