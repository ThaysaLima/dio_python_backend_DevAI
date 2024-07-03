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

contatos1 = {
    'nome': 'thaysa', 'idade': 20, 'contato':'xxxxxxxxx' 
            }

print(contatos1.get('nome')) # thaysa

# pode tambem colocar um valor para ele retornar se a chave não existir 

print(contatos1.get('chave', {})) # {}, como não existe 'chave' ele retornou o que foi pedido. 

# 5) {}.items

# 6) {}.keys

# 7) {}.pop

# 8) {}.popitem

# 9) {}.setdefault

# 10) {}.update 

# 11) {}.values

# 12) in 

# 13) del 