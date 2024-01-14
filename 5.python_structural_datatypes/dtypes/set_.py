def type_set():
    s = {1, 2, 3, 4, 5}
    print(s)  # {1, 2, 3, 4, 5}
    print(type(s))  # <class 'set'>

    try:
        print(s[0])  # TypeError: 'set' object is not subscriptable
    except TypeError as e:
        print(f"TypeError: {e}")

    s.add(6)
    print(s)  # {1, 2, 3, 4, 5, 6}

    s.add(1)
    print(s)  # {1, 2, 3, 4, 5, 6}

    # Set Comprehension
    s = {i for i in range(10)}
    print(s)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

    s1 = {i for i in range(10)}
    s2 = {i for i in range(5, 15)}
    print(s1)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    print(s2)  # {5, 6, 7, 8, 9, 10, 11, 12, 13, 14}

    # Union
    print(s1 | s2)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...}
    print(s1.union(s2))  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...}
    # Intersection
    print(s1 & s2)  # {8, 9, 5, 6, 7}
    print(s1.intersection(s2))  # {8, 9, 5, 6, 7}
    # Difference
    print(s1 - s2)  # {0, 1, 2, 3, 4}
    print(s1.difference(s2))  # {0, 1, 2, 3, 4}
    print(s2 - s1)  # {10, 11, 12, 13, 14}


def main():
    print("-- Set --")
    type_set()


if __name__ == "__main__":
    main()
