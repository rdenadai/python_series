"""
Docstrings
"""


def soma(x: int, y: int) -> int:
    """_summary_

    Args:
        x (int): _description_
        y (int): _description_

    Returns:
        int: _description_
    """
    return x + y


soma(1, 2)  # 3
print("===>", soma.__name__)  # 'soma'
print("===>", soma.__doc__)  # _summary_ ...
print("===>", soma.__annotations__)  # {'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}
