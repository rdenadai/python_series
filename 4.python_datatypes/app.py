"""
Python data types

- basics
    - bool
    - int
    - float
    - str
    - complex
    - byte

- others
    - None
    - Ellipsis
    - Fraction
    - Decimal
    - class (your own type!)
"""


from dtypes.bool_ import type_bool
from dtypes.byte_ import type_byte
from dtypes.complex_ import type_complex
from dtypes.decimal_ import type_decimal
from dtypes.ellipsis_ import type_ellipsis
from dtypes.float_ import type_float
from dtypes.fraction_ import type_fraction
from dtypes.int_ import type_int
from dtypes.none_ import type_none
from dtypes.str_ import type_str


def main():
    print("-- bool --")
    type_bool()
    print("-- int --")
    type_int()
    print("-- float --")
    type_float()
    print("-- str --")
    type_str()
    print("-- complex --")
    type_complex()
    print("-- byte --")
    type_byte()
    print("-- None --")
    type_none()
    print("-- Ellipsis --")
    type_ellipsis()
    print("-- Fraction --")
    type_fraction()
    print("-- Decimal --")
    type_decimal()


if __name__ == "__main__":
    main()
