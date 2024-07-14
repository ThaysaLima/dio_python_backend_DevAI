class Veiculo:
    def __init__(self, cor, placa, nmr_rodas):
        self.cor = cor
        self.placa = placa
        self.nmr_rodas = nmr_rodas

    def ligar_motor(self):
        print("Ligando motor...")


class Moto(Veiculo):
    def __str__(self):
        return f"Moto de cor {self.cor}, com placa {self.placa}, e {self.nmr_rodas} rodas."


class Carro(Veiculo):
   def __str__(self):
       return f"Carro de {self.cor}, com placa {self.placa}, e {self.nmr_rodas} rodas."

class Caminhao(Veiculo):
    def __init__(self, cor, placa, nmr_rodas, carregado= True):
        super().__init__(cor, placa, nmr_rodas) # esse super() serve para chamar métodos da classe mãe a partir de uma classe filha.
        self.carregado = carregado
    def esta_carregadado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado!")
    def __str__(self):
        return f"Caminhão de cor {self.cor}, com placa {self.placa}, e {self.nmr_rodas} rodas."

moto1 = Moto("Vermelho", "ABC-1234", 2)
moto1.ligar_motor()

print(moto1)

carro1 = Carro("Azul", "DEF-5678", 4)
carro1.ligar_motor()

print(carro1)

caminhao1 = Caminhao("Preto", "GHI-9101", 8, False)
caminhao1.ligar_motor()

print(caminhao1)
caminhao1.esta_carregadado()




