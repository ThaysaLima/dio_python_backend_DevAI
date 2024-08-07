# Aula 02, desafio inicial. 

#class nome_da_classe (pode ter letra maiuscula)
class Bicicleta:
    #sempre temos que colocar o __init__
    def __init__(self, cor, modelo, ano, valor):
        # e sempre o self no início.
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("BiBi")
    
    def parar(self):
        print("stop")

    def correr(self):
        print("Runnnn")
        # __repr__ =  representação oficial de um objeto, se não tiver isso e tentar imprimir ele vai dizer [<__main__.Bicicleta object at 0x102d788d0>], colocando isso ele imprime [Bicicleta = cor= Branca, modelo= Cannondale, ano= 2024, valor= R$345.0! Adicionada com sucesso]. 
    # def __repr__(self):
    #     return f"Bicicleta(cor= {self.cor}, modelo= {self.modelo}, ano= {self.ano}, valor= R${self.valor})"
    
    #podemos usar tb o __str__ = é que uma represetação mais amigável para o user. 
    # def __str__(self): 
    #     return f"Bicicleta de cor {self.cor}, no modelo {self.modelo}, do ano de {self.ano}, com o valor R${self.valor}"
    
    # outra maneira

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        
    
vendas = []

venda1 = Bicicleta("Branca", "Cannondale", 2024, 345.00)

vendas.append(venda1)

for venda in vendas:
    print(venda)

venda1.buzinar()
venda1.parar()
venda1.correr()

#Acessar
print(venda1.cor, venda1.modelo, venda1.ano, venda1.valor)

#Novo exemplo:
venda2 = Bicicleta("Vermelha", "Cannoy", 2013, 34.788)
vendas.append(venda2)

for venda in vendas:
    print(venda)

# Ambos são a mesma coisa.
Bicicleta.buzinar(venda2) 
venda2.buzinar()

