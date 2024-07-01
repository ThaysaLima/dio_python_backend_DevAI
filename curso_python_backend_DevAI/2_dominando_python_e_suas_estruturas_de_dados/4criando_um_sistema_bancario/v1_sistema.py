# Versão 1, do menu do banco que irá se chamar Banco Py. 

# 3 operações: 1 - Sacar dinheiro, mas so pode ser 3 por dia e até R$500,00. Se não houver saldo o suficiente no banco, então exibir uma mensagem informando que não será possível o saque.
#              2 - Depositar dinheiro, só pode ser valores inteiros e positivos, e todos os valores que entrar tem que ser armazenado numa variável para depois ser mostrada no extrato do banco. 
#              3 - Extrato, vai ter que mostras uma lista de todos os depósitos, todos os saque e informar o valor atual da conta. O formato do valor tem que está em R$xxx.xx 


menu = '''
    ========================== Bem vindos ao Banco Py ==========================

    d - Depositar 
    s - Sacar 
    e - Extrato
    q - Sair

    =========== Por favor insira a baixo o número da ação pretendida ===========

'''

#esse while true, vai fazer com que ele sempre repita essa opção. 
while True:

    opcao_bem_vindos = input(menu)

    if opcao_bem_vindos == "d":
        print("*DEPÓSITO*")
        deposito = float(input("Qual o valor do deposito: "))

    elif opcao_bem_vindos == "s":
        print("*SAQUE*")
        
    elif opcao_bem_vindos == "e": 
        print("*EXTRATO BANCÁRIO*")

    elif opcao_bem_vindos == "q": 
        print("*SAIR*")
        print("Obrigada pela visita, volte sempre!")
        break

    else:
        print("Por favor começe novamente e escolha uma opção válida.")

