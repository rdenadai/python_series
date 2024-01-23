from collections import Counter, defaultdict
from math import pow, sqrt
from typing import Callable


def euclidian(x: float, y: float) -> float:
    return sqrt(pow(x - y, 2))


def manhattan(x: float, y: float) -> float:
    return abs(x - y)


def cosine_similarity(x: float, y: float) -> float:
    return (x * y) / (sqrt(x) * sqrt(y))


def cosine_distance(x: float, y: float) -> float:
    return 1 - cosine_similarity(x, y)


class KNN:
    """K Nearest Neighbors Classifier One Dimensional"""

    def __init__(self, X: list[float], y: list[int]) -> None:
        self.__X: list[float] = X
        self.__y: list[int] = y

    def __idw(self, d: float) -> float:
        return round(1.0 / (pow(d, 2) + 1e-24), 10)

    def predict(
        self,
        P=list[float],
        k: int = 7,
        distance: Callable = euclidian,
        idw=False,
    ) -> list:
        predictions = []
        for y_ in P:
            fn_idw = self.__idw if idw else lambda d: d

            distances = []
            for i, x_ in enumerate(self.__X):
                distances.append((i, distance(x_, y_)))
            distances = sorted(distances, key=lambda d: d[1])
            xs, *_ = zip(*distances[:k])

            if idw:
                weighted_distance: dict = defaultdict(float)
                for i, d in distances[:k]:
                    weighted_distance[self.__y[i]] += fn_idw(d)
                distances = sorted(weighted_distance.items(), key=lambda d: d[1])
                pred = distances[-1][0]
            else:
                pred = Counter([self.__y[x_] for x_ in xs]).most_common(1)[0][0]

            predictions.append((pred, [(self.__X[x_], self.__y[x_]) for x_ in xs]))
        return predictions
