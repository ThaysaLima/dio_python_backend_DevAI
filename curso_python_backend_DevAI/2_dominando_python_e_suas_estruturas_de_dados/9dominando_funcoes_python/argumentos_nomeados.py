# Continuação da Aula 01

#ARGUMENTOS NOMEADOS

def salvar_carros(marca, modelo, ano, placa):

    print(f"Carro inserido com sucesso! {marca}/ {modelo}/ {ano}/ {placa}")

# maneiras de chamar a função 

salvar_carros("fiat", "palio", 1999, "ABC-1234") #desvantagem
salvar_carros(marca='hyundai', modelo='HB20', ano=2016, placa='DEF-5678') #vantagem
salvar_carros(**({'marca':'toyota', 'modelo':'SW4', 'ano': 2024, 'placa':'GHI-9101'})) #vantagem