from decimal import Context, Decimal, setcontext

setcontext(Context(prec=4))


def type_decimal():
    v = Decimal(1 / 3)
    print(v)  # 0.333333333333333314829616256247390992939472198486328125
    print(type(v))  # <class 'decimal.Decimal'>
    print(id(v))  # ex: 139716794520864

    v2 = Decimal("0.3333")
    print(v == v2)  # False

    v3 = Decimal(1 / 3)
    print(v == v3)  # True
    print(v + 2.0)  # TypeError: unsupported operand type(s) for +: 'decimal.Decimal' and 'float'


def main():
    print("-- Decimal --")
    type_decimal()


if __name__ == "__main__":
    main()
