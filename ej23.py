class Usuario:
    usuarios_activos = 0

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        Usuario.usuarios_activos += 1

    @classmethod
    def extraer_info(cls, cadena):
        nombre, apellido, edad = cadena.split(", ")
        return cls(nombre, apellido, int(edad))

    @classmethod
    def mostrar_usuarios_activos(cls):
        return f"Actualmente, hay {cls.usuarios_activos} usuario(s) activos"

    def desconectar(self):
        Usuario.usuarios_activos -= 1
        return f"El/La usuario/a {self.nombre} {self.apellido} se ha desconectado"

# Prueba
usuario_1 = Usuario("Martin", "Leboeuf", 35)
usuario_2 = Usuario.extraer_info("Emilie, Dupont, 28")

print(Usuario.mostrar_usuarios_activos())
print(usuario_2.desconectar())
print(Usuario.mostrar_usuarios_activos())
