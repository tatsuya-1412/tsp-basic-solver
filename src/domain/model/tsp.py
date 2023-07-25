import numpy as np
from amplify import (BinaryPoly, BinaryPolyArray, BinarySymbolGenerator,
                     sum_poly)


class Tsp:
    n_city: int
    d: np.ndarray
    model: BinaryPoly
    q : BinaryPolyArray

    def __init__(self, n_city: int, d: np.ndarray):
        self.n_city: int = n_city
        self.d: np.ndarray = d
        gen = BinarySymbolGenerator()
        self.q = gen.array(self.n_city, self.n_city)


    def create_model(self, alpha: int):
        q = self.q
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
            lambda n: (1-sum_poly(
                self.n_city,
                lambda i: q[n,i]
            ))**2,
        )
        col_constraints = sum_poly(
            self.n_city,
            lambda i: (1-sum_poly(
                self.n_city,
                lambda n: q[n,i])
            )**2,
        )
        constraints = row_constraints + col_constraints
        model = cost + alpha * constraints
        self.model = model

    def get_model(self):
        return self.model
    
    def get_route(self, values: dict):
        q_values = self.q.decode(values)
        route = np.where(np.array(q_values) == 1)[1]
        return route