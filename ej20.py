class TrabajadorEmpresa:
    def __init__(self, nombre_trabajador, salario, edad):
        self.nombre_trabajador = nombre_trabajador
        self.salario = salario
        self.edad = edad

    def mostrar_funcion(self):
        print("Soy un trabajador de una empresa")

    def mostrar_info(self):
        print("Nombre:", self.nombre_trabajador)
        print("Salario:", self.salario)
        print("Edad:", self.edad)

class Director(TrabajadorEmpresa):
    def __init__(self, nombre_director, salario, edad, prima):
        super().__init__(nombre_director, salario, edad)
        self.prima = prima

    def mostrar_funcion(self):
        print("Soy un director de empresa")

    def mostrar_info(self):
        super().mostrar_info()
        print(f"La prima anual percibida es de {self.prima} euros.")

class Ingeniero(TrabajadorEmpresa):
    def __init__(self, nombre_ingeniero, salario, edad, especialidad):
        super().__init__(nombre_ingeniero, salario, edad)
        self.especialidad = especialidad

    def mostrar_funcion(self):
        print("Soy un ingeniero")

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Soy un ingeniero especializado en {self.especialidad}.")

# Prueba
director = Director("Julien Lecoq", 75000, 43, 5000)
ingeniero = Ingeniero("Baptiste Leblanc", 40000, 32, "inteligencia artificial")

trabajadores = [director, ingeniero]

for trabajador in trabajadores:
    trabajador.mostrar_funcion()
    trabajador.mostrar_info()
    print()
