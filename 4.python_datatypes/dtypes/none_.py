def type_none():
    v = None
    print(v)  # None
    print(type(v))  # <class 'NoneType'>
    print(id(v))  # ex: 139716794520864

    v2 = None
    print(v == v2)  # True
    print(id(v) == id(v2))  # True


def main():
    print("-- None --")
    type_none()


if __name__ == "__main__":
    main()
