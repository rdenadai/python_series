from typing import Optional

import matplotlib
from matplotlib import pyplot as plt

matplotlib.use("TkAgg")


def condense_points(
    X: list[tuple[float, float]],
    y: list[int],
) -> tuple:
    x1, y1, x2, y2, x3, y3 = [], [], [], [], [], []
    for i, point in enumerate(X):
        if y[i] == 0:
            x1.append(point[0])
            y1.append(point[1])
        elif y[i] == 1:
            x2.append(point[0])
            y2.append(point[1])
        elif y[i] == 2:
            x3.append(point[0])
            y3.append(point[1])
    return x1, y1, x2, y2, x3, y3


def plot_values(
    X: list[tuple[float, float]],
    y: list[int],
    pX: Optional[list[tuple[float, float]]] = None,
    py: Optional[list[int]] = None,
) -> None:
    plt.title("Data Points")

    x1, y1, x2, y2, x3, y3 = condense_points(X, y)
    plt.scatter(x1, y1, color="blue")
    plt.scatter(x2, y2, color="green")
    plt.scatter(x3, y3, color="red")
    if pX and py:
        x1, y1, x2, y2, x3, y3 = condense_points(pX, py)
        plt.scatter(x1, y1, color="cyan")
        plt.scatter(x2, y2, color="lime")
        plt.scatter(x3, y3, color="orange")
    plt.show()
