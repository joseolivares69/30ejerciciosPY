class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        
    def presentarse(self):
        return f"Mi nombre es {self.nombre}, tengo {self.edad} años y soy un {self.genero}."
    
    def esAdulto(self):
        if self.edad >= 18:
            return True
        else:
            return False

# Prueba
persona1 = Persona("Martin", 23, "hombre")
print(persona1.presentarse())
print(persona1.esAdulto())
