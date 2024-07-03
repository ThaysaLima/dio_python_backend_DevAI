# Continuação Aula 1

#calcule o total de uma lista de números: 

def calcule_total(numeros):
    total_soma = sum(numeros)
    return total_soma

print(calcule_total([12,34,5,6,77,6,4,67])) # 211

# calcule o antecessor e o sucessor do número

numero_pedido = float(input("Diga o número que deseja: ")) # perguntei qual o número

def calcule_antecessor_sucessor(num):
    antecessor = (f"Esse é o antecessor {num-1}") 
    sucessor = (f"Esse é o sucessor {num +1}")
    return antecessor, sucessor

print(calcule_antecessor_sucessor(numero_pedido))

# se não espercificarmos o return, por padrão ele vai me dar um None

def ex1():
    print("olá, mundo!")

print(ex1()) # Olá, mundo! 
             # None