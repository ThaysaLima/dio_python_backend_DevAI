class Cachorro:
    # init sempre é utilizado quando iniciamos uma instância na classe. 
    def __init__(self, nome, cor, acordado=True):
        print("Iniciando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def falar(self):
        print("Au-Au")

c = Cachorro("Chappie", "Amarelo")