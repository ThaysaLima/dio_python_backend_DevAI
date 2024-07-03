# Parte 1, Aula 01

# SINTÁXE
# def nome_funcao(argumentos):
#     bloco de código

# chamar a função = nome_funcao()

def exibir_mensagem():
    print('hello, world!')

exibir_mensagem()

def exibir_mensagem2(nome):
    print(f"Olá bem vindo {nome}")

exibir_mensagem2('Nathan') #não é preciso colocar nome='Nathan'

def exibir_mensagem3(nome='N/A'):
    print(f"Olá, seja bem vindo {nome}")

exibir_mensagem3()
exibir_mensagem3(nome="Thaysa")