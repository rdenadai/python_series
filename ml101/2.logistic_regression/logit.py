from math import exp, log, sqrt
from random import random

import matplotlib
from matplotlib import pyplot as plt
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    RocCurveDisplay,
    confusion_matrix,
    roc_curve,
)


def plot_roc_curve(y_test, y_pred):
    matplotlib.use("TkAgg")

    fpr, tpr, _ = roc_curve(y_test, y_pred)
    RocCurveDisplay(fpr=fpr, tpr=tpr).plot(label="ROC Curve")
    plt.show()


def plt_confusion_matrix(y_test, y_pred):
    matplotlib.use("TkAgg")

    cm = confusion_matrix(y_test, y_pred)
    ConfusionMatrixDisplay(cm).plot()
    plt.show()


def sigmoid(x: float) -> float:
    return 1 / (1 + exp(-x))


def cross_entropy(y: float, y_hat: float) -> float:
    return -((y * log(y_hat)) + ((1 - y) * log(1 - y_hat)))


def logistic_regression(
    data: tuple,
    learning_rate: float = 1e-3,
    epochs: int = 1_000,
) -> tuple:
    weight, bias = random() * sqrt(2.0 / (2 - 1)), 1.0
    last_cost = 0.0
    for epoch in range(epochs + 1):
        cost = 0.0
        for X, y in zip(*data):
            y_hat = sigmoid(weight * X + bias)
            error = y_hat - y
            gradient = X * error
            weight -= learning_rate * gradient
            bias -= learning_rate * error
            cost += cross_entropy(y, y_hat)
        cost /= len(data[0])
        if epoch % 100 == 0:
            print(f"Epoch: {epoch} Cost: {cost:.3f}")
            if round(last_cost, 3) == round(cost, 3):
                break
            last_cost = cost
    return weight, bias
