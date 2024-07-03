# continuação Aula 1

# MÉTODOS DICT 
# 1) {}.clear, excluir todos os dados do dicionário

contatos = {
    'thaysa@gmail.com': {'nome': 'thaysa', 'idade': 20, 'contato':'xxxxxxxxx'},
    'cesar@gmail.com' : {'nome': 'cesar', 'idade': 24, 'contato':'xxxxxxxxx'},
    'francisca@gmail.com' : {'nome': 'francisca', 'idade': 52, 'contato': 'xxxxxxxxx'}, 
            }

contatos.clear() # {}
print(contatos) 

# 2) {}.copy, cria uma cópia da biblioteca onde não interfira com a original.

contatos = {
    'thaysa@gmail.com': {'nome': 'thaysa', 'idade': 20, 'contato':'xxxxxxxxx'},
    'cesar@gmail.com' : {'nome': 'cesar', 'idade': 24, 'contato':'xxxxxxxxx'},
    'francisca@gmail.com' : {'nome': 'francisca', 'idade': 52, 'contato': 'xxxxxxxxx'}, 
            } 

copia = contatos.copy()
print(copia)

# 3} {}.fromkeys, cria apenas as chaves quando não queremos atribuir nenhuma valor

contatos = {
    'thaysa@gmail.com': {'nome': 'thaysa', 'idade': 20, 'contato':'xxxxxxxxx'},
    'cesar@gmail.com' : {'nome': 'cesar', 'idade': 24, 'contato':'xxxxxxxxx'},
    'francisca@gmail.com' : {'nome': 'francisca', 'idade': 52, 'contato': 'xxxxxxxxx'}, 
            }

print(contatos.fromkeys(['nome', 'contato'])) # {'nome': None, 'contato': None}

#ou podemos escrever o que queremos onde não há valor

print(dict.fromkeys(['nome','contato'], 'vazio')) # {'nome': 'vazio', 'contato': 'vazio'}

# 4) {}.get, outra maneira de acessar. Se tentarmos acessar uma chave que não existe vai dar keyerror

contatos = {
    'nome': 'thaysa', 'idade': 20, 'contato':'xxxxxxxxx' 
            }

print(contatos.get('nome')) # thaysa

# pode tambem colocar um valor para ele retornar se a chave não existir 

print(contatos.get('chave', {})) # {}, como não existe 'chave' ele retornou o que foi pedido. 

# 5) {}.items, retorna uma lista de tuplas

contatos = {
    'thaysa@gmail.com': {'nome': 'thaysa', 'idade': 20, 'contato':'xxxxxxxxx'},
    'cesar@gmail.com' : {'nome': 'cesar', 'idade': 24, 'contato':'xxxxxxxxx'},
    'francisca@gmail.com' : {'nome': 'francisca', 'idade': 52, 'contato': 'xxxxxxxxx'}, 
            }

print(contatos.items()) # dict_items([('thaysa@gmail.com', {'nome': 'thaysa', 'idade': 20, 'contato': 'xxxxxxxxx'}), ('cesar@gmail.com', {'nome': 'cesar', 'idade': 24, 'contato': 'xxxxxxxxx'}), ('francisca@gmail.com', {'nome': 'francisca', 'idade': 52, 'contato': 'xxxxxxxxx'})])

# 6) {}.keys, retorna apenas as chaves

dicionario = {'nome': 'thaysa', 'idade': 20, 'profissão': 'programadora', 'contato': 936749530}

print(dicionario.keys()) # dict_keys(['nome', 'idade', 'profissão', 'contato'])

# 7) {}.pop, remover um valor do dicionário e retornar.

dicionario = {'nome': 'thaysa', 'idade': 20, 'profissão': 'programadora', 'contato': 936749530}
print(dicionario.pop('profissão')) # programadora
print(dicionario) # {'nome': 'thaysa', 'idade': 20, 'contato': 936749530}


# 8) {}.popitem,retira os itens na sequência. 

dicionario = {'nome': 'thaysa', 'idade': 20, 'profissão': 'programadora', 'contato': 936749530}
print(dicionario.popitem()) # ('contato', 936749530)
print(dicionario) # {'nome': 'thaysa', 'idade': 20, 'profissão': 'programadora'}


# 9) {}.setdefault, vai atribuir um valor a uma chave caso ela não exista. 

dicionario = {'nome': 'thaysa', 'idade': 20, 'profissão': 'programadora', 'contato': 936749530}
print(dicionario.setdefault('nome','thata')) # thaysa
                    # aqui ele vai verificar se existe a chave 'nome', se existir ele vai apenas ignorar, se não ele vai criar a chave 'nome' e atribuir o valor de 'thata'.

print(dicionario.setdefault('cidade', 'fortaleza')) # fortaleza, pois a chave cidade não existia. 
print(dicionario) # {'nome': 'thaysa', 'idade': 20, 'profissão': 'programadora', 'contato': 936749530, 'cidade': 'fortaleza'}

# 10) {}.update, atualiza o dicionário para outro dicionário. 

dicionario = {'nome': 'thaysa', 'idade': 20, 'profissão': 'programadora', 'contato': 936749530}
dicionario.update({'nome':'thata', 'idade':21, 'profissão': 'analista de dados', 'contato':936749531})
print(dicionario) # {'nome': 'thata', 'idade': 21, 'profissão': 'analista de dados', 'contato': 936749531} 

# e o que acontece que não tiver o dados que estamos atualizando? ele vai criar esse novo dado 

dicionario.update({'nome1':'nat', 'idade1':24, 'profissão1':'psicólogo', 'cantato1':921546789})
print(dicionario) # {'nome': 'thata', 'idade': 21, 'profissão': 'analista de dados', 'contato': 936749531, 'nome1': 'nat', 'idade1': 24, 'profissão1': 'psicólogo', 'cantato1': 921546789}

# 11) {}.values, retorna apenas os valores

dicionario = {'nome': 'thaysa', 'idade': 20, 'profissão': 'programadora', 'contato': 936749530}
print(dicionario.values()) # dict_values(['thaysa', 20, 'programadora', 936749530])

# 12) in, saber se a chave existe dentro do dicionário ou não. 

resultado = 'nome' in dicionario
print(resultado) # True

resultado2 = 'cabeça' in dicionario
print(resultado2) # False

# 13) del, outra forma de excluir um valor. 

dicionario = {'nome': 'thaysa', 'idade': 20, 'profissão': 'programadora', 'contato': 936749530}
del dicionario['nome']
print(dicionario) # {'idade': 20, 'profissão': 'programadora', 'contato': 936749530}

# 13) del, dicionários de dicionários

dicionario = {
    'usuario1': {'nome': 'thaysa', 'idade': 20},
    'usuario2': {'nome': 'joao', 'idade': 25}
}

del dicionario['usuario1']['idade']  # Remove o item 'idade' do dicionário 'usuario1'
print(dicionario) # {'usuario1': {'nome': 'thaysa'}, 'usuario2': {'nome': 'joao', 'idade': 25}}