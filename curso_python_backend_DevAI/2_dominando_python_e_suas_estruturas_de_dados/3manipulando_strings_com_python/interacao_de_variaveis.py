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