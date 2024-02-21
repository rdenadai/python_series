"""Funções Anônimas (Lambda)"""

from dataclasses import dataclass
from uuid import UUID, uuid4

# Funções lambda são funções anônimas curtas usadas para criar funções "temporárias".
# É desaconselhável usar funções lambda para criar funções complexas, pois elas podem ser difíceis de entender.
lambda x, y: x + y


@dataclass
class Product:
    id: UUID
    name: str
    category: str
    price: float


@dataclass
class ShoppingCart:
    items: list[Product]

    def total(self) -> float:
        return sum(map(lambda p: p.price, self.items))


cart = ShoppingCart(
    items=[
        Product(id=uuid4(), name="Shirt", category="clothes", price=20.0),
        Product(id=uuid4(), name="Shoes", category="clothes", price=50.0),
        Product(id=uuid4(), name="Hat", category="clothes", price=10.0),
    ]
)

print("==>", "Shopping total: ", cart.total())  # 80.0
