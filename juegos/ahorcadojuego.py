import random

DIBUJOS = [
    '''
       +---+
       |   |
           |
           |
           |
           |
    =========''', '''
       +---+
       |   |
       O   |
           |
           |
           |
    =========''', '''
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========''', '''
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========''', '''
       +---+
       |   |
       O   |
      /|\  |
           |
           |
    =========''', '''
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
    =========''', '''
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
    ========='''
]

def jugar_ahorcado():
    palabras = ["archivos","subcarpetas","extension","raiz","carpetas","binario","byte"]
    palabra_secreta = random.choice(palabras)
    
    letras_adivinadas = []
    vidas = 6

    print("¡Bienvenido al juego del Ahorcado!")

    while vidas > 0:
        errores = 6 - vidas
        print(DIBUJOS[errores])

        palabra_mostrada = ""
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                palabra_mostrada += letra + " "
            else:
                palabra_mostrada += "_ "
        
        print(f"\nPalabra: {palabra_mostrada}")
        print(f"Vidas restantes: {vidas}")

        if "_" not in palabra_mostrada:
            print("\n¡Felicidades! Adivinaste la palabra:", palabra_secreta)
            return  

        letra_usuario = input("\nIngresa una letra: ").lower()

        if len(letra_usuario) != 1 or not letra_usuario.isalpha():
            print("Por favor, ingresa solo una letra válida.")
            continue
        
        if letra_usuario in letras_adivinadas:
            print("Ya intentaste con esa letra. ¡Prueba otra!")
            continue

        letras_adivinadas.append(letra_usuario)
        
        if letra_usuario in palabra_secreta:
            print("¡Bien hecho! La letra está en la palabra.")
        else:
            print("¡Oh no! La letra no está.")
            vidas -= 1

    print(DIBUJOS[6])
    print("\n¡Te quedaste sin vidas! Fin del juego.")
    print(f"La palabra secreta era: {palabra_secreta}")

jugar_ahorcado()