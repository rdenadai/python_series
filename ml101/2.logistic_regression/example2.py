from random import random, seed

import numpy as np
from logit import logistic_regression, sigmoid
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

SEED = 42

seed(SEED)


def create_dataset(num_samples: int = 100) -> tuple:
    """
    Creates a synthetic dataset
    """
    X, y = [], []
    for _ in range(num_samples + 1):
        grade = int(random() * 100)
        X.append(grade)
        y.append(1 if grade >= 50 else 0)
    return X, y


def linspace(start, stop, num):
    step = (stop - start) / (num - 1)
    return [start + step * i for i in range(num)]


def main() -> None:
    X, y = create_dataset(num_samples=500)
    X = [x / 100 for x in X]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=SEED)

    weight, bias = logistic_regression((X_train, y_train), learning_rate=0.1, epochs=200)
    acc = 0.0
    for Xt, yt in zip(X_test, y_test):
        y_hat = sigmoid(weight * Xt + bias)
        acc += 1 if yt == (1 if y_hat >= 0.5 else 0) else 0
    acc /= len(X_test)
    print(f"Accuracy: {acc:.2f}")

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
