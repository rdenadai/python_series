def type_byte():
    v = b"abcd"
    print(v)  # b'abcd'
    print(type(v))  # <class 'bytes'>
    print(id(v))  # ex: 139716794520864
    print(v[2])  # 99

    v2 = b"abcd"
    print(v == v2)  # True
    print(id(v) == id(v2))  # True

    v2 = b"abcde"
    print(v == v2)  # False
    print(id(v) == id(v2))  # False


def main():
    print("-- byte --")
    type_byte()


if __name__ == "__main__":
    main()
