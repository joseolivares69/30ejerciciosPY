class MiCadenaPersonal:
    def __init__(self, variable_str):
        self.variable_str = variable_str

    def __add__(self, cadena):
        return self.variable_str + " | " + cadena.variable_str

    def __mul__(self, escalar):
        return self.variable_str * escalar

    def __len__(self):
        caracteres_a_eliminar = [",", "?", "!", " ", ".", "|"]
        cadena_limpia = self.variable_str
        for c in caracteres_a_eliminar:
            cadena_limpia = cadena_limpia.replace(c, "")
        return len(cadena_limpia)

    def __str__(self):
        return self.variable_str

    def __contains__(self, subCadena):
        return subCadena in self.variable_str

# Prueba
cadena_1 = MiCadenaPersonal("¡Hola, cómo estás?")
cadena_2 = MiCadenaPersonal("Bienvenido a este curso.")

print("Cadena_1 =", cadena_1)
print("Cadena_2 = ", cadena_2)
print("La concatenación de cadena_1 y cadena_2 da:", cadena_1 + cadena_2)
print("La longitud de cadena_1 es:", len(cadena_1))
print("La longitud de cadena_2 es:", len(cadena_2))
print("La cadena_1 contiene la palabra 'cómo':", "cómo" in cadena_1)
