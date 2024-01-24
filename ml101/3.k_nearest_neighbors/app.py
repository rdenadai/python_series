from random import uniform

from knn import KNN
from mplot import plot_values
from sklearn.datasets import make_classification

SEED = 42


def create_dataset(num_samples: int = 150, n_features: int = 2) -> tuple[list[tuple[float, float]], list[int]]:
    X, y = make_classification(
        n_samples=num_samples,
        n_features=n_features,
        n_classes=3,
        n_redundant=0,
        n_informative=n_features,
        n_clusters_per_class=1,
        random_state=SEED,
    )
    return list(X.tolist()), y.tolist()


def main() -> None:
    X, y = create_dataset()
    knn = KNN(X, y)

    plot_values(X, y)

    pX = [(round(uniform(-2, 2), 2), round(uniform(-2, 2), 2)) for _ in range(25)]
    preds = knn.predict(pX, idw=False)

    py = []
    for x, pred in zip(pX, preds):
        p, n = pred
        print(x, p)
        py.append(p)

    plot_values(X, y, pX, py)


if __name__ == "__main__":
    main()
