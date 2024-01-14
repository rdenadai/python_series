def type_dict():
    d = {"a": 1, "b": 2, "c": 3}
    print(d)  # {'a': 1, 'b': 2, 'c': 3}
    print(type(d))  # <class 'dict'>
    print(d["a"])  # 1
    print(d.get("a", None))  # 1
    print(d.get("d", None))  # None
    print(d.keys())  # dict_keys(['a', 'b', 'c'])
    print(d.values())  # dict_values([1, 2, 3])
    print(d.items())  # dict_items([('a', 1), ('b', 2), ('c', 3)])

    l1 = ["a", "b", "c"]
    l2 = [1, 2, 3]
    d = dict(zip(l1, l2))
    print(d)  # {'a': 1, 'b': 2, 'c': 3}

    d["d"] = 4
    print(d)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    # Dictionary Comprehension
    d = {i: i for i in range(10)}
    print(d)  # {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, ...}


def main():
    print("-- Dict --")
    type_dict()


if __name__ == "__main__":
    main()
