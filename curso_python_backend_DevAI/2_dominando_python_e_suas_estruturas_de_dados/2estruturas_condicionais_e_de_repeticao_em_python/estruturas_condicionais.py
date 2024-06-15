# Aula 02
#if 
idade = int(input("Por favor insira a sua idade: "))

if idade >= 18:
    print("Você está habilitado a tirar a carteira de motorista!")

if idade < 18: 
    print("Para tirar a carteira de motorista você deve ter no mínimo 18 anos.")

#if e else

opcao = int(input("Insira sua idade: "))

if opcao == str: 
    print("Por favor apresente apenas valores numéricos!")

else:
    print(f"Sua idade é {opcao} anos")

#if, elif e else

opcao = int(input("Informe o número da opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1: 
    int(input("Insira a quantidade que deseja sacar: "))

elif opcao == 2: 
    print("Exibindo o extrato...")

else:
    print("Por favor, tente novamente e insira uma opção válida.")