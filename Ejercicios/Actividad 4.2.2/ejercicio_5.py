numero = int(input("Ingrese un numero: "))

for i in range(11):
    multiplicar_numero = numero*i
    print(multiplicar_numero)
contador = 0
while contador <= 10:
    contador += 1
    multiplicar_numero = contador*numero
    print(multiplicar_numero)