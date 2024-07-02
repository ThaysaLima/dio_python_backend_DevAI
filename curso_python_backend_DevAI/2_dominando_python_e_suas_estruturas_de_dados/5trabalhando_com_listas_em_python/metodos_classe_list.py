# Aula 02

# append: vai adicionar algo na lista, de 1 em 1.

lista = []

lista.append(1)
lista.append("Thaysa Lima")
lista.append([20, 50, 67])

print(lista)

# clear: vai retirar tudo que há dentro da lista e transformar em uma lista vazia. 

lista2 = [1, 'Thaysa Lima', [20, 50, 67]] 
print(lista2)

lista2.clear()
print(lista2)


# copy, copiar um objeto mas com ids diferentes.

lista3 = [1, 'Thaysa Lima', [20, 50, 67]]
l3 = lista3.copy()

print(lista3)
print(id(l3), id(lista3)) #São objetos diferentes, o que eu faço em l3 não interfere em lista3. 

l3[0] = 2
print(l3) # >>> [2, 'Thaysa Lima', [20, 50, 67]]

# count



# extend



# index



# pop



# remove 



# reverse



# sort



# len 



# sorted 


