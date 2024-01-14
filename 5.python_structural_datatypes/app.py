"""
Python data types

- list
- dict
- tuple
- set
- frozenset
- array
- bytearray
- memoryview
- namedtuple
- deque # stack
- Counter
- heapq # priority queue
- typing.NamedTuple
- typing.TypedDict

"""

from dtypes.dict_ import type_dict
from dtypes.list_ import type_list
from dtypes.set_ import type_set
from dtypes.tuple_ import type_tuple


def main():
    print("Python structure types")
    print("-- List --")
    type_list()
    print("-- Tuple --")
    type_tuple()
    print("-- Dict --")
    type_dict()
    print("-- Set --")
    type_set()


if __name__ == "__main__":
    main()
