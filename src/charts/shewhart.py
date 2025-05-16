
class Limits:
    def __init__(self, ucl, cl, lcl):
        self.ucl = ucl
        self.cl = cl
        self.lcl = lcl

    def __repr__(self):
        return f'ucl: {self.ucl}\n' + f'cl: {self.cl}\n' + f'lcl: {self.lcl}'


class ShewhartMethods:
    @staticmethod
    def xcl(mu, sigma, n):
        k = 3. * sigma / n ** 0.5
        ucl = mu + k
        lcl = mu - k
        cl = mu

        return ucl, cl, lcl

    @staticmethod
    def shewhart_limits(mean, sigma, n):
        y_ucl, y_cl, y_lcl = \
            ShewhartMethods.xcl(mean, sigma, n)
        print(f'y1_ucl, y1_cl, y1_lcl = {y_ucl, y_cl, y_lcl}')

        return Limits(y_ucl, y_cl, y_lcl)


    @staticmethod
    def get_limits(mean, sigma, n):
        y1_ucl, y1_cl, y1_lcl = \
            ShewhartMethods.xcl(mean[0], sigma[0], n)
        y2_ucl, y2_cl, y2_lcl = \
            ShewhartMethods.xcl(mean[1], sigma[1], n)
        print(f'y1_ucl, y1_cl, y1_lcl = {y1_ucl, y1_cl, y1_lcl}')
        print(f'y2_ucl, y2_cl, y2_lcl = {y2_ucl, y2_cl, y2_lcl}')

        return Limits(y1_ucl, y1_cl, y1_lcl), \
            Limits(y2_ucl, y2_cl, y2_lcl)


class ShewhartPCA:
    @staticmethod
    def fcl(lam, n):
        ucl = 3. * (lam / n) ** 0.5
        lcl = -ucl
        cl = 0.

        return ucl, cl, lcl

    @staticmethod
    def get_limits(lam, n):
        f1_ucl, f1_cl, f1_lcl = ShewhartPCA.fcl(lam[0], n)
        f2_ucl, f2_cl, f2_lcl = ShewhartPCA.fcl(lam[1], n)
        print(f'f1_ucl, f1_cl, f1_lcl = {f1_ucl, f1_cl, f1_lcl}')
        print(f'f2_ucl, f2_c2, f2_lcl = {f2_ucl, f2_cl, f2_lcl}')

        return Limits(f1_ucl, f1_cl, f1_lcl), \
            Limits(f2_ucl, f2_cl, f2_lcl)
