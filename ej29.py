import random

class PiedraPapelTijeras:
    def __init__(self):
        self.opciones = ["Piedra", "Papel", "Tijeras"]
        self.puntajes = {"Ganado": 0, "Perdido": 0, "Empate": 0}
        self.historial = []
        self.num_turno = 0

    def obtener_eleccion_jugador(self):
        while True:
            eleccion = input(f"Introduce tu elección entre las siguientes opciones {tuple(self.opciones)}: ")
            if eleccion in self.opciones:
                return eleccion
            print("Elección no válida. Inténtalo de nuevo.")

    def jugar(self):
        self.num_turno += 1
        print(f"Turno N°{self.num_turno}")

        eleccion_jugador = self.obtener_eleccion_jugador()
        eleccion_computadora = random.choice(self.opciones)
        print("Elección de la computadora:", eleccion_computadora)

        self.historial.append((eleccion_jugador, eleccion_computadora))
        
        resultado = ""
        
        if eleccion_jugador == eleccion_computadora:
            resultado = "Empate"
            self.puntajes["Empate"] += 1
        elif (eleccion_jugador == "Piedra" and eleccion_computadora == "Tijeras") or \
             (eleccion_jugador == "Papel" and eleccion_computadora == "Piedra") or \
             (eleccion_jugador == "Tijeras" and eleccion_computadora == "Papel"):
            resultado = "Ganado"
            self.puntajes["Ganado"] += 1
        else:
            resultado = "Perdido"
            self.puntajes["Perdido"] += 1
            
        print("Resultado:", resultado)
        
    def mostrar_resultado_final(self):
        print("Historial de partidas jugadas:")
        print(self.historial)
        print("Tu puntuación es:", self.puntajes)
        
        ganadas = self.puntajes["Ganado"]
        perdidas = self.puntajes["Perdido"]
        
        print("Resultado final:")
        if ganadas > perdidas:
            print("¡Has ganado!")
        elif perdidas > ganadas:
            print("¡Has perdido!")
        else:
            print("¡Están empatados!")
