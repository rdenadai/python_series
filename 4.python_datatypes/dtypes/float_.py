def type_float():
    v = 1.0
    print(v)  # 1.0
    print(type(v))  # <class 'float'>
    print(id(v))  # ex: 139716794520864
    print(v.__ceil__())  # 1
    print(1e-3)  # 0.001
    print(1e3)  # 1000.0


def main():
    print("-- float --")
    type_float()


if __name__ == "__main__":
    main()
