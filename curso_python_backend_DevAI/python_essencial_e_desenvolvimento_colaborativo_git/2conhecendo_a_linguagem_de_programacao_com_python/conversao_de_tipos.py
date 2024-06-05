#Aula 4

#CONVERSÃO PARA TIPO NUMÉRICO PARA STR 
#Serve muito para formatação de texto 

idade = 20 
nome = "Thaysa"
texto = f"A idade de {idade} anos é da {nome}"
#Essa saída irá dar erro, pois a formatação só aceita strings, e na {idade} é um int. Então fazemos a conversão. 

idade = str(idade)
texto = f"A idade de {idade} anos é da {nome}"
print(texto)

#numa conversão do tipo float para int, ele sempre irá arredondar para baixo. 

numero_float = 10.45
numero_int = int(numero_float)
print(numero_int) #saída = 10