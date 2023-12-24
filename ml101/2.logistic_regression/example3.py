from random import seed

import numpy as np
from logit import logistic_regression, plot_roc_curve, plt_confusion_matrix, sigmoid
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

SEED = 42

seed(SEED)


def plot_values(X, y):
    import matplotlib
    from matplotlib import pyplot as plt

    matplotlib.use("TkAgg")

    plt.title("Sigmoid Function")
    plt.scatter(X, y)

    x = np.linspace(min(X), max(X), len(X) - 1)  # Ajuste os limites aqui para alterar o intervalo do eixo x
    y = [sigmoid(x_) for x_ in x]

    plt.plot(x, y, color="red")
    plt.show()


def create_dataset(num_samples: int = 1000, n_features=1) -> tuple:
    X, y = make_classification(
        n_samples=num_samples,
        n_features=n_features,
        n_classes=2,
        n_redundant=0,
        n_informative=1,
        n_clusters_per_class=n_features,
        random_state=SEED,
    )
    return X, y


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
    plt_confusion_matrix(y_test, [(1 if y_hat >= 0.5 else 0) for y_hat in y_pred])

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
