from math import sqrt
from random import random, seed

import numpy as np
from sklearn.linear_model import LinearRegression

seed(42)


def plot_values(X, y, slop=1, intercep=1):
    import matplotlib
    from matplotlib import pyplot as plt

    matplotlib.use("TkAgg")
    plt.title(f"Linear Regression: {slop:.3f}x + {intercep:.3f}")
    plt.scatter(X, y)
    plt.plot(X, [slop * x + intercep for x in X], color="red")
    plt.show()


def create_dataset(num_samples: int = 100) -> tuple:
    """
    Creates a synthetic dataset
    """
    X = [2 * random() for _ in range(num_samples + 1)]  # Study hours (independent var)
    y = [3 * x_ + random() for x_ in X]  # Grades (dependent var)
    return X, y


def linear_regression_normal(data: tuple) -> tuple:
    """
    Linear regression using normal equation
    """
    X, y = data

    xm = sum(X) / len(X)
    ym = sum(y) / len(y)

    numerator = sum((x - xm) * (y - ym) for x, y in zip(X, y))  # X.T * y
    denominator = sum((x - xm) ** 2 for x in X)  # X.T * X
    slop = numerator / denominator  # (X.T * X)^-1 * X.T * y
    intercep = sum(y - slop * x for x, y in zip(X, y)) / len(X)  # b = y - mx
    return slop, intercep


def linear_regression_gd(data: tuple, learning_rate: float = 1e-3, epochs: int = 1_000) -> tuple:
    """
    Linear regression using gradient descent
    """
    slop, intercep = random() * sqrt(2.0 / (2 - 1)), 1
    for _ in range(epochs + 1):
        for X, y in zip(*data):
            y_hat = slop * X + intercep
            error = y_hat - y
            gradient = X * error
            slop -= learning_rate * gradient
            intercep -= learning_rate * error
    return slop, intercep


def main() -> None:
    X, y = create_dataset()
    slop, intercep = linear_regression_gd((X, y))
    # plot_values(X, y, slop, intercep)
    print(slop, intercep)
    slop, intercep = linear_regression_normal((X, y))
    # plot_values(X, y, slop, intercep)
    print(slop, intercep)

    X = np.array(X)
    X = X.reshape(-1, 1)
    reg = LinearRegression().fit(X, y)
    print(reg.coef_[0], reg.intercept_)


if __name__ == "__main__":
    main()
