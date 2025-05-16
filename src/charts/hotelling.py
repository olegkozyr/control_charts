# hotelling control charts
# https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc341.htm
import numpy as np
from scipy.stats import chi2

from src.stats.covariance import covariance_matrix, sigma_covarience_matrix
from src.test import initials


class Hotelling:
    @staticmethod
    def t2_statistics(x, cov, n):
        t2 = np.zeros(x.shape[0])
        cov_inv = np.linalg.inv(cov)
        for i in range(t2.shape[0]):
            t2[i] = n * (x[i, :] @ cov_inv @ x[i, :])

        return t2

    @staticmethod
    def ucl(alpha, p):
         return chi2.ppf(alpha, p)

    @staticmethod
    def _t2h(x, cov, c, n):
        t2h = n * (c @ (x.reshape(-1, 1))**2) / \
              (c @ cov @ c.T)

        return t2h[0, 0]

    @staticmethod
    def criterion(x, cov, n):
        c1 = np.zeros((1, 2))
        c2 = c1.copy()
        c1[0, 0] = 1
        c2[0, 1] = 1

        m = x.shape[0]

        t2h = np.zeros((m, 2))
        for i in range(m):
            t2h1 = Hotelling._t2h(x[i], cov, c1, n)
            t2h2 = Hotelling._t2h(x[i], cov, c2, n)
            t2h[i] = np.array([t2h1, t2h2])

        return t2h


if __name__ == '__main__':
    alpha = 0.005
    p = 2
    ucl = Hotelling.ucl(1-alpha, p)
    print(f'ucl = {ucl}')

    #=======================================
    # test private criterion
    #=======================================
    print('first example')
    n1 = 1
    x1 = np.array([14, 12, 16, 14, 15, 18, 22, 20, 19, 9], dtype=float)
    x2 = np.array([19, 15, 19, 17, 24, 12, 10, 15, 18, 20], dtype=float)
    a1 = np.array([x1.mean(), x2.mean()])
    print(f'a1 = {a1}')

    y1 = np.vstack([x1, x2]).T

    s1 = covariance_matrix(y1)
    print(f's1 = {s1}')
    print(f'det = {np.linalg.det(s1)}')

    t2h1 = Hotelling.criterion(y1 - a1, s1, n1)
    print(f't2h1 =\n{np.round(t2h1, 0)}')

    #=======================================
    print('second example')
    data = initials.get_inits()
    n2 = data['n']
    a2 = data['mean']
    sigma = data['sigma']
    rho = data['rho']
    y2 = data['x']
    print(f'y2 =\n{y2}')
    s2 = sigma_covarience_matrix(sigma, rho)
    print(f's2 = {s2}')

    t2h2 = Hotelling.criterion(y2 - a2, s2, n2)
    print(f't2h2 =\n{np.round(t2h2, 2)}')

