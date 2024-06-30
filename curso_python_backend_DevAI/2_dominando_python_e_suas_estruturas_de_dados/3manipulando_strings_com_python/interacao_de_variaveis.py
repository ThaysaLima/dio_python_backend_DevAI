# Aula 02, Maneiras de interpolação. 

#1ª Maneira, old style
nome = "Thaysa Lima"
idade = 20
profissao = "Programadora"
cidade = "Fortaleza-CE"

print("Olá, eu sou a %s e tenho %d. Nasci na cidade de %s e atualmente atuo como %s" %(nome, idade, cidade, profissao)) # %s para valores em string, %d para valores em inteiro, %f para valores em flutuante. 

#2ª maneira, format. 

print("Olá, e chamo {} e tenho {}. Nasci na cidade de {} e atualmente atuo como {}".format(nome, idade, cidade, profissao))

#3ª maneira, f-string e a mais utilizada. 
print(f"Olá, meu nome é {nome}, tenho {idade} anos. Nasci na cidade de {cidade} e atualmente atuo como {profissao}")

#Há como formatar o f-string também. 

PI = 3.14159
print(f"O valor de PI: {PI:.2f}") #Esse .2f significa quantas casas decimais eles irão utilizar. >>> O valor de PI: 3.14

print(f"O valor de PI: {PI: 10.2f}") #Esse 10.2f significa que 10 será os espaços contados até a tring, e o 2f é as casas decimais. >>> O valor de PI:          3.14