# Aula 03
#Exemplo de utilizando interável
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto: 
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else: 
    print() #Podemos usar também o else(), para caso a lógica der erro, não ficar ali solta. 

#Exemplo utilizando a função build-in range
#RANGE, recebe 3 argumentos = range(start, stop [, step])
for numero in range(0, 11, 5): 
    print(numero, end=" ")


