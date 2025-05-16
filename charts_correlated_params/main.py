from src.test import initials

from src.stats.covariance import sigma_covarience_matrix
from src.pca import pca
from src.charts import shewhart as sh, hotelling as hot

from src.plots import plot
from src.plots import shewhart_plot as sh_plot
from src.plots import pca_shewhart_plot as pca_sh_plot
from src.plots import hotelling_plot as hot_plot


alpha = 0.005
p = 2

data = initials.get_inits()
n = data['n']
m = data['m']
mean = data['mean']
sigma = data['sigma']
rho = data['rho']
x = data['x']
points = data['points']

x1 = x[:, 0]
x2 = x[:, 1]

cov = sigma_covarience_matrix(sigma, rho)
print(f'cov = {cov}')

plot.Plot.plot_factors(points, x1, x2, mean)
plot.Plot.plot_scatter(x1, x2, mean)

## shewhart
sl1, sl2 = sh.ShewhartMethods.get_limits(mean, sigma, n)
print(f'sl1 = {sl1}\nsl2 = {sl2}')
sh_plot.ShewhartPlot.plot_2shewharts(points,
                                     x1, x2,
                                     sl1, sl2)

## pca
pca_data = pca.PCA_NUM.pca_eig_num(x - mean, cov)
pc = pca_data.pc
lam = pca_data.eig_values
eigenvectors = pca_data.coefs
fsl1, fsl2 = sh.ShewhartPCA.get_limits(lam, n)
pca_sh_plot.PCAShewhartPlot.plot_2pcashewharts(points,
                                               pc[:, 0], pc[:, 1],
                                               fsl1, fsl2)

## hotelling
print(f'x =\n{x}')
t2 = hot.Hotelling.t2_statistics(x - mean, cov, n)
print(f't2 =\n{t2}')
hot_ucl = hot.Hotelling.ucl(1 - alpha, p)
hot_plot.HotellingPlot.plot_hotelling(points, t2, hot_ucl)

## hotelling criterion
t2h = hot.Hotelling.criterion(x - mean, cov, n)
hot_plot.HotellingPlot.plot_hotelling_criterion(points, t2h, hot_ucl)
