# Aula 1, parte 2. Continuação 2.2


def resultado(a,b, operacao):
    resultado = operacao(a,b)
    print(f"O resultado da operação é = {resultado}")

def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def teste(a,b):
    return 2*a ** 4*3

resultado(12, 13, teste)
