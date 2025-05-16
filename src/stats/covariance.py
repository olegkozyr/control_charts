import numpy as np


def sigma_covarience_matrix(sigma, p):
    size = sigma.shape[0]

    sigma = sigma.reshape(-1, 1)
    cov = sigma * sigma.T

    rho_tri = np.zeros_like(cov)
    rho_tri[np.triu_indices(size, 1)] = p
    rho_tri += rho_tri.T + np.identity(size)

    cov *= rho_tri

    return cov


def covariance_matrix(x):
    m = x.shape[0]
    mean = x.mean()
    x -= mean
    s = (1. / (m - 1.)) * (x.T @ x)

    return s

