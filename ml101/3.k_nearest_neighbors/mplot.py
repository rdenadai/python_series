from typing import Optional

import matplotlib
from matplotlib import pyplot as plt

matplotlib.use("TkAgg")


def plot_values(
    X: list[float],
    y: list[int],
    pX: Optional[list[float]] = None,
    py: Optional[list[int]] = None,
) -> None:
    plt.title("Data Points")
    plt.scatter(X, y)
    if pX and py:
        plt.scatter(pX, py, color="red")
    plt.show()


def plot_one_dim_values(
    X: list[float],
    y: list[int],
    pX: Optional[list[float]] = None,
    py: Optional[list[int]] = None,
) -> None:
    plt.title("Data Points")

    X1, X2 = [], []
    for i, y_ in enumerate(y):
        if y_ == 0:
            X1.append(X[i])
        else:
            X2.append(X[i])
    plt.scatter(X1, X1, color="blue")
    plt.scatter(X2, X2, color="green")

    if pX and py:
        X1, X2 = [], []
        for i, y_ in enumerate(py):
            if y_ == 0:
                X1.append(pX[i])
            else:
                X2.append(pX[i])
        plt.scatter(X1, X1, color="cyan")
        plt.scatter(X2, X2, color="lime")
    plt.show()
