# Aula 01

# tuplas são muito parecidas com as listas, a diferença é que TUPLAS são IMUTÁVEIS e as LISTAS são MUTÁVEIS.

# as tuplas são colocadas em () e com , 

frutas = ("laranja", "maça", "mamão", "pêra",) # e no final de cada tupla sempre tem que ter uma vírgula sobrando. 

# do mesmo jeito das listas, elas também são acessadas por index 

print(frutas[0]) # >>> laranja
print(frutas[-1]) # >>> pêra

# tuplas aninhadas 

matriz = (
    # 0  1  2
    (1,"a",2), #0
    ("b",3,4), #1
    (5,6,"c"), #2

)

# e do mesmo modo que as listas acessamos ela pelas linhas e colunas. 

print(matriz[0]) # >>> (1,"a",2)
print(matriz[2][2]) # >>> c

# também há os métodos, mas são bem menos pois as tuplas não podem ser alteradas. 

nomes = ("thaysa", "nathan", "ana", "cauan",)

print(nomes.count("thaysa")) # count = para saber quantas vezes o item aparece na lista. 

print(nomes.index("ana")) # index = saber qual posição está o item. 

print(len(nomes)) # len = saber o tamanho da tuplas

 