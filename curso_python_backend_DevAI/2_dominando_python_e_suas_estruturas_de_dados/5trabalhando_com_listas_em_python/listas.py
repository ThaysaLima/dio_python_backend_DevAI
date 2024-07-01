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

# Fatiamento, estrair conjuntos de valores de uma sequência. 
# start : stop [:step], onde o start e o step tem o número incluso e o stop não é incluso. 

lista = ["T", "h", "a", "y", "s", "a"]

print(lista[2:]) # >>> a, y, s, a. começa do 2 a seguir. 
print(lista[:2]) # >>> T, h. Vai do 0 até o 1.  
print(lista[1:3]) # >>> h, a. Vai do 1 até o 2
print(lista[0:3:2]) # >>> T, a. Vai do 0 até o 2 pulando de 2 em 2 
print(lista[::]) # >>> T, h, a, y, s, a. Vai me dar tudo
print(lista[::-1]) # >>> a, s, y, a, h, T. Vai me tar tudo invertido

# Iteração de listas, a forma mais comum é com o comando FOR.
carros = ["gol", "pálio", "celta", "SW4"]

for carro in carros:
    print(carro) # não irá retornar em lista/objeto

# Função enumarate
carros2 = ["gol", "pálio", "celta", "SW4"]

for indice,carro in enumerate(carros):
    print(f"{indice} : {carro}")

# Compreensão de listas

#V1
numeros = [1, 3, 56, 9, 34, 22, 67, 93]
pares = []

for numero in numeros:
    if numero %2 == 0: 
        pares.append(numero)

print(pares)

#V2
numeros2 = [1, 3, 56, 9, 34, 22, 67, 93, 2]
pares2 = [numero2 for numero2 in numeros2 if numero2 % 2 == 0]

print(pares2)

# Modificando valores

#V1
numeros3 = [1, 3, 56, 9, 34, 22, 67, 93]
quadrado = []

for numero3 in numeros3:
    quadrado.append(numero3 ** 2)

print(quadrado) # >>> [1, 9, 3136, 81, 1156, 484, 4489, 8649]

#V2
numeros4 = [1, 3, 56, 9, 34, 22, 67, 93]

quadrado2 = [numero4 ** 2 for numero4 in numeros4]
print(quadrado2)