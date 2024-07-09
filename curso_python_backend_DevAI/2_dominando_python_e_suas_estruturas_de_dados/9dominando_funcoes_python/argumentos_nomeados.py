# Continuação da Aula 01

#ARGUMENTOS NOMEADOS

def salvar_carros(marca, modelo, ano, placa):

    print(f"Carro inserido com sucesso! {marca}/ {modelo}/ {ano}/ {placa}")

# maneiras de chamar a função 

salvar_carros("fiat", "palio", 1999, "ABC-1234") #desvantagem
salvar_carros(marca='hyundai', modelo='HB20', ano=2016, placa='DEF-5678') #vantagem
salvar_carros(**({'marca':'toyota', 'modelo':'SW4', 'ano': 2024, 'placa':'GHI-9101'})) #vantagem, kwargs. 

# *ARGS e **KWARGS

#exemplo fácil 

def funcao_exemplo(**kwargs): 
    for chave,valor in kwargs.items():
        print(f"{chave} : {valor}")

funcao_exemplo(nome="Thaysa", idade= 20, cidade= "Fortaleza")

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}:{valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Zen of Python", "Beautiful is better than ugly", autor="Tim Peaters", ano= 1999)