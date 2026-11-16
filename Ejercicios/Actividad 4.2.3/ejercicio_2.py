import random


lista_numeros_random = []
mayor_numero = -1
menor_numero = 101

for i in range(10):
    lista_numeros_random.append(random.randint(1, 100))

    if lista_numeros_random[i] > mayor_numero:
        mayor_numero = lista_numeros_random[i]

    if lista_numeros_random[i] < menor_numero:
        menor_numero = lista_numeros_random[i]

print(lista_numeros_random)
print(f"El numero mayor es: {mayor_numero}")
print(f"El numero menor es: {menor_numero}")







