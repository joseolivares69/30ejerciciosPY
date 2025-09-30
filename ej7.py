# Reutilizamos la clase Persona
class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

class Estudiante(Persona):
    def __init__(self, nombre, edad, genero, nivel):
        super().__init__(nombre, edad, genero)
        self.nivel = nivel
        
    def inscripcion(self, estudiantes_inscritos):
        info_estudiante = (self.nombre, self.edad, self.genero, self.nivel)
        estudiantes_inscritos.append(info_estudiante)

# Prueba
estudiantes_inscritos = []
estudiante1 = Estudiante("Fabrice", 17, "hombre", "segundo año")
estudiante1.inscripcion(estudiantes_inscritos)
estudiante2 = Estudiante("Julie", 8, "mujer", "primaria")
estudiante2.inscripcion(estudiantes_inscritos)
print("Los estudiantes inscritos en los cursos son:", estudiantes_inscritos)
