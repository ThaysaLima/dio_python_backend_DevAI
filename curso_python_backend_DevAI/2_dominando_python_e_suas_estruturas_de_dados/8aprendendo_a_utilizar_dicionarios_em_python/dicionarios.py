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

# DICIONARIOS ANINHADOS, a chave tem que ser imutável, então o valor será um outro dicionário.

contatos_empresa = {

    "nathan@gmail.com" : {"nome":"nathan", "número":914225144},
    "thaysa@gmail.com" : {"nome":"thaysa", "número":936749530},
    "francisca@gmail.com" : {"nome":"francisca", "número":936749531},

}

# para acessar = nome_dicionario[chave][chave_dicinario_interno]

print(contatos_empresa["thaysa@gmail.com"]["número"]) # 936749530



