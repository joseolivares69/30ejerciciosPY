class Operacion:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def suma(self):
        return self.x + self.y
    
    def multiplicacion(self):
        return self.x * self.y
    
    def division(self):
        if self.y != 0:
            return self.x / self.y
        else:
            return "¡División de x por y es imposible!"

# Prueba
operacion1 = Operacion(3, 2)
print("La suma es:", operacion1.suma())
print("La multiplicación es:", operacion1.multiplicacion())
print("La división es:", operacion1.division())
operacion1.y = 0
print(operacion1.division())
