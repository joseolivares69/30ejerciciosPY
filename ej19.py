class Texto:
    def __init__(self, frase):
        self.frase = frase

    def mostrar_texto(self):
        print(self.frase)

class TextoItalico(Texto):
    def __init__(self, frase):
        super().__init__(frase)

    def mostrar_texto(self):
        print(f"_{self.frase}_")

class TextoNegrita(Texto):
    def __init__(self, frase):
        super().__init__(frase)

    def mostrar_texto(self):
        print(f"**{self.frase}**")

# Prueba
frase_base = "Aprender POO en Python a través de la práctica"
texto_1 = Texto(frase_base)
texto_2 = TextoItalico(frase_base)
texto_3 = TextoNegrita(frase_base)

texto_1.mostrar_texto()
texto_2.mostrar_texto()
texto_3.mostrar_texto()
