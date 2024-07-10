# CLASSE 

class Cachorro:
    def __init__(self, nome, cor, acordado= True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print("AuAu")

    def dormir(self):
        self.acordado = False
        print("Zzz...")

# OBJETO 

cao_1 = Cachorro("Chappie", "amarelo", False)
cao_2 = Cachorro("Vuitton", "branco")

cao_1.latir() #não entendi muito bem. 


