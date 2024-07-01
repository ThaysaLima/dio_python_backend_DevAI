# Aula 04, como fazer multiplas linhas de string. 

#Forma 1
nome = "Thaysa"
mensagem = f"""
Olá, meu nome é {nome}. 
E atualmente estudo Python.
"""
print(mensagem)

mensagem2 = f"""
Olá, meu nome é {nome}. 

#os espaços em branco serão mostrados no print.

E atualmente estudo Python.
"""
print(mensagem2)

#Forma 2