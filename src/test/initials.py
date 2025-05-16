import numpy as np


def get_x():
    x1 = np.array([2.05, 1.87, 2.36, 1.99, 2.11, 2.35, 2.16, 1.75, 2.36, 2.32])
    x2 = np.array(
        [12.28, 11.37, 10.82, 11.13, 12.23, 13.29, 12.06, 12.75, 13.25, 13.11])
    return np.vstack([x1, x2]).transpose()


def get_inits():
    data = {'n': 5, 'm': 10, 'mean': np.array([2., 12.]),
            'sigma': np.array([0.35, 1.]), 'rho': 0.5}
    data['points'] = np.arange(data['m'])
    data['x'] = get_x()

    return data
