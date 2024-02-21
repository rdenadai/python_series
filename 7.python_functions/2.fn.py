"""
Funções usando *args e **kwargs
"""


# Função que recebe N argumentos usando *args (positional arguments)
def sum_args(*args):
    total = 0
    for arg in args:
        total += arg
    return total


# Função que recebe N argumentos usando **kwargs (keyword arguments)
def sum_kwargs(**kwargs):
    total = 0
    for value in kwargs.values():
        total += value
    return total


def sum_args_kwargs(*args, **kwargs):
    total = 0
    for arg in args:
        total += arg
    for value in kwargs.values():
        total += value
    return total


print("==>", sum_args(1, 2, 3, 4, 5))  # 15


print("==>", sum_kwargs(a=1, b=2, c=3, d=4, e=5))  # 15


print("==>", sum_args_kwargs(1, 2, 3, 4, 5, a=1, b=2, c=3, d=4, e=5))  # 30
