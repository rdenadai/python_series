def soma(x, y):
    return x + y


# Observe o uso de * e ** para desempacotar os argumentos

num = [1, 2]
# soma(num[0], num[1])
print("==>", soma(*num))  # 3


num = {"x": 1, "y": 2}
print("==>", soma(**num))  # 3


def distribute(word):
    return list(word)


print("==>", distribute("word"))  # ['w', 'o', 'r', 'd']

w, o, r, d = distribute("word")
print("==>", w, o, r, d)  # w o r d

w, o, *resto = distribute("word")
print("==>", w, o, resto)  # w o ['r', 'd']
