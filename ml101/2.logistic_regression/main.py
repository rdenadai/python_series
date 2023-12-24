from random import seed

import matplotlib
import numpy as np
from logit import logistic_regression, sigmoid
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import RocCurveDisplay, accuracy_score
from sklearn.model_selection import train_test_split

matplotlib.use("TkAgg")

SEED = 42

seed(SEED)


def plot_values(X, y):
    plt.title("Sigmoid Function")
    plt.scatter(X, y)

    x = linspace(min(X), max(X), len(X) - 1)  # Ajuste os limites aqui para alterar o intervalo do eixo x
    y = [sigmoid(x_) for x_ in x]

    plt.plot(x, y, color="red")
    plt.show()


def plot_roc_curve(y_test, y_pred):
    RocCurveDisplay.from_predictions(y_test, y_pred)
    plt.show()


def create_dataset(num_samples: int = 100) -> tuple:
    """
    Creates a synthetic dataset
    """
    X, y = [], []
    space = linspace(-5, 5, num_samples)
    mean = sum(space) / len(space)
    for k in space:
        X.append(k)
        y.append(1 if k >= mean // 2 else 0)
    return X, y


def linspace(start, stop, num):
    step = (stop - start) / (num - 1)
    return [start + step * i for i in range(num)]


def main() -> None:
    X, y = create_dataset()
    plot_values(X, y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=SEED)

    weight, bias = logistic_regression((X_train, y_train))
    acc, y_pred = 0.0, []
    for Xt, yt in zip(X_test, y_test):
        y_hat = sigmoid(weight * Xt + bias)
        y_pred.append(y_hat)
        acc += 1 if yt == (1 if y_hat >= 0.5 else 0) else 0
    acc /= len(X_test)
    print(f"Accuracy: {acc:.2f}")

    plot_roc_curve(y_test, y_pred)

    X_train = np.array(X_train)
    X_train = X_train.reshape(-1, 1)
    X_test = np.array(X_test)
    X_test = X_test.reshape(-1, 1)

    reg = LogisticRegression().fit(X_train, y_train)
    y_pred = reg.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {acc:.2f}")


if __name__ == "__main__":
    main()
