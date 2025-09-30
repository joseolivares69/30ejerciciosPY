class Calculadora:
    def __init__(self, variable):
        self.variable = variable

    @staticmethod
    def suma(x, y):
        return x + y

    @staticmethod
    def multiplicacion(x, y):
        return x * y

    @staticmethod
    def division(x, y):
        if y == 0:
            return "Operación imposible"
        else:
            return x / y

# Prueba
c1 = Calculadora(10)

print("Suma de dos números:", Calculadora.suma(2, 4))
print("Multiplicación de dos números:", Calculadora.multiplicacion(4, 8))
print("División de dos números:", Calculadora.division(4, 2))
print("Suma de dos números usando una instancia de clase:", c1.suma(3, 5))
