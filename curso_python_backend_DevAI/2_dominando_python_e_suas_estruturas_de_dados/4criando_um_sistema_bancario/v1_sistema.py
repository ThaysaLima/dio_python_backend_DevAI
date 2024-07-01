# Versão 1, do menu do banco que irá se chamar Banco Py. 

# 3 operações: 1 - Sacar dinheiro, mas so pode ser 3 por dia e até R$500,00. Se não houver saldo o suficiente no banco, então exibir uma mensagem informando que não será possível o saque.
#              2 - Depositar dinheiro, só pode ser valores inteiros e positivos, e todos os valores que entrar tem que ser armazenado numa variável para depois ser mostrada no extrato do banco. 
#              3 - Extrato, vai ter que mostras uma lista de todos os depósitos, todos os saque e informar o valor atual da conta. O formato do valor tem que está em R$xxx.xx 


inicio_projeto = '''
    ========================== Bem vindos ao Banco Py ==========================

    1 - Depositar 
    2 - Sacar 
    3 - Extrato
    0 - Sair

    =========== Por favor insira a baixo o número da ação pretendida ===========

'''

print(inicio_projeto)

opcao_bem_vindos = int(input("Digite aqui a opção escolhida: "))
if opcao_bem_vindos == 1:
    print("Opção Depositar.")
elif opcao_bem_vindos == 2:
    print("Opção Sacar.")
elif opcao_bem_vindos == 3: 
    print("Opção Extrato Bancário.")
elif opcao_bem_vindos == 0: 
    print("Opção Sair.")
else:
    print("Por favor começe novamente e escolha uma opção válida.")