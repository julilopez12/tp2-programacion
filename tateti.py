#   TA - TE - TI  con  Algoritmo de la Burbuja (Bubble Sort)

# El Bubble Sort se usa para ordenar el ranking de jugadores
# de mayor a menor cantidad de victorias al mostrar el marcador.

# BUBBLE SORT

def bubble_sort_optimizado(lista):
    """
    Ordena una lista de diccionarios de mayor a menor
    según la clave 'victorias'.

    Complejidad:
      - Mejor caso  : O(n)   — lista ya ordenada
      - Caso promedio: O(n²)
      - Peor caso   : O(n²)  — lista completamente desordenada
    """
    n = len(lista)
    for i in range(n):
        intercambio = False
        for j in range(n - i - 1):
            if lista[j]["victorias"] < lista[j + 1]["victorias"]:   # Mayor A Menor
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True
        if not intercambio:   # Condición de parada: si no hubo cambios, ya está ordenado
            break


# Datos De Los Jugadores

jugador1 = input("Nombre del jugador 1 (X): ")
jugador2 = input("Nombre del jugador 2 (O): ")

victorias1 = 0
victorias2 = 0
empates    = 0

# Tablaro TA TE TI

while True:

    # Tablero Ta-Te-Ti
    tablero = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    def mostrar():
        print()
        for fila in tablero:
            print(fila[0], "|", fila[1], "|", fila[2])
            print("-" * 9)
        print()
        
    # Formas De Ganar

    def ganador(simbolo):

        # Filas
        
        for fila in tablero:
            if fila[0] == fila[1] == fila[2] == simbolo:
                return True
        
        # Columnas

        for i in range(3):
            if tablero[0][i] == tablero[1][i] == tablero[2][i] == simbolo:
                return True
        
        # Diagonales

        if tablero[0][0] == tablero[1][1] == tablero[2][2] == simbolo:
            return True
        if tablero[0][2] == tablero[1][1] == tablero[2][0] == simbolo:
            return True
        return False

    # Juego

    turno  = "X"
    jugadas = 0

    while True:

        mostrar()

        if turno == "X":
            print("Turno de", jugador1)
        else:
            print("Turno de", jugador2)

        while True:
            fila    = int(input("Fila (1 | 2 | 3): "))
            columna = int(input("Columna (1 | 2 | 3): "))

            if 1 <= fila <= 3 and 1 <= columna <= 3:
                fila    -= 1
                columna -= 1
                break
            else:
                print("Número no válido. Debe ingresar 1, 2 o 3.")

        if tablero[fila][columna] != " ":
            print("Casilla ocupada.")
            continue

        tablero[fila][columna] = turno
        jugadas += 1

        if ganador(turno):
            mostrar()
            if turno == "X":
                print("¡¡ Ganó", jugador1, "!!")
                victorias1 += 1
            else:
                print("¡¡ Ganó", jugador2, "!!")
                victorias2 += 1
            break

        if jugadas == 9:
            mostrar()
            print("¡Empate!")
            empates += 1
            break

        turno = "O" if turno == "X" else "X"

    # MARCADOR CON BUBBLE SORT

    # Armamos una lista de jugadores y la ordenamos de mayor a menor victorias
    # usando el Algoritmo de la Burbuja antes de mostrar el ranking.

    jugadores = [
        {"nombre": jugador1, "victorias": victorias1, "simbolo": "X"},
        {"nombre": jugador2, "victorias": victorias2, "simbolo": "O"},
    ]

    print("\n  [Bubble Sort] Ordenando ranking por victorias...")
    bubble_sort_optimizado(jugadores)

    print("\n========== MARCADOR ==========")
    for pos, j in enumerate(jugadores, start=1):
        print(f"  #{pos}  {j['nombre']} ({j['simbolo']})  —  Victorias: {j['victorias']}")
    print(f"  Empates: {empates}")
    print("==============================")

    # ¿Otra Partida?

    while True:
        jugar = input("\n¿Desean jugar otra partida? (S/N): ")
        if jugar.upper() == "S":
            break
        elif jugar.upper() == "N":
            print("\nGracias por jugar.")
            exit()
        else:
            print("Opción no válida. Debe ingresar S o N.")