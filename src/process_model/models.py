import numpy as np


_seed = 1234


def multivatiate_random_process(mean, cov, n, m, seed=_seed):
    x = (np.random.default_rng(seed)
         .multivariate_normal(mean,
                              cov,
                              (n, m))
         .mean(axis=0))

    return x


def random_process(mean, sigma, n, m, seed=_seed):
    x = (np.random.default_rng(seed)
         .normal(mean, sigma, (n, m))
         .mean(axis=0))

    return x


if __name__ == '__main__':
    n = 5
    m = 10
    mean = 4.5
    sigma = 1.0

    x = random_process(mean, sigma, n, m)
    print(f'x = {x.shape}')

