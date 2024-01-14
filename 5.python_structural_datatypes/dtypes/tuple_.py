def type_tuple():
    t = (1, 2, 3, 4, 5)
    print(t)  # (1, 2, 3, 4, 5)
    print(type(t))  # <class 'tuple'>
    print(t[0])  # 1
    print(t[:3])  # (1, 2, 3)
    print(t[-1])  # 5

    try:
        t[0] = 10  # TypeError: 'tuple' object does not support item assignment
    except TypeError as e:
        print(f"TypeError: {e}")

    t = ([1, 2], [3, 4])
    t[0].append(3)
    print(t)  # ([1, 2, 3], [3, 4])

    # Generator Expression
    t = (i for i in range(10))
    print(t)  # <generator object type_tuple.<locals>.<genexpr> at 0x7f9b1c0b4f20>
    print(type(t))  # <class 'generator'>

    t = tuple(i for i in range(10))
    print(t)  # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    print(type(t))  # <class 'tuple'>


def main():
    print("-- Tuple --")
    type_tuple()


if __name__ == "__main__":
    main()
