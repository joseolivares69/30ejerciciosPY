class Libro:
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        
    def mostrar_informaciones(self):
        print(f"El libro titulado '{self.titulo}', escrito por la autora '{self.autor}', se vende a {self.precio} euros.")

# Prueba
libro_1 = Libro("100 Ejercicios Python para practicar", "Laurentine K.Masson", 9.99)
libro_1.mostrar_informaciones()
