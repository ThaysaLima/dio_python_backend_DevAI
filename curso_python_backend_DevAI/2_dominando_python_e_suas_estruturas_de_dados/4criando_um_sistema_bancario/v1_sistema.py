# Versão 1, do menu do banco que irá se chamar Banco Py. 

# 3 operações: 1 - Sacar dinheiro, mas so pode ser 3 por dia e até R$500,00. Se não houver saldo o suficiente no banco, então exibir uma mensagem informando que não será possível o saque.
#              2 - Depositar dinheiro, só pode ser valores inteiros e positivos, e todos os valores que entrar tem que ser armazenado numa variável para depois ser mostrada no extrato do banco. 
#              3 - Extrato, vai ter que mostras uma lista de todos os depósitos, todos os saque e informar o valor atual da conta. O formato do valor tem que está em R$xxx.xx 

#valores inicias. 
saldo = 0.0
transacoes = []
saques_diarios = 0
LIMITE_SAQUE_DIARIO = 3
LIMITE_SAQUE_VALOR = 500.0

menu = '''
    ========================== Bem vindos ao Banco Py ==========================

    1 - Depositar 
    2 - Sacar 
    3 - Extrato
    0 - Sair

    =========== Por favor insira a baixo o número da ação pretendida ===========

'''

#esse while true, vai fazer com que ele sempre repita essa opção. 
while True:

    opcao_bem_vindos = input(menu)

    if opcao_bem_vindos == "1":
        print("*DEPÓSITO*")
        valor = float(input("Digite o valor a ser depositado: "))
        saldo += valor
        transacoes.append(f"Depósito: +R${valor:.2f}")
        print(f"Você depositou R${valor:.2f}. Seu novo saldo é R${saldo:.2f}.")



    elif opcao_bem_vindos == "2":
        print("\n*SAQUE*")
        if saques_diarios >= LIMITE_SAQUE_DIARIO:
            print("Você atingiu o limite de 3 saques diários.")

        else:
            valor = float(input("Digite o valor a ser sacado (máximo R$500,00): "))
            if valor > saldo:
                print("Saldo insuficiente!")
            elif valor > LIMITE_SAQUE_VALOR:
                print("Você não pode sacar mais de R$500,00 por transação.")
            else:
                saldo -= valor
                saques_diarios += 1
                transacoes.append(f"Saque: -R${valor:.2f}")
                print(f"Você sacou R${valor:.2f}. Seu novo saldo é R${saldo:.2f}.")

    elif opcao_bem_vindos == "3": 
        print("\n*EXTRATO BANCÁRIO*")
        if not transacoes:
            print("Nenhuma transação realizada.")
        else:
            for transacao in transacoes:
                print(transacao)
            print(f"Saldo atual: R${saldo:.2f}")

    elif opcao_bem_vindos == "0": 
        print("\n*SAIR*")
        print("Obrigada pela visita, volte sempre!")
        break

    else:
        print("Por favor começe novamente e escolha uma opção válida.")

