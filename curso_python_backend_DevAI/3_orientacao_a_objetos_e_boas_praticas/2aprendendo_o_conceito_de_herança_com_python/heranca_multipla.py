class Animal:
    def __init__(self, nmr_patas):
        self.nmr_patas = nmr_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        


class Mamifero(Animal):
    def __init__(self, nmr_patas, cor_pelo):
        self.cor_pelo = cor_pelo
        super().__init__(nmr_patas)


class Ave(Animal):
    def __init__(self, nmr_patas):
        super().__init__(nmr_patas)


class Gato(Mamifero):
    pass


class Onitorrinco(Mamifero, Ave):
    pass


# gato = Gato(4, "Preto")
# print(gato) # Gato: nmr_patas= 4

ornitorrinco = Onitorrinco(2, "Verde")
print(ornitorrinco)