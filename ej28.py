class MiDiccionario:
    def __init__(self):
        self.objetos = {}

    def agregar_elemento(self, clave, valor):
        self.objetos[clave] = valor

    def eliminar_elemento(self, clave):
        del self.objetos[clave]

    def __iter__(self):
        return iter(self.objetos)

    def __getitem__(self, clave):
        return self.objetos[clave]

    def __setitem__(self, clave, valor):
        self.objetos[clave] = valor

    def __len__(self):
        return len(self.objetos)

    def __str__(self):
        return f"El contenido del diccionario es: {self.objetos}"

    def listar_claves(self):
        return list(self.objetos.keys())

    def listar_valores(self):
        return list(self.objetos.values())

    def listar_elementos(self):
        return list(self.objetos.items())

    def limpiar_diccionario(self):
        self.objetos.clear()

    def contiene_clave(self, clave):
        return clave in self.objetos

# Prueba
dicc_1 = MiDiccionario()
dicc_1.agregar_elemento("fruta", "manzana")
dicc_1.agregar_elemento("vegetal", "zanahoria")
dicc_1.agregar_elemento("carne", "res")
print(dicc_1)
print("-" * 20)

iter_dicc_1 = iter(dicc_1)
print("primera iteración:")
print(next(iter_dicc_1))
print("segunda iteración:")
print(next(iter_dicc_1))
print("tercera iteración:")
print(next(iter_dicc_1))
print("-" * 20)

print(f"El número de elementos en el diccionario es: {len(dicc_1)}")
print(f"Las claves del diccionario 'dicc_1' son: {dicc_1.listar_claves()}")
print(f"Los valores del diccionario 'dicc_1' son: {dicc_1.listar_valores()}")
print(f"'fruta' está en 'dicc_1': {dicc_1.contiene_clave('fruta')}")
print(f'La lista de elementos del diccionario "dicc_1" es: {dicc_1.listar_elementos()}')
print("-" * 20)

dicc_1.limpiar_diccionario()
print("Después de limpiar el diccionario:")
print(dicc_1)
