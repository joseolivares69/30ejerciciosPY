class CuentaBancaria:
    tipo_de_cuenta = "Ahorros"
    tasa_interes = 0.07

    def __init__(self, nombre, apellido, num_cuenta, saldo_cuenta):
        self.nombre = nombre
        self.apellido = apellido
        self.num_cuenta = num_cuenta
        self.saldo_cuenta = saldo_cuenta

    @classmethod
    def establecer_tasa_interes(cls, nueva_tasa):
        cls.tasa_interes = nueva_tasa

    @classmethod
    def cambiar_tipo_cuenta(cls, tipo_cuenta):
        cls.tipo_de_cuenta = tipo_cuenta

    def deposito(self, cantidad):
        self.saldo_cuenta += cantidad

    def retiro(self, cantidad):
        if cantidad > self.saldo_cuenta:
            print("====Su saldo es insuficiente====")
        else:
            self.saldo_cuenta -= cantidad

    def aplicar_tasa_interes(self):
        self.saldo_cuenta -= self.saldo_cuenta * CuentaBancaria.tasa_interes

    def __str__(self):
        return (f"Número de cuenta: {self.num_cuenta}\n"
                f"Tipo de cuenta: {CuentaBancaria.tipo_de_cuenta}\n"
                f"Titular de la cuenta: {self.nombre} {self.apellido}\n"
                f"Saldo de la cuenta: {self.saldo_cuenta} euros.")

# Prueba
CuentaBancaria.cambiar_tipo_cuenta("Corriente")
CuentaBancaria.establecer_tasa_interes(0.05)

cuenta_1 = CuentaBancaria("Laurent", "Dubois", "983750XZ", 3000)
print(cuenta_1)
print("-" * 20)
print("Retiro de una cantidad de 4000 euros.")
cuenta_1.retiro(4000)
print(cuenta_1)
print("-" * 20)
print("Retiro de una cantidad de 1500 euros.")
cuenta_1.retiro(1500)
print(cuenta_1)
print("-" * 20)
print("Depósito de una cantidad de 500 euros.")
cuenta_1.deposito(500)
print(cuenta_1)
print("-" * 20)
print(f"Aplicación de la tasa de interés de: {CuentaBancaria.tasa_interes}")
cuenta_1.aplicar_tasa_interes()
print(cuenta_1)
