class Animal:
    def __init__(self, nmr_patas):
        self.nmr_patas = nmr_patas
        


class Mamifero(Animal):
    def __init__(self, nmr_patas):
        self.nmr_patas = nmr_patas
        super().__init__(nmr_patas)


class Ave(Animal):
    def __init__(self, nmr_patas):
        self.nmr_patas = nmr_patas
        super().__init__(nmr_patas)


class Gato(Mamifero):
    pass


class Onitorrinco(Mamifero, Ave):
    pass