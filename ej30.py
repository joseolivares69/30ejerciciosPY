import random

class TresEnLinea:
    def __init__(self):
        self.tablero = [[" " for _ in range(3)] for _ in range(3)]
        self.jugador_humano = ""
        self.jugador_ordenador = ""
        self.jugador_actual = ""
        self.partidas_jugadas = 0

    def mostrar_tablero(self):
        print("\n  0 1 2")
        for i, fila in enumerate(self.tablero):
            print(f"{i} |" + "|".join(fila) + "|")
        print()

    def obtener_simbolo_jugador(self):
        while True:
            simbolo = input("Ingrese el símbolo con el que desea jugar [X/O]:").upper()
            if simbolo in ['X', 'O']:
                self.jugador_humano = simbolo
                self.jugador_ordenador = 'O' if simbolo == 'X' else 'X'
                return
            print("Elección no válida. Debe ser 'X' o 'O'.")

    def elegir_primer_jugador(self):
        self.jugador_actual = random.choice([self.jugador_humano, self.jugador_ordenador])
        print(f"Es el ordenador con el símbolo {self.jugador_ordenador} quien jugará primero.")

    def hacer_movimiento_humano(self):
        while True:
            try:
                entrada = input(f"Es el turno del jugador '{self.jugador_actual}', ingrese las coordenadasx y separadas por un espacio: ")
                x, y = map(int, entrada.split())
                
                if 0 <= x < 3 and 0 <= y < 3 and self.tablero[x][y] == " ":
                    self.tablero[x][y] = self.jugador_actual
                    break
                else:
                    print("Elección no válida")
            except ValueError:
                print("Elección no válida")

    def hacer_movimiento_ordenador(self):
        casillas_vacias = [(r, c) for r in range(3) for c in range(3) if self.tablero[r][c] == " "]
        if casillas_vacias:
            x, y = random.choice(casillas_vacias)
            self.tablero[x][y] = self.jugador_ordenador

    def verificar_ganador(self):
        simbolo = self.jugador_actual
        for i in range(3):
            if all([self.tablero[i][j] == simbolo for j in range(3)]) or \
               all([self.tablero[j][i] == simbolo for j in range(3)]):
                return True
        if (self.tablero[0][0] == simbolo and self.tablero[1][1] == simbolo and self.tablero[2][2] == simbolo) or \
           (self.tablero[0][2] == simbolo and self.tablero[1][1] == simbolo and self.tablero[2][0] == simbolo):
            return True
        return False

    def verificar_empate(self):
        return all(self.tablero[r][c] != " " for r in range(3) for c in range(3))

    def cambiar_turno(self):
        self.jugador_actual = self.jugador_ordenador if self.jugador_actual == self.jugador_humano else self.jugador_humano

    def iniciar_partida(self):
        self.tablero = [[" " for _ in range(3)] for _ in range(3)]
        self.obtener_simbolo_jugador()
        self.elegir_primer_jugador()
        self.mostrar_tablero()
        
        self.partidas_jugadas += 1
        
        juego_terminado = False
        while not juego_terminado:
            
            if self.jugador_actual == self.jugador_humano:
                self.hacer_movimiento_humano()
            else:
                self.hacer_movimiento_ordenador()

            self.mostrar_tablero()
            
            if self.verificar_ganador():
                print(f"El jugador '{self.jugador_actual}' ha ganado la partida!")
                juego_terminado = True
            elif self.verificar_empate():
                print("¡La partida ha terminado en empate!")
                juego_terminado = True
            else:
                self.cambiar_turno()
        
    def jugar_juego(self):
        while True:
            self.iniciar_partida()
            jugar_otra = input("¿Desea jugar otra partida? [S/N]").upper()
            if jugar_otra != 'S':
                print(f"Has jugado {self.partidas_jugadas} partida(s).")
                break
