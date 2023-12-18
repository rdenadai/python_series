from typing import Any, Callable, Iterator, Sequence

from tco import tail_call

# from sys import setrecursionlimit
# setrecursionlimit(5_000)


@tail_call
def _recursive(fnc, initializer, iterator):
    try:
        initializer = fnc(initializer, next(iterator))
        return _recursive(fnc, initializer, iterator)
    except StopIteration:
        return initializer


def _reduce(fnc: Callable, items: Iterator | Sequence, initializer: Any = None) -> Any:
    if not items:
        raise TypeError("reduce() of empty sequence with no initial value")

    items = iter(items)
    if initializer is None:
        initializer = next(items)
    return _recursive(fnc, initializer, items)


def main() -> None:
    # Without decorator tail_call or setting setrecursionlimit
    # 1000 calls => RecursionError: maximum recursion depth exceeded
    assert _reduce(lambda acc, cur: acc + cur, range(10_000), 0) == sum(range(10_000))


if __name__ == "__main__":
    main()
