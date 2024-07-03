# Aula 01

lista = {1,3,4,5,6,6,7,6,5,3,2}
print(set(lista)) # {1, 2, 3, 4, 5, 6, 7}

# pode ser com () ou com {}

exemplo = {"python", 2, 4, 5, "thaysa", 3, 5, 3}
print(set(exemplo)) # {'thaysa', 2, 3, 4, 5, 'python'}

# conjuntos não aceitam ser indexados, então para acessar ele temos que transformar numa lista. 

lista2 = {1,3,4,5,6,6,7,6,5,3,2}

lista_indexada = list(lista2)
print(lista_indexada) # >>> [1, 2, 3, 4, 5, 6, 7]

# podemos percorrer

carros = {"gol", "palio", "celta"}

for carro in carros: 
    print(carro)
