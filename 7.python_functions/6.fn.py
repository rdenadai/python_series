from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int


@dataclass
class Budget:
    value: float
    currency: str

    def __add__(self, other: "Budget") -> "Budget":
        if self.currency != other.currency:
            raise ValueError("Cannot sum budgets with different currencies")
        return Budget(value=self.value + other.value, currency=self.currency)

    def __radd__(self, other: "Budget") -> "Budget":
        if isinstance(other, int):
            return Budget(value=self.value + other, currency=self.currency)
        if self.currency != other.currency:
            raise ValueError("Cannot sum budgets with different currencies")
        return self.__add__(other)


def print_person(person: Person) -> None:
    print(f"{person.name} is {person.age} years old")


def print_budget_sum(*args) -> Budget:
    return sum(args)


print_person(Person(name="John", age=30))  # John is 30 years old

budgts = [
    Budget(value=100, currency="USD"),
    Budget(value=200, currency="USD"),
    Budget(value=1000, currency="USD"),
]

print("==>", print_budget_sum(*budgts))
