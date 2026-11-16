import random

try:
    numero_random  = random.randint(1,10)
    intentos = 0

    while intentos < 3:
        numero = int(input("Introduce el numero secreto: "))
        if numero > numero_random:
            print("Tu numero es mayor que el numero secreto")
            intentos = intentos + 1
            print(f"Intentos: {intentos}")
        elif numero < numero_random:
            print("Tu numero es menor que el numero secreto")
            intentos = intentos + 1
            print(f"Intentos: {intentos}")
        elif numero == numero_random:
            print("HAS GANADO. Tu numero es igual que el numero secreto")
            print(f"Intentos: {intentos}")
            print(f"numero random: {numero_random}")
            intentos = 4
except:
    print("Error en el servidor")


