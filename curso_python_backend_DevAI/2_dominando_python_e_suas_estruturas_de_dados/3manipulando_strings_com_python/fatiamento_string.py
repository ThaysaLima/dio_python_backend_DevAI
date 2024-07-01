# Aula 03, fatiamento de strig. 
nome = "Thaysa Pereira dos Reis Lima"

print(nome[0]) # >>> T
print(nome[:7]) # >>> Thaysa, pois o 7 não é incluso (o 7 vai parar no espaço que tembém é contado como um caracter)
print(nome[7:]) # >>> Pereira dos Reis Lima, vai do caracter pedido até o final.
print(nome[7:15]) # >>> Pereira, isola os strings que vai do 7 ao 15
print(nome[7:24:2]) # >>> PriadsRi, ele basicmente fala "vai do caractere 7 ao 24 de 2 em 2"
print(nome[:]) # >>> Thaysa Pereira dos Reis Lima, mostra tudo
print(nome[::-1]) # >>> amiL sieR sod ariereP asyahT, deixa tudo ao contrário. 

print(nome[-1]) # >>> a, ele vai pegar a última letra.