def type_str():
    v = "abcd"
    print(v)  # abc
    print(type(v))  # <class 'str'>
    print(id(v))  # ex: 139716794520864
    print(v[2])  # c
    v[2] = "z"  # TypeError: 'str' object does not support item assignment

    v2 = "abcd"
    print(v == v2)  # True
    print(id(v) == id(v2))  # True

    v2 = "abcde"
    print(v == v2)  # False
    print(id(v) == id(v2))  # False


def main():
    print("-- str --")
    type_str()


if __name__ == "__main__":
    main()
