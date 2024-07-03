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

# 3} {}.fromkeys

# 4) {}.set

# 5) {}.items

# 6) {}.keys

# 7) {}.pop

# 8) {}.popitem

# 9) {}.setdefault

# 10) {}.update 

# 11) {}.values

# 12) in 

# 13) del 