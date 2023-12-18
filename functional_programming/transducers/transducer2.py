from typing import Callable, Iterable

from reduce import _reduce


def _map(fnc: Callable) -> Callable:
    def _map_inner(transformer):
        def _map_inner_inner(acc, cur):
            print("map:", cur)
            return transformer(acc, fnc(cur))

        return _map_inner_inner

    return _map_inner


def _filter(predicate: Callable) -> Callable:
    def _filter_inner(transformer):
        def _filter_inner_inner(acc, cur):
            print("filter:", cur)
            return transformer(acc, cur) if predicate(cur) else acc

        return _filter_inner_inner

    return _filter_inner


def _sum(fnc: Callable) -> Callable:
    def _sum_inner(transformer):
        def _sum_inner_inner(acc, cur):
            print("sum:", cur)
            return transformer(acc, fnc(acc, cur))

        return _sum_inner_inner

    return _sum_inner


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

    assert _reduce(T, iter([1, 2, 3, 4, 5, 6]), 0) == 15


if __name__ == "__main__":
    main()
