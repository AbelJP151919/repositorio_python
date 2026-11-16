numeroEntero = input("Escribe un numero entero: ")

n = 15

suma = 0

sumatorio = 0


if int(numeroEntero) == n:
    suma = n * (n + 1) / 2
    print(suma)
else:
    for i in range(1, int(numeroEntero)+1):
        sumatorio+= i

print(sumatorio)