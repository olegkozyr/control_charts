import numpy as np


class CoefData:
    def __init__(self, coefs, eig_values, characteristic_matrises,
                 system_matrises, right_vectors, system_equation_roots):
        self.coefs = coefs
        self.eig_values = eig_values
        self.characteristic_matrises = characteristic_matrises
        self.system_matrises = system_matrises
        self.right_vectors = right_vectors
        self.system_equation_roots = system_equation_roots


class PCA_Data(CoefData):
    def __init__(self, pc, covar, *args):
        super().__init__(*args)
        self.pc = pc
        self.covar = covar

    @classmethod
    def from_coefs(cls, pc, covar, coefs):
        return cls(pc, covar, coefs.coefs, coefs.eig_values,
                   coefs.characteristic_matrises, coefs.system_matrises,
                   coefs.right_vectors, coefs.system_equation_roots)


class PCA_NUM:
    @staticmethod
    def eig_num(covar):
        # eigenvalues count
        p = covar.shape[1]
        # get eigenvalues by solving characteristic equation
        eig_values = np.sort(np.roots(np.poly(covar)))[::-1]

        # get eigenvectors
        coefs = []
        characteristic_matrises = []
        system_matrises = []
        right_vectors = []
        system_equation_roots = []
        for i in range(p):
            characteristic_matrix = covar - eig_values[i] * np.eye(p)
            characteristic_matrises.append(characteristic_matrix)
            # drop last equation
            m = np.delete(characteristic_matrix, -1, 0)
            system_matrix = np.delete(m, i, 1)
            system_matrises.append(system_matrix)
            vector = m[:, i]
            # move values to the left of the = sign in linear equation
            vector *= -1.
            right_vectors.append(vector)
            roots = np.linalg.solve(system_matrix, vector)
            roots = np.insert(roots, i, 1.)
            system_equation_roots.append(roots)
            coefs.append(roots / (roots @ roots)**0.5)

        return CoefData(
            np.vstack(coefs).transpose(), eig_values, characteristic_matrises,
            system_matrises, right_vectors, system_equation_roots)

    @staticmethod
    def pca_eig_num(x, covar):
        coefs = PCA_NUM.eig_num(covar)
        pc = x @ coefs.coefs

        return PCA_Data.from_coefs(pc, covar, coefs)


class PCA:
    @staticmethod
    def get_eig(covar):
        eig = np.linalg.eig(covar)

        eigenvalues = eig[0]
        inds = np.argsort(eigenvalues)[::-1]
        eigenvalues = eigenvalues[inds]

        eigenvectors = eig[1][:, inds]

        return eigenvalues, eigenvectors

    @staticmethod
    def get_pca_eig(x, cov, method=get_eig):
        eigenvalues, eigenvectors = method(cov)
        pc = x @ eigenvectors

        return pc, eigenvalues, eigenvectors
