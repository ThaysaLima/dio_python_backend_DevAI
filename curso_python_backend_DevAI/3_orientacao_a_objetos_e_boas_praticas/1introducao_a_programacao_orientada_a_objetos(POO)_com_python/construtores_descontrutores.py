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

c = Cachorro("Chappie", "Amarelo")
c.falar()

criar_cachorro()

#o del ele sempre vai ser "chamado" no final. 
# mesmo eu colocando esse monte de print, ele irá imprimir todos e APENAS no final é que ele vai deletar a instância.
print("Olá, mundo!")
print("Olá, mundo!")

del c

print("Olá, mundo!")
print("Olá, mundo!")
print("Olá, mundo!")

# mas se eu quiser que ele remova no meio, posso simplesmente usar a palavra reservada del 

# >>>
# Olá, mundo!
# Olá, mundo!
# Removendo instância da classe
# Olá, mundo!
# Olá, mundo!
# Olá, mundo!