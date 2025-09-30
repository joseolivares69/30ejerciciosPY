class Calculo_Numerico:
    def __init__(self, numero):
        self.numero = numero

    def calculo_factorial(self):
        if self.numero < 0:
            return "El factorial no está definido para números negativos."
        if self.numero == 0:
            return 1
        
        resultado_fact = 1
        for i in range(1, self.numero + 1):
            resultado_fact *= i
        return resultado_fact

    def lista_divisores(self):
        divisores = []
        for i in range(1, self.numero + 1):
            if self.numero % i == 0:
                divisores.append(i)
        return divisores

    def esPrimo(self):
        lista_divisores = self.lista_divisores()
        
        if len(lista_divisores) == 2 and self.numero > 1:
            print(f"El número {self.numero} es primo")
        else:
            print(f"El número {self.numero} no es primo")

    def esPar(self):
        if self.numero % 2 == 0:
            print(f"El número {self.numero} es Par")
        else:
            print(f"El número {self.numero} es Impar")

# Prueba
primer_calculo = Calculo_Numerico(5)
print(f"El factorial del número 5 es: {primer_calculo.calculo_factorial()}")
print(f"La lista de divisores del número 5 es: {primer_calculo.lista_divisores()}")
primer_calculo.esPar()
primer_calculo.esPrimo()
print("\n")
segundo_calculo = Calculo_Numerico(14)
print(f"El factorial del número 14 es: {segundo_calculo.calculo_factorial()}")
print(f"La lista de divisores del número 14 es: {segundo_calculo.lista_divisores()}")
segundo_calculo.esPar()
segundo_calculo.esPrimo()
