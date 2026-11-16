import time

try:

    funcion = 0
    while funcion !=5:
        funcion = int(input("Introduce el numero de la funcion que deseas hacer:1. sumar; 2, restar; 3, multiplicar; 4, dividir; 5, salir; "))
        match funcion:

            case 1:
                numero_1 = int(input("Introduce el primer numero: "))
                numero_2 = int(input("Introduce el segundo numero: "))
                resultado = numero_1 + numero_2
                print(f"Resultado de la suma es: {resultado}")

            case 2:
                numero_1 = int(input("Introduce el primer numero: "))
                numero_2 = int(input("Introduce el segundo numero: "))
                resultado = numero_1 - numero_2
                print(f"Resultado de la resta es: {resultado}")

            case 3:
                numero_1 = int(input("Introduce el primer numero: "))
                numero_2 = int(input("Introduce el segundo numero: "))
                resultado = numero_1 * numero_2
                print(f"Resultado de la multiplicacion es: {resultado}")

            case 4:
                numero_1 = int(input("Introduce el primer numero: "))
                numero_2 = int(input("Introduce el segundo numero: "))
                resultado = numero_1 / numero_2
                print(f"Resultado de la division es: {resultado}")

            case 5:
                print("Saliendo de la calculadora...")
                time.sleep(0.5)
                funcion = 5

            case _:
                print("No puedes introducir eso")



except:
    print("Error en el servidor")



