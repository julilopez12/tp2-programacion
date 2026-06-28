# --------------------------------------
# CARRERA DE DADOS
# Programación I
# --------------------------------------

import random

META = 20

ganadores = []

def tirar_dado():

    dado = random.randint(1, 6)

    print("El dado sacó:", dado)

    return dado


def jugar():
    print("\n===== CARRERA DE DADOS =====")
    jugador1 = input("Nombre del Jugador 1: ")
    jugador2 = input("Nombre del Jugador 2: ")

    posicion1 = 0
    posicion2 = 0

    while posicion1 < META and posicion2 < META:

        print("\nTurno de", jugador1)
        input("Presione ENTER para tirar el dado...")
        dado = tirar_dado()
        posicion1 += dado
        print("\nMETA:", META)
        print(jugador1, ":", posicion1, "/", META)
        print(jugador2, ":", posicion2, "/", META)
        if posicion1 >= META:

         print("\n¡¡Ganó", jugador1, "!!")

         ganadores.append(jugador1)

         archivo = open("ganadores.txt", "a")

         archivo.write(jugador1 + "\n")

         archivo.close()

         break

        print("\nTurno de", jugador2)
        input("Presione ENTER para tirar el dado...")
        dado = tirar_dado()
        posicion2 += dado
        print("\nMETA:", META)
        print(jugador1, ":", posicion1, "/", META)
        print(jugador2, ":", posicion2, "/", META)
        if posicion2 >= META:

         print("\n¡¡Ganó", jugador2, "!!")

         ganadores.append(jugador2)

         archivo = open("ganadores.txt", "a")

         archivo.write(jugador2 + "\n")

         archivo.close()

         break


def menu():

    opcion = -1

    while opcion != 0:

        print("\n==============================")
        print("     CARRERA DE DADOS")
        print("==============================")
        print("1 - Jugar")
        print("2 - Ver ganadores")
        print("0 - Salir")

        try:
            opcion = int(input("Ingrese una opción: "))

            if opcion == 1:
                jugar()

            elif opcion == 2:
                mostrar_ganadores()

            elif opcion == 0:
                print("Gracias por jugar.")
            else:
                print("Opción incorrecta.")

        except:
            print("Debe ingresar un número.")
  

# Ordenamiento por Burbuja
def ordenar_burbuja(lista):

    n = len(lista)

    for i in range(n - 1):

        for j in range(n - 1 - i):

            if lista[j] > lista[j + 1]:

                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
 
def mostrar_ganadores():

    if len(ganadores) == 0:

        print("\nNo hay ganadores registrados.")

    else:

        ordenar_burbuja(ganadores)

        print("\n===== GANADORES ORDENADOS =====")

        for nombre in ganadores:

            print(nombre)
menu()
