def type_bool():
    true = True
    false = False

    print(true, false)  # True False
    print(id(true))  # ex: 139716794520864
    print(id(false))  # ex: 139716794520416
    print(type(true))  # <class 'bool'>
    print(type(false))  # <class 'bool'>
    print(true.to_bytes())  # \b'\x01'
    print(false.to_bytes())  # \b'\x00'
    print(true == 1)  # True
    print(false == 0)  # True
    print(id(true) == id(True))  # True
    print(id(false) == id(False))  # True

    # Truthy and Falsy values
    print(false == bool(0))  # True
    print(true == bool("a"))  # True
    print(false == bool(""))  # True
    print(true == bool([0]))  # True
    print(false == bool([]))  # True
    print(true == bool({"a": 0}))  # True
    print(false == bool({}))  # True
    print(false == bool(None))  # True
    print(false is None)  # False
    print(false is False)  # True


def main():
    print("-- bool --")
    type_bool()


if __name__ == "__main__":
    main()
