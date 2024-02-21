from decimal import Decimal

# Numeric = Union[int, float, complex, Decimal]
Numeric = int | float | complex | Decimal


def soma(x: int, y: int) -> int:
    return x + y


def generic_soma(x: Numeric, y: Numeric) -> Numeric:
    return x + y


print("==>", soma(1, 2))  # 3
print("==>", generic_soma(1, 2))  # 3
print("==>", generic_soma(1.0, 2))  # 3.0
print("==>", generic_soma(1.0, 2.0))  # 3.0
print("==>", generic_soma(1 + 2j, 2 + 1j))  # 3+3j
print("==>", generic_soma(Decimal("1"), Decimal("2")))  # 3.0
