import random
numero_random = random.randint(1, 101)
print(numero_random)

def juego_con_for():
    n_intentos = 9999
    nuevo_numero_intento = n_intentos
    respuesta_usuario = int(input("Introduce tu numero del 1 al 100 para adivinar el numero secreto: "))
    for i in range(1, n_intentos):
        if respuesta_usuario > numero_random:
            print("El numero secreto es menor que el introducido")
            nuevo_numero_intento -= 1
            print(f"Te quedan {nuevo_numero_intento} intentos")
            respuesta_usuario = int(
                input("vuelve a introducir tu numero del 1 al 100 para adivinar el numero secreto: "))
        elif respuesta_usuario < numero_random:
            print("El numero secreto es mayor que el introducido")
            nuevo_numero_intento -= 1
            print(f"Te quedan {nuevo_numero_intento} intentos")
            respuesta_usuario = int(
                input("vuelve a introducir tu numero del 1 al 100 para adivinar el numero secreto: "))

        elif respuesta_usuario == numero_random:
            print("HAS ACERTADO")
            print("Tus intentos restantes: ", nuevo_numero_intento)
            break

def juego_con_while():

    contador_intentos = 0

    respuesta_usuario = int(input("Introduce tu numero del 1 al 100 para adivinar el numero secreto: "))
    while numero_random != respuesta_usuario:
        if respuesta_usuario > numero_random:
            print("El numero secreto es menor que el introducido")
            contador_intentos += 1
            respuesta_usuario = int(
                input("vuelve a introducir tu numero del 1 al 100 para adivinar el numero secreto: "))
        elif respuesta_usuario < numero_random:
            print("El numero secreto es mayor que el introducido")
            contador_intentos += 1

            respuesta_usuario = int(
                input("vuelve a introducir tu numero del 1 al 100 para adivinar el numero secreto: "))
        elif respuesta_usuario == numero_random:
            print("HAS ACERTADO")
            print("Tus intentos restantes: ", contador_intentos)

juego_con_while()

