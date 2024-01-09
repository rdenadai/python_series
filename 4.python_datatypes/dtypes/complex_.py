def type_complex():
    v = 1 + 2j
    print(v)  # (1+2j)
    print(v.conjugate())  # (1-2j)
    print(type(v))  # <class 'complex'>
    print(id(v))  # ex: 139716794520864
    print(v.real)  # 1.0
    print(v.imag)  # 2.0
    print(v + 1.5)  # (2.5+2j)
    print(v + 2)  # (3+2j)


def main():
    print("-- complex --")
    type_complex()


if __name__ == "__main__":
    main()
