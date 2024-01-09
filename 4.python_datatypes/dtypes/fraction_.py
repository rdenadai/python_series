from fractions import Fraction


def type_fraction():
    v = Fraction(1, 3)
    print(v)  # 1/3
    print(v.__round__(2))  # 33/100
    print(v.__float__())  # 0.3333333333333333
    print(type(v))  # <class 'fractions.Fraction'>
    print(id(v))  # ex: 139716794520864

    v2 = 1 / 3
    print(round(v.__float__(), 2) == round(v2, 2))  # True
    print(round(v + 2.0, 2))  # 2.33
    print(v + 1)  # 4/3


def main():
    print("-- Fraction --")
    type_fraction()


if __name__ == "__main__":
    main()
