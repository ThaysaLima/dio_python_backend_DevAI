# Aula 03
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto: 
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else: 
    print() #Podemos usar também o else(), para caso a lógica der erro, não ficar ali solta. 




