import re

# Crie uma função chamada 'validate_numero_telefone' que aceite um argumento 'phone_number'
def validate_numero_telefone(phone_number):
    # Defina um padrão de expressão regular (regex) para validar números de telefone no formato (XX) 9XXXX-XXXX
    pattern = r'^\(\d{2}\) 9\d{4}-\d{4}$'
    
    # A função 're.match()' verifica se o padrão definido corresponde ao número de telefone fornecido
    if re.match(pattern, phone_number):
        # Retorna que o número de telefone é válido
        return "Número de telefone válido"
    else:
        # Retorna que o número de telefone é inválido
        return "Número de telefone inválido"

# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'
phone_number = input("Informe o número de telefone: ")

# Chame a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento e armazene o resultado retornado na variável 'result'
result = validate_numero_telefone(phone_number)

# Imprime o resultado
print(result)