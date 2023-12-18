"""
Please check Brandon Rozek post about this code
https://brandonrozek.com/blog/tcopython/

Python Decorator that enables tail call
optimization through Exception Trampolines.
"""
import functools
import inspect
from dataclasses import dataclass, field
from typing import Any


@dataclass
class TailRecurseException(Exception):
    """Exception to enable tail call recursion."""

    args: list[Any] = field(default_factory=list)
    kwargs: dict[Any, Any] = field(default_factory=dict)


def tail_call(func):
    """
    Decorator that performs tail call optimization.

    Notes
    =====
    Works by throwing an exception to exit the stack
    when the function sees itself as its grandparent in
    the stack trace. It then calls itself with its new
    arguments.
    """

    @functools.wraps(func)
    def recurse(*args, **kwargs):
        frame = inspect.currentframe()
        if frame.f_back is not None and frame.f_back.f_back is not None and frame.f_back.f_back.f_code == frame.f_code:
            raise TailRecurseException(args, kwargs)
        while True:
            try:
                return func(*args, **kwargs)
            except TailRecurseException as exception:
                args = exception.args
                kwargs = exception.kwargs

    return recurse
