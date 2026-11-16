import random


lista_numeros_random = []

for i in range(10):
    numeros_random = random.randint(1, 100)
    lista_numeros_random.append(numeros_random)


print(lista_numeros_random)
lista_numeros_random.reverse()
print(lista_numeros_random)

