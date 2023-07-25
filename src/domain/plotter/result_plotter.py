import matplotlib.pyplot as plt
import numpy as np


class ResultPlotter:
    route: list
    distances: np.ndarray
    points: np.ndarray

    def __init__(self, route: list, distances: np.ndarray, points: np.ndarray) -> None:
        self.route = route
        self.distances = distances
        self.points = points

    def show(self, is_saved=False, file_path="../results/img.pdf"):
        n_city = len(self.route)
        path_length = sum([self.distances[self.route[i], self.route[(i+1)%n_city]] for i in range(n_city)])
        x = [p[0] for p in self.points]
        y = [p[1] for p in self.points]

        plt.figure(figsize=(7,7))
        plt.title(f"path length: {path_length}")
        plt.xlabel("x")
        plt.ylabel("y")

        for i in range(n_city):
            r_p = self.route[i]
            r_n = self.route[(i+1)%n_city]
            plt.plot([x[r_p], x[r_n]], [y[r_p], y[r_n]], "b-")

        plt.plot(x, y, "ro")
        if is_saved:
            plt.savefig(file_path)
        else:
            plt.show()