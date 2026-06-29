# -------
# TA TE TI con Algoritmo de la Burbuja (Bubble Sort)
# -------

def bubble_sort_optimizado(lista):
    n = len(lista)
    for i in range(n):
        intercambio = False
        for j in range(n - i - 1):
            if lista[j]["victorias"] < lista[j + 1]["victorias"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True
        if not intercambio:
            break

# -------
# Interfas 
# -------

def mostrar_menu():
    print("\n" + "_" * 40)
    print("       TA - TE - TI  (Bubble Sort)")
    print("_" * 40)
    print("1 - Jugar")
    print("2 - Reglas del Juego")
    print("3 - Ranking")
    print("0 - Salir")
    print("_" * 40)

# -------
# Reglas del Juego
# -------

def mostrar_reglas():
    print("\n" + "_" * 40)
    print("         REGLAS DEL JUEGO")
    print("_" * 40)
    print("- Dos jugadores se turnan para marcar")
    print("  casillas en un tablero de 3x3.")
    print("- El jugador 1 usa la X.")
    print("- El jugador 2 usa la O.")
    print("- Gana quien complete una fila,")
    print("  columna o diagonal.")
    print("- Si se llenan las 9 casillas sin")
    print("  ganador, es EMPATE.")
    print("- El ranking se ordena con Bubble Sort")
    print("  de mayor a menor victorias.")
    print("_" * 40)

# -------
# Ranking de los Jugadores
# -------

def mostrar_ranking(jugadores_historial):
    print("\n" + "_" * 40)
    print("            RANKING")
    print("_" * 40)
    if not jugadores_historial:
        print("  Todavía no hay partidas jugadas.")
    else:
        for pos, j in enumerate(jugadores_historial, start=1):
            print(f"  #{pos}  {j['nombre']} ({j['simbolo']})  —  Victorias: {j['victorias']}")
    print("_" * 40)

# -------
# Juego
# -------

def jugar(victorias1, victorias2, empates, jugador1, jugador2):

    # -------
    # Datos de los Jugadores
    # -------

    if jugador1 == "" and jugador2 == "":
        jugador1 = input("\nNombre del jugador 1 (X): ")
        jugador2 = input("Nombre del jugador 2 (O): ")
    
    # -------
    # Creacion del Tablero
    # -------

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
    
    # -------
    # Formas de Ganar
    # -------

    def ganador(simbolo):
        for fila in tablero:
            if fila[0] == fila[1] == fila[2] == simbolo:
                return True
        for i in range(3):
            if tablero[0][i] == tablero[1][i] == tablero[2][i] == simbolo:
                return True
        if tablero[0][0] == tablero[1][1] == tablero[2][2] == simbolo:
            return True
        if tablero[0][2] == tablero[1][1] == tablero[2][0] == simbolo:
            return True
        return False
    
    # -------
    # Turnos, Filas y Columnas
    # -------

    turno   = "X"
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

    return victorias1, victorias2, empates, jugador1, jugador2

    # -------
    # Codigo Principal 
    # -------

victorias1 = 0
victorias2 = 0
empates    = 0
jugador1   = ""
jugador2   = ""

while True:

    mostrar_menu()

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":

        victorias1, victorias2, empates, jugador1, jugador2 = jugar(victorias1, victorias2, empates, jugador1, jugador2)

    elif opcion == "2":

        mostrar_reglas()

    elif opcion == "3":

        jugadores_ranking = [
            {"nombre": jugador1, "victorias": victorias1, "simbolo": "X"},
            {"nombre": jugador2, "victorias": victorias2, "simbolo": "O"},
        ]
        bubble_sort_optimizado(jugadores_ranking)
        mostrar_ranking(jugadores_ranking)

    elif opcion == "0":

        print("\nGracias por jugar Ta-Te-Ti. ¡Hasta la próxima!")
        break

    else:

        print("\nOpción incorrecta. Intente nuevamente.")
       


       
           

   
               
       
           

    
    

   
    
    
  

    
          
