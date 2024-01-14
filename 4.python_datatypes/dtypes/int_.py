def type_int():
    v = 1

    print(v)  # 1
    print(type(v))  # <class 'int'>
    print(id(v))  # ex: 139716794520864
    print(v.to_bytes(1, "big"))  # b'\x01'
    print(12_000_000, 12000000)


def main():
    print("-- int --")
    type_int()


if __name__ == "__main__":
    main()
