# Aula 02

# a.append(x): vai adicionar algo na lista, de 1 em 1.

lista = []

lista.append(1)
lista.append("Thaysa Lima")
lista.append([20, 50, 67])

print(lista)

# a.clear(): vai retirar tudo que há dentro da lista e transformar em uma lista vazia. 

lista2 = [1, 'Thaysa Lima', [20, 50, 67]] 
print(lista2)

lista2.clear()
print(lista2)


# a.copy(), copiar um objeto mas com ids diferentes.

lista3 = [1, 'Thaysa Lima', [20, 50, 67]]
l3 = lista3.copy()

print(lista3)
print(id(l3), id(lista3)) #São objetos diferentes, o que eu faço em l3 não interfere em lista3. 

l3[0] = 2
print(l3) # >>> [2, 'Thaysa Lima', [20, 50, 67]]

# a.count(x): irá contar quantas vezes o item aparece na lista. 

cores = ["Azul", "Verde", "Verde", "Vermelho", "Preto", "Vermelho", "Amarelo", "Azul"]

print(cores.count("Vermelho")) # >>> 2. O vermelho apareceu 2 vezes na mesma lista
print(cores.count("Preto")) # >>> 1

# a.extend(interável): junção de duas listas, se nessas duas listas tiverem itens iguais elas vão se repetir quanod juntarem. 

linguagens = ["python", "c", "js", "r"]

print(linguagens)

linguagens.extend(["java", "csharp", "c"])

print(linguagens) # >>> ['python', 'c', 'js', 'r', 'java', 'csharp', 'c']

# a.index(x[, start[,end]]): irá indicar qual a posição do item na lista. 

linguagens2 = ['python', 'c', 'js', 'r', 'java', 'csharp']

print(linguagens2.index("java")) #4
print(linguagens2.index("c")) #1

# a.pop([i]): remove o item na posição fornecida na lista e retorna. Se nada for especificado ele vai remover o último ítem da lista

linguagens3 = ["python", "js", "c", "java", "csharp"]
print(linguagens3.pop()) # >>> csharp, o último da lista. 
print(linguagens3.pop(2)) # >>> c, ele vai me retorna a posição 3. 
print(linguagens3) # >>> ['python', 'js', 'java'], vai me retornar o que restou na lista. 

# remove 



# reverse



# sort



# len 



# sorted 


