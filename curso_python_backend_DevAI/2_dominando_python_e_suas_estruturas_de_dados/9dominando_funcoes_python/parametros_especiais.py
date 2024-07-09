# Aula 01, parte 2. 

# PARÂMETROS ESPECIAIS 

#SINTÁXE: 

    # antes da / NÃO se pode passar o argumento na hora de chamar. 
# def f(pos1, pos2, / , pos or kwd, * , kwd1, kwd2): # depois do * TEM que passar o argumento na hora de chamar.
                # o que está entre a / e o * PODE ou NÃO passar o argumento na hora de chamar ele.


# APENAS POSIÇÃO (pos)

def carros(modelo, ano, placa, / , marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

carros("Pálio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # JEITO VÁLIDO 

carros("Pálio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina") # JEITO VÁLIDO

carros(modelo="Pálio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # JEITO INVÁLIDO, pois foi passado os argumento na chamada da função. (carros() got some positional-only arguments passed as keyword arguments)

# APENAS KEYWORD (kwd) 

def carros2(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

carros2(modelo="Pálio", ano=1999, placa="ABC-1234", marca="Fiat", motor="2.0", combustivel="Gasolina") # JEITO VÁLIDO

carros2("Pálio", 1999, "ABC-1234", marca="Fiat", motor="2.0", combustivel="Gasolina") # JEITO INVÁLIDO, obrigatório passar os argumentos na hora de chamar. (carros2() takes 0 positional arguments but 3 positional arguments (and 3 keyword-only arguments) were given)

# POISIÇÃO E KEYWORD (pos e kwd)

def carros3(modelo, ano, placa, / , * , marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

carros3("Pálio", 1999, "ABC-1234", marca="Fiat", motor="3.0", combustivel="Gasolina") # JEITO VÁLIDO

carros3(modelo="Pálio", ano=1999, placa="ABC-1234", marca="Fiat", motor="3.0", combustivel="Gasolina") # JEITO INVÁLIDO

# exemplo meu 

def dados_clientes(nome, idade, /, estado_civil, *, local_nascimento, ano_nascimento):
    impressao = f"Nome do Cliente: {nome}\nIdade: {idade} anos\nEstado Civil: {estado_civil}\nNascido em: {local_nascimento}, no ano de {ano_nascimento}."
    print(impressao)

dados_clientes("Thaysa Lima", 20, estado_civil="Solteira", local_nascimento="Fortaleza-Ce", ano_nascimento=2003)

