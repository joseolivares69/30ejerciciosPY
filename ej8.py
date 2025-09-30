import random

class Dado:
    def __init__(self, resultado=0):
        self.resultado = resultado
        
    def lanzar_dado(self):
        self.resultado = random.randint(1, 6)
        return self.resultado
        
    def mostrar_puntos(self):
        print("El número de puntos obtenidos es:", self.resultado)

# Prueba
lanzamiento_1 = Dado()
lanzamiento_1.lanzar_dado()
lanzamiento_1.mostrar_puntos()
