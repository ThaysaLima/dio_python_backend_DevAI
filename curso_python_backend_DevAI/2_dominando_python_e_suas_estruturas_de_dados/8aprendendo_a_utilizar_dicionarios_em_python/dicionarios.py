# Aula 01

#conjunto de dados não ordenados de pares {chave:valor}, o contúdo da chave é único. 

# 1) método

pessoa = {"nome":"thaysa", "idade":20, "profissão":"programadora"} # {'nome': 'thaysa', 'idade': 20, 'profissão': 'programadora'}

# 2) método 

pessoa = dict(nome = "thaysa", idade=20, profissão="programadora") # {'nome': 'thaysa', 'idade': 20, 'profissão': 'programadora'}

# para ADICIONAR um chave e valor não existente = nome_dicionario[chave] = valor

pessoa["número"] = 936749530
print(pessoa) # {'nome': 'thaysa', 'idade': 20, 'profissão': 'programadora', 'número': 936749530} 

# se eu colocar uma chave JÁ EXISTENTE, ele irá substituir o valor antigo. 

pessoa["idade"] = 21 
print(pessoa) # {'nome': 'thaysa', 'idade': 21, 'profissão': 'programadora', 'número': 936749530}

# para ACESSAR o dicionário = nome_dicionario[chave] e ele vai retornar o valor

print(pessoa["profissão"]) # programadora



