import random
import string

class GeneradorContrasena:
    def __init__(self, longitud, caracteres_especiales=True, numeros=True, mayusculas=True, minusculas=True):
        self.longitud = longitud
        self.caracteres_especiales = caracteres_especiales
        self.numeros = numeros
        self.mayusculas = mayusculas
        self.minusculas = minusculas

    def incluir_mayusculas(self, mayusculas):
        self.mayusculas = mayusculas

    def incluir_minusculas(self, minusculas):
        self.minusculas = minusculas

    def incluir_numeros(self, numeros):
        self.numeros = numeros

    def incluir_caracteres_especiales(self, caracteres_especiales):
        self.caracteres_especiales = caracteres_especiales

    def modificar_longitud(self, longitud):
        self.longitud = longitud

    def generar_contrasena(self):
        caracteres_concat = ""
        
        if self.caracteres_especiales:
            caracteres_concat += "!@#$%^&*()"
        
        if self.numeros:
            caracteres_concat += string.digits
        
        if self.mayusculas:
            caracteres_concat += string.ascii_uppercase
        if self.minusculas:
            caracteres_concat += string.ascii_lowercase

        if not caracteres_concat:
            return "Error"

        contrasena = ""
        for _ in range(self.longitud):
            contrasena += random.choice(caracteres_concat)
        
        return contrasena

    def evaluar_contrasena(self, contrasena):
        robustez = 0
        
        if len(contrasena) >= 10:
            robustez += 1
        if any(char.islower() for char in contrasena):
            robustez += 1
        if any(char.isupper() for char in contrasena):
            robustez += 1
        if any(char.isdigit() for char in contrasena):
            robustez += 1
        if any(char in "!@#$%^&*()" for char in contrasena):
            robustez += 1

        if robustez == 5:
            return "Contraseña muy fuerte"
        elif robustez == 4:
            return "Contraseña fuerte"
        elif robustez == 3:
            return "Contraseña media"
        else:
            return "Contraseña débil"

    def guardar_contrasena(self, contrasena, ruta_archivo):
        with open(ruta_archivo, "w") as f:
            f.write(contrasena)

    def leer_contrasena(self, ruta_archivo):
        with open(ruta_archivo, "r") as f:
            return f.read().strip()

# Prueba (Nota: la salida de generación de contraseña será aleatoria)
generador_contrasena = GeneradorContrasena(12)
contrasena_1 = generador_contrasena.generar_contrasena()
print(contrasena_1)
print("Robustez de la contraseña 1:", generador_contrasena.evaluar_contrasena(contrasena_1))
print("-" * 20)

generador_contrasena.incluir_caracteres_especiales(False)
contrasena_2 = generador_contrasena.generar_contrasena()
print(contrasena_2)
print("Robustez de la contraseña 2:", generador_contrasena.evaluar_contrasena(contrasena_2))
print("-" * 20)

generador_contrasena.incluir_caracteres_especiales(True)
generador_contrasena.incluir_mayusculas(False)
generador_contrasena.incluir_minusculas(False)
contrasena_3 = generador_contrasena.generar_contrasena()
print(contrasena_3)
print("Robustez de la contraseña 3:", generador_contrasena.evaluar_contrasena(contrasena_3))
print("-" * 30)

ruta_archivo = "contrasena_test.txt"
print("Guardando la contraseña en curso...")
generador_contrasena.guardar_contrasena(contrasena_1, ruta_archivo)
print("Guardado de la contraseña -- OK")
print("Leyendo la contraseña guardada:")
print(generador_contrasena.leer_contrasena(ruta_archivo))
