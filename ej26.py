class CarritoCompra:
    def __init__(self):
        self.articulos_precio_total = {}
        self.articulos_cantidad = {}
        self.articulos_precio_u = {}

    def agregar_articulo(self, articulo, precio_u, cantidad):
        precio_total_nuevo = round(precio_u * cantidad, 2)
        
        if articulo in self.articulos_precio_total:
            self.articulos_precio_total[articulo] += precio_total_nuevo
            self.articulos_cantidad[articulo] += cantidad
        else:
            self.articulos_precio_total[articulo] = precio_total_nuevo
            self.articulos_cantidad[articulo] = cantidad
            self.articulos_precio_u[articulo] = precio_u

    def eliminar_articulo(self, articulo, cantidad_a_eliminar):
        if articulo in self.articulos_cantidad:
            cantidad_actual = self.articulos_cantidad[articulo]
            precio_u = self.articulos_precio_u[articulo]
            
            nueva_cantidad = max(0, cantidad_actual - cantidad_a_eliminar)
            self.articulos_cantidad[articulo] = nueva_cantidad
            self.articulos_precio_total[articulo] = round(precio_u * nueva_cantidad, 2)
            
            if nueva_cantidad == 0:
                del self.articulos_precio_total[articulo]
                del self.articulos_cantidad[articulo]
                del self.articulos_precio_u[articulo]

    def precio_total(self):
        return round(sum(self.articulos_precio_total.values()), 2)

    def listar_articulos(self):
        return list(self.articulos_precio_total.keys())

    def costo_total_articulo(self, articulo):
        return self.articulos_precio_total[articulo]

    def obtener_cantidad(self, articulo):
        return self.articulos_cantidad.get(articulo, 0)

    def contar_articulos_distintos(self):
        return len(self.articulos_precio_total)

    def __str__(self):
        return (f"Los artículos contenidos en el carrito son: {self.listar_articulos()}\n"
                f"El costo actual del carrito es: {self.precio_total()} euros.")

# Prueba
carrito_1 = CarritoCompra()
carrito_1.agregar_articulo("zumo de naranja", 2, 4)
carrito_1.agregar_articulo("pan", 1.2, 3)

print("La cantidad de zumo de naranja seleccionada es:", carrito_1.obtener_cantidad("zumo de naranja"))
print("El costo total del 'pan' es:", carrito_1.costo_total_articulo("pan"), "euros.")
print("-" * 20)
print("Estado actual del carrito:")
print(carrito_1)
print("-" * 20)
carrito_1.eliminar_articulo("pan", 2)
print("El costo total del artículo 'pan' después de haber quitado 2 unidades del carrito es:", carrito_1.costo_total_articulo("pan"))
print("-" * 20)
print("Estado actual del carrito:")
print(carrito_1)
print("-" * 20)
print("El número de artículos distintos comprados es:", carrito_1.contar_articulos_distintos())
print("Artículos y el precio total correspondiente en el carrito:", carrito_1.articulos_precio_total)
