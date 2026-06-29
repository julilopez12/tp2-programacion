import random
#La empresa Play.in Diseño este juego para que los niños/adultos puedan aprender jugando o divertirse
# PREGUNTAS
# -----------------------------
preguntas = [
    ("Capital de Argentina", "buenos aires"),
    ("¿Cuánto es 15 + 20?", "35"),
    ("Color del cielo", "azul"),
    ("Lenguaje que usamos", "python"),
    ("Días de una semana", "7"),
    ("8 x 9", "72"),
    ("Animal que dice miau", "gato"),
    ("Mes después de enero", "febrero"),
    ("¿Quien es el mas lindo del curso'?", "el profe"),
    ("¿Cuántos meses tiene un año?", "12"),
    ("¿Cual es el café mas peligroso?", "el ex-preso"),
]

def menu():
    print("\n===== PING PONG DE PREGUNTAS =====")
    print("1. Jugar")
    print("2. Ver reglas")
    print("3. Ver ranking")
    print("4. Salir")

def reglas():
    print("\nREGLAS")
    print("- Juegan dos personas.")
    print("- Cada respuesta correcta vale 1 punto.")
    print("- Gana quien llegue primero a 5 puntos.")

def ranking():
    print("\n===== RANKING =====")
    try:
        with open("ranking.txt", "r") as archivo:
            print(archivo.read())
    except FileNotFoundError:
        print("Todavía no hay partidas registradas.")

def guardar(nombre, puntos):
    with open("ranking.txt", "a") as archivo:
        archivo.write(f"{nombre} - {puntos} puntos\n")

def jugar():
    j1 = input("Nombre del Jugador 1: ")
    j2 = input("Nombre del Jugador 2: ")

    p1 = 0
    p2 = 0
    turno = 0
    usadas = []

    while p1 < 5 and p2 < 5:

        if len(usadas) == len(preguntas):
            usadas.clear()

        while True:
            i = random.randint(0, len(preguntas)-1)
            if i not in usadas:
                usadas.append(i)
                break

        pregunta, respuesta = preguntas[i]

        if turno == 0:
            print("\n----------------------------")
            print("🏓 La pelota viene hacia vos...")
            print(f"\nTurno de {j1}")
            
            
        else:
            print("\n----------------------------")
            print(f"\nTurno de {j2}")
            print("¡🏓La pelota vuelve a", j2 + "!")

        print("Pregunta:", pregunta)
        
        r = input("Respuesta: ").lower().strip()

        if r == respuesta:
            print("✅ ¡Correcto!")
            
            if turno == 0:
                p1 += 1
            else:
                p2 += 1
        else:
            print("🏓 La pelota vuelve a", j1 + "!")
        print("❌ Incorrecto. Era:", respuesta)
        print(f"\nPuntaje: {j1}={p1} | {j2}={p2}")
        
       

        if turno == 0:
            turno = 1
        else:
            turno = 0

    if p1 > p2:
        ganador = j1
        puntos = p1
    else:
        ganador = j2
        puntos = p2

# GANADOR
# -----------------------------
    print("\nGANADOR:", ganador)
    guardar(ganador, puntos)
    input("\nPresione ENTER para volver al menú...")

while True:
    menu()
    op = input("Seleccione una opción: ")

    if op == "1":
        jugar()

    elif op == "2":
        reglas()
        input("\nENTER para volver...")

    elif op == "3":
        ranking()
        input("\nENTER para volver...")

    elif op == "4":
        print("Gracias por jugar. Espero te haya gustado el juego. ¡Hasta la próxima!")
        break

    else:
        print("Opción inválida.")