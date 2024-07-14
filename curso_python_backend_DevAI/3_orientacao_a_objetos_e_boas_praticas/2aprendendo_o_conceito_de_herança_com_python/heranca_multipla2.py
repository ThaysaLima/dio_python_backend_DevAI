from typing import Any


class Animal:
    def __init__(self, nmr_patas):
        self.nmr_patas = nmr_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave,valor in self.__dict__.items()])}"


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

gato = Gato(nmr_patas=4, cor_pelo="Preto e Laranja")
print(gato)

ornitorrinco = Onitorrinco(nmr_patas=2, cor_pelo="Verde", cor_bico="Amarelo") # quando usamos os **kw (keywords) lá em cima temos que colocar os nomes=
print(ornitorrinco)