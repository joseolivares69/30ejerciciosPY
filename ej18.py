class Animal:
    def __init__(self, nombre_animal):
        self.nombre_animal = nombre_animal

    def hablar(self):
        pass

class Gato(Animal):
    def __init__(self, nombre_gato):
        super().__init__(nombre_gato)

    def hablar(self):
        return f"{self.nombre_animal} dice ¡Miau miau!"

class Perro(Animal):
    def __init__(self, nombre_perro):
        super().__init__(nombre_perro)

    def hablar(self):
        return f"{self.nombre_animal} dice ¡Guau guau!"

# Prueba
rocky = Perro("Rocky")
felix = Gato("Felix")

print(rocky.hablar())
print(felix.hablar())
