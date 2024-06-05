# Aula 05

nome = input("Informe seu nome: ")
print(f"O seu nome é {nome}") # o nome vai ser substituido pelo o que o usuário responder em cima

#MANEIRAS DE USAR O PRINT()
nome = "Guilherme"
sobrenome = "Carvalho"

print(nome, sobrenome) #Guilherme Carvalho
print(nome, sobrenome, end="...\n") #Guilherme Carvalho... 
                                    #

                                    #por padrão o end= já faz a quebra da linha \n, mas como foi modificado tem que colocar dnv. 
print(nome, sobrenome, sep=" # ") #Guilherme # Carvalho
                                #Por padrão o sep= faz a separação com 1 espaço para cada lado, mas como foi modificado temos que colocar dnv. 