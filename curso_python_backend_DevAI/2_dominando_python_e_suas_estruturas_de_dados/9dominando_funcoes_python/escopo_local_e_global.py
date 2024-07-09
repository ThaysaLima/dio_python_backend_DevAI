# Aula 1, parte 2. 

# ESCOPO LOCAL (dentro do bloco de código) E ESCOPO GLOBAL (fora do bloco de código)
salario = 2000

def bonus_salario(bonus):
    global salario
    salario += bonus
    return salario

print(bonus_salario(500)) # 2500