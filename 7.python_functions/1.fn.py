# A função mais simples que podemos fazer é uma que não recebe nenhum argumento e não retorna nada
def void():
    pass


# Função que recebe argumentos e retorna um valor
def soma(x, y):
    return x + y


# ----------------------------------------------

s = soma
print("==>", s)  # <function soma at 0x7f8e3e3e3d08>
print("==>", type(s))  # <class 'function'>
