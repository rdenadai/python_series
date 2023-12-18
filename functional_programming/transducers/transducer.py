from typing import Callable, Iterable

from reduce import _reduce


def _map(fnc: Callable) -> Callable:
    return lambda transformer: lambda acc, cur: transformer(acc, fnc(cur))


def _filter(predicate: Callable) -> Callable:
    return lambda transformer: lambda acc, cur: transformer(acc, cur) if predicate(cur) else acc


def _sum(fnc: Callable) -> Callable:
    return lambda transformer: lambda acc, cur: transformer(acc, fnc(acc, cur))


def compose(*fncs: Iterable[Callable]) -> Callable:
    return lambda initializer=None: _reduce(lambda acc, cur: cur(acc), reversed(fncs), initializer)


def transducer(composable: Callable) -> Callable:
    def append(acc, val):
        if isinstance(acc, Iterable):
            acc.append(val)
        else:
            acc = val
        return acc

    return composable(append)


def main():
    T = transducer(
        compose(
            _filter(lambda x: x % 2 == 0),
            _map(lambda x: x + 1),
            _sum(lambda x, y: x + y),
        )
    )

    assert _reduce(T, [1, 2, 3, 4, 5, 6], 0) == 15


if __name__ == "__main__":
    main()
