class ManipuladoresArchivos:
    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo
        # Abre el archivo en el directorio actual para simplicidad del ejemplo
        self.archivo = open(self.nombreArchivo, "r+")
        print(f"¡El archivo '{self.nombreArchivo}' ha sido abierto en modo lectura y escritura!")

    def escribir_archivo(self, frase):
        self.archivo.write(frase)
        print(f"La frase '{frase}' ha sido escrita en el archivo {self.nombreArchivo}")

    def __del__(self):
        self.archivo.close()
        print(f"El archivo {self.nombreArchivo} ha sido cerrado.")

# Prueba (Nota: crea un archivo 'archivo_prueba.txt' en el directorio de ejecución)
archivo_1 = ManipuladoresArchivos("archivo_prueba.txt")
archivo_1.escribir_archivo("Hola, ¿cómo estás?")
del archivo_1
