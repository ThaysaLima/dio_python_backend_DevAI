# Aula 05

#IS e IS NOT, servem para comparar se dois obejtos pertencem a mesma posição na memória. 

curso_1 = "Curso de Python"
nome_curso1 = curso_1 
print(curso_1 is nome_curso1) #>>> True 
                                #Aqui só foi True por que por acaso o nome_curso1 recebe uma variável chamada curso_1 que por sua vez se chama "Curso de Python"

nome_curso2 = "AI Dev"
print(curso_1 is nome_curso2) #>>> False 

#OUTRO EXEMPLO 

saldo = 1000 
limite = 100 

print(saldo is limite) #>>> False
print(saldo is not limite) #>>> True