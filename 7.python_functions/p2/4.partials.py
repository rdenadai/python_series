from functools import partial
from math import pow

Numeric = int | float


def multiple_power(power: int = 2, *nums: tuple[Numeric, ...]) -> tuple[Numeric, ...]:
    return tuple(pow(num, power) for num in nums)  # type: ignore


power_of_two = partial(multiple_power, 2)
power_of_three = partial(multiple_power, 3)
print(type(power_of_two))  # <class 'functools.partial'>

print("==> ", power_of_two(2, 3, 4))  # (4.0, 9.0, 16.0)
print("==> ", power_of_two(2.5, 6.7))  # (6.25, 44.89)
print("==> ", power_of_three(1, 2, 3, 4))  # (1.0, 8.0, 27.0, 64.0)
print("==> ", power_of_three(1.65, 2.5, 6))  # (4.492125, 15.625, 216.0)
