from itertools import chain
from random import uniform

from knn import KNN
from mplot import plot_one_dim_values, plot_values
from sklearn.datasets import make_classification

SEED = 42


def create_dataset(num_samples: int = 125, n_features: int = 1) -> tuple[list[float], list[int]]:
    X, y = make_classification(
        n_samples=num_samples,
        n_features=n_features,
        n_classes=2,
        n_redundant=0,
        n_informative=1,
        n_clusters_per_class=n_features,
        random_state=SEED,
    )
    return list(chain(*X.tolist())), y.tolist()


def main() -> None:
    X, y = create_dataset()
    knn = KNN(X, y)

    plot_values(X, y)

    pX = [round(uniform(-2, 2), 2) for _ in range(15)]
    preds = knn.predict(pX, idw=False)

    py = []
    for x, pred in zip(pX, preds):
        p, n = pred
        print(x, p, "<==>", [(round(k, 5), j) for k, j in n])
        py.append(p)

    plot_values(X, y, pX, py)
    plot_one_dim_values(X, y, pX, py)


if __name__ == "__main__":
    main()
