#Aula 3.3, break
#Ideia, vamos fazer um sistema onde pediremos ao usuário colocar um número, para esse sistema começar a rodar ele deve ser diferente de zero, se for um número ímpar irá exibir um número, se for um número par ira exibir um outro número. Se o número for 10, irá interroper o sistema. 

# while True: 
#     numero = int(input("Coloque um número: "))

#     if numero == 10: 
#         break

#     print(numero)

#outro exemplo

for numero in range(100):
    if numero == 45:
        break
    print(numero, end=" ")

#continue, serve para pular uma condição
#aqui no caso, vai pular o 45...

for numero in range(100):
    if numero == 45:
        continue

    print(numero, end=" ")