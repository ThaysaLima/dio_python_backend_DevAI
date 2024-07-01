# Aula 01 

#ñ é preciso espeficicar o que há na lista, a partir do momento que ela está la dentro ele vira um objeto. Já que python é orientado a objeto. 

frutas = ["melância", "laranja", "maçã"]
print(frutas)

frutas2 = []
print(frutas2)

letras = list("Python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

# Acesso direto, vamos buscar algo específico da lista. 

# quando vamos buscar da esquerda para a direita, o índice começa por 0.
# quando vamos buscar da direita para a esquerda, o índice começa por -1. 
print(frutas[1]) # >>> Laranja
print(frutas[-3]) # >>> Melância

# Listas aninhadas, listas dentro de listas. 

matriz = [

    [1, "a", 2],
    ["b", 3, 4], 
    [5, 6, "c"]

] # Horizontal é linhas e vertical é coluna. 

print(matriz[0]) # >>> [1, "a", 2], vai dar acesso apenas a linha completa.
print(matriz[0][1]) # >>> "a", o primeiro [] é a linha e o segundo é a coluna. 
print(matriz[0][-1]) # >>> 2, também podemos usar os índices negativos. 
print(matriz[])