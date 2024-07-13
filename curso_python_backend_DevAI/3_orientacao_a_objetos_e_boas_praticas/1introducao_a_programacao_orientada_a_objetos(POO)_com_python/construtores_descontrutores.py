class Cachorro:
    # init sempre é utilizado quando iniciamos uma instância na classe. 
    def __init__(self, nome, cor, acordado=True):
        print("Iniciando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo instância da classe")

    def falar(self):
        print("Au-Au")

def criar_cachorro():
    c = Cachorro("Zeus", "Branco", False)
    print(c.nome)

# c = Cachorro("Chappie", "Amarelo")
# c.falar()

criar_cachorro()
