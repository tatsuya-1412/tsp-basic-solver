import numpy as np
from amplify import BinaryPoly, BinarySymbolGenerator, sum_poly


class Tsp:
    n_city: int
    d: np.ndarray
    model: BinaryPoly

    def __init__(self, n_city: int):
        self.n_city: int = n_city
        self.d: np.ndarray = np.ones((n_city, n_city))

    def create_model(self, alpha: int):
        gen = BinarySymbolGenerator()
        q = gen.array(self.n_city, self.n_city)
        cost = sum_poly(
            self.n_city,
            lambda n: sum_poly(
                self.n_city,
                lambda i: sum_poly(
                    self.n_city,
                    lambda j: self.d[i,j]*q[n,i]*q[(n+1)%self.n_city,j]
                ),
            ),
        )
        row_constraints = sum_poly(
            self.n_city,
            lambda n: sum_poly(
                self.n_city,
                lambda i: (1-q[n,i])**2
            ),
        )
        col_constraints = sum_poly(
            self.n_city,
            lambda i: sum_poly(
                self.n_city,
                lambda n: (1-q[n,i])**2
            ),
        )
        constraints = row_constraints + col_constraints
        model = cost + alpha * constraints
        self.model = model

    def get_model(self):
        return self.model