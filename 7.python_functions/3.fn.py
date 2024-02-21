def soma_positional_or_keyword(x, y):
    return x + y


def soma_positional_only(x, y, /):
    return x + y


def soma_keyword_only(*, x, y):
    return x + y


def mixture_of_positional_only_and_keyword_only(x, /, *, y):
    return x + y


print("- Positional or Keyword arguments")
print("==>", soma_positional_or_keyword(1, 2))  # 3
print("==>", soma_positional_or_keyword(x=1, y=2))  # 3

print()
print("- Positional-only arguments")
print("==>", soma_positional_only(1, 2))  # 3
try:
    # TypeError: soma_positional_args() got some positional-only arguments passed as keyword arguments: 'x', 'y'
    print("==>", soma_positional_only(x=1, y=2))
except TypeError as e:
    print("==>", e)


print()
print("- Keyword-only arguments")
print("==>", soma_keyword_only(x=1, y=2))  # 3
try:
    # TypeError: soma_keyword_only() takes 0 positional arguments but 2 were given
    print("==>", soma_keyword_only(1, 2))
except TypeError as e:
    print("==>", e)

print()
print("- Mixture of positional-only and keyword-only arguments")
print("==>", mixture_of_positional_only_and_keyword_only(1, y=2))  # 3
