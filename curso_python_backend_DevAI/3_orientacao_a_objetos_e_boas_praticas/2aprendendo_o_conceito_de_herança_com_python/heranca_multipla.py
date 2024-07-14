class Animal:
    def __init__(self, nmr_patas):
        self.nmr_patas = nmr_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        

# ao tentar chamar o ornitorrinco o python vai ficar confuso com 3 argumentos, quando na verdade no def Mamifero/Ave apenas tem 2. para isso vamos usar o **kw no lugar do 3º argumento.

#vamos apagar todos os argumentos que estão na classe filha, mas que pertencem a classe mãe (nmr_patas), com isso vamos ter que mudar o super().__init__(nmr_patas) para super().__init__(**kw)

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Gato(Mamifero):
    pass


class Onitorrinco(Mamifero, Ave):
    pass


gato = Gato(nmr_patas=4, cor_pelo="Preto")
print(gato) # Gato: nmr_patas= 4

# a partir do momento que colocamos os **kw lá em cima, aqui em baixo temos que nomear os argumentos 
ornitorrinco = Onitorrinco(nmr_patas=2, cor_pelo="Verde", cor_bico="Laranja")
print(ornitorrinco) #Onitorrinco: cor_pelo=Verde, cor_bico=Laranja, nmr_patas=2

