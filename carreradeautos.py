import random

# =====================================
# FUNCIONES
# =====================================

def mostrar_menu():
    print("\n" + "=" * 40)
    print("         BUBBLE RACE")
    print("=" * 40)
    print("1 - Jugar")
    print("2 - Ver Ranking")
    print("3 - Créditos")
    print("0 - Salir")
    print("=" * 40)


def crear_autos():
    nombres = ["Rojo", "Azul", "Verde", "Amarillo", "Negro"]
    autos = []

    for nombre in nombres:
        tiempo = random.randint(20, 99)
        autos.append([nombre, tiempo])

    return autos


def mostrar_autos(autos):

    print("\n" + "-" * 35)
    print("       CARRERA DE AUTOS")
    print("-" * 35)

    for i in range(len(autos)):
        print(f"{i+1}. {autos[i][0]:10} {autos[i][1]} segundos")

    print("-" * 35)


def guardar_ranking(nombre, puntaje):

    archivo = open("ranking.txt", "a")

    archivo.write(nombre + " - " + str(puntaje) + "\n")

    archivo.close()


def ver_ranking():

    print("\n===== RANKING =====")

    try:

        archivo = open("ranking.txt", "r")

        lineas = archivo.readlines()

        archivo.close()

        if len(lineas) == 0:
            print("Todavía no hay puntajes.")
        else:
            for linea in lineas:
                print(linea.strip())

    except FileNotFoundError:
        print("Todavía no existe el archivo ranking.txt")


def jugar():

    nombre = input("\nIngrese su nombre: ")

    vidas = 3

    puntaje = 0

    autos = crear_autos()

    print("\nBienvenido", nombre)

    print("Vidas:", vidas)

    print("Puntaje:", puntaje)

    mostrar_autos(autos)

    input("\nPresione ENTER para comenzar la carrera...")

    # =====================================
    # METODO BURBUJA
    # =====================================

    for i in range(len(autos)-1):

        print("\n==============================")
        print("PASADA", i + 1)
        print("==============================")

        for j in range(len(autos)-1-i):

            print("\nComparando:")

            print(autos[j][0], "-", autos[j][1], "segundos")

            print(autos[j+1][0], "-", autos[j+1][1], "segundos")

            while True:

                respuesta = input("¿Se intercambian? (S/N): ").upper()

                if respuesta == "S" or respuesta == "N":
                    break

                print("Ingrese S o N solamente.")

            if autos[j][1] > autos[j+1][1]:
                correcta = "S"
            else:
                correcta = "N"

            if respuesta == correcta:

                print("✔ Correcto")

                puntaje += 10

            else:

                print("✘ Incorrecto")

                vidas -= 1

                print("Vidas restantes:", vidas)

            if autos[j][1] > autos[j+1][1]:

                aux = autos[j]

                autos[j] = autos[j+1]

                autos[j+1] = aux

            mostrar_autos(autos)

            if vidas == 0:

                print("\nTe quedaste sin vidas.")

                guardar_ranking(nombre, puntaje)

                return
                print("\n")
    print("=" * 35)
    print("🏁 CARRERA FINALIZADA 🏁")
    print("=" * 35)

    for i in range(len(autos)):
        print(f"{i+1}° Lugar: {autos[i][0]} - {autos[i][1]} segundos")

    print("\nPuntaje final:", puntaje)

    guardar_ranking(nombre, puntaje)

    print("\n¡Tu puntaje fue guardado correctamente!")

def creditos():

    print("\n" + "=" * 40)
    print("             CRÉDITOS")
    print("=" * 40)
    print("Juego desarrollado para")
    print("Programación I")
    print("Tema: Optimización por Burbuja")
    print("=" * 40)


# =====================================
# PROGRAMA PRINCIPAL
# =====================================

while True:

    mostrar_menu()

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":

        jugar()

    elif opcion == "2":

        ver_ranking()

    elif opcion == "3":

        creditos()

    elif opcion == "0":

        print("\nGracias por jugar Bubble Race.")
        break

    else:

        print("\nOpción incorrecta.")