from dataclasses import dataclass
from typing import Callable, TypeVar

T = TypeVar("T")


def Memory(state: T | None = None) -> tuple[Callable, ...]:
    memory: list[T] = []
    if state:
        memory.append(state)

    def add_mem_state(state: T) -> None:
        memory.append(state)

    def get_mem_state(state: T) -> T | None:
        try:
            idx: int = memory.index(state)
            return memory[idx]
        except IndexError:
            return None

    def get_all_state() -> list[T]:
        return memory

    return get_all_state, add_mem_state, get_mem_state


@dataclass
class Person:
    name: str
    age: int


persons = [Person("Rodolfo", 42), Person("Alice", 25)]

get_all_state, add_mem_state, get_mem_state = Memory()
for person in persons:
    add_mem_state(person)
print("==>", get_mem_state(persons[1]))
print("==>", get_all_state())
