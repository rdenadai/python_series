def type_list():
    l = [1, 2, 3, 4, 5]
    print(l)  # [1, 2, 3, 4, 5]
    print(type(l))  # <class 'list'>
    print(l[0])  # 1
    print(l[:3])  # [1, 2, 3]
    print(l[-1])  # 5
    print(l[-3:])  # [3, 4, 5]

    l.append(6)  # [1, 2, 3, 4, 5, 6]
    k = l.pop()  # [1, 2, 3, 4, 5]
    print(k)  # 6

    print(l.index(3))  # 2

    # List Comprehension
    l = [i for i in range(10)]
    print(l)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def main():
    print("-- List --")
    type_list()


if __name__ == "__main__":
    main()
