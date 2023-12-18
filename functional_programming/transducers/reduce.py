from typing import Any, Callable, Iterator, Sequence


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
    assert _reduce(lambda acc, cur: acc + cur, [1, 2, 3, 4, 5], 0) == 15
    assert _reduce(lambda acc, cur: f"{acc}+{cur}", [1, 2, 3, 4, 5], "") == "+1+2+3+4+5"
    assert _reduce(lambda acc, cur: [cur, *acc], [1, 2, 3, 4, 5], []) == [5, 4, 3, 2, 1]
    assert _reduce(lambda acc, cur: {**{cur: cur}, **acc}, [1, 2, 3, 4, 5], {}) == {5: 5, 4: 4, 3: 3, 2: 2, 1: 1}
    assert _reduce(lambda acc, cur: {*acc, cur}, [1, 2, 3, 4, 5], set()) == {1, 2, 3, 4, 5}


if __name__ == "__main__":
    main()
