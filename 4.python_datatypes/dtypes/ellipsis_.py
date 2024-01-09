def type_ellipsis():
    v = ...
    print(v)  # Ellipsis
    print(type(v))  # <class 'ellipsis'>
    print(id(v))  # ex: 139716794520864

    v2 = ...
    print(v == v2)  # True
    print(id(v) == id(v2))  # True


def main():
    print("-- Ellipsis --")
    type_ellipsis()


if __name__ == "__main__":
    main()
