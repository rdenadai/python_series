from dataclasses import dataclass
from functools import reduce
from operator import add

# lambda argumentos: expressão
add_ = lambda x, y: x + y  # noqa: E731


print(add_(2, 3))
print(add(2, 3))


@dataclass
class Product:
    name: str
    category: str
    price: float


shopping_cart = [
    Product("Coca-Cola", "Bebida", 12.31),
    Product("Coca-Cola", "Bebida", 12.31),
    Product("Coca-Cola", "Bebida", 12.31),
    Product("Cerveja", "Bebida", 56.68),
    Product("Cerveja", "Bebida", 56.68),
    Product("Picanha", "Carne", 99.90),
    Product("Picanha", "Carne", 99.90),
    Product("Pão de alho", "Pão", 14.90),
]


beverages = filter(lambda x: x.category == "Bebida", shopping_cart)
total = reduce(lambda x, y: x + y.price, beverages, 0.0)
print(total)  # 150.29

# fmt: off
total = reduce(
    lambda x, y: x + y.price,
    filter(
        lambda x: x.category == "Bebida",
        shopping_cart
    ),
    0.0
)
# fmt: on
print(total)  # 150.29
