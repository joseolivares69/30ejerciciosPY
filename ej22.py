class Computadora:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    @staticmethod
    def listar_marcas():
        return ('Dell', 'HP', 'Lenovo', 'Apple')

class ComputadoraDeEscritorio(Computadora):
    def __init__(self, marca, modelo, precio, tamano_unidad_central):
        super().__init__(marca, modelo, precio)
        self.tamano_unidad_central = tamano_unidad_central

    def mostrar_informacion(self):
        return f"La computadora de escritorio de la marca {self.marca} {self.modelo} con una unidad central de tamaño {self.tamano_unidad_central} cm cuesta {self.precio} euros."

class ComputadoraPortatil(Computadora):
    def __init__(self, marca, modelo, precio, tamano_pulgadas):
        super().__init__(marca, modelo, precio)
        self.tamano_pulgadas = tamano_pulgadas

    def mostrar_informacion(self):
        return f"La computadora portátil de la marca {self.marca} {self.modelo} con una pantalla de {self.tamano_pulgadas} pulgadas cuesta {self.precio} euros."

# Prueba
print("Las marcas de computadoras disponibles son:")
print(Computadora.listar_marcas())

comp_escritorio = ComputadoraDeEscritorio("Dell", "7010", 800, 55)
comp_portatil = ComputadoraPortatil("HP", "830 G5", 489, 15.6)

print(comp_escritorio.mostrar_informacion())
print(comp_portatil.mostrar_informacion())
